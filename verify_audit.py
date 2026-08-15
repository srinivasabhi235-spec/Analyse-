#!/usr/bin/env python3
"""
Master audit: the "good but with friction" claim, and a full concept re-check.

PART A tests the claim.  "Good" is a statement about the NET outcome balance;
"friction" is a statement about RESISTANCE -- which is a different quantity
from cost, and has its own measurable signature.  Both are computed.

PART B re-derives every headline figure the reading rests on, from the natal
longitudes alone, and asserts it.  Anything that has drifted across the
document's many revisions fails loudly here rather than quietly in prose.
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
ASPECT = {'Mangal': [4, 7, 8], 'Guru': [5, 7, 9], 'Shani': [3, 7, 10],
          'Rahu': [5, 7, 9], 'Ketu': [5, 7, 9]}
RAKSHASA = {3, 9, 10, 14, 16, 18, 19, 23, 24}

# --- verified tables (verify_bala.py) --------------------------------------
ISHTA = {'Shukra': 47.49, 'Surya': 46.88, 'Guru': 37.30, 'Chandra': 24.54,
         'Mangal': 19.66, 'Budha': 18.91, 'Shani': 12.48}
KASHTA = {'Shani': 46.83, 'Mangal': 38.87, 'Budha': 30.32, 'Guru': 15.10,
          'Shukra': 11.87, 'Surya': 7.83, 'Chandra': 4.49}
RATIO = {'Surya': 2.2782, 'Shani': 1.2784, 'Mangal': 1.2657, 'Guru': 1.2636,
         'Shukra': 1.2148, 'Chandra': 1.0705, 'Budha': 0.9234}
VIMSHOPAKA = {'Surya': 16.85, 'Chandra': 15.32, 'Shukra': 12.60, 'Guru': 12.32,
              'Budha': 11.45, 'Shani': 11.22, 'Mangal': 10.30}
SAV = {'Mesha': 21, 'Vrishabha': 22, 'Mithuna': 29, 'Karka': 28, 'Simha': 24,
       'Kanya': 29, 'Tula': 24, 'Vrischika': 28, 'Dhanu': 29, 'Makara': 29,
       'Kumbha': 41, 'Meena': 33}
BHAVA_RANK = [5, 3, 8, 2, 6, 10, 4, 12, 7, 9, 11, 1]
VIM_YEARS = {'Ketu': 7, 'Shukra': 20, 'Surya': 6, 'Chandra': 10, 'Mangal': 7,
             'Rahu': 18, 'Guru': 16, 'Shani': 19, 'Budha': 17}
DISP_PROXY = {'Rahu': 'Shukra', 'Ketu': 'Mangal'}


def dms(s, d, m, sec=0):
    return SIGNS.index(s) * 30 + d + m / 60 + sec / 3600


def fmt(l):
    return f"{int(l % 30):02d}°{round((l % 1) * 60):02d}′ {SIGNS[int(l // 30)]}"


def nak_i(l):
    return int(l // (360 / 27))


def navamsha(l):
    sign, rem = int(l // 30), l % 30
    return ({0: sign, 1: (sign + 8) % 12, 2: (sign + 4) % 12}[sign % 3]
            + int(rem // (30 / 9))) % 12


D1 = {'Lagna': dms('Kanya', 27, 37, 37), 'Surya': dms('Mesha', 1, 28, 3),
      'Chandra': dms('Vrishabha', 1, 47, 15), 'Mangal': dms('Vrishabha', 7, 19, 32),
      'Budha': dms('Mesha', 10, 27, 50), 'Guru': dms('Mithuna', 14, 47, 52),
      'Shukra': dms('Mesha', 23, 36, 49), 'Shani': dms('Vrishabha', 17, 54, 25),
      'Rahu': dms('Vrishabha', 26, 55, 52), 'Ketu': dms('Vrischika', 26, 55, 52)}
GRAHAS = [g for g in D1 if g != 'Lagna']
CLASSICAL = [g for g in GRAHAS if g not in ('Rahu', 'Ketu')]
LAG = int(D1['Lagna'] // 30)
sg = lambda g: int(D1[g] // 30)
h = lambda g: (sg(g) - LAG) % 12 + 1
RD = {g: LORD[sg(g)] for g in GRAHAS}
ND = {g: NAK_LORD[nak_i(D1[g])] for g in GRAHAS}
rule = lambda t: print('\n' + '=' * 92 + f'\n{t}\n' + '=' * 92)

PASS, FAIL = [], []


def check(label, got, want, tol=0.0):
    ok = (abs(got - want) <= tol) if isinstance(want, (int, float)) \
        and not isinstance(want, bool) else (got == want)
    (PASS if ok else FAIL).append(label)
    print(f'  {"OK  " if ok else "FAIL"}  {label:58} {got}'
          + ('' if ok else f'   (expected {want})'))


# ===========================================================================
rule('PART A — "GOOD BUT WITH FRICTION", TESTED')

print('  A1. IS THE NET GOOD?  Outcome balance weighted by dasha duration.\n')
net = {g: ISHTA[g] - KASHTA[g] for g in CLASSICAL}
for g in sorted(net, key=lambda x: -net[x]):
    bar = '+' * int(max(net[g], 0) / 3) + '-' * int(max(-net[g], 0) / 3)
    print(f'    {g:9} {net[g]:+7.2f}  {VIM_YEARS[g]:>2} yrs   {bar}')
tot_c = sum(net[g] * VIM_YEARS[g] for g in CLASSICAL)
yrs_c = sum(VIM_YEARS[g] for g in CLASSICAL)
tot_a = tot_c + sum(net[DISP_PROXY[g]] * VIM_YEARS[g] for g in ('Rahu', 'Ketu'))
print(f'\n    Positive-net grahas: {sum(1 for g in net if net[g] > 0)} of 7   '
      f'(Surya, Shukra, Guru, Chandra)')
print(f'    Negative-net grahas: {sum(1 for g in net if net[g] < 0)} of 7   '
      f'(Shani, Mangal, Budha)')
print(f'\n    Duration-weighted mean, 95 classical years : {tot_c / yrs_c:+.2f}')
print(f'    Duration-weighted mean, full 120-year cycle: {tot_a / 120:+.2f}')
print('\n    POSITIVE, but modestly.  The chart is not a good-fortune chart and')
print('    it is not an affliction chart; it is a mildly favourable one whose')
print('    positive grahas hold the LONGER dashas.  Shukra (20y), Guru (16y)')
print('    and Rahu-via-Shukra (18y) between them own 54 of 120 years and are')
print('    all net-positive.  Shani\'s 19 negative years are the single largest')
print('    drag, and they arrive last.')

print('\n  A2. IS THERE FRICTION?  Seven independent resistance markers.\n')
FR = []
mismatch = sum(1 for g in GRAHAS if RD[g] != ND[g])
FR.append(('Dispositor mismatch (field lord != star lord)',
           f'{mismatch}/9 = {mismatch / 9 * 100:.0f}%', mismatch == 9))
kendra_occ = [g for g in GRAHAS if h(g) in (1, 4, 7, 10)]
FR.append(('Kendras occupied by a classical graha',
           f'{len([g for g in kendra_occ if g in CLASSICAL])}/4 houses '
           f'({", ".join(kendra_occ) or "none"})', True))
FR.append(('Lagna lord Shadbala ratio', f'{RATIO["Budha"]:.4f} — below 1.0',
           RATIO['Budha'] < 1))
s8 = (LAG + 7) % 12
asp8 = [g for g, o in ASPECT.items()
        if any((sg(g) + x - 1) % 12 == s8 for x in o)]
FR.append(('Aspects onto the 8th', f'{len(asp8)} — none', not asp8))
spread = max(SAV.values()) - min(SAV.values())
FR.append(('SAV spread across the twelve signs',
           f'{spread} (from {min(SAV.values())} to {max(SAV.values())})', True))
raks = sum(1 for k in ('Lagna', 'Chandra') if nak_i(D1[k]) + 1 in RAKSHASA)
FR.append(('Personal points in Rakshasa gana', f'{raks}/2', raks == 2))
water = sum(1 for g in CLASSICAL if sg(g) % 4 == 3)
FR.append(('Classical grahas in water signs', f'{water} — none', water == 0))
for label, val, _ in FR:
    print(f'    {label:46} {val}')

print('\n  A3. THE VERDICT ON THE CLAIM\n')
for line in [
    'BOTH HALVES ARE CORRECT, and they measure different things.',
    '',
    '"Good" is about the NET, and the net is positive: four of seven grahas',
    f'carry a positive outcome balance, the duration-weighted mean is',
    f'{tot_c / yrs_c:+.2f} across the classical dashas, and the long dashas',
    'belong to the favourable grahas.',
    '',
    '"Friction" is about RESISTANCE, and it is extreme -- but note that it is',
    'STRUCTURAL rather than malefic.  Nothing in the list above is an',
    'affliction in the classical sense.  There is no Kemadruma, no Kalasarpa,',
    'no debilitated lagna lord, no graha in the 6th or 12th.  What there is:',
    'every placement delivered by a different graha than owns its field, four',
    'empty kendras but for Guru, a lagna lord 8% short of its minimum, an 8th',
    'house nothing can reach, a 20-bindu spread between the best and worst',
    'signs, both personal points uncompromising by gana, and no water anywhere',
    'to lubricate any of it.',
    '',
    'THE PRECISE FORMULATION: this is a good engine in a chassis with no',
    'bearings.  The outputs are genuinely favourable; every single one of them',
    'has to be dragged across a surface that offers no assistance.  Nothing',
    'here is trying to hurt him.  Nothing here is helping him either.',
]:
    print('    ' + line)

# ===========================================================================
rule('PART B — FULL CONCEPT AUDIT: every headline figure re-derived')

print('\n  B1. Chart geometry\n')
check('Lagna sign is Kanya', SIGNS[LAG], 'Kanya')
check('Lagna degrees from the Tula cusp', round(30 - D1['Lagna'] % 30, 2), 2.37, 0.01)
check('Grahas in three signs only',
      len({sg(g) for g in CLASSICAL}), 3)
check('Occupied houses are 8, 9, 10',
      sorted({h(g) for g in CLASSICAL}), [8, 9, 10])
check('Ecliptic span of the seven classical grahas (deg)',
      round(max(D1[g] for g in CLASSICAL) - min(D1[g] for g in CLASSICAL), 1), 73.3, 0.1)
check('Rahu-Ketu exactly 180 apart',
      round(abs(D1['Rahu'] - D1['Ketu']), 6), 180.0, 1e-6)

print('\n  B2. Strength tables\n')
check('Sarvashtakavarga total', sum(SAV.values()), 337)
check('Lowest SAV sign is the 8th (Mesha)',
      min(SAV, key=SAV.get), 'Mesha')
check('Highest SAV sign is the 6th (Kumbha)',
      max(SAV, key=SAV.get), 'Kumbha')
check('Weakest bhava is the 8th', BHAVA_RANK.index(12) + 1, 8)
check('Strongest bhava is the 12th', BHAVA_RANK.index(1) + 1, 12)
check('Budha is the only graha below its Shadbala minimum',
      [g for g in RATIO if RATIO[g] < 1], ['Budha'])
check('Surya ranks 1 by Shadbala ratio',
      max(RATIO, key=RATIO.get), 'Surya')
check('Surya ranks 1 by Vimshopaka',
      max(VIMSHOPAKA, key=VIMSHOPAKA.get), 'Surya')
check('Chandra ranks 2 by Vimshopaka',
      sorted(VIMSHOPAKA, key=lambda x: -VIMSHOPAKA[x])[1], 'Chandra')
check('Shani carries the worst net outcome balance',
      min(net, key=net.get), 'Shani')

print('\n  B3. Yogas and exchanges\n')
check('Parivartana: Mangal in Shukra sign and Shukra in Mangal sign',
      LORD[sg('Mangal')] == 'Shukra' and LORD[sg('Shukra')] == 'Mangal', True)
check('That exchange is between the 8th and 9th lords',
      sorted([[i + 1 for i in range(12) if LORD[(LAG + i) % 12] == 'Mangal'][1],
              [i + 1 for i in range(12) if LORD[(LAG + i) % 12] == 'Shukra'][1]]),
      [8, 9])
check('DKY: 9th lord and 10th lord conjunct in one house',
      h('Shukra') == h('Budha') == 8, True)
check('DKY separation (deg)',
      round(abs(D1['Shukra'] - D1['Budha']), 2), 13.15, 0.01)
check('Vimala: 12th lord Surya sits in the 8th', h('Surya'), 8)
check('Nakshatra parivartana Budha <-> Ketu',
      ND['Budha'] == 'Ketu' and ND['Ketu'] == 'Budha', True)
check('Shukra stands in its own nakshatra', ND['Shukra'], 'Shukra')
check('Every rashi chain ends in Mangal <-> Shukra',
      RD['Mangal'] == 'Shukra' and RD['Shukra'] == 'Mangal', True)

print('\n  B4. Jaimini and sensitive points\n')
byd = sorted(CLASSICAL, key=lambda g: -(D1[g] % 30))
check('Atmakaraka', byd[0], 'Shukra')
check('Amatyakaraka', byd[1], 'Shani')
check('Darakaraka', byd[-1], 'Surya')
check('Karakamsa (AK navamsha sign)', SIGNS[navamsha(D1[byd[0]])], 'Vrischika')
check('Rahu is in Marana Karaka Sthana (9th)', h('Rahu'), 9)
check('Bhrigu Bindu (Chandra-Rahu midpoint)',
      fmt((D1['Chandra'] + D1['Rahu']) / 2), '14°22′ Vrishabha')

print('\n  B5. Vargottama, avastha, gana\n')
check('Vargottama placements',
      [k for k in ['Lagna'] + GRAHAS if int(D1[k] // 30) == navamsha(D1[k])],
      ['Lagna', 'Surya'])
check('Surya is exalted and vargottama',
      EXALT['Surya'] == sg('Surya') == navamsha(D1['Surya']), True)
check('Chandra Baladi avastha is Mrita',
      4 - int((D1['Chandra'] % 30) // 6), 4)
check('Surya Baladi avastha is Bala',
      int((D1['Surya'] % 30) // 6), 0)
check('Janma nakshatra', NAK[nak_i(D1['Chandra'])], 'Krittika')
check('Lagna nakshatra', NAK[nak_i(D1['Lagna'])], 'Chitra')
check('Both personal points are Rakshasa gana',
      all(nak_i(D1[k]) + 1 in RAKSHASA for k in ('Lagna', 'Chandra')), True)

print('\n  B6. Structural counts\n')
inside = [i + 1 for i in range(12) if sg(LORD[(LAG + i) % 12]) == s8]
tied = sorted(set(inside) | {3, 8})
check('Houses whose lord sits in the 8th', inside, [1, 2, 9, 10, 12])
check('Total houses tied to the 8th', len(tied), 7)
check('Grahas aspecting the 8th', len(asp8), 0)
TRI = {'Dharma': [1, 5, 9], 'Artha': [2, 6, 10],
       'Kama': [3, 7, 11], 'Moksha': [4, 8, 12]}
counts = {k: sum(1 for g in GRAHAS if h(g) in v) for k, v in TRI.items()}
check('Purushartha tally D/A/K/M',
      [counts['Dharma'], counts['Artha'], counts['Kama'], counts['Moksha']],
      [4, 1, 1, 3])
check('Dharma + Moksha share of the nine grahas',
      counts['Dharma'] + counts['Moksha'], 7)
check('Only Ketu occupies the kama trikona',
      [g for g in GRAHAS if h(g) in TRI['Kama']], ['Ketu'])
routed = {}
for i in range(12):
    routed.setdefault(ND[LORD[(LAG + i) % 12]], []).append(i + 1)
check('Grahas that deliver at least one house', len(routed), 5)
check('Ketu delivers houses 1, 10, 12', sorted(routed['Ketu']), [1, 10, 12])
check('Surya delivers houses 3, 8, 11', sorted(routed['Surya']), [3, 8, 11])
check('Dispositor mismatch rate', mismatch, 9)

print('\n  B7. Cost structure\n')
sp = {'Mangal': 212, 'Shani': 184, 'Budha': 152, 'Surya': 138,
      'Shukra': 95, 'Guru': 81, 'Chandra': 33}
ra = {k: i for i, k in enumerate(sorted(sp, key=lambda x: -sp[x]))}
rb = {k: i for i, k in enumerate(sorted(KASHTA, key=lambda x: -KASHTA[x]))}
rho = 1 - 6 * sum((ra[k] - rb[k]) ** 2 for k in sp) / (7 * 48)
check('Delivery-vs-cost Spearman rho', round(rho, 3), 0.821, 0.001)
check('Lowest Kashta outright is Chandra, not Surya',
      min(KASHTA, key=KASHTA.get), 'Chandra')
check('Surya is the cheapest graha with real delivery capacity',
      min((g for g in KASHTA if sp[g] >= 95), key=KASHTA.get), 'Surya')
check('Surya has the best net balance', max(net, key=net.get), 'Surya')
check('Surya rules the 12th',
      [i + 1 for i in range(12) if LORD[(LAG + i) % 12] == 'Surya'], [12])
check('The 8th lord stands in Surya\'s nakshatra', ND['Mangal'], 'Surya')

# ===========================================================================
rule('AUDIT RESULT')
print(f'  {len(PASS)} checks passed, {len(FAIL)} failed.')
if FAIL:
    print('\n  FAILURES:')
    for f in FAIL:
        print(f'    - {f}')
else:
    print('\n  Every headline figure the reading rests on re-derives from the')
    print('  natal longitudes and the supplied strength tables.  Nothing has')
    print('  drifted across the document\'s revisions.')
