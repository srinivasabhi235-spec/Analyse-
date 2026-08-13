#!/usr/bin/env python3
"""
The 8th house: a full dossier.

The reading has repeatedly called the 8th this chart's engine without ever
auditing the house itself.  This computes what is actually in it, what routes
through it, how weak it measures, what its lord is doing, how it repeats across
the vargas, and when its apparatus matures -- so the transformation mechanism
is demonstrated rather than asserted.

Vargas are recomputed from the verified D1 longitudes; D9, D10, D27 and D30 all
reproduce the supplied charts exactly (checked in verify_chart.py).
"""
SIGNS = ['Mesha', 'Vrishabha', 'Mithuna', 'Karka', 'Simha', 'Kanya',
         'Tula', 'Vrischika', 'Dhanu', 'Makara', 'Kumbha', 'Meena']
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
DEBIL = {k: (v + 6) % 12 for k, v in EXALT.items()}
OWN = {'Surya': [4], 'Chandra': [3], 'Mangal': [0, 7], 'Budha': [2, 5],
       'Guru': [8, 11], 'Shukra': [1, 6], 'Shani': [9, 10]}
ASPECT = {'Mangal': [4, 7, 8], 'Guru': [5, 7, 9], 'Shani': [3, 7, 10],
          'Rahu': [5, 7, 9], 'Ketu': [5, 7, 9]}
MATURITY = {'Guru': 16, 'Surya': 22, 'Chandra': 24, 'Shukra': 25,
            'Mangal': 28, 'Budha': 32, 'Shani': 36, 'Rahu': 42, 'Ketu': 48}
# Ashtakavarga, verified in verify_bala.py. Lagna,Su,Ch,Ma,Bu,Gu,Sk,Sa,SAV
AV = {'Mesha': (4, 2, 2, 1, 4, 4, 5, 3, 21), 'Vrishabha': (4, 3, 2, 3, 4, 5, 3, 2, 22),
      'Mithuna': (3, 4, 6, 4, 6, 5, 3, 1, 29), 'Karka': (8, 3, 6, 2, 2, 5, 5, 5, 28),
      'Simha': (2, 4, 2, 4, 6, 4, 4, 0, 24), 'Kanya': (3, 2, 4, 4, 3, 6, 5, 5, 29),
      'Tula': (4, 4, 6, 1, 2, 3, 3, 5, 24), 'Vrischika': (5, 5, 4, 5, 4, 3, 3, 4, 28),
      'Dhanu': (2, 5, 2, 2, 7, 6, 5, 2, 29), 'Makara': (2, 4, 5, 2, 4, 6, 6, 2, 29),
      'Kumbha': (7, 7, 6, 6, 7, 5, 5, 5, 41), 'Meena': (5, 5, 4, 5, 5, 4, 5, 5, 33)}
COLS = ['Lagna', 'Surya', 'Chandra', 'Mangal', 'Budha', 'Guru', 'Shukra', 'Shani']


def dms(s, d, m, sec=0):
    return SIGNS.index(s) * 30 + d + m / 60 + sec / 3600


def fmt(l):
    return f"{int(l % 30):02d}°{round((l % 1) * 60):02d}′ {SIGNS[int(l // 30)]}"


def nak_of(l):
    i = int(l // (360 / 27))
    return NAK[i], int((l % (360 / 27)) // (360 / 108)) + 1, NAK_LORD[i]


def varga(l, n):
    """D9, D10, D27, D30 -- the divisions this chart's sources supply."""
    sign, rem = int(l // 30), l % 30
    if n == 9:
        start = {0: sign, 1: (sign + 8) % 12, 2: (sign + 4) % 12}[sign % 3]
        return (start + int(rem // (30 / 9))) % 12
    if n == 10:
        start = sign if sign % 2 == 0 else (sign + 8) % 12
        return (start + int(rem // 3)) % 12
    if n == 27:
        start = {0: 0, 1: 3, 2: 6, 3: 9}[sign % 4]
        return (start + int(rem // (30 / 27))) % 12
    if n == 30:
        odd = [(5, 0), (10, 10), (18, 8), (25, 2), (30, 6)]
        even = [(5, 1), (12, 5), (20, 11), (25, 9), (30, 7)]
        for lim, sg in (odd if sign % 2 == 0 else even):
            if rem < lim:
                return sg
    raise ValueError(n)


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
UPAGRAHA = {'Mrityu': dms('Mesha', 26, 49), 'Yama Ghantaka': dms('Mithuna', 12, 42),
            'Gulika': dms('Karka', 25, 16), 'Mandi': dms('Karka', 22, 22),
            'Kala': dms('Kanya', 10, 9), 'Dhuma': dms('Simha', 14, 48),
            'Parivesha': dms('Vrishabha', 15, 12), 'Upaketu': dms('Meena', 1, 28),
            'Ardha Prahara': dms('Vrishabha', 20, 48), 'Vyatipata': dms('Vrischika', 15, 12),
            'Indra Chapa': dms('Kumbha', 14, 48)}
GRAHAS = [g for g in D1 if g != 'Lagna']
LAG = int(D1['Lagna'] // 30)
S8 = (LAG + 7) % 12
h = lambda s: (s - LAG) % 12 + 1
sign_of = lambda g: int(D1[g] // 30)
occ = lambda s: [g for g in GRAHAS if sign_of(g) == s]

rule = lambda t: print('\n' + '=' * 90 + f'\n{t}\n' + '=' * 90)

# --- 1 ---------------------------------------------------------------------
rule('1. WHAT IS ACTUALLY IN THE 8TH')
print(f'  8th house = {SIGNS[S8]}, lord {LORD[S8]}\n')
for g in occ(S8):
    n, p, nl = nak_of(D1[g])
    rules = [str(i + 1) for i in range(12) if LORD[(LAG + i) % 12] == g]
    print(f'  {g:8} {fmt(D1[g]):16} {dignity(g, S8):12} {n} p{p} (lord {nl})')
    print(f'  {"":8} rules house(s) {"+".join(rules)}   matures at age {MATURITY[g]}')
print(f'\n  Upagrahas in the 8th: '
      f'{[k for k, v in UPAGRAHA.items() if int(v // 30) == S8]}')
asp = [g for g, o in ASPECT.items() if any((sign_of(g) + x - 1) % 12 == S8 for x in o)]
asp += [g for g in GRAHAS if g not in ASPECT and (sign_of(g) + 6) % 12 == S8]
print(f'  Aspects onto the 8th: {asp or "NONE"}')
print('\n  No graha in the chart casts a drishti onto Mesha.  The 8th receives')
print('  zero external support and zero external interference: a sealed chamber')
print('  holding the lagna lord, the Atmakaraka and the exalted Sun.  Whatever')
print('  happens in there is settled in there.')

# --- 2 ---------------------------------------------------------------------
rule('2. HOW MUCH OF THE CHART ROUTES THROUGH IT')
inside, ruled = [], []
for i in range(12):
    lord = LORD[(LAG + i) % 12]
    if sign_of(lord) == S8:
        inside.append((i + 1, lord))
    if lord == LORD[S8]:
        ruled.append(i + 1)
print('  Houses whose LORD SITS IN the 8th:')
for hn, l in inside:
    print(f'    house {hn:<2} -> lord {l}')
print(f'\n  The 8th lord {LORD[S8]} also rules house(s) '
      f'{", ".join(str(x) for x in ruled if x != 8)}')
tot = sorted({hn for hn, _ in inside} | set(ruled))
print(f'\n  Total houses tied to the 8th: {tot}  -> {len(tot)} of 12')
print('  Self, wealth-and-family, courage, dharma-and-father, career, and loss')
print('  all deliver through the house of upheaval.  This is not one house among')
print('  twelve here -- it is the processing plant for half the chart.')

# --- 3 ---------------------------------------------------------------------
rule('3. HOW WEAK THE HOUSE MEASURES')
sav = {k: v[8] for k, v in AV.items()}
rank = sorted(sav, key=lambda k: -sav[k]).index(SIGNS[S8]) + 1
print(f'  Sarvashtakavarga of {SIGNS[S8]}: {sav[SIGNS[S8]]}  '
      f'-- rank {rank} of 12, the LOWEST in the chart')
print(f'  Bhava Bala rank: 12 of 12 (weakest bhava, from the supplied table)\n')
for i, c in enumerate(COLS):
    v = AV[SIGNS[S8]][i]
    r = sorted((AV[s][i] for s in SIGNS), reverse=True).index(v) + 1
    flag = '  <-- below the 4-bindu delivery threshold' if v < 4 else ''
    lowest = min(AV[x][i] for x in SIGNS)
    extra = ("  <== its OWN lord's joint-lowest cell in the whole ashtakavarga"
             if c == 'Mangal' and v == lowest else '')
    print(f'  {c:9} {v} bindus  (ranks {SIGNS[S8]} #{r} of 12){flag}{extra}')
print('\n  The chart\'s best-dignified graha (Surya, exalted + vargottama), its')
print('  Atmakaraka (Shukra, highest Ishta Phala) and its lagna lord all sit in')
print('  the single weakest-supported sign it owns.  That is the paradox in one')
print('  sentence: maximum cargo, minimum road.')

# --- 4 ---------------------------------------------------------------------
rule('4. THE 8TH LORD — the engine itself')
m = LORD[S8]
n, p, nl = nak_of(D1[m])
print(f'  {m} {fmt(D1[m])}, house {h(sign_of(m))}, {n} p{p} (lord {nl})')
print(f'  Rules houses {", ".join(str(i + 1) for i in range(12) if LORD[(LAG + i) % 12] == m)}')
print(f'  Sits in {SIGNS[sign_of(m)]}, ruled by {LORD[sign_of(m)]} -- which sits in '
      f'{SIGNS[sign_of(LORD[sign_of(m)])]}, house {h(sign_of(LORD[sign_of(m)]))}')
print('\n  PARIVARTANA: the 8th lord is in the 9th and the 9th lord is in the 8th.')
print('  A perfect exchange between transformation and dharma.  Neither house can')
print('  act without the other; every crisis is routed through meaning and every')
print('  belief is tested by crisis.')
print('\n  Mangal carries the HIGHEST Shodhya Pinda in the chart (delivery capacity)')
print('  and the LOWEST Vimshopaka (10.30), with 4 debilitations across 16 vargas.')
print('  Maximum output, minimum dignity: it delivers hard and it delivers rough.')

# --- 5 ---------------------------------------------------------------------
rule('5. THE 8TH ACROSS THE VARGAS — does the pattern repeat?')
for n_, label in [(9, 'D9  Navamsha'), (10, 'D10 Dashamsha'),
                  (27, 'D27 Bhamsha'), (30, 'D30 Trimshamsha')]:
    vl = varga(D1['Lagna'], n_)
    v8 = (vl + 7) % 12
    who = [g for g in GRAHAS if varga(D1[g], n_) == v8]
    dig = [f'{g} ({dignity(g, v8)})' if dignity(g, v8) else g for g in who]
    print(f'  {label:16} lagna {SIGNS[vl]:11} 8th = {SIGNS[v8]:11} '
          f'{", ".join(dig) or "empty"}')
print('  D8  Ashtamsha    lagna Meena       8th = Tula      '
      'Shukra (own sign + MOOLTRIKONA)')
print('\n  The 8th is occupied in FIVE of the six charts.  The one exception is')
print('  D27, the vitality and longevity varga -- the single chart in which an')
print('  empty 8th is the reassuring result.  That is the strongest structural')
print('  argument in the whole reading that the transformations are survivable.')
print('\n  Surya occupies the 8th in BOTH D1 and D9.  Rahu occupies the 8th of')
print('  D10.  And in D8 -- the varga OF the 8th house -- Shukra sits in its own')
print('  mooltrikona in that chart\'s own 8th.  The signature is not an artifact')
print('  of one chart; it is built at four levels.')

# --- 6 ---------------------------------------------------------------------
rule('6. WHEN THE APPARATUS COMES ONLINE — graha maturity')
crew = occ(S8) + [LORD[S8]]
for g in sorted(set(crew), key=lambda x: MATURITY[x]):
    role = 'the 8th lord' if g == LORD[S8] else 'in the 8th'
    print(f'  {g:8} matures at {MATURITY[g]:>2}  = year {2002 + MATURITY[g]}   ({role})')
lo = min(MATURITY[g] for g in crew); hi = max(MATURITY[g] for g in crew)
print(f'\n  The whole 8th-house apparatus matures across ages {lo}-{hi}, '
      f'= {2002 + lo}-{2002 + hi}.')
print('  The transformation windows computed in verify_timeline.py peak at')
print('  2028-2033, ages 26-31 -- INSIDE that maturity span, not before it.')
print('  The house comes online exactly when the transits fire it.')

# --- 7 ---------------------------------------------------------------------
rule('7. THE YOGAS THAT FORM THERE')
print('  Vimala Yoga        12th lord Surya in the 8th -- a Vipreeta Raja Yoga.')
print('                     Adversity converted, not merely endured.')
print('  Dharma-Karmadhipati 9th lord Shukra with 10th lord Budha, 13°09′ apart,')
print('                     IN THE 8TH.  The chart\'s ONLY kendra-trikona raja')
print('                     yoga forms inside the house of upheaval, so it can')
print('                     only fire THROUGH upheaval.')
print('  Budha-Aditya       lagna lord fused into the exalted Sun, combust.')
print('\n  Both of this chart\'s raja-yoga-class formations are in the 8th.  There')
print('  is no version of this life where the good things arrive by another road.')

# --- 8 ---------------------------------------------------------------------
rule('8. THE MECHANISM, STATED PLAINLY')
for line in [
    'Identity     lagna lord Budha in the 8th, combust: the self is rebuilt by',
    '             dissolution rather than built by accumulation.',
    'Career       Budha also rules the 10th, and D10 Rahu sits in D10\'s 8th:',
    '             advancement arrives attached to disruption, never to tenure.',
    'Money        Shukra rules the 2nd and sits in the 8th, inside the Khara',
    '             drekkana with Mrityu 3° away: capital comes from other people\'s',
    '             resources -- equity, settlement, inheritance, crisis -- not salary.',
    'Belief       Shukra also rules the 9th: dharma is examined under pressure,',
    '             and the parivartana means it cannot be examined any other way.',
    'Loss         Surya rules the 12th and sits exalted in the 8th: what he loses',
    '             becomes the instrument.  This is Vimala, and it is why the',
    '             direction of resolution is upward.',
]:
    print('  ' + line)
