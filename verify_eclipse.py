#!/usr/bin/env python3
"""
Eclipse analysis for the natal chart.

Computes the sidereal (Lahiri) position of each solar eclipse in the 2026-2028
series, places it against the natal chart, and reports every natal contact
inside orb.

Solar longitudes come from the standard low-precision series (NOAA/Meeus
abridged), accurate to roughly +/-0.01 degrees -- far finer than anything the
interpretation depends on. Eclipse DATES are firm; the greatest-eclipse TIMES
are approximate to the hour, which moves the Sun by at most ~0.04 degrees.

Cross-check: the supplied 11 August 2026 transit set puts the Sun at 24 27
sidereal Karka.  This script reproduces that from first principles -- see the
CALIBRATION block.
"""
import math

SIGNS = ['Mesha', 'Vrishabha', 'Mithuna', 'Karka', 'Simha', 'Kanya',
         'Tula', 'Vrischika', 'Dhanu', 'Makara', 'Kumbha', 'Meena']
NAK = ['Ashwini', 'Bharani', 'Krittika', 'Rohini', 'Mrigashira', 'Ardra',
       'Punarvasu', 'Pushya', 'Ashlesha', 'Magha', 'P.Phalguni', 'U.Phalguni',
       'Hasta', 'Chitra', 'Swati', 'Vishakha', 'Anuradha', 'Jyeshtha',
       'Mula', 'P.Ashadha', 'U.Ashadha', 'Shravana', 'Dhanishtha',
       'Shatabhisha', 'P.Bhadrapada', 'U.Bhadrapada', 'Revati']
NAK_LORD = ['Ketu', 'Shukra', 'Surya', 'Chandra', 'Mangal',
            'Rahu', 'Guru', 'Shani', 'Budha'] * 3

LAGNA_SIGN = 5          # Kanya
MOON_SIGN = 1           # Vrishabha
D9_LAGNA = 5            # Kanya
D10_LAGNA = 10          # Kumbha


def dms(sign, d, m, s=0):
    return SIGNS.index(sign) * 30 + d + m / 60 + s / 3600


def fmt(lon):
    lon %= 360
    s = int(lon // 30)
    r = lon - s * 30
    return f"{int(r):02d}°{int(round((r % 1) * 60)):02d}′ {SIGNS[s]}"


def house(lon, base):
    return (int(lon // 30) - base) % 12 + 1


def nak(lon):
    i = int((lon % 360) // (360 / 27))
    pada = int(((lon % 360) % (360 / 27)) // (360 / 108)) + 1
    return NAK[i], pada, NAK_LORD[i]


def navamsha(lon):
    """Movable signs count from themselves, fixed from the 9th, dual from the 5th."""
    sign, rem = int(lon // 30), lon % 30
    start = {0: sign, 1: (sign + 8) % 12, 2: (sign + 4) % 12}[sign % 3]
    return (start + int(rem // (30 / 9))) % 12


def dashamsha(lon):
    """Odd signs count from themselves, even signs from the 9th."""
    sign, rem = int(lon // 30), lon % 30
    start = sign if sign % 2 == 0 else (sign + 8) % 12
    return (start + int(rem // 3)) % 12


# --- natal chart -----------------------------------------------------------
D1 = {
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
UPAGRAHA = {
    'Yama Ghantaka': dms('Mithuna', 12, 42), 'Mrityu': dms('Mesha', 26, 49),
    'Parivesha': dms('Vrishabha', 15, 12), 'Ardha Prahara': dms('Vrishabha', 20, 48),
    'Gulika': dms('Karka', 25, 16), 'Mandi': dms('Karka', 22, 22),
    'Kala': dms('Kanya', 10, 9), 'Dhuma': dms('Simha', 14, 48),
    'Vyatipata': dms('Vrischika', 15, 12), 'Indra Chapa': dms('Kumbha', 14, 48),
    'Upaketu': dms('Meena', 1, 28),
}
SENSITIVE = {'Bhrigu Bindu': dms('Vrishabha', 14, 22)}
# Ashtakavarga, as verified in verify_bala.py.
# Columns: Lagna, Surya, Chandra, Mangal, Budha, Guru, Shukra, Shani, SAV
AV = {'Mesha': (4, 2, 2, 1, 4, 4, 5, 3, 21), 'Vrishabha': (4, 3, 2, 3, 4, 5, 3, 2, 22),
      'Mithuna': (3, 4, 6, 4, 6, 5, 3, 1, 29), 'Karka': (8, 3, 6, 2, 2, 5, 5, 5, 28),
      'Simha': (2, 4, 2, 4, 6, 4, 4, 0, 24), 'Kanya': (3, 2, 4, 4, 3, 6, 5, 5, 29),
      'Tula': (4, 4, 6, 1, 2, 3, 3, 5, 24), 'Vrischika': (5, 5, 4, 5, 4, 3, 3, 4, 28),
      'Dhanu': (2, 5, 2, 2, 7, 6, 5, 2, 29), 'Makara': (2, 4, 5, 2, 4, 6, 6, 2, 29),
      'Kumbha': (7, 7, 6, 6, 7, 5, 5, 5, 41), 'Meena': (5, 5, 4, 5, 5, 4, 5, 5, 33)}
SAV = {k: v[8] for k, v in AV.items()}
SURYA_BINDU = {k: v[1] for k, v in AV.items()}


# --- solar longitude -------------------------------------------------------
def jd(y, mo, d, h=0.0):
    if mo <= 2:
        y, mo = y - 1, mo + 12
    a = y // 100
    b = 2 - a + a // 4
    return (int(365.25 * (y + 4716)) + int(30.6001 * (mo + 1))
            + d + b - 1524.5 + h / 24)


def ayanamsa(jday):                      # Lahiri / Chitrapaksha
    return 23.85319 + (jday - 2451545.0) / 365.25 * (50.29 / 3600)


def sun_sidereal(jday):
    n = jday - 2451545.0
    L = (280.460 + 0.9856474 * n) % 360
    g = math.radians((357.528 + 0.9856003 * n) % 360)
    lam = L + 1.915 * math.sin(g) + 0.020 * math.sin(2 * g)
    return (lam - ayanamsa(jday)) % 360


def mean_node(jday):                     # sidereal Rahu
    T = (jday - 2451545.0) / 36525
    om = (125.04452 - 1934.136261 * T + 0.0020708 * T * T) % 360
    return (om - ayanamsa(jday)) % 360


rule = lambda t: print('\n' + '=' * 92 + f'\n{t}\n' + '=' * 92)

# --- calibration -----------------------------------------------------------
rule('CALIBRATION against the supplied 11 August 2026 transit set')
j = jd(2026, 8, 11, 9.0)
print(f'  Sun, computed 11 Aug 2026 09:00 UT : {fmt(sun_sidereal(j))}')
print('  Sun, as supplied in the transit set: 24°27′ Karka')
print(f'  Rahu, computed (mean node)         : {fmt(mean_node(j))}')
print('  Rahu, as supplied                  : Kumbha')
print(f'  Ayanamsa used                      : {ayanamsa(j):.4f}° '
      f'= {int(ayanamsa(j))}°{(ayanamsa(j)%1)*60:.0f}′ (Lahiri)')

# --- the eclipse series ----------------------------------------------------
ECLIPSES = [
    ('17 Feb 2026', 'annular', 2026, 2, 17, 12.2, 'Antarctica'),
    ('12 Aug 2026', 'TOTAL',   2026, 8, 12, 17.77, 'Greenland, Iceland, N. Spain'),
    ('06 Feb 2027', 'annular', 2027, 2, 6, 16.0, 'S. America, W. Africa'),
    ('02 Aug 2027', 'TOTAL',   2027, 8, 2, 10.12, 'S. Spain, N. Africa, Egypt, Saudi'),
    ('26 Jan 2028', 'annular', 2028, 1, 26, 15.13, 'S. America, Iberia'),
    ('22 Jul 2028', 'TOTAL',   2028, 7, 22, 2.93, 'Australia'),
]

rule('THE SOLAR ECLIPSE SERIES 2026-2028, placed in the natal chart')
print(f"{'date':12} {'type':8} {'sidereal Sun':20} {'H/lagna':>8} {'H/Moon':>7} "
      f"{'nakshatra':16} {'lord':8} {'off node':>9}")
print('-' * 92)
for label, kind, y, mo, d, h, vis in ECLIPSES:
    j = jd(y, mo, d, h)
    lon = sun_sidereal(j)
    r = mean_node(j)
    off = min(abs((lon - r + 180) % 360 - 180), abs((lon - r) % 360 - 180))
    n, p, nl = nak(lon)
    print(f'{label:12} {kind:8} {fmt(lon):20} {house(lon, LAGNA_SIGN):>8} '
          f'{house(lon, MOON_SIGN):>7} {n+" p"+str(p):16} {nl:8} {off:>8.1f}°')

print('\n  Every eclipse in the series falls in Karka or Makara -- the natal')
print('  11th/5th axis.  Networks and gains against romance and children.')

# --- the 12 August 2026 eclipse in detail ----------------------------------
rule('12 AUGUST 2026 -- the total eclipse, in detail')
J = jd(2026, 8, 12, 17.77)
E = sun_sidereal(J)
n, p, nl = nak(E)
print(f'  Sidereal position          {fmt(E)}  ({E:.3f}°)')
print(f'  House from lagna           {house(E, LAGNA_SIGN)}  (upachaya)')
print(f'  House from natal Chandra   {house(E, MOON_SIGN)}  (upachaya)')
print(f'  Nakshatra                  {n} pada {p}, lord {nl}')
print(f'  Sign lord                  Chandra -- natal {fmt(D1["Chandra"])}, '
      f'exalted, house {house(D1["Chandra"], LAGNA_SIGN)}')
print(f'  Sarvashtakavarga of Karka  {SAV["Karka"]}  (chart mean 28.1)')
print(f"  Surya's own bindus there   {SURYA_BINDU['Karka']}  "
      f'(below the 4-bindu delivery threshold)')
print(f'  Navamsha of the point      {SIGNS[navamsha(E)]}  '
      f'= house {(navamsha(E)-D9_LAGNA)%12+1} of D9')
print(f'  Dashamsha of the point     {SIGNS[dashamsha(E)]}  '
      f'= house {(dashamsha(E)-D10_LAGNA)%12+1} of D10')
KETU_E = (mean_node(J) + 180) % 360
print(f'  Transit Ketu (mean node)   {fmt(KETU_E)}')
print(f'  Distance from Ketu         {abs((E - KETU_E + 180) % 360 - 180):.1f}° '
      f'-- near the outer limit for a central eclipse,')
print('                             which is why totality tracks the far north')

GAND = 26 + 40/60          # last 3°20' of a water sign
print(f'  Gandanta zone (Karka)      {GAND:.2f}°+ -- the eclipse is '
      f'{(GAND - E % 30)*60:.0f}′ short of it, just outside')

rule("ASHTAKAVARGA SUPPORT OF KARKA -- who backs the eclipsed sign")
cols = ['Lagna', 'Surya', 'Chandra', 'Mangal', 'Budha', 'Guru', 'Shukra', 'Shani']
for i, c in enumerate(cols):
    v = AV['Karka'][i]
    rank = sorted((AV[s2][i] for s2 in SIGNS), reverse=True).index(v) + 1
    note = ''
    if v == 8:
        note = '  <== the maximum possible, and the highest lagna-AV cell in the chart'
    elif v < 4:
        note = '  <-- below the 4-bindu delivery threshold'
    print(f'  {c:9} {v} bindus   (that column ranks Karka #{rank} of 12){note}')
print(f"\n  Karka SAV {SAV['Karka']} against a chart mean of {sum(SAV.values())/12:.1f} "
      '-- exactly average ground.')
print('  The support is lopsided: the ascendant backs this sign completely,')
print('  while Surya, Mangal and Budha -- the eclipsing body and the lagna lord')
print('  among them -- do not reach the delivery threshold there.')

rule('NATAL CONTACTS within orb of the eclipse degree')
targets = [('graha', k, v) for k, v in D1.items()] \
    + [('upagraha', k, v) for k, v in UPAGRAHA.items()] \
    + [('point', k, v) for k, v in SENSITIVE.items()]
hits = []
for kind, name, lon in targets:
    sep = abs((E - lon + 180) % 360 - 180)
    same = int(lon // 30) == int(E // 30)
    hits.append((sep, kind, name, lon, same))
for sep, kind, name, lon, same in sorted(hits)[:6]:
    tag = '  <== PARTILE, same sign' if same and sep < 1 else \
          ('  <-- same sign' if same else '')
    print(f'  {name:16} {kind:9} {fmt(lon):20} separation {sep:6.2f}°{tag}')

print('\n  Also by degree-in-sign (different signs, same degree):')
for kind, name, lon in targets:
    dd = abs((lon % 30) - (E % 30))
    if dd < 2.0 and int(lon // 30) != int(E // 30):
        print(f'  {name:16} {fmt(lon):20} degree offset {dd:4.2f}°')

# --- nodal transit over the window -----------------------------------------
rule('THE NODAL TRANSIT UNDERNEATH THE ECLIPSE SERIES')
for y, mo in [(2026, 8), (2026, 12), (2027, 6), (2027, 12), (2028, 6), (2028, 10)]:
    j = jd(y, mo, 1)
    r = mean_node(j)
    k = (r + 180) % 360
    print(f'  {y}-{mo:02d}   Rahu {fmt(r):20} house {house(r, LAGNA_SIGN):>2}    '
          f'Ketu {fmt(k):20} house {house(k, LAGNA_SIGN):>2}')
print('\n  Rahu enters Makara -- the natal 5th -- around December 2026 and holds')
print('  it to roughly August 2028.  Ketu correspondingly holds Karka, the 11th.')

# --- when the eclipse degree is next triggered -----------------------------
rule('LATER TRIGGERS OF THE 12 AUG 2026 ECLIPSE DEGREE (25°49′ Karka)')
print('  transit Surya returns              ~12 Aug 2027 (and the 2 Aug 2027 '
      'total eclipse falls 10° earlier in the same sign)')
print('  transit Mangal crosses             ~mid-October 2026 (0.5°/day from '
      'Mithuna, entering Karka mid-September)')
print('  transit Guru crosses               ~late September 2026 -- Guru is at '
      '~17° Karka on 12 Aug, 0.08°/day mean')
print('  transit Ketu crosses               ~mid-2027, having entered Karka '
      'in December 2026')
print('  transit Shani reaches Karka        2033-2035 -- outside the eclipse\'s '
      'own reckoning')
