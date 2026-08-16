#!/usr/bin/env python3
"""
Who loves him, when he gets to feel it, and whether the marriage satisfies.

Affection is not one house.  Jyotisha distributes it: the 2nd for family, the
4th for mother and emotional ground, the 5th for children, the 7th for spouse,
the 9th for father and mentors, the 11th for peers.  Ranking those six against
each other says which registers of love actually reach him.

Marital satisfaction is then read in BOTH directions -- his experience of her
from the 7th and the 7th from Chandra, hers of him from the 7th-from-the-7th,
which is his own lagna.
"""
from datetime import datetime, timedelta

SIGNS = ['Mesha', 'Vrishabha', 'Mithuna', 'Karka', 'Simha', 'Kanya',
         'Tula', 'Vrischika', 'Dhanu', 'Makara', 'Kumbha', 'Meena']
NAK_LORD = ['Ketu', 'Shukra', 'Surya', 'Chandra', 'Mangal',
            'Rahu', 'Guru', 'Shani', 'Budha'] * 3
LORD = ['Mangal', 'Shukra', 'Budha', 'Chandra', 'Surya', 'Budha',
        'Shukra', 'Mangal', 'Guru', 'Shani', 'Shani', 'Guru']
ASPECT = {'Mangal': [4, 7, 8], 'Guru': [5, 7, 9], 'Shani': [3, 7, 10],
          'Rahu': [5, 7, 9], 'Ketu': [5, 7, 9]}
SAV = {'Mesha': 21, 'Vrishabha': 22, 'Mithuna': 29, 'Karka': 28, 'Simha': 24,
       'Kanya': 29, 'Tula': 24, 'Vrischika': 28, 'Dhanu': 29, 'Makara': 29,
       'Kumbha': 41, 'Meena': 33}
BHAVA_RANK = [5, 3, 8, 2, 6, 10, 4, 12, 7, 9, 11, 1]
RUPAS = {'Surya': 11.39, 'Guru': 8.21, 'Shukra': 6.68, 'Budha': 6.46,
         'Chandra': 6.42, 'Shani': 6.39, 'Mangal': 6.33}
UPAGRAHA = {'Mrityu': 'Mesha', 'Yama Ghantaka': 'Mithuna', 'Gulika': 'Karka',
            'Mandi': 'Karka', 'Kala': 'Kanya', 'Dhuma': 'Simha',
            'Parivesha': 'Vrishabha', 'Upaketu': 'Meena',
            'Ardha Prahara': 'Vrishabha', 'Vyatipata': 'Vrischika',
            'Indra Chapa': 'Kumbha'}


def dms(s, d, m, sec=0):
    return SIGNS.index(s) * 30 + d + m / 60 + sec / 3600


D1 = {'Lagna': dms('Kanya', 27, 37, 37), 'Surya': dms('Mesha', 1, 28, 3),
      'Chandra': dms('Vrishabha', 1, 47, 15), 'Mangal': dms('Vrishabha', 7, 19, 32),
      'Budha': dms('Mesha', 10, 27, 50), 'Guru': dms('Mithuna', 14, 47, 52),
      'Shukra': dms('Mesha', 23, 36, 49), 'Shani': dms('Vrishabha', 17, 54, 25),
      'Rahu': dms('Vrishabha', 26, 55, 52), 'Ketu': dms('Vrischika', 26, 55, 52)}
GRAHAS = [g for g in D1 if g != 'Lagna']
LAG = int(D1['Lagna'] // 30)
sg = lambda g: int(D1[g] // 30)
sign_of_house = lambda n: (LAG + n - 1) % 12
occ = lambda s: [g for g in GRAHAS if sg(g) == s]
ND = {g: NAK_LORD[int(D1[g] // (360 / 27))] for g in GRAHAS}
rule = lambda t: print('\n' + '=' * 92 + f'\n{t}\n' + '=' * 92)


def aspects_on(sign):
    return [g for g in GRAHAS
            if any((sg(g) + o - 1) % 12 == sign for o in ASPECT.get(g, [7]))]


# --- 1 ----------------------------------------------------------------------
rule('1. THE SIX REGISTERS OF LOVE, RANKED AGAINST EACH OTHER')
REG = [(4, 'mother, home, emotional ground'), (2, 'family, kutumba'),
       (7, 'spouse'), (5, 'children, disciples'),
       (9, 'father, gurus, mentors'), (11, 'friends, peers')]
print(f'  {"house":6}{"register":34}{"sign":11}{"SAV":>5}{"Bhava rank":>12}'
      f'   occupants / notes')
for n, label in sorted(REG, key=lambda x: BHAVA_RANK[x[0] - 1]):
    s = sign_of_house(n)
    ups = [k for k, v in UPAGRAHA.items() if v == SIGNS[s]]
    note = ', '.join(occ(s)) or 'empty'
    if ups:
        note += '  + ' + ', '.join(ups)
    print(f'  {n:<6}{label:34}{SIGNS[s]:11}{SAV[SIGNS[s]]:>5}'
          f'{BHAVA_RANK[n - 1]:>12}   {note}')
print('\n  The four best-built relational houses are the VERTICAL and INTIMATE')
print('  ones -- home, family, spouse, children.  The house of PEERS ranks')
print('  11 of 12 and carries both harsh shadow points.')
print('\n  That is the whole answer to who loves him: FAMILY, SPOUSE, ELDERS')
print('  AND CHILDREN, structurally well.  PEERS, structurally badly.  He is')
print('  loved downward and upward, and competed with sideways.')

# --- 2 ----------------------------------------------------------------------
rule('2. THE STRONGEST ONE — the 4th house')
s4 = sign_of_house(4)
print(f'  4th house {SIGNS[s4]}, SAV {SAV[SIGNS[s4]]}, Bhava rank '
      f'{BHAVA_RANK[3]} of 12 -- SECOND-STRONGEST BHAVA IN THE CHART')
print(f'  Occupants {occ(s4) or "empty"};  aspects {", ".join(aspects_on(s4))}')
print(f'  Lord {LORD[s4]}, in house {(sg(LORD[s4]) - LAG) % 12 + 1}, forming '
      'AMALA YOGA')
print(f'  The UPAPADA also falls here -- so the marriage attaches to the')
print('  second-strongest house in the chart.')
print('\n  But note the same pattern as everywhere: the HOUSE is superb and its')
print('  LORD is besieged.  Guru carries the worst Drik Bala in the chart')
print('  (-8.58) and Yama Ghantaka 2 05 away.  The capacity to be loved is')
print('  excellent; the channel that delivers it is under pressure.')

# --- 3 ----------------------------------------------------------------------
rule('3. WHEN HE ACTUALLY FEELS IT — every Shukra period')
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
print('  Shukra is the Atmakaraka, is self-disposited at nakshatra level, holds')
print('  the HIGHEST Ishta Phala in the chart, and rules the 2nd (family) and')
print('  the 9th (dharma).  Its periods are when affection is actually felt\n')
for s, e, md, ad in seq:
    if ad == 'Shukra' and e.year >= 2026:
        print(f'  {md}-{ad:8} {s.strftime("%b %Y")} - {e.strftime("%b %Y")}   '
              f'ages {s.year - 2002}-{e.year - 2002}')
# pratyantardashas of the current antardasha
gs = [x for x in seq if x[2] == 'Rahu' and x[3] == 'Guru'][0]
span = (gs[1] - gs[0]).total_seconds(); t2 = gs[0]; i0 = order.index('Guru')
print('\n  And inside the running Rahu-Guru antardasha:')
for n in range(9):
    nm = order[(i0 + n) % 9]
    e2 = t2 + timedelta(seconds=span * D[nm] / 120)
    if nm in ('Shukra', 'Surya'):
        tag = '  <== the relationship becomes real' if nm == 'Shukra' else \
              '  <== recognition and disclosure'
        print(f'    Rahu-Guru-{nm:8} {t2.strftime("%b %Y")} -> '
              f'{e2.strftime("%b %Y")}{tag}')
    t2 = e2
print('\n  Add the 4th/7th lord Guru\'s own mahadasha, Dec 2040 - Dec 2056:')
print('  SIXTEEN YEARS governed by the lord of home and marriage, entirely')
print('  inside the Sade Sati-free window.  That is the long stretch in which')
print('  the relational houses are simply switched on.')

# --- 4 ----------------------------------------------------------------------
rule('4. MARITAL SATISFACTION -- HIS SIDE')
s7 = sign_of_house(7)
print(f'  7th house {SIGNS[s7]}, SAV {SAV[SIGNS[s7]]} (2nd highest in the '
      f'chart), Bhava rank {BHAVA_RANK[6]} of 12')
print(f'  Lord {LORD[s7]} -- {RUPAS[LORD[s7]]} raw Shadbala rupas, second only '
      f'to Surya\'s {RUPAS["Surya"]}')
print(f'  Occupants {occ(s7) or "EMPTY"};  aspects {", ".join(aspects_on(s7))}')
print(f'  Upagraha in the 7th: '
      f'{[k for k, v in UPAGRAHA.items() if v == SIGNS[s7]]}')
s7m = (sg('Chandra') + 6) % 12
print(f'\n  7th from Chandra (how the marriage FEELS) = {SIGNS[s7m]}, '
      f'holding {", ".join(occ(s7m)) or "nothing"}')
print('\n  The house is well built: 33 bindus, rank 4, a strong lord.  The')
print('  problem is not capacity.  It is that KETU is the only graha aspecting')
print('  the 7th, UPAKETU sits inside it, and KETU also occupies the 7th from')
print('  Chandra.  Three detachment contacts on the same axis.')
print('\n  Ketu\'s signature is not absence of love.  It is "the thing obtained')
print('  is not the thing wanted" -- a structural sense of incompleteness that')
print('  would attach to ANY partner.  His dissatisfaction, where it appears,')
print('  is not evidence about her.')

# --- 5 ----------------------------------------------------------------------
rule('5. MARITAL SATISFACTION -- HER SIDE')
print('  Her experience of him is the 7th FROM the 7th -- which is his own')
print(f'  lagna: {SIGNS[LAG]}, Bhava rank {BHAVA_RANK[0]} of 12, and')
print('  VARGOTTAMA -- the same sign in D1 and D9.')
print('\n  What she gets is a man who is the SAME PERSON at every level.  No')
print('  split, no performance, no second self.  Against a Kanya lagna that is')
print('  reliable, precise and useful.  That is a genuinely satisfying husband')
print('  on the dimensions that matter over decades.')
for off, label in [(4, 'her domestic happiness'), (5, 'her romantic expression'),
                   (2, 'the marriage\'s material sustenance'),
                   (10, 'her own standing')]:
    s = (s7 + off - 1) % 12
    hn = (s - LAG) % 12 + 1
    ups = [k for k, v in UPAGRAHA.items() if v == SIGNS[s]]
    ordn = {2: '2nd', 4: '4th', 5: '5th', 10: '10th'}[off]
    print(f'\n  {ordn} from the 7th ({label})')
    print(f'    = {SIGNS[s]}, his house {hn}, rank {BHAVA_RANK[hn - 1]}, '
          f'{", ".join(occ(s)) or "empty"}'
          + (f'  + {", ".join(ups)}' if ups else ''))
print('\n  Two of those matter.  HER DOMESTIC HAPPINESS derives to his 10th,')
print('  holding Guru and Amala yoga: her contentment runs through his WORK')
print('  and his good name rather than through his attention -- and it is')
print('  therefore exposed to whatever pressures his reputation.')
print('\n  HER ROMANTIC EXPRESSION derives to his 11th -- the second-weakest')
print('  bhava, carrying Gulika and Mandi.  The affection is real; the CHANNEL')
print('  is shadowed.  It comes out as loyalty and practical care rather than')
print('  as demonstrated warmth.  He should not read undemonstrativeness as')
print('  absence, and this is the single most useful line in this section.')

# --- 6 ----------------------------------------------------------------------
rule('6. THE ASYMMETRY, STATED PLAINLY')
for line in [
    'SHE IS LIKELY TO BE MORE SATISFIED WITH HIM THAN HE IS WITH HER, and the',
    'reason is structural rather than personal.',
    '',
    'What she experiences of him is his VARGOTTAMA LAGNA -- consistency, no',
    'gap between the presented and the actual, reliability that compounds.',
    '',
    'What he experiences of her is a 7th house touched only by KETU, an',
    'UPAKETU inside it, and KETU again on the 7th from his Moon.  He will feel',
    'a gap even when nothing is wrong.',
    '',
    'The marriage is sustained by the 2nd from the Upapada -- MAKARA under',
    'SHANI: duty, endurance, slow deepening.  Neither of them will describe it',
    'as effusive.  Both of them will still be in it.',
    '',
    'The instruction that follows is unusually concrete.  His satisfaction',
    'depends on not measuring the marriage by intensity of feeling, which is',
    'the one axis Ketu guarantees will read low.  Hers depends on his work',
    'holding up, because her contentment is routed through it.  Those are',
    'different maintenance tasks, and each of them is doing the one the other',
    'cannot see.',
]:
    print('  ' + line)
