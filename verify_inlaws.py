#!/usr/bin/env python3
"""
The spouse's family, by bhavat bhavam.

Treat the 7th house as the spouse's lagna and derive her family from it: her
2nd is his 8th, her 9th (father) is his 3rd, her 4th (mother, home) is his
10th, her 10th (standing) is his 4th.  Then measure each derived house by
Bhava Bala rank and Sarvashtakavarga, and check the Upapada and arudha routes
against the result.

Bhava ranks and bindus are the supplied, verified tables (verify_bala.py).
"""
SIGNS = ['Mesha', 'Vrishabha', 'Mithuna', 'Karka', 'Simha', 'Kanya',
         'Tula', 'Vrischika', 'Dhanu', 'Makara', 'Kumbha', 'Meena']
LORD = ['Mangal', 'Shukra', 'Budha', 'Chandra', 'Surya', 'Budha',
        'Shukra', 'Mangal', 'Guru', 'Shani', 'Shani', 'Guru']
EXALT = {'Surya': 0, 'Chandra': 1, 'Mangal': 9, 'Budha': 5,
         'Guru': 3, 'Shukra': 11, 'Shani': 6}
DEBIL = {k: (v + 6) % 12 for k, v in EXALT.items()}
OWN = {'Surya': [4], 'Chandra': [3], 'Mangal': [0, 7], 'Budha': [2, 5],
       'Guru': [8, 11], 'Shukra': [1, 6], 'Shani': [9, 10]}
SAV = {'Mesha': 21, 'Vrishabha': 22, 'Mithuna': 29, 'Karka': 28, 'Simha': 24,
       'Kanya': 29, 'Tula': 24, 'Vrischika': 28, 'Dhanu': 29, 'Makara': 29,
       'Kumbha': 41, 'Meena': 33}
BHAVA_RANK = [5, 3, 8, 2, 6, 10, 4, 12, 7, 9, 11, 1]   # houses 1..12


def dms(s, d, m, sec=0):
    return SIGNS.index(s) * 30 + d + m / 60 + sec / 3600


def fmt(l):
    return f"{int(l % 30):02d}°{round((l % 1) * 60):02d}′ {SIGNS[int(l // 30)]}"


def navamsha(l):
    sign, rem = int(l // 30), l % 30
    return ({0: sign, 1: (sign + 8) % 12, 2: (sign + 4) % 12}[sign % 3]
            + int(rem // (30 / 9))) % 12


def dignity(g, s):
    if EXALT.get(g) == s: return 'exalted'
    if DEBIL.get(g) == s: return 'debilitated'
    if s in OWN.get(g, []): return 'own'
    return ''


D1 = {'Lagna': dms('Kanya', 27, 37, 37), 'Surya': dms('Mesha', 1, 28, 3),
      'Chandra': dms('Vrishabha', 1, 47, 15), 'Mangal': dms('Vrishabha', 7, 19, 32),
      'Budha': dms('Mesha', 10, 27, 50), 'Guru': dms('Mithuna', 14, 47, 52),
      'Shukra': dms('Mesha', 23, 36, 49), 'Shani': dms('Vrishabha', 17, 54, 25),
      'Rahu': dms('Vrishabha', 26, 55, 52), 'Ketu': dms('Vrischika', 26, 55, 52)}
UPAGRAHA = {'Mrityu': dms('Mesha', 26, 49), 'Gulika': dms('Karka', 25, 16),
            'Mandi': dms('Karka', 22, 22), 'Yama Ghantaka': dms('Mithuna', 12, 42),
            'Kala': dms('Kanya', 10, 9), 'Dhuma': dms('Simha', 14, 48),
            'Parivesha': dms('Vrishabha', 15, 12), 'Upaketu': dms('Meena', 1, 28),
            'Ardha Prahara': dms('Vrishabha', 20, 48),
            'Vyatipata': dms('Vrischika', 15, 12), 'Indra Chapa': dms('Kumbha', 14, 48)}
GRAHAS = [g for g in D1 if g != 'Lagna']
LAG = int(D1['Lagna'] // 30)
sg = lambda g: int(D1[g] // 30)
hs = lambda s: (s - LAG) % 12 + 1
occ = lambda s: [g for g in GRAHAS if sg(g) == s]
rule = lambda t: print('\n' + '=' * 92 + f'\n{t}\n' + '=' * 92)

# --- 1 ---------------------------------------------------------------------
rule('1. THE DERIVED HOUSES — the spouse\'s family, read from the 7th as her lagna')
DERIVED = [
    ('her 1st  — herself', 1, 7),
    ('her 2nd  — FAMILY WEALTH', 2, 8),
    ('her 3rd  — her siblings', 3, 9),
    ('her 4th  — her MOTHER, home, property', 4, 10),
    ('her 9th  — her FATHER, fortune', 9, 3),
    ('her 10th — the family\'s STANDING', 10, 4),
    ('her 11th — their gains', 11, 5),
    ('her 12th — their outgoings, foreign', 12, 6),
]
print(f"{'derived house':40} {'his H':>5} {'sign':11} {'lord':8} "
      f"{'SAV':>4} {'Bhava rank':>11}  occupants")
print('-' * 92)
for label, _, hn in DERIVED:
    s = (LAG + hn - 1) % 12
    who = [f'{g}{" (" + dignity(g, s) + ")" if dignity(g, s) else ""}' for g in occ(s)]
    up = [k for k, v in UPAGRAHA.items() if int(v // 30) == s]
    print(f'{label:40} {hn:>5} {SIGNS[s]:11} {LORD[s]:8} {SAV[SIGNS[s]]:>4} '
          f'{BHAVA_RANK[hn - 1]:>11}  {", ".join(who + ["+" + u for u in up]) or "empty"}')

# --- 2 ---------------------------------------------------------------------
rule('2. THE WEALTH HOUSE ITSELF — his 8th, her 2nd')
s = (LAG + 7) % 12
print(f'  Sign {SIGNS[s]}, lord {LORD[s]} (in house {hs(sg(LORD[s]))})')
print(f'  Sarvashtakavarga {SAV[SIGNS[s]]}  -- the LOWEST of the twelve')
print(f'  Bhava Bala rank  {BHAVA_RANK[7]} of 12 -- the WEAKEST bhava')
print(f'  Mrityu upagraha inside; the whole sign is the 22nd (Khara) drekkana zone\n')
print('  But look at who is standing in it:')
for g in occ(s):
    rules = [str(i + 1) for i in range(12) if LORD[(LAG + i) % 12] == g]
    print(f'    {g:8} {fmt(D1[g]):18} {dignity(g, s):12} rules house(s) '
          f'{"+".join(rules)}')
print('\n    Shukra is the natural karaka of wealth AND his 2nd lord AND his 9th')
print('    lord AND the Atmakaraka AND holds the highest Ishta Phala in the chart.')
print(f'    Shukra\'s own bindus in Mesha: 5 -- and that ranks Mesha #2 of 12 in')
print('    Shukra\'s column.  The house is the chart\'s weakest; the wealth-karaka')
print('    treats it as one of its two best signs.')

# --- 3 ---------------------------------------------------------------------
rule('3. THE WEALTH-HOUSE LORD — who actually holds their money')
m = LORD[s]
print(f'  Her 2nd lord = his 8th lord = {m}, in {SIGNS[sg(m)]}, his house {hs(sg(m))}')
print(f'  {SIGNS[sg(m)]} is ruled by {LORD[sg(m)]}, which sits in '
      f'{SIGNS[sg(LORD[sg(m)])]} -- the wealth house itself.')
print('\n  PARIVARTANA.  The lord of her family\'s wealth and the occupant of her')
print('  family\'s wealth house exchange signs.  Technically: her family\'s')
print('  resources and HIS 9th house -- fortune, father, dharma -- are locked')
print('  into each other.  The two families\' fortunes are entangled by')
print('  construction, not by circumstance.')
print('\n  Mangal\'s specification: highest Shodhya Pinda in the chart (delivery),')
print('  lowest Vimshopaka (10.30), four debilitations across sixteen vargas.')
print('  Their wealth is real and roughly held.')

# --- 4 ---------------------------------------------------------------------
rule('4. STANDING vs LIQUIDITY — the split that answers the question')
pairs = [('Family STANDING (his 4th)', 4), ('Family WEALTH (his 8th)', 8)]
for label, hn in pairs:
    s2 = (LAG + hn - 1) % 12
    print(f'  {label:28} {SIGNS[s2]:11} SAV {SAV[SIGNS[s2]]:>3}   '
          f'Bhava rank {BHAVA_RANK[hn - 1]:>2} of 12')
print('\n  Her family\'s STANDING house is the 2nd-strongest bhava in the chart.')
print('  Her family\'s WEALTH house is the weakest, with the lowest bindu count.')
print('  Those are not contradictory readings -- they are the answer:')
print('  RESPECTABLE AND WELL-REGARDED, NOT CONSPICUOUSLY LIQUID.')
print('\n  And the UPAPADA itself falls in that same 4th house, ruled by Guru in')
print('  the 10th where it forms AMALA YOGA -- the yoga of spotless reputation.')
print('  The marriage attaches to a family whose asset is its good name.')

# --- 5 ---------------------------------------------------------------------
rule('5. THE UPAPADA ROUTE — what sustains the marriage materially')
ul = 8      # Dhanu, computed in verify_spouse.py
ul2 = (ul + 1) % 12
print(f'  Upapada        {SIGNS[ul]:11} house {hs(ul)}  lord {LORD[ul]} '
      f'(in house {hs(sg(LORD[ul]))})')
print(f'  2nd from UL    {SIGNS[ul2]:11} house {hs(ul2)}  lord {LORD[ul2]} '
      f'(in house {hs(sg(LORD[ul2]))})  SAV {SAV[SIGNS[ul2]]}, empty')
print('\n  Makara under Shani, with Shani rank 2 in Shadbala: conservative,')
print('  structured, slow-appreciating holdings -- land, long-held assets,')
print('  pension-grade security.  Not cash flow, not display.  An EMPTY 2nd')
print('  from UL with a strong lord elsewhere means the resource exists but is')
print('  not sitting in the marriage; it is held by the older generation.')

# --- 6 ---------------------------------------------------------------------
rule('6. THE ARUDHA ROUTE — how their money APPEARS')
s7 = (LAG + 6) % 12
step = (sg(LORD[s7]) - s7) % 12
a7 = (sg(LORD[s7]) + step) % 12
if (a7 - s7) % 12 in (0, 6):
    a7 = (a7 + 9) % 12
a7_2 = (a7 + 1) % 12
print(f'  A7 (Darapada) = {SIGNS[a7]}, holding {occ(a7) or "nothing"} '
      f'-- the partnership\'s public image')
print(f'  2nd from A7   = {SIGNS[a7_2]}, SAV {SAV[SIGNS[a7_2]]}, lord {LORD[a7_2]} '
      f'({dignity(LORD[a7_2], sg(LORD[a7_2])) or "—"}, house {hs(sg(LORD[a7_2]))})')
print(f'  Upagrahas there: '
      f'{[k for k, v in UPAGRAHA.items() if int(v // 30) == a7_2]}')
print('\n  The image house is respectable -- Guru sitting in A7.  But the house')
print('  that IMAGES their money carries GULIKA and MANDI, the two shadow')
print('  points, on an otherwise average sign whose lord is exalted.  Read')
print('  carefully: the appearance is comfortable and the dispositor is strong,')
print('  but two shadow points on the image house mean apparent standing and')
print('  actual liquidity should not be assumed to match.  Verify rather than')
print('  infer -- and note that the 12 Aug 2026 eclipse fell 33 arcminutes from')
print('  Gulika, in exactly this house.')

# --- 7 ---------------------------------------------------------------------
rule('7. THE NAVAMSHA CROSS-CHECK')
D9 = {k: navamsha(v) for k, v in D1.items()}
d9l = D9['Lagna']
d9_8 = (d9l + 7) % 12
who = [f'{g} ({dignity(g, d9_8)})' if dignity(g, d9_8) else g
       for g in GRAHAS if D9[g] == d9_8]
print(f'  D9 lagna {SIGNS[d9l]};  her 2nd = D9 8th = {SIGNS[d9_8]}: '
      f'{", ".join(who) or "empty"}')
print('  Surya EXALTED in the 8th of D9 as well as of D1.  At navamsha depth the')
print('  spouse\'s family-wealth house holds the best-dignified body in the chart.')

# --- 8 ---------------------------------------------------------------------
rule('8. THE ANSWER, AND ITS LIMIT')
for line in [
    'Wealthy in the sense of STATUS: yes.  Her standing house is the 2nd-',
    'strongest bhava, the Upapada sits in it, and its lord forms Amala yoga.',
    'Educated, respected, well-regarded -- a family whose asset is its name.',
    '',
    'Wealthy in the sense of LIQUID MONEY: not conspicuously.  The house that',
    'holds their wealth is the chart\'s weakest bhava and lowest bindu count,',
    'with the Mrityu upagraha inside and the Khara drekkana across it.',
    '',
    'But it is an EIGHTH house, and that is the whole nuance.  The 8th is the',
    'house of inheritance, joint holdings, insurance, settlements and what',
    'passes from others.  Wealth on her side is more likely INHERITED, TIED UP,',
    'or ARRIVING THROUGH AN EVENT than visible as income.  The wealth-karaka',
    'sits there in one of its two strongest cells, so what transfers is real.',
    '',
    'Directionally it favours HIM.  The 8th is the classical house of gain',
    'through the spouse\'s family, it holds his Atmakaraka at the chart\'s',
    'highest Ishta Phala, and its lord is in parivartana with his 9th.  What',
    'he receives through that marriage is significant -- but it arrives as a',
    'transfer attached to an event, not as a standard of living handed over.',
    '',
    'LIMIT: all of this is derived from HIS chart.  It describes the in-laws',
    'as his nativity signifies them.  Their actual balance sheet requires',
    'their charts, and no bhavat-bhavam derivation substitutes for that.',
]:
    print('  ' + line)
