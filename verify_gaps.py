#!/usr/bin/env python3
"""
What is still missing -- vargas not computed, techniques not applied, and data
not supplied.

Three kinds of gap, and they are not equally closable:

  1. VARGAS beyond the sixteen.  Some are cheap and unambiguous; some rest on
     rules the schools genuinely disagree about, and those are named rather
     than guessed at.
  2. TECHNIQUES never applied -- whole systems, not details.
  3. DATA never supplied.  This is the binding constraint, and the arithmetic
     below shows exactly where it bites.
"""
SIGNS = ['Mesha', 'Vrishabha', 'Mithuna', 'Karka', 'Simha', 'Kanya',
         'Tula', 'Vrischika', 'Dhanu', 'Makara', 'Kumbha', 'Meena']
LORD = ['Mangal', 'Shukra', 'Budha', 'Chandra', 'Surya', 'Budha',
        'Shukra', 'Mangal', 'Guru', 'Shani', 'Shani', 'Guru']
MOV, FIX = {0, 3, 6, 9}, {1, 4, 7, 10}


def d(sg, a, b, c=0):
    return SIGNS.index(sg) * 30 + a + b / 60 + c / 3600


D1 = {'Lagna': d('Kanya', 27, 37, 37), 'Surya': d('Mesha', 1, 28, 3),
      'Chandra': d('Vrishabha', 1, 47, 15), 'Mangal': d('Vrishabha', 7, 19, 32),
      'Budha': d('Mesha', 10, 27, 50), 'Guru': d('Mithuna', 14, 47, 52),
      'Shukra': d('Mesha', 23, 36, 49), 'Shani': d('Vrishabha', 17, 54, 25),
      'Rahu': d('Vrishabha', 26, 55, 52), 'Ketu': d('Vrischika', 26, 55, 52)}
GRAHAS = [g for g in D1 if g != 'Lagna']
LAG = int(D1['Lagna'] // 30)
sg = lambda g: int(D1[g] // 30)
h = lambda s: (s - LAG) % 12 + 1
occ = lambda s: [g for g in GRAHAS if sg(g) == s]
rule = lambda t: print('\n' + '=' * 92 + f'\n{t}\n' + '=' * 92)

DONE = [1, 2, 3, 4, 7, 9, 10, 12, 16, 20, 24, 27, 30, 40, 45, 60]
SUPPLIED_EXTRA = {8: 'Ashtamsha — supplied', 11: 'Rudramsha — supplied'}

# --- 1 ----------------------------------------------------------------------
rule('1. VARGAS — what is computed, what is not, and why')
print('  The Shodashavarga is sixteen charts and all sixteen are computed.')
print('  The source also supplied D8 and D11, which are outside that scheme.')
print(f'  So EIGHTEEN divisional charts are on the table.\n')
print('  Beyond them, the remaining named vargas fall into two classes:\n')
LINEAR = [(81, 'Nava-navamsha', 'the navamsha of the navamsha'),
          (108, 'Ashtottaramsha', 'D9 x D12'),
          (144, 'Dwadash-dwadashamsha', 'D12 x D12'),
          (150, 'Nadiamsha', 'the finest classical division')]
CONTESTED = [(5, 'Panchamamsha', 'fame, authority'),
             (6, 'Shashtamsha', 'health, disease'),
             (15, 'Panchadashamsha', 'demerits'),
             (18, 'Ashtadashamsha', 'variant scheme'),
             (22, 'Dwavimshamsha', 'variant scheme'),
             (36, 'Shattrimshamsha', 'variant scheme')]
print('  (a) COMPUTABLE WITHOUT AMBIGUITY — pure linear maps, no start-sign rule:')
for n, nm, what in LINEAR:
    vl = int(D1['Lagna'] * n / 30) % 12
    arc = 30 / n
    print(f'      D{n:<4} {nm:22} lagna would be {SIGNS[vl]:11} '
          f'(division = {arc*60:.1f} arcmin)')
print('\n  (b) RULE-CONTESTED — the schools disagree on the starting sign, so a')
print('      number here would be a guess wearing a decimal point:')
for n, nm, what in CONTESTED:
    print(f'      D{n:<4} {nm:22} {what}')
print('\n  D6 in particular would be worth having -- it is the health varga and')
print('  this chart has a thin Moon and a failing lagna lord.  It is left out')
print('  because the odd/even starting rule is not settled, not because it')
print('  would be hard to compute.')

# --- 2 ----------------------------------------------------------------------
rule('2. THE BINDING CONSTRAINT — how much birth time each varga needs')
print('  The lagna is 27°37\'37" Kanya.  Every varga divides a sign into n')
print('  parts, so the lagna must be known to better than 30/n degrees for that')
print('  varga\'s ascendant to be trustworthy.  The ascendant moves at roughly')
print('  1 degree every 4 minutes of clock time.\n')
print(f'  {"varga":7}{"division":>12}{"birth time needed":>20}   status')
ALL = sorted(set(DONE) | {8, 11} | {n for n, _, _ in LINEAR})
for n in ALL:
    arc = 30 / n
    mins = arc * 4
    tag = ('computed' if n in DONE else
           'supplied' if n in SUPPLIED_EXTRA else 'not computed')
    warn = ''
    if mins < 10:
        warn = '  <-- finer than the birth time is known to'
    print(f'  D{n:<6}{arc*60:>9.1f}\'{mins:>17.1f} min   {tag}{warn}')
print('\n  The derived birth date is solid -- three independent confirmations.')
print('  The birth TIME is not: it is pinned only by the lagna falling in Kanya')
print('  rather than Tula, which is a window of about TEN MINUTES.')
print('\n  So the honest boundary is: every varga up to about D16 is safe at the')
print('  ten-minute level.  D20 and finer are progressively less certain, and')
print('  D60 -- which this reading leans on for the destination -- needs the')
print('  birth time to 2 minutes.  D150 would need it to 48 seconds.')

# --- 3 ----------------------------------------------------------------------
rule('3. HOW MUCH MOVES IF THE BIRTH TIME IS WRONG')


def varga_lagna(l, n):
    s, p = int(l // 30), l % 30
    if n == 9:  return int(l * 9 / 30) % 12
    if n == 10: return ((s if s % 2 == 0 else (s + 8) % 12) + int(p / 3)) % 12
    if n == 24: return ((4 if s % 2 == 0 else 3) + int(p / 1.25)) % 12
    if n == 27: return int(l * 27 / 30) % 12
    if n == 60: return (s + int(p * 2)) % 12
    if n == 16: return ((0 if s in MOV else 4 if s in FIX else 8)
                        + int(p / 1.875)) % 12
    raise ValueError(n)


base = D1['Lagna']
print('  Shifting the ascendant by +/- a few arcminutes and watching which')
print('  varga ascendants change:\n')
print(f'  {"shift":>10}{"~clock":>9}   D9      D10     D16     D24     D27     D60')
for shift in (-30/60, -15/60, -5/60, 0, 5/60, 15/60, 30/60):
    l = base + shift
    cells = [SIGNS[varga_lagna(l, n)][:5] for n in (9, 10, 16, 24, 27, 60)]
    mark = '  <== as read' if shift == 0 else ''
    print(f'  {shift*60:>+8.0f}\'{shift*4:>+8.1f}m   '
          + '  '.join(f'{c:<6}' for c in cells) + mark)
# derive the stability band for each varga from the scan rather than assert it
print('\n  Stability band around the read position (how far the ascendant can')
print('  move before that varga\'s lagna changes):\n')
for n in (9, 10, 16, 24, 27, 60):
    lo = hi = 0.0
    step = 1/60
    while varga_lagna(base - (lo + step), n) == varga_lagna(base, n) and lo < 1:
        lo += step
    while varga_lagna(base + (hi + step), n) == varga_lagna(base, n) and hi < 1:
        hi += step
    band = (lo + hi) * 60
    print(f'    D{n:<4} -{lo*60:4.0f}\' to +{hi*60:4.0f}\'   '
          f'= {band:5.0f} arcmin  = {band/60*4:5.2f} min of birth time')
print('\n  D9 and D10 are the most robust; D60 is by far the least.')
print('\n  Conclusion, stated plainly: the D60-based claim about the destination')
print('  (Shukra exalted in its 12th) rests on the narrowest band of any')
print('  structural finding in this reading.  It agrees with four other')
print('  techniques, which is why it survives -- but on its own it would not.')

# --- 4 ----------------------------------------------------------------------
rule('4. TECHNIQUES NEVER APPLIED — whole systems, not details')
GAPS = [
 ('Chara dasha (Jaimini)', 'HIGH',
  'The main Jaimini rashi-dasha system.  An entirely independent timing '
  'scheme, and the natural cross-check on the Vimshottari-based timeline. '
  'Computable from what is already here.'),
 ('Argala (Jaimini intervention)', 'HIGH',
  'Which houses intervene on which, and which of those interventions are '
  'obstructed.  A whole Jaimini layer, and the chart\'s 2/4/11 and 12/3/10 '
  'relationships are exactly where it would bite.'),
 ('Rashi drishti (sign aspects)', 'MEDIUM',
  'Jaimini sign-to-sign aspects, which are different from graha drishti and '
  'would give a second reading of what reaches the empty 8th.'),
 ('Bhava Chalit / cuspal houses', 'HIGH',
  'This reading uses whole-sign houses throughout.  With the lagna at 27°37\', '
  'a cuspal system would push several grahas into adjacent houses.  This is '
  'the single largest METHODOLOGICAL gap.'),
 ('Kakshya transit (Ashtakavarga)', 'MEDIUM',
  'Each sign divides into eight kakshyas; transits are read as passing '
  'through supported or unsupported ones.  Would sharpen the transit work '
  'from months to weeks.'),
 ('Varshaphal / Tajika annual chart', 'MEDIUM',
  'Solar-return chart with Muntha, year-lord and Sahams.  Would give a '
  'dedicated reading of 2027 rather than a dasha-plus-transit composite.'),
 ('Ashtottari, Yogini, Kalachakra dashas', 'LOW',
  'Alternative dasha systems.  Ashtottari has conditional applicability that '
  'would need checking first.'),
 ('Tara Bala and Chandra avasthas', 'LOW',
  'Nakshatra-cycle strength from the janma nakshatra; refinement rather '
  'than new structure.'),
 ('Shubha / Papa Kartari yogas', 'LOW',
  'Whether key houses are hemmed between benefics or malefics.  Quick to '
  'check and would refine the 7th and 10th readings.'),
]
print(f'  {"technique":38}{"value":8}why it matters')
for t, v, why in GAPS:
    print(f'\n  {t:38}{v:8}{why[:44]}')
    rest = why[44:]
    while rest:
        print(f'  {"":46}{rest[:44]}')
        rest = rest[44:]

# --- 5 ----------------------------------------------------------------------
rule('5. DATA NEVER SUPPLIED — the gaps no computation can close')
for item, why in [
    ('EXACT BIRTH TIME',
     'The binding constraint. Pins D20 and finer, every house cusp, and all '
     'the upagrahas. Currently known only to ~10 minutes.'),
    ('BIRTH PLACE / COORDINATES',
     'Never supplied. Needed for the true ascendant, for Bhava Chalit cusps, '
     'and for any location-dependent work.'),
    ('HER BIRTH DATA',
     'No guna milan, no ashtakoota, no Mangal-dosha comparison, no reading '
     'of her own dashas. Everything said about her is derived from HIS chart.'),
    ('CONFIRMED LIFE EVENTS',
     'Nothing to rectify against. One falsifiable retrodiction was offered '
     '(a relationship beginning Jan-May 2026); it remains unconfirmed.'),
    ('THE PARENTS\' CHARTS',
     'The father and mother threads are read by bhavat bhavam from his chart '
     'alone.'),
]:
    print(f'\n  {item}')
    rest = why
    while rest:
        cut = rest[:70].rfind(' ') if len(rest) > 70 else len(rest)
        print(f'    {rest[:cut]}')
        rest = rest[cut:].lstrip()

# --- 6 ----------------------------------------------------------------------
rule('6. THE RANKED ANSWER')
for n, line in enumerate([
    'BIRTH TIME to the minute.  It is the only input that would materially '
    'change conclusions rather than add to them, and it gates D20 through '
    'D60, every house cusp, and the whole upagraha set.',
    'HER CHART.  Half the partnership analysis is currently one-sided by '
    'necessity.',
    'CHARA DASHA and ARGALA.  Two whole Jaimini systems, both computable '
    'from data already in hand, and the Chara dasha would independently '
    'test the entire timeline.',
    'BHAVA CHALIT.  Whole-sign has been used throughout without ever '
    'checking what a cuspal system would move.',
    'CONFIRMED EVENTS.  Without one, this is an unfalsified reading rather '
    'than a tested one.',
], 1):
    print(f'\n  {n}. ', end='')
    rest = line
    first = True
    while rest:
        cut = rest[:72].rfind(' ') if len(rest) > 72 else len(rest)
        print(('' if first else '     ') + rest[:cut])
        first = False
        rest = rest[cut:].lstrip()
print('\n  Everything else on the list would enrich the reading.  Only the')
print('  birth time could overturn part of it.')
