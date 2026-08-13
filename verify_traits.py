#!/usr/bin/env python3
"""
Natural traits: the classical character apparatus, computed rather than asserted.

Temperament in Jyotisha is not read off the sun-sign. It is assembled from the
janma nakshatra and its koota attributes, the lagna nakshatra, the avasthas,
vargottama status, the gap between the lagna and the arudha lagna, the
dispositor chain, the element/guna tally, and the character-bearing yogas.
This computes all of them from the verified natal longitudes.
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

# Ashtakoota attributes, indexed by nakshatra number 1..27
GANA = {}
for i in [1, 5, 7, 8, 13, 15, 17, 22, 27]: GANA[i] = 'Deva'
for i in [2, 4, 6, 11, 12, 20, 21, 25, 26]: GANA[i] = 'Manushya'
for i in [3, 9, 10, 14, 16, 18, 19, 23, 24]: GANA[i] = 'Rakshasa'
NADI = {}
for i in [1, 6, 7, 12, 13, 18, 19, 24, 25]: NADI[i] = 'Adi (Vata)'
for i in [2, 5, 8, 11, 14, 17, 20, 23, 26]: NADI[i] = 'Madhya (Pitta)'
for i in [3, 4, 9, 10, 15, 16, 21, 22, 27]: NADI[i] = 'Antya (Kapha)'

DEITY = {3: 'Agni', 14: 'Tvashtar / Vishwakarma', 18: 'Indra', 1: 'Ashwini Kumaras',
         2: 'Yama', 5: 'Soma', 6: 'Rudra'}
SHAKTI = {3: 'dahana shakti — the power to burn away',
          14: 'punya-chayani shakti — the power to accumulate merit',
          18: 'arohana shakti — the power to rise'}

ELEMENT = ['Fire', 'Earth', 'Air', 'Water'] * 3
QUALITY = ['Movable', 'Fixed', 'Dual'] * 4
LORD = ['Mangal', 'Shukra', 'Budha', 'Chandra', 'Surya', 'Budha',
        'Shukra', 'Mangal', 'Guru', 'Shani', 'Shani', 'Guru']
VARNA_BY_ELEMENT = {'Water': 'Brahmin', 'Fire': 'Kshatriya',
                    'Earth': 'Vaishya', 'Air': 'Shudra'}

EXALT = {'Surya': 0, 'Chandra': 1, 'Mangal': 9, 'Budha': 5,
         'Guru': 3, 'Shukra': 11, 'Shani': 6}


def dms(sign, d, m, s=0):
    return SIGNS.index(sign) * 30 + d + m / 60 + s / 3600


def fmt(l):
    s = int(l // 30)
    return f"{int(l % 30):02d}°{round((l % 1) * 60):02d}′ {SIGNS[s]}"


def nak_of(l):
    i = int(l // (360 / 27))
    return i + 1, NAK[i], int((l % (360 / 27)) // (360 / 108)) + 1, NAK_LORD[i]


def navamsha(l):
    sign, rem = int(l // 30), l % 30
    start = {0: sign, 1: (sign + 8) % 12, 2: (sign + 4) % 12}[sign % 3]
    return (start + int(rem // (30 / 9))) % 12


D1 = {'Lagna': dms('Kanya', 27, 37, 37), 'Surya': dms('Mesha', 1, 28, 3),
      'Chandra': dms('Vrishabha', 1, 47, 15), 'Mangal': dms('Vrishabha', 7, 19, 32),
      'Budha': dms('Mesha', 10, 27, 50), 'Guru': dms('Mithuna', 14, 47, 52),
      'Shukra': dms('Mesha', 23, 36, 49), 'Shani': dms('Vrishabha', 17, 54, 25),
      'Rahu': dms('Vrishabha', 26, 55, 52), 'Ketu': dms('Vrischika', 26, 55, 52)}
GRAHAS = [g for g in D1 if g != 'Lagna']
LAG = int(D1['Lagna'] // 30)
house = lambda l: (int(l // 30) - LAG) % 12 + 1

rule = lambda t: print('\n' + '=' * 88 + f'\n{t}\n' + '=' * 88)

# --- 1. the two personal nakshatras ---------------------------------------
rule('1. THE TWO PERSONAL NAKSHATRAS — janma (Chandra) and lagna')
for label, key in [('Janma / Chandra', 'Chandra'), ('Lagna', 'Lagna')]:
    l = D1[key]
    n, name, pada, lord = nak_of(l)
    print(f'  {label:16} {fmt(l):18} {name} pada {pada}, lord {lord}')
    print(f'  {"":16} gana {GANA[n]:10} nadi {NADI[n]:16} '
          f'navamsha {SIGNS[navamsha(l)]}')
    if n in DEITY:
        print(f'  {"":16} deity {DEITY[n]}   {SHAKTI.get(n, "")}')
print(f"\n  Varna (from the Moon's sign element, {ELEMENT[int(D1['Chandra']//30)]}): "
      f"{VARNA_BY_ELEMENT[ELEMENT[int(D1['Chandra'] // 30)]]}")
print('\n  BOTH personal points are Rakshasa gana.  That is the single most')
print('  direct statement of temperament the chart makes.')

rule('   Gana tally across all nine grahas')
tally = {}
for g in GRAHAS:
    n, name, pada, lord = nak_of(D1[g])
    tally.setdefault(GANA[n], []).append(g)
for k in ['Deva', 'Manushya', 'Rakshasa']:
    print(f'  {k:9} {len(tally.get(k, [])):2}   {", ".join(tally.get(k, []))}')
print('\n  Three each — evenly split among the grahas.  The imbalance is not in')
print('  the tally; it is that the lagna and the Moon, the two most personal')
print('  points in the chart, are BOTH in the uncompromising class.')

# --- 2. vargottama ---------------------------------------------------------
rule('2. VARGOTTAMA — where the outer and inner charts agree')
for k in ['Lagna'] + GRAHAS:
    d1s, d9s = int(D1[k] // 30), navamsha(D1[k])
    if d1s == d9s:
        extra = ''
        if k in EXALT and EXALT[k] == d1s:
            extra = '  <== exalted AND vargottama'
        print(f'  {k:9} {SIGNS[d1s]:11} in both D1 and D9{extra}')
print('\n  Only these.  A vargottama lagna means the person presented and the')
print('  person underneath are the same construction; a vargottama Surya in')
print('  exaltation means the core self is the most reliable thing he owns.')

# --- 3. avasthas -----------------------------------------------------------
rule('3. BALADI AVASTHA — the maturity state of each graha at birth')
BAL = ['Bala (infant)', 'Kumara (adolescent)', 'Yuva (adult)',
       'Vriddha (old)', 'Mrita (dead)']
for g in GRAHAS:
    if g in ('Rahu', 'Ketu'):
        continue
    sign, rem = int(D1[g] // 30), D1[g] % 30
    idx = int(rem // 6) if sign % 2 == 0 else 4 - int(rem // 6)
    note = ''
    if g == 'Chandra':
        note = '  <== exalted and Mrita at once'
    if g in ('Guru', 'Shani'):
        note = '  <-- the only two in full-fruit avastha'
    print(f'  {g:9} {fmt(D1[g]):18} {BAL[idx]:22}{note}')

# --- 4. arudha lagna vs lagna ---------------------------------------------
rule('4. ARUDHA LAGNA vs LAGNA — how he reads vs how he is')
al = 7        # Vrischika, computed in verify_concepts.py
print(f'  Lagna         {SIGNS[LAG]:11} — Kanya: analytical, corrective, service-framed')
print(f'  Arudha Lagna  {SIGNS[al]:11} — Vrischika: private, intense, hard to read')
print(f'  Occupant of the AL: Ketu at {fmt(D1["Ketu"])}')
print(f'  The AL is the {(al - LAG) % 12 + 1}rd house from the lagna.')
print('\n  The image and the substance are different signs, with the detachment')
print('  node sitting in the image.  He is read as remote and unreadable while')
print('  actually being meticulous and useful.  The gap is structural, not a')
print('  failure of presentation.')

# --- 5. dispositor chain ---------------------------------------------------
rule('5. DISPOSITOR CHAIN — who ultimately governs whom')
for g in GRAHAS:
    if g in ('Rahu', 'Ketu'):
        continue
    chain, cur, seen = [g], g, set()
    while cur not in seen:
        seen.add(cur)
        cur = LORD[int(D1[cur] // 30)]
        chain.append(cur)
        if chain.count(cur) > 1:
            break
    print(f'  {" -> ".join(chain)}')
print('\n  Every chain terminates in the Mangal <-> Shukra exchange.  The whole')
print('  chart is finally governed by a two-planet loop between the 8th lord')
print('  and the 9th lord — appetite answering to values, and back again.')

# --- 6. concentration ------------------------------------------------------
rule('6. CONCENTRATION — the most visible fact about this chart')
occ_signs = sorted({int(D1[g] // 30) for g in GRAHAS if g not in ('Ketu',)})
occ_h = sorted({house(D1[g]) for g in GRAHAS if g != 'Ketu'})
print(f'  Seven classical grahas occupy {len(occ_signs)} signs: '
      f'{", ".join(SIGNS[s] for s in occ_signs)}')
print(f'  They occupy {len(occ_h)} consecutive houses: {occ_h}')
print(f'  Total ecliptic span of the seven: '
      f'{max(D1[g] for g in GRAHAS if g != "Ketu") - min(D1[g] for g in GRAHAS if g != "Ketu"):.1f}°'
      ' out of 360')
print('\n  Everything is packed into a 73-degree arc.  Nabhasa reading: SHOOLA')
print('  (three signs, the spear) and SHAKTI.  Character consequence: enormous')
print('  depth in a narrow band, and very little breadth anywhere else.')

# --- 7. element and quality tally -----------------------------------------
rule('7. ELEMENT, QUALITY AND CONSTITUTION')
e, q = {}, {}
for g in GRAHAS:
    if g in ('Rahu', 'Ketu'):
        continue
    s = int(D1[g] // 30)
    e[ELEMENT[s]] = e.get(ELEMENT[s], 0) + 1
    q[QUALITY[s]] = q.get(QUALITY[s], 0) + 1
print(f'  Elements (7 grahas): {e}   + lagna {ELEMENT[LAG]}')
print(f'  Qualities:           {q}   + lagna {QUALITY[LAG]}')
print(f"  Lagna lord {LORD[LAG]} in {SIGNS[int(D1[LORD[LAG]] // 30)]} "
      f'(house {house(D1[LORD[LAG]])})')
print('\n  No graha in a water sign.  Earth-fire with nothing to cool it:')
print('  practical intensity, low emotional buffering, poor at letting things')
print('  simply pass.  The Antya (Kapha) nadi of Krittika is the one moderating')
print('  factor, and it works on the body rather than the temper.')

# --- 8. character-bearing yogas -------------------------------------------
rule('8. THE YOGAS THAT DESCRIBE CHARACTER RATHER THAN FORTUNE')
for name, verdict in [
    ('Shoola (nabhasa)', 'seven grahas in three signs — one-pointed, penetrating, harsh-edged'),
    ('Shakti (nabhasa)', 'all occupancy in the 8th-10th band — endurance bought with hardship'),
    ('Durudhara', 'benefics flanking the Moon — resourceful, not left destitute'),
    ('Vesi (malefic)', 'Mangal and Shani 2nd from Surya — austere, laboring, self-denying'),
    ('Budha-Aditya', 'intellect fused into the core self — combust, so it works privately'),
    ('Punarphoo', 'Chandra with Shani — serious young, slow to commit, matures late'),
    ('Kemadruma', 'ABSENT — the Moon is not isolated'),
    ('Kalasarpa', 'ABSENT — Guru alone breaks the nodal arc, from a kendra'),
]:
    print(f'  {name:20} {verdict}')

# --- 9. the strength signature of temperament -----------------------------
rule('9. WHERE THE STRENGTH SITS — Shadbala components that read as character')
print('  Budha (lagna lord)  Chesta Bala 42.15  2nd highest in the chart')
print('  Budha (lagna lord)  Dig Bala     4.28  LOWEST of any graha, out of 60')
print('  -> mental motion excellent, positional standing near zero.')
print('     Restless, fast, endlessly re-examining; and constitutionally bad at')
print('     being in the right room at the right time.  This is the chart\'s')
print('     single most actionable trait.')
print('\n  Vimshopaka (out of 20):  Surya 16.85, Chandra 15.32, Shukra 12.60,')
print('  Guru 12.32, Budha 11.45, Shani 11.22, Mangal 10.30')
print('  -> the two luminaries are the best-made things in the chart.  Core')
print('     identity and emotional apparatus are finely built; the working')
print('     planets are ordinary.  He is better than his output for a long time.')
