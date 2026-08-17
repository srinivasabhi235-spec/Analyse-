#!/usr/bin/env python3
"""
How uncommon is this chart, actually?

"Unique" is a claim about frequency, so it is testable.  This generates a large
population of synthetic charts under a realistic null model and measures how
often each of this chart's notable features occurs.

NULL MODEL, stated honestly:
  - Lagna and the slow grahas (Mangal, Guru, Shani, Rahu) uniform on the circle.
  - Rahu and Ketu exactly 180 degrees apart, as in reality.
  - Chandra uniform.
  - Budha and Shukra constrained to their real maximum elongations from Surya
    (28 and 47 degrees), because uniform placement would badly overstate how
    often they scatter away from the Sun -- and this chart's tightest feature
    is a cluster.

That is a fair null for sign-and-house questions.  It ignores the fact that the
outer grahas move slowly (so real charts from one era correlate), which would
if anything make tight clusters MORE common than modelled, not less.
"""
import random

random.seed(20260812)
N = 200_000
SIGNS = ['Mesha', 'Vrishabha', 'Mithuna', 'Karka', 'Simha', 'Kanya',
         'Tula', 'Vrischika', 'Dhanu', 'Makara', 'Kumbha', 'Meena']
LORD = ['Mangal', 'Shukra', 'Budha', 'Chandra', 'Surya', 'Budha',
        'Shukra', 'Mangal', 'Guru', 'Shani', 'Shani', 'Guru']
NAK_LORD = ['Ketu', 'Shukra', 'Surya', 'Chandra', 'Mangal',
            'Rahu', 'Guru', 'Shani', 'Budha'] * 3
EXAL = {'Surya': 0, 'Chandra': 1, 'Mangal': 9, 'Budha': 5,
        'Guru': 3, 'Shukra': 11, 'Shani': 6}
RAKSHASA = {3, 9, 10, 14, 16, 18, 19, 23, 24}
ASPECT = {'Mangal': [4, 7, 8], 'Guru': [5, 7, 9], 'Shani': [3, 7, 10],
          'Rahu': [5, 7, 9], 'Ketu': [5, 7, 9]}
CLASSICAL = ['Surya', 'Chandra', 'Mangal', 'Budha', 'Guru', 'Shukra', 'Shani']
ALL9 = CLASSICAL + ['Rahu', 'Ketu']


def dms(s, d, m, sec=0):
    return SIGNS.index(s) * 30 + d + m / 60 + sec / 3600


REAL = {'Lagna': dms('Kanya', 27, 37, 37), 'Surya': dms('Mesha', 1, 28, 3),
        'Chandra': dms('Vrishabha', 1, 47, 15), 'Mangal': dms('Vrishabha', 7, 19, 32),
        'Budha': dms('Mesha', 10, 27, 50), 'Guru': dms('Mithuna', 14, 47, 52),
        'Shukra': dms('Mesha', 23, 36, 49), 'Shani': dms('Vrishabha', 17, 54, 25),
        'Rahu': dms('Vrishabha', 26, 55, 52), 'Ketu': dms('Vrischika', 26, 55, 52)}

sgn = lambda l: int(l // 30) % 12
nak = lambda l: int((l % 360) // (360 / 27))
nav = lambda l: int((l % 360) * 9 / 30) % 12


def make():
    su = random.uniform(0, 360)
    c = {'Surya': su,
         'Budha': (su + random.uniform(-28, 28)) % 360,
         'Shukra': (su + random.uniform(-47, 47)) % 360,
         'Chandra': random.uniform(0, 360),
         'Mangal': random.uniform(0, 360),
         'Guru': random.uniform(0, 360),
         'Shani': random.uniform(0, 360),
         'Lagna': random.uniform(0, 360)}
    r = random.uniform(0, 360)
    c['Rahu'], c['Ketu'] = r, (r + 180) % 360
    return c


# ---------------------------------------------------------------- features --
def house(c, g):
    return (sgn(c[g]) - sgn(c['Lagna'])) % 12 + 1


def f_three_signs(c):
    return len({sgn(c[g]) for g in CLASSICAL}) <= 3


def f_span(c):
    """Seven classical grahas inside a 75-degree arc."""
    xs = sorted(c[g] % 360 for g in CLASSICAL)
    best = 360.0
    for i in range(7):
        lo = xs[i]
        arc = max((x - lo) % 360 for x in xs)
        best = min(best, arc)
    return best <= 75


def f_one_kendra(c):
    return len({house(c, g) for g in CLASSICAL} & {1, 4, 7, 10}) <= 1


def f_disp_mismatch(c):
    return all(LORD[sgn(c[g])] != NAK_LORD[nak(c[g])] for g in ALL9)


def f_both_lum_exalted(c):
    return sgn(c['Surya']) == 0 and sgn(c['Chandra']) == 1


def f_lum_exalted_weak_avastha(c):
    if not f_both_lum_exalted(c):
        return False
    # Surya in Bala (odd sign, first 6 deg); Chandra in Mrita (even sign, first 6)
    return (c['Surya'] % 30) < 6 and (c['Chandra'] % 30) < 6


def f_lagna_and_sun_vargottama(c):
    return sgn(c['Lagna']) == nav(c['Lagna']) and sgn(c['Surya']) == nav(c['Surya'])


def f_sun_exal_varg_gandanta(c):
    return (sgn(c['Surya']) == 0 and nav(c['Surya']) == 0
            and (c['Surya'] % 30) <= 3 + 20 / 60)


def f_both_personal_rakshasa(c):
    return (nak(c['Lagna']) + 1 in RAKSHASA) and (nak(c['Chandra']) + 1 in RAKSHASA)


def f_nak_parivartana(c):
    for i, a in enumerate(ALL9):
        for b in ALL9[i + 1:]:
            if NAK_LORD[nak(c[a])] == b and NAK_LORD[nak(c[b])] == a:
                return True
    return False


def f_own_nakshatra(c):
    return any(NAK_LORD[nak(c[g])] == g for g in ALL9)


def f_no_aspect_on_8th(c):
    s8 = (sgn(c['Lagna']) + 7) % 12
    for g in ALL9:
        for o in ASPECT.get(g, [7]):
            if (sgn(c[g]) + o - 1) % 12 == s8:
                return False
    return True


def f_8th_9th_parivartana(c):
    lag = sgn(c['Lagna'])
    l8, l9 = LORD[(lag + 7) % 12], LORD[(lag + 8) % 12]
    if l8 == l9:
        return False
    return (sgn(c[l8]) == (lag + 8) % 12) and (sgn(c[l9]) == (lag + 7) % 12)


def f_seven_in_two_houses(c):
    from collections import Counter
    ct = Counter(house(c, g) for g in ALL9)
    top = ct.most_common(2)
    if len(top) < 2:
        return True
    return (top[0][1] + top[1][1] >= 7 and abs(top[0][0] - top[1][0]) == 1)


def f_no_water(c):
    return all(sgn(c[g]) % 4 != 3 for g in CLASSICAL)


def _nav(l):
    sign, rem = int(l // 30) % 12, l % 30
    return ({0: sign, 1: (sign + 8) % 12, 2: (sign + 4) % 12}[sign % 3]
            + int(rem // (30 / 9))) % 12


def _d10(l):
    s, p = int(l // 30) % 12, l % 30
    return ((s if s % 2 == 0 else (s + 8) % 12) + int(p / 3)) % 12


def _d12(l):
    return (int(l // 30) % 12 + int((l % 30) / 2.5)) % 12


def _d30(l):
    s, p = int(l // 30) % 12, l % 30
    lim = ([(5, 0), (10, 10), (18, 8), (25, 2), (30, 6)] if s % 2 == 0
           else [(5, 1), (12, 5), (20, 11), (25, 9), (30, 7)])
    for hi, sg_ in lim:
        if p < hi:
            return sg_
    return lim[-1][1]


def f_sun_exal_many_vargas(c):
    """Surya exalted in D1, D9, D10, D12 and D30 simultaneously."""
    l = c['Surya']
    return (int(l // 30) % 12 == 0 and _nav(l) == 0 and _d10(l) == 0
            and _d12(l) == 0 and _d30(l) == 0)


def f_both_rajayoga_houses_in_8th(c):
    """9th lord, 10th lord AND 12th lord all sitting in the 8th house."""
    lag = int(c['Lagna'] // 30) % 12
    s8 = (lag + 7) % 12
    l9, l10, l12 = (LORD[(lag + 8) % 12], LORD[(lag + 9) % 12],
                    LORD[(lag + 11) % 12])
    return all(sgn(c[g]) == s8 for g in {l9, l10, l12})


FEATURES = [
 ('Surya exalted in D1, D9, D10, D12 and D30 at once', f_sun_exal_many_vargas),
 ('9th, 10th and 12th lords ALL in the 8th house', f_both_rajayoga_houses_in_8th),
 ('Seven classical grahas in 3 signs or fewer', f_three_signs),
 ('Seven classical grahas inside a 75-degree arc', f_span),
 ('At most one kendra occupied', f_one_kendra),
 ('No graha in any water sign', f_no_water),
 ('Some graha in its own nakshatra', f_own_nakshatra),
 ('A nakshatra parivartana exists', f_nak_parivartana),
 ('Nothing aspects the 8th house', f_no_aspect_on_8th),
 ('Both luminaries exalted', f_both_lum_exalted),
 ('Both personal points in Rakshasa gana', f_both_personal_rakshasa),
 ('Lagna AND Surya both vargottama', f_lagna_and_sun_vargottama),
 ('8th lord and 9th lord in mutual exchange', f_8th_9th_parivartana),
 ('Seven of nine grahas in two adjacent houses', f_seven_in_two_houses),
 ('Sign lord != star lord for ALL NINE grahas', f_disp_mismatch),
 ('Both luminaries exalted AND both weak by avastha', f_lum_exalted_weak_avastha),
 ('Surya exalted AND vargottama AND gandanta', f_sun_exal_varg_gandanta),
]

print('=' * 92)
print(f'RARITY BY MONTE CARLO — {N:,} synthetic charts')
print('=' * 92)
print('\nFirst: confirm each feature is actually true of the real chart.\n')
for name, fn in FEATURES:
    print(f'  {"YES" if fn(REAL) else "*** NO ***":12} {name}')

counts = {name: 0 for name, _ in FEATURES}
for _ in range(N):
    c = make()
    for name, fn in FEATURES:
        if fn(c):
            counts[name] += 1

print('\n' + '=' * 92)
print('FREQUENCY IN THE SYNTHETIC POPULATION')
print('=' * 92)
print(f'\n  {"feature":52}{"frequency":>12}   about 1 in')
rows = sorted(FEATURES, key=lambda x: counts[x[0]])
for name, _ in rows:
    k = counts[name]
    pct = 100 * k / N
    one_in = f'{N/k:,.0f}' if k else f'>{N:,}'
    star = '  <==' if k and N / k >= 1000 else ''
    print(f'  {name:52}{pct:>11.3f}%   {one_in:>9}{star}')

print('\n' + '=' * 92)
print('THE COMBINATION')
print('=' * 92)
rare = [(n, f) for n, f in FEATURES if counts[n] and N / counts[n] >= 100]
print(f'\n  Features occurring in fewer than 1 chart in 100:')
for n, _ in rare:
    print(f'    - {n}  (1 in {N/counts[n]:,.0f})')

# measure the JOINT frequency empirically rather than assuming independence
joint = 0
for _ in range(N):
    c = make()
    if all(f(c) for _, f in rare):
        joint += 1
print(f'\n  Charts carrying ALL {len(rare)} of them simultaneously, measured')
print(f'  directly rather than multiplied out: {joint} of {N:,}')
if joint:
    print(f'  = about 1 in {N/joint:,.0f}')
else:
    print(f'  = ZERO occurrences.  The true rate is below 1 in {N:,}; this')
    print('    simulation cannot resolve it further.')

print('\n  AND THE DEFLATIONS, which matter just as much:')
common = sorted(((counts[n], n) for n, _ in FEATURES if counts[n] / N > 0.10),
                reverse=True)
for k, n in common:
    print(f'    {100*k/N:5.1f}%  {n}')
print('\n  Those are ORDINARY.  Any reading that presents them as remarkable')
print('  is overselling, and this reading did exactly that for the')
print('  dispositor-mismatch figure.')
print('\n  CAVEAT worth stating: a uniform null overstates rarity for features')
print('  driven by slow grahas, because real charts from one era share Guru')
print('  and Shani positions.  It understates it for nothing here.  Read the')
print('  numbers as order-of-magnitude, not as precise odds.')
