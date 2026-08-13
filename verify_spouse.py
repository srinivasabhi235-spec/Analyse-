#!/usr/bin/env python3
"""
The spouse, described from his chart alone.

Classical practice reads the partner from five independent apparatuses:
the 7th house and its lord, the karaka Shukra, the Jaimini Darakaraka and its
navamsha (Darakaramsa), the Upapada and the 2nd from it, and the 7th of D9.
This computes all five and reports where they agree and where they conflict.

Everything here is derived from HIS chart.  Nothing about her own nativity is
known, and no koota matching is possible without it -- that limit is stated
in the output rather than papered over.
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
ELEMENT = ['Fire', 'Earth', 'Air', 'Water'] * 3
QUALITY = ['Movable', 'Fixed', 'Dual'] * 4
EXALT = {'Surya': 0, 'Chandra': 1, 'Mangal': 9, 'Budha': 5,
         'Guru': 3, 'Shukra': 11, 'Shani': 6}
DEBIL = {k: (v + 6) % 12 for k, v in EXALT.items()}
OWN = {'Surya': [4], 'Chandra': [3], 'Mangal': [0, 7], 'Budha': [2, 5],
       'Guru': [8, 11], 'Shukra': [1, 6], 'Shani': [9, 10]}
FRIEND = {'Guru': ['Surya', 'Chandra', 'Mangal'], 'Surya': ['Chandra', 'Mangal', 'Guru'],
          'Shukra': ['Budha', 'Shani'], 'Shani': ['Budha', 'Shukra'],
          'Budha': ['Surya', 'Shukra'], 'Chandra': ['Surya', 'Budha'],
          'Mangal': ['Surya', 'Chandra', 'Guru']}
ASPECT = {'Mangal': [4, 7, 8], 'Guru': [5, 7, 9], 'Shani': [3, 7, 10],
          'Rahu': [5, 7, 9], 'Ketu': [5, 7, 9]}


def dms(sign, d, m, s=0):
    return SIGNS.index(sign) * 30 + d + m / 60 + s / 3600


def fmt(l):
    return f"{int(l % 30):02d}°{round((l % 1) * 60):02d}′ {SIGNS[int(l // 30)]}"


def nak_of(l):
    i = int(l // (360 / 27))
    return NAK[i], int((l % (360 / 27)) // (360 / 108)) + 1, NAK_LORD[i]


def navamsha(l):
    sign, rem = int(l // 30), l % 30
    return ({0: sign, 1: (sign + 8) % 12, 2: (sign + 4) % 12}[sign % 3]
            + int(rem // (30 / 9))) % 12


def dignity(g, sign):
    if EXALT.get(g) == sign: return 'EXALTED'
    if DEBIL.get(g) == sign: return 'debilitated'
    if sign in OWN.get(g, []): return 'own sign'
    if LORD[sign] in FRIEND.get(g, []): return 'friend'
    if g in ('Rahu', 'Ketu'): return '—'
    return 'enemy' if LORD[sign] not in FRIEND.get(g, []) else 'neutral'


def baladi(g, l):
    sign, rem = int(l // 30), l % 30
    i = int(rem // 6) if sign % 2 == 0 else 4 - int(rem // 6)
    return ['Bala', 'Kumara', 'Yuva', 'Vriddha', 'Mrita'][i]


D1 = {'Lagna': dms('Kanya', 27, 37, 37), 'Surya': dms('Mesha', 1, 28, 3),
      'Chandra': dms('Vrishabha', 1, 47, 15), 'Mangal': dms('Vrishabha', 7, 19, 32),
      'Budha': dms('Mesha', 10, 27, 50), 'Guru': dms('Mithuna', 14, 47, 52),
      'Shukra': dms('Mesha', 23, 36, 49), 'Shani': dms('Vrishabha', 17, 54, 25),
      'Rahu': dms('Vrishabha', 26, 55, 52), 'Ketu': dms('Vrischika', 26, 55, 52)}
GRAHAS = [g for g in D1 if g != 'Lagna']
LAG = int(D1['Lagna'] // 30)
D9 = {k: navamsha(v) for k, v in D1.items()}
D9LAG = D9['Lagna']
h1 = lambda s: (s - LAG) % 12 + 1
h9 = lambda s: (s - D9LAG) % 12 + 1
occ = lambda s: [g for g in GRAHAS if int(D1[g] // 30) == s]
occ9 = lambda s: [g for g in GRAHAS if D9[g] == s]

rule = lambda t: print('\n' + '=' * 90 + f'\n{t}\n' + '=' * 90)


def describe(g, tag=''):
    l = D1[g]
    s = int(l // 30)
    n, p, nl = nak_of(l)
    return (f'  {g:8} {fmt(l):18} H{h1(s):<2} {dignity(g, s):12} '
            f'{n} p{p} (lord {nl}), {baladi(g, l)}, D9 {SIGNS[D9[g]]}{tag}')


# --- 1. the 7th house ------------------------------------------------------
rule('1. THE 7TH HOUSE — the relationship container')
S7 = (LAG + 6) % 12
print(f'  7th sign      {SIGNS[S7]} — {ELEMENT[S7]}, {QUALITY[S7]}, lord {LORD[S7]}')
print(f'  Occupants     {occ(S7) or "EMPTY"}')
asp = []
for g, offs in ASPECT.items():
    if (int(D1[g] // 30) + o - 1) % 12 == S7 if False else \
       any((int(D1[g] // 30) + o - 1) % 12 == S7 for o in offs):
        asp.append(g)
for g in GRAHAS:
    if g not in ASPECT and (int(D1[g] // 30) + 6) % 12 == S7:
        asp.append(g)
print(f'  Aspected by   {asp or "nothing"}')
print(describe(LORD[S7], '   <== the 7th lord'))
print(f'\n  Meena is Guru\'s own water sign, dual, and the softest sign in the')
print('  zodiac.  It is EMPTY, receives only Ketu\'s 5th aspect, and its lord')
print('  sits in an enemy sign in the 10th.  Container: gentle, undefended,')
print('  and administered from a distance by a graha that is busy elsewhere.')

# --- 2. the karaka ---------------------------------------------------------
rule('2. SHUKRA — the natural karaka of the wife')
print(describe('Shukra'))
print('  Also: Atmakaraka (highest degree), highest Ishta Phala in the chart,')
print('  in parivartana with Mangal, inside the 22nd (Khara) drekkana with the')
print('  Mrityu upagraha 3°13′ away, and in its OWN nakshatra Bharani.')
print('\n  Shukra in Mesha: quick to attach, direct, impatient with ambiguity.')
print('  Bharani: endurance through burden, the nakshatra of restraint and of')
print('  bearing what must be borne.  Vriddha avastha: old, experienced, spent')
print('  of naivety.  This is not a light or decorative Venus.')

# --- 3. Jaimini Darakaraka -------------------------------------------------
rule('3. DARAKARAKA — the Jaimini spouse-significator')
dk = min((g for g in GRAHAS if g not in ('Rahu', 'Ketu')), key=lambda g: D1[g] % 30)
print(f'  Darakaraka = {dk} (lowest degree-in-sign, {D1[dk] % 30:.2f}°)')
print(describe(dk))
dka = D9[dk]
print(f'\n  Darakaramsa (DK\'s navamsha sign) = {SIGNS[dka]} '
      f'— {ELEMENT[dka]}, {QUALITY[dka]}, lord {LORD[dka]}')
print(f'  Grahas in the Darakaramsa in D9: {occ9(dka) or "none"}')
print(f'  That sign is the {h9(dka)}th house of D9.')
print('\n  The Darakaraka is Surya EXALTED and VARGOTTAMA, in the 8th.')
print('  Jaimini treats the DK as the most personal descriptor of the spouse.')
print('  An exalted, vargottama Sun says: sovereign, proud, self-directed,')
print('  used to being the centre — and the Darakaramsa in Mesha doubles it.')

# --- 4. Upapada ------------------------------------------------------------
rule('4. UPAPADA LAGNA — the marriage itself and the spouse it brings')
l12 = (LAG + 11) % 12
lord12 = LORD[l12]
step = (int(D1[lord12] // 30) - l12) % 12
ul = (int(D1[lord12] // 30) + step) % 12
if (ul - l12) % 12 in (0, 6):
    ul = (ul + 9) % 12
print(f'  12th sign {SIGNS[l12]}, lord {lord12} in {SIGNS[int(D1[lord12] // 30)]} '
      f'-> Upapada = {SIGNS[ul]} (house {h1(ul)})')
print(f'  UL lord      {LORD[ul]} — {fmt(D1[LORD[ul]])}, H{h1(int(D1[LORD[ul]] // 30))}')
ul2 = (ul + 1) % 12
print(f'  2nd from UL  {SIGNS[ul2]}, lord {LORD[ul2]} — {fmt(D1[LORD[ul2]])}, '
      f'H{h1(int(D1[LORD[ul2]] // 30))}')
print(f'  Occupants of UL: {occ(ul) or "empty"};  of the 2nd from UL: '
      f'{occ(ul2) or "empty"}')
print('\n  Upapada in Dhanu: the marriage carries a dharmic, philosophical,')
print('  foreign-leaning signature — and Dhanu is the most straightforward')
print('  sign in the zodiac, so honesty is structural to her.')
print('  The 2nd from UL is Makara under Shani: the union is SUSTAINED by')
print('  duty and endurance rather than by romance.  Shani there is also the')
print('  classical marker of a partner who is sober, older in manner, or both.')

# --- 5. the 7th of D9 ------------------------------------------------------
rule('5. THE NAVAMSHA — the chart of the spouse')
print(f'  D9 lagna {SIGNS[D9LAG]} (vargottama)')
for g in GRAHAS:
    print(f'  {g:8} D9 {SIGNS[D9[g]]:11} H{h9(D9[g]):<3} {dignity(g, D9[g])}')
S79 = (D9LAG + 6) % 12
print(f'\n  D9 7th house  {SIGNS[S79]}, lord {LORD[S79]}')
print(f'  Occupants     {occ9(S79) or "EMPTY"}')
print(f'  D9 7th lord {LORD[S79]} sits in {SIGNS[D9[LORD[S79]]]}, '
      f'H{h9(D9[LORD[S79]])} of D9')

# --- 6. the 7th from Chandra and from Shukra -------------------------------
rule('6. THE 7TH FROM CHANDRA AND FROM SHUKRA — how she is experienced')
for base in ('Chandra', 'Shukra'):
    s = (int(D1[base] // 30) + 6) % 12
    print(f'  7th from {base:8} = {SIGNS[s]:11} lord {LORD[s]:8} '
          f'occupants {occ(s) or "empty"}')

# --- 7. the 7th across the vargas -----------------------------------------
rule('7. THE 7TH ACROSS THE SUPPLIED VARGAS — where Ketu keeps appearing')
VARGA7 = {
    'D1  (Meena)':      occ(S7),
    'D9  (Meena)':      occ9(S79),
    'D10 (Simha, lagna Kumbha)': ['Ketu'],
    'D11 (Mithuna, lagna Dhanu)': ['Ketu'],
    'D30 (Vrischika, lagna Vrishabha)': ['Chandra', 'Ketu'],
}
for k, v in VARGA7.items():
    print(f'  {k:34} {v or "empty"}')
print('\n  Ketu occupies or aspects the 7th in four of the seven supplied')
print('  vargas, and in D30 it sits 4° from Chandra there.  That is the single')
print('  most repeated statement the chart makes about the partnership.')

# --- 7b. the element split -------------------------------------------------
rule('7b. THE ELEMENT SPLIT — the woman vs the container')
markers = [
    ('Darakaraka Surya, sign', int(D1['Surya'] // 30)),
    ('Darakaramsa', D9['Surya']),
    ('Karaka Shukra, sign', int(D1['Shukra'] // 30)),
    ('Upapada', ul),
]
containers = [
    ('7th house from lagna', S7),
    ('7th house of D9', S79),
    ('7th from Chandra', (int(D1['Chandra'] // 30) + 6) % 12),
]
print('  Significators OF HER:')
for k, s2 in markers:
    print(f'    {k:26} {SIGNS[s2]:11} {ELEMENT[s2]}')
print('  Houses that CONTAIN the relationship:')
for k, s2 in containers:
    print(f'    {k:26} {SIGNS[s2]:11} {ELEMENT[s2]}')
me = {}
for _, s2 in markers: me[ELEMENT[s2]] = me.get(ELEMENT[s2], 0) + 1
ce = {}
for _, s2 in containers: ce[ELEMENT[s2]] = ce.get(ELEMENT[s2], 0) + 1
print(f'\n  Her significators: {me}')
print(f'  The container:     {ce}')
print('\n  Every significator of the woman herself is FIRE.  Every house that')
print('  holds the relationship is WATER.  She is a fire-natured person inside')
print('  a water-signed marriage -- which is exactly why the reading keeps')
print('  producing both "direct and unbudgeable" and "gentle and undefended".')
print('  They are describing different objects.')

# --- 8. the limit ----------------------------------------------------------
rule('8. WHAT CANNOT BE DERIVED')
print('  Ashtakoota / guna milan, her Mangal dosha, her dasha sequence, her')
print('  own lagna: all require HER birth data.  None of it is present.')
print('  Everything above describes the spouse as HIS chart signifies her,')
print('  which is a description of the role she plays in his life -- not a')
print('  substitute for reading her nativity.')
