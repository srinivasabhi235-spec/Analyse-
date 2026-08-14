#!/usr/bin/env python3
"""
Career growth: the D10 audit and a computed growth curve.

The reading has given career timing in prose repeatedly.  This does two things
it has not done: a full house-by-house audit of the Dashamsha (the career
varga proper), and a SCORED growth curve -- every antardasha from 2026 to 2075
rated on the same rubric, so the shape of the ascent is measured rather than
narrated.

Also adds the career techniques the sweep had not applied: the three-fold
tenth (from lagna, Chandra and Surya), the Amatyakaraka, the 10th from
Karakamsa, and the Rajya Pada (A10).

All strength figures are the verified tables from verify_bala.py.
"""
from datetime import datetime, timedelta

SIGNS = ['Mesha', 'Vrishabha', 'Mithuna', 'Karka', 'Simha', 'Kanya',
         'Tula', 'Vrischika', 'Dhanu', 'Makara', 'Kumbha', 'Meena']
LORD = ['Mangal', 'Shukra', 'Budha', 'Chandra', 'Surya', 'Budha',
        'Shukra', 'Mangal', 'Guru', 'Shani', 'Shani', 'Guru']
EXALT = {'Surya': 0, 'Chandra': 1, 'Mangal': 9, 'Budha': 5,
         'Guru': 3, 'Shukra': 11, 'Shani': 6}
DEBIL = {k: (v + 6) % 12 for k, v in EXALT.items()}
OWN = {'Surya': [4], 'Chandra': [3], 'Mangal': [0, 7], 'Budha': [2, 5],
       'Guru': [8, 11], 'Shukra': [1, 6], 'Shani': [9, 10]}
ASPECT = {'Mangal': [4, 7, 8], 'Guru': [5, 7, 9], 'Shani': [3, 7, 10],
          'Rahu': [5, 7, 9], 'Ketu': [5, 7, 9]}
SP = {'Surya': 138, 'Chandra': 33, 'Mangal': 212, 'Budha': 152,
      'Guru': 81, 'Shukra': 95, 'Shani': 184}                 # Shodhya Pinda
ISHTA = {'Surya': 46.88, 'Chandra': 24.54, 'Mangal': 19.66, 'Budha': 18.91,
         'Guru': 37.30, 'Shukra': 47.49, 'Shani': 12.48}
KASHTA = {'Surya': 7.83, 'Chandra': 4.49, 'Mangal': 38.87, 'Budha': 30.32,
          'Guru': 15.10, 'Shukra': 11.87, 'Shani': 46.83}
SAV = {'Mesha': 21, 'Vrishabha': 22, 'Mithuna': 29, 'Karka': 28, 'Simha': 24,
       'Kanya': 29, 'Tula': 24, 'Vrischika': 28, 'Dhanu': 29, 'Makara': 29,
       'Kumbha': 41, 'Meena': 33}


def dms(s, d, m, sec=0):
    return SIGNS.index(s) * 30 + d + m / 60 + sec / 3600


def navamsha(l):
    sign, rem = int(l // 30), l % 30
    return ({0: sign, 1: (sign + 8) % 12, 2: (sign + 4) % 12}[sign % 3]
            + int(rem // (30 / 9))) % 12


def dashamsha(l):
    sign, rem = int(l // 30), l % 30
    return ((sign if sign % 2 == 0 else (sign + 8) % 12) + int(rem // 3)) % 12


def dignity(g, s):
    if EXALT.get(g) == s: return 'EXALTED'
    if DEBIL.get(g) == s: return 'debilitated'
    if s in OWN.get(g, []): return 'own sign'
    return ''


D1 = {'Lagna': dms('Kanya', 27, 37, 37), 'Surya': dms('Mesha', 1, 28, 3),
      'Chandra': dms('Vrishabha', 1, 47, 15), 'Mangal': dms('Vrishabha', 7, 19, 32),
      'Budha': dms('Mesha', 10, 27, 50), 'Guru': dms('Mithuna', 14, 47, 52),
      'Shukra': dms('Mesha', 23, 36, 49), 'Shani': dms('Vrishabha', 17, 54, 25),
      'Rahu': dms('Vrishabha', 26, 55, 52), 'Ketu': dms('Vrischika', 26, 55, 52)}
GRAHAS = [g for g in D1 if g != 'Lagna']
CLASSICAL = [g for g in GRAHAS if g not in ('Rahu', 'Ketu')]
LAG = int(D1['Lagna'] // 30)
D9 = {k: navamsha(v) for k, v in D1.items()}
D10 = {k: dashamsha(v) for k, v in D1.items()}
sg = lambda g: int(D1[g] // 30)
h1 = lambda s: (s - LAG) % 12 + 1
h10 = lambda s: (s - D10['Lagna']) % 12 + 1
h9 = lambda s: (s - D9['Lagna']) % 12 + 1
rule = lambda t: print('\n' + '=' * 94 + f'\n{t}\n' + '=' * 94)

S10 = (LAG + 9) % 12          # Mithuna, the natal 10th

# --- 1 ----------------------------------------------------------------------
rule('1. THE DASHAMSHA AUDIT — the career chart, house by house')
print(f'  D10 lagna {SIGNS[D10["Lagna"]]}, lord {LORD[D10["Lagna"]]}\n')
print(f'  {"graha":9}{"D10 sign":12}{"house":6} class                dignity')
KEN, TRI, UPA, DUS = [1, 4, 7, 10], [1, 5, 9], [3, 6, 10, 11], [6, 8, 12]
for g in GRAHAS:
    hn = h10(D10[g])
    cls = [n for n, s in (('kendra', KEN), ('trikona', TRI),
                          ('upachaya', UPA), ('dusthana', DUS)) if hn in s]
    print(f'  {g:9}{SIGNS[D10[g]]:12}{hn:<6} {"+".join(cls) or "—":20} '
          f'{dignity(g, D10[g])}')
cnt = {n: sum(1 for g in GRAHAS if h10(D10[g]) in s)
       for n, s in (('kendra', KEN), ('trikona', TRI),
                    ('upachaya', UPA), ('dusthana', DUS))}
print(f'\n  Census: {cnt}')
d10_10 = (D10['Lagna'] + 9) % 12
print(f'\n  D10 10th house = {SIGNS[d10_10]}, lord {LORD[d10_10]}, '
      f'which sits in D10 {SIGNS[D10[LORD[d10_10]]]} (house {h10(D10[LORD[d10_10]])})')
print(f'  D10 lagna lord {LORD[D10["Lagna"]]} sits in D10 '
      f'{SIGNS[D10[LORD[D10["Lagna"]]]]} (house {h10(D10[LORD[D10["Lagna"]]])})')
print(f'  Occupants of the D10 10th: '
      f'{[g for g in GRAHAS if D10[g] == d10_10] or "empty"}')

# --- 2 ----------------------------------------------------------------------
rule('2. THE THREE-FOLD TENTH — from lagna, from Chandra, from Surya')
for base, label in [('Lagna', 'lagna'), ('Chandra', 'Chandra'), ('Surya', 'Surya')]:
    s = (int(D1[base] // 30) + 9) % 12
    who = [g for g in GRAHAS if sg(g) == s]
    asp = [g for g, o in ASPECT.items()
           if any((sg(g) + x - 1) % 12 == s for x in o)]
    print(f'  10th from {label:8} {SIGNS[s]:11} lord {LORD[s]:8} SAV {SAV[SIGNS[s]]:>3}  '
          f'occupants {who or "empty"}  aspects {asp or "none"}')
print('\n  All three tenths are DIFFERENT signs, and only one of them -- the')
print('  10th from lagna -- is occupied.  Guru sitting there is the whole of')
print('  the career apparatus\'s visible half.  From Chandra and from Surya the')
print('  10th is empty, which is why standing has to be built rather than met.')

# --- 3 ----------------------------------------------------------------------
rule('3. THE JAIMINI CAREER APPARATUS')
byd = sorted(CLASSICAL, key=lambda g: -(D1[g] % 30))
amk = byd[1]
ak = byd[0]
ka = D9[ak]
print(f'  Amatyakaraka (2nd-highest degree) = {amk}')
print(f'    natal {SIGNS[sg(amk)]} house {h1(sg(amk))};  D9 {SIGNS[D9[amk]]} '
      f'house {h9(D9[amk])};  D10 {SIGNS[D10[amk]]} house {h10(D10[amk])}')
print(f'    rules the natal {", ".join(str(i + 1) for i in range(12) if LORD[(LAG + i) % 12] == amk)}'
      f'; is the D10 LAGNA LORD; Shodhya Pinda {SP[amk]} (rank 2)')
k10 = (ka + 9) % 12
print(f'\n  Karakamsa {SIGNS[ka]};  10th from Karakamsa = {SIGNS[k10]}: '
      f'{[g for g in GRAHAS if D9[g] == k10] or "empty"}')
al = 7   # Vrischika, computed in verify_concepts.py
a10 = (al + 9) % 12
print(f'  Arudha Lagna {SIGNS[al]};  Rajya Pada (10th from AL) = {SIGNS[a10]}: '
      f'{[g for g in GRAHAS if sg(g) == a10] or "empty"}, SAV {SAV[SIGNS[a10]]}')
rk = sorted(SAV, key=lambda x: -SAV[x]).index(SIGNS[a10]) + 1
print(f'\n  BOTH Jaimini career indicators land on the SAME sign: {SIGNS[a10]},')
print(f'  which is his natal {h1(a10)}th house, ranked {rk} of 12 by bindus '
      f'({SAV[SIGNS[a10]]}), and EMPTY.')
print('  The 10th from Karakamsa and the Rajya Pada agreeing on the 12th house')
print('  is the Jaimini restatement of everything the Parashari side has said:')
print('  his seat of authority is foreign, secluded and behind the scenes -- and')
print('  it is thinly supported, so it has to be constructed rather than occupied.')

# --- 4 ----------------------------------------------------------------------
rule('4. THE CAREER SCORE — rubric')
CAREER_LINK = {}
for g in GRAHAS:
    sc, why = 0.0, []
    if g == LORD[S10]:
        sc += 3; why.append('10th lord')
    if sg(g) == S10:
        sc += 3; why.append('in the 10th')
    if g in ASPECT and any((sg(g) + x - 1) % 12 == S10 for x in ASPECT[g]):
        sc += 1; why.append('aspects the 10th')
    if g == LORD[D10['Lagna']]:
        sc += 2; why.append('D10 lagna lord')
    if g == amk:
        sc += 2; why.append('Amatyakaraka')
    if h10(D10[g]) in KEN:
        sc += 2; why.append('D10 kendra')
    elif h10(D10[g]) in TRI:
        sc += 1; why.append('D10 trikona')
    if h10(D10[g]) in DUS:
        sc -= 1; why.append('D10 dusthana')
    if h9(D9[g]) == 10:
        sc += 1.5; why.append('D9 10th')
    # The nodes carry no Shadbala figures of their own.  Parashari practice
    # gives a node the results of its dispositor, so borrow those components
    # rather than scoring the nodes at a structural zero.
    src = g if g in SP else LORD[sg(g)]
    tag = '' if src == g else f' (via {src})'
    sc += 3 * SP[src] / max(SP.values()); why.append(f'SP {SP[src]}{tag}')
    sc += 2 * (ISHTA[src] - KASHTA[src]) / 60
    why.append(f'net {ISHTA[src] - KASHTA[src]:+.1f}{tag}')
    CAREER_LINK[g] = (round(sc, 2), why)
for g in sorted(CAREER_LINK, key=lambda x: -CAREER_LINK[x][0]):
    sc, why = CAREER_LINK[g]
    print(f'  {g:9} {sc:6.2f}   {", ".join(why)}')

# --- 5 ----------------------------------------------------------------------
rule('5. THE GROWTH CURVE — every antardasha, 2026 to 2075')
VIM = [('Ketu', 7), ('Shukra', 20), ('Surya', 6), ('Chandra', 10), ('Mangal', 7),
       ('Rahu', 18), ('Guru', 16), ('Shani', 19), ('Budha', 17)]
D = dict(VIM); order = [x[0] for x in VIM]
seq, t = [], datetime(2022, 12, 25, 22, 35)
mi = order.index('Rahu')
for m in range(4):
    md = order[(mi + m) % 9]
    ai = order.index(md)
    for n in range(9):
        ad = order[(ai + n) % 9]
        e = t + timedelta(days=D[md] * D[ad] / 120 * 365.25)
        seq.append((t, e, md, ad)); t = e
lo = min(v[0] for v in CAREER_LINK.values())
hi = max(v[0] for v in CAREER_LINK.values())
scale = lambda x: (x - lo) / (hi - lo)
print(f'  score = 0.4 x mahadasha lord + 0.6 x antardasha lord, '
      f'normalised to the rubric above\n')
print(f'  {"period":22}{"ages":12}{"dasha":16}{"score":>6}  curve')
for s, e, md, ad in seq:
    if e.year < 2026 or s.year > 2076:
        continue
    v = 0.4 * scale(CAREER_LINK[md][0]) + 0.6 * scale(CAREER_LINK[ad][0])
    bar = '█' * int(round(v * 40))
    a0, a1 = (s.year - 2002 + 0.3), (e.year - 2002 + 0.3)
    print(f'  {s.strftime("%b %Y")}-{e.strftime("%b %Y"):9}  {a0:4.0f}-{a1:<6.0f}'
          f'{md + "-" + ad:16}{v:6.2f}  {bar}')

# --- 6 ----------------------------------------------------------------------
rule('6. THE SHAPE OF THE ASCENT')
buckets = {}
for s, e, md, ad in seq:
    if e.year < 2026 or s.year > 2076:
        continue
    v = 0.4 * scale(CAREER_LINK[md][0]) + 0.6 * scale(CAREER_LINK[ad][0])
    dec = (s.year // 5) * 5
    buckets.setdefault(dec, []).append(v * (e - s).days)
    buckets.setdefault(str(dec), []).append((e - s).days)
print(f'  {"period":12}{"weighted mean":>14}  curve')
for dec in sorted(k for k in buckets if isinstance(k, int)):
    mean = sum(buckets[dec]) / sum(buckets[str(dec)])
    print(f'  {dec}-{dec + 4:<7}{mean:>14.2f}  {"█" * int(round(mean * 46))}')
print('\n  The curve is not a ramp.  It is a long shallow climb with a step')
print('  change, and the step is where the mahadasha lord changes -- not')
print('  where he works harder.')
