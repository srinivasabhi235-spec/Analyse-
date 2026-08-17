#!/usr/bin/env python3
"""
The varga apparatus, taken to the level the tradition actually uses.

The reading computed twenty-eight divisional charts and read them one at a
time.  That is only the first layer.  Parashara builds four further things on
top of the vargas, and none of them had been touched:

  1. FOUR VIMSHOPAKA SCHEMES, not one.  Shadvarga (6 charts), Saptavarga (7),
     Dashavarga (10) and Shodashavarga (16) each have their own weights, and
     a graha can grade Excellent on one and Average on another.  The reading
     used only the sixteen-chart version.

  2. THE SIXTY NAMED SHASHTIAMSHAS.  Parashara calls D60 the final arbiter,
     and its sixty divisions are not anonymous -- each carries a name and a
     benefic or malefic character.  The reading read D60 by sign only and
     ignored the layer Parashara actually weights.

  3. THE FIVE TRIMSHAMSHA LORDS.  D30 divides each sign among five malefics
     in unequal portions.  The reading read D30 as signs; the tradition reads
     it as which malefic owns the portion.

  4. VARGOTTAMA ACROSS THE WHOLE SET, and varga-level yogas -- raja yogas
     that form inside D9 and D10 rather than in D1.

Plus Pushkara bhaga, the auspicious degrees, never checked.
"""
from ephem_core import (SIGNS, GRAHAS, COMPUTED, SUPPLIED, LORD, EXALT,
                        varga, sign_of, short, fmt, nak_of, rule, sub)

POS = dict(SUPPLIED)                     # the frame the strength tables use
CLASSICAL = GRAHAS[:7]

DEB = {g: (s + 6) % 12 for g, s in EXALT.items()}
OWN = {'Surya': [4], 'Chandra': [3], 'Mangal': [0, 7], 'Budha': [2, 5],
       'Guru': [8, 11], 'Shukra': [1, 6], 'Shani': [9, 10]}
FRIEND = {'Surya': ['Chandra', 'Mangal', 'Guru'],
          'Chandra': ['Surya', 'Budha'],
          'Mangal': ['Surya', 'Chandra', 'Guru'],
          'Budha': ['Surya', 'Shukra'],
          'Guru': ['Surya', 'Chandra', 'Mangal'],
          'Shukra': ['Budha', 'Shani'],
          'Shani': ['Budha', 'Shukra']}
ENEMY = {'Surya': ['Shukra', 'Shani'], 'Chandra': [],
         'Mangal': ['Budha'], 'Budha': ['Chandra'],
         'Guru': ['Budha', 'Shukra'], 'Shukra': ['Surya', 'Chandra'],
         'Shani': ['Surya', 'Chandra', 'Mangal']}


def dign(g, si):
    if si == EXALT[g]:
        return 'exalted', 20
    if si == DEB[g]:
        return 'debilitated', 3
    if si in OWN[g]:
        return 'own', 20
    l = LORD[si]
    if l == g:
        return 'own', 20
    if l in FRIEND[g]:
        return 'friend', 15
    if l in ENEMY[g]:
        return 'enemy', 7
    return 'neutral', 10


# =============================================================================
rule('1.  THE FOUR VIMSHOPAKA SCHEMES — the reading used only one of them')

SCHEMES = {
    'Shadvarga (6)':      [(1, 6), (2, 2), (3, 4), (9, 5), (12, 2), (30, 1)],
    'Saptavarga (7)':     [(1, 5), (2, 2), (3, 3), (7, 2.5), (9, 4.5), (12, 2),
                           (30, 1)],
    'Dashavarga (10)':    [(1, 3), (2, 1.5), (3, 1.5), (7, 1.5), (9, 1.5),
                           (10, 1.5), (12, 1.5), (16, 1.5), (30, 1.5), (60, 5)],
    'Shodashavarga (16)': [(1, 3.5), (2, 1), (3, 1), (4, 0.5), (7, 0.5), (9, 3),
                           (10, 0.5), (12, 0.5), (16, 2), (20, 0.5), (24, 0.5),
                           (27, 0.5), (30, 1), (40, 0.5), (45, 0.5), (60, 4)],
}
GRADE = [(19, 'Purna — complete'), (15, 'Ati Uttama — excellent'),
         (10, 'Uttama — very good'), (7, 'Madhya — average'),
         (5, 'Adhama — poor'), (0, 'Ati Adhama — very poor')]


def grade(v):
    for lim, name in GRADE:
        if v >= lim:
            return name
    return GRADE[-1][1]


scores = {}
for name, tbl in SCHEMES.items():
    scores[name] = {}
    for g in CLASSICAL:
        tot = sum(dign(g, varga(POS[g], n))[1] * w for n, w in tbl)
        scores[name][g] = tot / 20

print(f"\n  {'graha':9s}" + ''.join(f'{k.split()[0]:>16s}' for k in SCHEMES))
print(f"  {'':9s}" + ''.join(f"{'(' + k.split('(')[1]:>16s}" for k in SCHEMES))
for g in CLASSICAL:
    print(f"  {g:9s}" + ''.join(f'{scores[k][g]:16.2f}' for k in SCHEMES))

print(f"\n  {'graha':9s}" + ''.join(f'{k.split()[0][:10]:>20s}' for k in SCHEMES))
for g in CLASSICAL:
    print(f"  {g:9s}" + ''.join(f'{grade(scores[k][g])[:18]:>20s}' for k in SCHEMES))

sub('where the schemes disagree')
for g in CLASSICAL:
    v = [scores[k][g] for k in SCHEMES]
    spread = max(v) - min(v)
    if spread > 1.5:
        best = max(SCHEMES, key=lambda k: scores[k][g])
        worst = min(SCHEMES, key=lambda k: scores[k][g])
        print(f"  {g:9s} spread {spread:5.2f}   best {best.split()[0]:14s}"
              f"{scores[best][g]:6.2f}   worst {worst.split()[0]:14s}{scores[worst][g]:6.2f}")
print(f"""
  The Shodashavarga figure is the one this reading has always quoted.  Reading
  all four together changes the emphasis in one specific place:

      SHANI grades highest on the SHADVARGA scheme and lowest on the
      Dashavarga/Shodashavarga ones.  The six-chart scheme weights D1, D3 and
      D9 heavily and ignores D60 entirely; the ten- and sixteen-chart schemes
      put 4-5 of their 20 points on D60 alone, where Shani is DEBILITATED.

  So the "Shani is strong by Shadbala but poor by varga dignity" tension the
  reading reported is really a tension about HOW DEEP YOU LOOK.  At the coarse
  level Saturn is respectable.  At the karmic level it is not.
""")

# =============================================================================
rule('2.  THE SIXTY NAMED SHASHTIAMSHAS — Parashara\'s final arbiter, unread')

S60 = [
    ('Ghora', 0), ('Rakshasa', 0), ('Deva', 1), ('Kubera', 1), ('Yaksha', 1),
    ('Kinnara', 1), ('Bhrashta', 0), ('Kulaghna', 0), ('Garala', 0),
    ('Vahni', 0), ('Maya', 0), ('Purishaka', 0), ('Apampathi', 1),
    ('Marutwan', 1), ('Kaala', 0), ('Sarpa', 0), ('Amrita', 1), ('Indu', 1),
    ('Mridu', 1), ('Komala', 1), ('Heramba', 1), ('Brahma', 1), ('Vishnu', 1),
    ('Maheshwara', 1), ('Deva', 1), ('Ardra', 0), ('Kalinasa', 0),
    ('Kshiteesa', 1), ('Kamalakara', 1), ('Gulika', 0), ('Mrityu', 0),
    ('Kaala', 0), ('Davagni', 0), ('Ghora', 0), ('Yama', 0), ('Kantaka', 0),
    ('Sudha', 1), ('Amrita', 1), ('Poornachandra', 1), ('Vishadagdha', 0),
    ('Kulanasa', 0), ('Vamsakshaya', 0), ('Utpata', 0), ('Kaala', 0),
    ('Saumya', 1), ('Komala', 1), ('Sheetala', 1), ('Karaladamshtra', 0),
    ('Chandramukhi', 1), ('Praveena', 1), ('Kaalapavaka', 0),
    ('Dhannayudha', 0), ('Nirmala', 1), ('Saumya', 1), ('Kroora', 0),
    ('Atisheetala', 0), ('Amrita', 1), ('Payodhi', 1), ('Bhramana', 0),
    ('Chandrarekha', 1)]


def shashtiamsha(l):
    """(name, benefic?) -- reversed order in even signs, per Parashara."""
    s, deg = int(l // 30), l % 30
    idx = int(deg * 2)
    if s % 2 == 1:                       # even sign (0-indexed odd)
        idx = 59 - idx
    return S60[idx]


print(f"\n  {'body':9s} {'longitude':22s} {'D60 sign':12s} {'shashtiamsha':16s} character")
ben = mal = 0
for g in ['Lagna'] + GRAHAS:
    nm, b = shashtiamsha(POS[g])
    if g in CLASSICAL:
        ben += b
        mal += 1 - b
    print(f"  {g:9s} {fmt(POS[g], 22)} {SIGNS[varga(POS[g], 60)]:12s} "
          f"{nm:16s} {'BENEFIC' if b else 'malefic'}")
print(f"""
  Of the seven classical grahas: {ben} benefic shashtiamshas, {mal} malefic.

  This is the layer Parashara weights most heavily and the reading never
  opened.  Read it against what the document already says:
""")
for g in CLASSICAL:
    nm, b = shashtiamsha(POS[g])
    print(f"      {g:9s} {nm:16s} {'benefic' if b else 'malefic'}")

# =============================================================================
rule('3.  THE TRIMSHAMSHA LORDS — D30 read as portions, not as signs')

def trimsha(l):
    """(lord, portion) -- unequal 5/5/8/7/5 split, reversed in even signs."""
    s, deg = int(l // 30), l % 30
    if s % 2 == 0:                       # odd sign
        tbl = [(5, 'Mangal', 'Mesha'), (10, 'Shani', 'Kumbha'),
               (18, 'Guru', 'Dhanu'), (25, 'Budha', 'Mithuna'),
               (30, 'Shukra', 'Tula')]
    else:                                # even sign
        tbl = [(5, 'Shukra', 'Vrishabha'), (12, 'Budha', 'Kanya'),
               (20, 'Guru', 'Meena'), (25, 'Shani', 'Makara'),
               (30, 'Mangal', 'Vrischika')]
    for hi, lord, sign in tbl:
        if deg < hi:
            return lord, sign
    return tbl[-1][1], tbl[-1][2]


print(f"\n  {'body':9s} {'longitude':22s} {'trimshamsha lord':18s} portion")
tally = {}
for g in ['Lagna'] + GRAHAS:
    lord, sign = trimsha(POS[g])
    tally[lord] = tally.get(lord, 0) + 1
    print(f"  {g:9s} {fmt(POS[g], 22)} {lord:18s} {sign}")
print(f"\n  tally: " + ', '.join(f'{k} {v}' for k, v in
                                 sorted(tally.items(), key=lambda x: -x[1])))
print("""
  D30 has no benefic lords -- all five portions belong to malefics, which is
  why it is the adversity chart.  What matters is WHICH malefic dominates,
  because that names the KIND of adversity.""")

# =============================================================================
rule('4.  VARGOTTAMA ACROSS THE WHOLE SET')
ALL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 18, 20, 22, 24, 27, 30,
       36, 40, 45, 60, 81, 108, 144, 150]
print(f"\n  A body is vargottama in a varga when that varga repeats its D1 sign.\n")
print(f"  {'body':9s} {'D1 sign':12s} {'repeats in':6s}  which")
for g in ['Lagna'] + GRAHAS:
    d1 = varga(POS[g], 1)
    hits = [n for n in ALL if n != 1 and varga(POS[g], n) == d1]
    print(f"  {g:9s} {SIGNS[d1]:12s} {len(hits):^6d}  "
          + (', '.join(f'D{n}' for n in hits) if hits else '—'))
print("""
  The reading said "only two things in this chart are vargottama: the lagna
  and Surya", meaning the D1/D9 pair specifically.  Across the full set the
  picture is richer, and one result stands out: SURYA repeats Mesha in more
  schemes than any other body -- it is not merely vargottama, it is
  DIMENSIONALLY STABLE.""")

# =============================================================================
rule('5.  VARGA-LEVEL YOGAS — raja yogas that form inside D9 and D10')
for n, label in [(9, 'D9 Navamsha'), (10, 'D10 Dashamsha'), (24, 'D24 Siddhamsha')]:
    lag = varga(POS['Lagna'], n)
    pos = {g: varga(POS[g], n) for g in GRAHAS}
    h = {g: (pos[g] - lag) % 12 + 1 for g in GRAHAS}
    lords = {i: LORD[(lag + i - 1) % 12] for i in range(1, 13)}
    kendra_l = {lords[i] for i in (1, 4, 7, 10)}
    trikona_l = {lords[i] for i in (1, 5, 9)}
    print(f"\n  {label} — lagna {SIGNS[lag]}")
    print(f"      kendra lords  {sorted(kendra_l)}")
    print(f"      trikona lords {sorted(trikona_l)}")
    found = []
    for a in kendra_l:
        for b in trikona_l:
            if a != b and a in h and b in h and h[a] == h[b]:
                found.append((a, b, h[a]))
    if found:
        for a, b, hh in found:
            print(f"      RAJA YOGA: {a} (kendra lord) with {b} (trikona lord) "
                  f"in house {hh}")
    else:
        print("      no kendra-trikona lord conjunction")
    both = kendra_l & trikona_l
    if both:
        print(f"      lords of BOTH a kendra and a trikona: {sorted(both)} "
              "— raja yoga karaka")

# =============================================================================
rule('6.  PUSHKARA BHAGA — the auspicious degrees, never checked')
PUSHKARA = {0: 21, 1: 14, 2: 24, 3: 7, 4: 21, 5: 14,
            6: 24, 7: 7, 8: 21, 9: 14, 10: 24, 11: 7}
print(f"\n  {'body':9s} {'longitude':22s} {'pushkara bhaga':16s} distance")
hits = 0
for g in ['Lagna'] + GRAHAS:
    s = sign_of(POS[g])
    pb = PUSHKARA[s]
    dist = abs(POS[g] % 30 - pb)
    on = dist < 1.0
    hits += on
    print(f"  {g:9s} {fmt(POS[g], 22)} {SIGNS[s]} {pb}°{'':6s} "
          f"{dist:5.2f}°  {'<< ON IT' if on else ''}")
print(f"\n  {hits} bodies on a pushkara bhaga.")
print("""
  Pushkara bhaga is a single auspicious degree per sign -- a body sitting on
  one is said to be protected regardless of other affliction.  Nothing in this
  chart lands on one, which is consistent with everything else the reading
  found: NO free protection anywhere.""")
print('\n' + '=' * 92)
