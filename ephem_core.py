#!/usr/bin/env python3
"""
Shared ephemeris core.

Until now every script in this repository worked from a supplied table of
longitudes, because the birth time was unknown to about ten minutes.  The
birth data is now known:

    15 April 2002, 18:02:45 IST, Guntur, Andhra Pradesh, India

This module computes the chart from first principles with the Swiss Ephemeris
and exposes it to every other script, so that the things which were previously
impossible -- cuspal houses, sunrise-based upagrahas, the vargas finer than
D12, exact transit dates -- can be computed instead of approximated.

It deliberately keeps BOTH chart versions available:

    SUPPLIED  the longitudes given with the source data, on which every
              Shadbala, Ashtakavarga and Shodhya Pinda figure in this
              repository was built
    COMPUTED  the Swiss Ephemeris positions for the stated birth moment

They agree to better than one arcminute for all nine grahas.  Nothing is
silently switched: scripts that rest on the supplied strength tables keep
using SUPPLIED, and the new work states which it used.
"""
import swisseph as swe

# ---------------------------------------------------------------- birth data
BIRTH = dict(
    date=(2002, 4, 15),
    time=(18, 2, 45),          # IST, as supplied
    tz=5.5,
    place='Guntur, Andhra Pradesh, India',
    lat=16.3067,
    lon=80.4365,
    alt=33.0,                  # metres, for refraction-correct rise/set
)

SIGNS = ['Mesha', 'Vrishabha', 'Mithuna', 'Karka', 'Simha', 'Kanya',
         'Tula', 'Vrischika', 'Dhanu', 'Makara', 'Kumbha', 'Meena']
SIGN_EN = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra',
           'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
NAK = ['Ashwini', 'Bharani', 'Krittika', 'Rohini', 'Mrigashira', 'Ardra',
       'Punarvasu', 'Pushya', 'Ashlesha', 'Magha', 'P.Phalguni', 'U.Phalguni',
       'Hasta', 'Chitra', 'Swati', 'Vishakha', 'Anuradha', 'Jyeshtha',
       'Mula', 'P.Ashadha', 'U.Ashadha', 'Shravana', 'Dhanishtha',
       'Shatabhisha', 'P.Bhadrapada', 'U.Bhadrapada', 'Revati']
NAK_LORD = ['Ketu', 'Shukra', 'Surya', 'Chandra', 'Mangal',
            'Rahu', 'Guru', 'Shani', 'Budha'] * 3
LORD = ['Mangal', 'Shukra', 'Budha', 'Chandra', 'Surya', 'Budha',
        'Shukra', 'Mangal', 'Guru', 'Shani', 'Shani', 'Guru']
EXALT = {'Surya': 0, 'Chandra': 1, 'Mangal': 9, 'Budha': 5,
         'Guru': 3, 'Shukra': 11, 'Shani': 6}
EXALT_DEG = {'Surya': 10, 'Chandra': 3, 'Mangal': 28, 'Budha': 15,
             'Guru': 5, 'Shukra': 27, 'Shani': 20}
MOOLA = {'Surya': (4, 0, 20), 'Chandra': (1, 3, 30), 'Mangal': (0, 0, 12),
         'Budha': (5, 15, 20), 'Guru': (8, 0, 10), 'Shukra': (6, 0, 15),
         'Shani': (10, 0, 20)}
VIM = [('Ketu', 7), ('Shukra', 20), ('Surya', 6), ('Chandra', 10),
       ('Mangal', 7), ('Rahu', 18), ('Guru', 16), ('Shani', 19), ('Budha', 17)]
WEEKDAY = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
           'Friday', 'Saturday']
WEEKDAY_LORD = ['Surya', 'Chandra', 'Mangal', 'Budha', 'Guru', 'Shukra', 'Shani']

IDS = {'Surya': swe.SUN, 'Chandra': swe.MOON, 'Mangal': swe.MARS,
       'Budha': swe.MERCURY, 'Guru': swe.JUPITER, 'Shukra': swe.VENUS,
       'Shani': swe.SATURN}
GRAHAS = ['Surya', 'Chandra', 'Mangal', 'Budha', 'Guru', 'Shukra', 'Shani',
          'Rahu', 'Ketu']

swe.set_sid_mode(swe.SIDM_LAHIRI)
FLAG = swe.FLG_SWIEPH | swe.FLG_SIDEREAL | swe.FLG_SPEED


# ------------------------------------------------------------------ helpers
def jd_ut(y, m, d, h, mi, s, tz):
    """Julian day (UT) from local civil time."""
    return swe.julday(y, m, d, h + mi / 60 + s / 3600 - tz)


JD = jd_ut(*BIRTH['date'], *BIRTH['time'], BIRTH['tz'])
AYANAMSA = swe.get_ayanamsa_ut(JD)


def dms(s, d, m, sec=0):
    """Sign name + d/m/s -> absolute sidereal longitude."""
    return SIGNS.index(s) * 30 + d + m / 60 + sec / 3600


def fmt(l, width=0):
    l %= 360
    out = f"{int(l % 30):02d}°{int(l % 1 * 60):02d}′{round(l * 3600 % 60):02d}″ {SIGNS[int(l // 30)]}"
    return f"{out:{width}s}" if width else out


def short(l):
    l %= 360
    return f"{int(l % 30):02d}°{int(l % 1 * 60):02d}′ {SIGNS[int(l // 30)]}"


def nak_of(l):
    """(nakshatra, pada, lord, degrees into the nakshatra)."""
    span = 360 / 27
    i = int(l % 360 // span)
    into = l % 360 - i * span
    return NAK[i], int(into // (span / 4)) + 1, NAK_LORD[i], into


def sign_of(l):
    return int(l % 360 // 30)


def positions(jd=JD, true_node=False):
    """Sidereal longitudes of all nine grahas plus speeds."""
    out, spd = {}, {}
    for n, i in IDS.items():
        x = swe.calc_ut(jd, i, FLAG)[0]
        out[n], spd[n] = x[0] % 360, x[3]
    node = swe.TRUE_NODE if true_node else swe.MEAN_NODE
    x = swe.calc_ut(jd, node, FLAG)[0]
    out['Rahu'], spd['Rahu'] = x[0] % 360, x[3]
    out['Ketu'], spd['Ketu'] = (x[0] + 180) % 360, x[3]
    return out, spd


def ascendant(jd=JD, hsys=b'P'):
    """(cusps, ascmc) sidereal, for the birth place."""
    return swe.houses_ex(jd, BIRTH['lat'], BIRTH['lon'], hsys,
                         swe.FLG_SIDEREAL)


def rise_set(jd, body=swe.SUN, rise=True):
    """UT julian day of the next rise/set of `body` at the birth place."""
    rsmi = swe.CALC_RISE if rise else swe.CALC_SET
    res, t = swe.rise_trans(jd, body, rsmi,
                            (BIRTH['lon'], BIRTH['lat'], BIRTH['alt']),
                            0.0, 0.0, swe.FLG_SWIEPH)
    return t[0]


def local(jd):
    """Julian day (UT) -> local civil clock string."""
    y, m, d, h = swe.revjul(jd + BIRTH['tz'] / 24)
    hh = int(h)
    mm = int((h - hh) * 60)
    ss = round(((h - hh) * 60 - mm) * 60)
    if ss == 60:
        ss, mm = 0, mm + 1
    if mm == 60:
        mm, hh = 0, hh + 1
    return f"{d:02d}/{m:02d}/{y} {hh:02d}:{mm:02d}:{ss:02d}"


# ------------------------------------------------- the two chart versions
SUPPLIED = {
    'Lagna':   dms('Kanya', 27, 37, 37),
    'Surya':   dms('Mesha', 1, 28, 3),
    'Chandra': dms('Vrishabha', 1, 47, 15),
    'Mangal':  dms('Vrishabha', 7, 19, 32),
    'Budha':   dms('Mesha', 10, 27, 50),
    'Guru':    dms('Mithuna', 14, 47, 52),
    'Shukra':  dms('Mesha', 23, 36, 49),
    'Shani':   dms('Vrishabha', 17, 54, 25),
    'Rahu':    dms('Vrishabha', 26, 55, 52),
    'Ketu':    dms('Vrischika', 26, 55, 52),
}

_p, SPEED = positions()
COMPUTED = dict(_p)
COMPUTED['Lagna'] = ascendant()[1][0] % 360


# --------------------------------------------------------- the varga engine
def varga(l, n):
    """
    Classical Parashari divisional mapping, extended to every scheme this
    repository uses.  Returns a sign index 0..11.

    The linear schemes (D9, D27, D81, D108, D144, D150, and D60's doubled
    form) have no start-sign convention to disagree about.  The others use
    the standard Parashara rule stated in the comment beside them.
    """
    l %= 360
    s, deg = int(l // 30), l % 30
    part = int(deg / (30.0 / n))
    if n == 1:
        return s
    if n == 2:                                    # Hora: Simha / Karka
        return 4 if (s % 2 == 0) == (deg < 15) else 3
    if n == 3:                                    # 1st, 5th, 9th from sign
        return (s + part * 4) % 12
    if n == 4:                                    # kendras from sign
        return (s + part * 3) % 12
    if n == 5:                                    # odd: from sign; even: 9th
        return ((s if s % 2 == 0 else s + 8) + part) % 12
    if n == 6:                                    # odd: from Mesha; even: Tula
        return ((0 if s % 2 == 0 else 6) + part) % 12
    if n == 7:                                    # odd: from sign; even: 7th
        return ((s if s % 2 == 0 else s + 6) + part) % 12
    if n == 8:                                    # movable Mesha, fixed Dhanu,
        return ({0: 0, 1: 8, 2: 4}[s % 3] + part) % 12   # dual Simha
    if n == 9:
        return int(l / (30.0 / 9)) % 12
    if n == 10:                                   # odd: from sign; even: 9th
        return ((s if s % 2 == 0 else s + 8) + part) % 12
    if n == 11:                                   # Rudramsha: start = 12 - sign
        return (part - s) % 12
    if n == 12:                                   # from the sign itself
        return (s + part) % 12
    if n == 15:                                   # movable/fixed/dual starts
        return ({0: 0, 1: 4, 2: 8}[s % 3] + part) % 12
    if n == 16:                                   # Mesha/Simha/Dhanu
        return ({0: 0, 1: 4, 2: 8}[s % 3] + part) % 12
    if n == 18:
        return ({0: 0, 1: 4, 2: 8}[s % 3] + part) % 12
    if n == 20:                                   # Mesha/Dhanu/Simha
        return ({0: 0, 1: 8, 2: 4}[s % 3] + part) % 12
    if n == 22:
        return (s + part) % 12
    if n == 24:                                   # odd from Simha, even Karka
        return ((4 if s % 2 == 0 else 3) + part) % 12
    if n == 27:
        return int(l / (30.0 / 27)) % 12
    if n == 30:                                   # unequal Trimshamsha
        lim = ([(5, 0), (10, 10), (18, 8), (25, 2), (30, 6)] if s % 2 == 0
               else [(5, 1), (12, 5), (20, 11), (25, 9), (30, 7)])
        for hi, sign in lim:
            if deg < hi:
                return sign
        return lim[-1][1]
    if n == 36:
        return (s + part) % 12
    if n == 40:                                   # odd from Mesha, even Tula
        return ((0 if s % 2 == 0 else 6) + part) % 12
    if n == 45:                                   # Mesha/Simha/Dhanu
        return ({0: 0, 1: 4, 2: 8}[s % 3] + part) % 12
    if n == 60:
        return (s + int(deg * 2)) % 12
    if n in (81, 108, 144, 150):                  # pure linear maps
        return int(l / (30.0 / n)) % 12
    raise ValueError(f'no rule for D{n}')


def dignity(g, s):
    """Exalted / debilitated / own / friend / neutral / enemy in sign s."""
    if g in ('Rahu', 'Ketu'):
        return '—'
    if EXALT.get(g) == s:
        return 'exalted'
    if EXALT.get(g) == (s + 6) % 12:
        return 'debilitated'
    if LORD[s] == g:
        return 'own'
    return RELATION.get((g, LORD[s]), 'neutral')


FRIEND = {
    'Surya':   (['Chandra', 'Mangal', 'Guru'], ['Budha'], ['Shukra', 'Shani']),
    'Chandra': (['Surya', 'Budha'], ['Mangal', 'Guru', 'Shukra', 'Shani'], []),
    'Mangal':  (['Surya', 'Chandra', 'Guru'], ['Shukra', 'Shani'], ['Budha']),
    'Budha':   (['Surya', 'Shukra'], ['Mangal', 'Guru', 'Shani'], ['Chandra']),
    'Guru':    (['Surya', 'Chandra', 'Mangal'], ['Shani'], ['Budha', 'Shukra']),
    'Shukra':  (['Budha', 'Shani'], ['Mangal', 'Guru'], ['Surya', 'Chandra']),
    'Shani':   (['Budha', 'Shukra'], ['Guru'], ['Surya', 'Chandra', 'Mangal']),
}
RELATION = {}
for _g, (_f, _n, _e) in FRIEND.items():
    for _x in _f:
        RELATION[(_g, _x)] = 'friend'
    for _x in _n:
        RELATION[(_g, _x)] = 'neutral'
    for _x in _e:
        RELATION[(_g, _x)] = 'enemy'
    RELATION[(_g, _g)] = 'own'


def rule(t):
    print('\n' + '=' * 92 + f'\n  {t}\n' + '=' * 92)


def sub(t):
    print(f'\n  --- {t} ' + '-' * max(2, 80 - len(t)))


if __name__ == '__main__':
    rule('EPHEMERIS CORE — self-test')
    print(f"\n  {BIRTH['place']}   {BIRTH['lat']}°N  {BIRTH['lon']}°E")
    print(f"  {BIRTH['date'][2]:02d}/{BIRTH['date'][1]:02d}/{BIRTH['date'][0]}"
          f"  {BIRTH['time'][0]:02d}:{BIRTH['time'][1]:02d}:{BIRTH['time'][2]:02d}"
          f"  IST (UTC+{BIRTH['tz']})")
    print(f"  JD(UT) {JD:.7f}   Lahiri ayanamsa {AYANAMSA:.6f}° "
          f"= {int(AYANAMSA)}°{(AYANAMSA % 1) * 60:.0f}′")
    print(f"\n  {'body':9s} {'computed':24s} {'supplied':24s}  delta")
    worst = 0.0
    for g in ['Lagna'] + GRAHAS:
        d = ((COMPUTED[g] - SUPPLIED[g] + 180) % 360 - 180) * 60
        worst = max(worst, abs(d))
        print(f"  {g:9s} {fmt(COMPUTED[g], 24)} {fmt(SUPPLIED[g], 24)}  {d:+7.2f}′")
    print(f"\n  worst deviation {worst:.2f}′")
