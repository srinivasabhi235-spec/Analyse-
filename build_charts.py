#!/usr/bin/env python3
"""
Emit the complete Shodashavarga as markdown.

Every one of the sixteen divisional charts is computed from the verified D1
longitudes using the same varga engine as verify_shodasha.py -- which is
calibrated by the fact that its D9, D10, D27 and D30 reproduce the supplied
source tables exactly.

Writes a markdown fragment to stdout: a master grid, then each varga in full
with its own lagna, house numbers and dignities.
"""
SIGNS = ['Mesha', 'Vrishabha', 'Mithuna', 'Karka', 'Simha', 'Kanya',
         'Tula', 'Vrischika', 'Dhanu', 'Makara', 'Kumbha', 'Meena']
# Vrishabha and Vrischika both truncate to "Vris", so the grid uses explicit
# unambiguous four-letter codes rather than a naive slice.
ABBR = ['Mesh', 'Vrsb', 'Mith', 'Kark', 'Simh', 'Kany',
        'Tula', 'Vrsc', 'Dhan', 'Maka', 'Kumb', 'Meen']
S = SIGNS.index
BODIES = ['Lagna', 'Surya', 'Chandra', 'Mangal', 'Budha',
          'Guru', 'Shukra', 'Shani', 'Rahu', 'Ketu']
GRAHAS = BODIES[1:]
CLASSICAL = BODIES[1:8]


def d(sg, a, b, c=0):
    return S(sg) * 30 + a + b / 60 + c / 3600


D1 = {'Lagna': d('Kanya', 27, 37, 37), 'Surya': d('Mesha', 1, 28, 3),
      'Chandra': d('Vrishabha', 1, 47, 15), 'Mangal': d('Vrishabha', 7, 19, 32),
      'Budha': d('Mesha', 10, 27, 50), 'Guru': d('Mithuna', 14, 47, 52),
      'Shukra': d('Mesha', 23, 36, 49), 'Shani': d('Vrishabha', 17, 54, 25),
      'Rahu': d('Vrishabha', 26, 55, 52), 'Ketu': d('Vrischika', 26, 55, 52)}

MOV = {0, 3, 6, 9}
FIX = {1, 4, 7, 10}
sgn = lambda l: int(l // 30)
pos = lambda l: l % 30


def v(l, n):
    """Divisional sign index for division n, standard Parashari rules."""
    s, p = sgn(l), pos(l)
    if n == 1:  return s
    if n == 2:  return 4 if (p < 15) == (s % 2 == 0) else 3
    if n == 3:  return (s + 4 * int(p // 10)) % 12
    if n == 4:  return (s + 3 * int(p // 7.5)) % 12
    if n == 7:  return ((s if s % 2 == 0 else (s + 6) % 12) + int(p / (30 / 7))) % 12
    if n == 9:  return int(l * 9 / 30) % 12
    if n == 10: return ((s if s % 2 == 0 else (s + 8) % 12) + int(p / 3)) % 12
    if n == 12: return (s + int(p / 2.5)) % 12
    if n == 16: return ((0 if s in MOV else 4 if s in FIX else 8) + int(p / 1.875)) % 12
    if n == 20: return ((0 if s in MOV else 8 if s in FIX else 4) + int(p / 1.5)) % 12
    if n == 24: return ((4 if s % 2 == 0 else 3) + int(p / 1.25)) % 12
    if n == 27: return int(l * 27 / 30) % 12
    if n == 30:
        lim = ([(5, 0), (10, 10), (18, 8), (25, 2), (30, 6)] if s % 2 == 0
               else [(5, 1), (12, 5), (20, 11), (25, 9), (30, 7)])
        for hi, sg_ in lim:
            if p < hi: return sg_
        return lim[-1][1]
    if n == 40: return ((0 if s % 2 == 0 else 6) + int(p / 0.75)) % 12
    if n == 45: return ((0 if s in MOV else 4 if s in FIX else 8) + int(p / (2 / 3))) % 12
    if n == 60: return (s + int(p * 2)) % 12
    raise ValueError(n)


OWN = {'Surya': [4], 'Chandra': [3], 'Mangal': [0, 7], 'Budha': [2, 5],
       'Guru': [8, 11], 'Shukra': [1, 6], 'Shani': [9, 10]}
EXAL = {'Surya': 0, 'Chandra': 1, 'Mangal': 9, 'Budha': 5,
        'Guru': 3, 'Shukra': 11, 'Shani': 6}
DEB = {g: (x + 6) % 12 for g, x in EXAL.items()}
FRIEND = {'Surya': ['Chandra', 'Mangal', 'Guru'], 'Chandra': ['Surya', 'Budha'],
          'Mangal': ['Surya', 'Chandra', 'Guru'], 'Budha': ['Surya', 'Shukra'],
          'Guru': ['Surya', 'Chandra', 'Mangal'], 'Shukra': ['Budha', 'Shani'],
          'Shani': ['Budha', 'Shukra']}
ENEMY = {'Surya': ['Shukra', 'Shani'], 'Chandra': [], 'Mangal': ['Budha'],
         'Budha': ['Chandra'], 'Guru': ['Budha', 'Shukra'],
         'Shukra': ['Surya', 'Chandra'], 'Shani': ['Surya', 'Chandra', 'Mangal']}
LORD = ['Mangal', 'Shukra', 'Budha', 'Chandra', 'Surya', 'Budha',
        'Shukra', 'Mangal', 'Guru', 'Shani', 'Shani', 'Guru']


def dignity(g, si):
    if g in ('Rahu', 'Ketu', 'Lagna'): return '—'
    if si == EXAL[g]: return '**exalted**'
    if si == DEB[g]:  return '*debilitated*'
    if si in OWN[g]:  return '**own sign**'
    l = LORD[si]
    if l in FRIEND[g]: return 'friend'
    if l in ENEMY[g]:  return 'enemy'
    return 'neutral'


VARGAS = [(1, 'D1', 'Rashi', 'the body, and everything else'),
          (2, 'D2', 'Hora', 'wealth and its source'),
          (3, 'D3', 'Drekkana', 'siblings, courage, self-effort'),
          (4, 'D4', 'Chaturthamsha', 'property, fixed assets, home'),
          (7, 'D7', 'Saptamsha', 'children and progeny'),
          (9, 'D9', 'Navamsha', 'the spouse, and the chart\'s inner strength'),
          (10, 'D10', 'Dashamsha', 'career, action, standing'),
          (12, 'D12', 'Dwadashamsha', 'parents and lineage'),
          (16, 'D16', 'Shodashamsha', 'vehicles, comforts, happiness'),
          (20, 'D20', 'Vimshamsha', 'spiritual practice and devotion'),
          (24, 'D24', 'Siddhamsha', 'education and learning'),
          (27, 'D27', 'Bhamsha', 'strength, vitality, constitution'),
          (30, 'D30', 'Trimshamsha', 'misfortune, adversity, character flaws'),
          (40, 'D40', 'Khavedamsha', 'maternal legacy, auspicious effects'),
          (45, 'D45', 'Akshavedamsha', 'paternal legacy, overall conduct'),
          (60, 'D60', 'Shashtiamsha', 'accumulated karma — the finest division')]
KEN, TRI, UPA, DUS = [1, 4, 7, 10], [1, 5, 9], [3, 6, 10, 11], [6, 8, 12]

out = []
w = out.append

# ---- master grid -----------------------------------------------------------
w('#### The master grid — every body in every varga\n')
w('| Body | ' + ' | '.join(n for _, n, _, _ in VARGAS) + ' |')
w('|---' * (len(VARGAS) + 1) + '|')
for b in BODIES:
    cells = []
    for n, _, _, _ in VARGAS:
        si = v(D1[b], n)
        nm = ABBR[si]
        if b not in ('Lagna', 'Rahu', 'Ketu'):
            if si == EXAL[b]: nm = f'**{nm}**'
            elif si == DEB[b]: nm = f'*{nm}*'
        cells.append(nm)
    label = f'**{b}**' if b == 'Lagna' else b
    w(f'| {label} | ' + ' | '.join(cells) + ' |')
w('')
w('*Bold = exalted · italic = debilitated. Codes: Vrsb = Vrishabha, '
  'Vrsc = Vrischika; the rest are the first four letters. Full tables '
  'follow.*\n')

# ---- dignity tallies -------------------------------------------------------
w('#### Dignity across all sixteen\n')
w('| Graha | Exalted | Own | Debilitated | Friend | Neutral | Enemy |')
w('|---|---|---|---|---|---|---|')
for g in CLASSICAL:
    t = {'**exalted**': 0, '**own sign**': 0, '*debilitated*': 0,
         'friend': 0, 'neutral': 0, 'enemy': 0}
    for n, _, _, _ in VARGAS:
        t[dignity(g, v(D1[g], n))] += 1
    w(f'| **{g}** | {t["**exalted**"]} | {t["**own sign**"]} | '
      f'{t["*debilitated*"]} | {t["friend"]} | {t["neutral"]} | {t["enemy"]} |')
w('')

# ---- each varga in full ----------------------------------------------------
for n, code, name, what in VARGAS:
    vl = v(D1['Lagna'], n)
    w(f'#### {code} · {name} — *{what}*\n')
    census = {'kendra': 0, 'trikona': 0, 'upachaya': 0, 'dusthana': 0}
    rows = []
    for b in GRAHAS:
        si = v(D1[b], n)
        hn = (si - vl) % 12 + 1
        cls = [k for k, s in (('kendra', KEN), ('trikona', TRI),
                              ('upachaya', UPA), ('dusthana', DUS)) if hn in s]
        for c in cls:
            census[c] += 1
        rows.append((b, SIGNS[si], hn, '+'.join(cls) or '—', dignity(b, si)))
    w(f'**Lagna {SIGNS[vl]}**, lord **{LORD[vl]}** '
      f'(in {SIGNS[v(D1[LORD[vl]], n)]}, house '
      f'{(v(D1[LORD[vl]], n) - vl) % 12 + 1} of this varga)\n')
    w('| Body | Sign | House | Class | Dignity |')
    w('|---|---|---|---|---|')
    for b, s, hn, cls, dg in rows:
        w(f'| {b} | {s} | {hn} | {cls} | {dg} |')
    w('')
    w(f'*Census — kendra {census["kendra"]} · trikona {census["trikona"]} · '
      f'upachaya {census["upachaya"]} · dusthana {census["dusthana"]}*\n')

print('\n'.join(out))
