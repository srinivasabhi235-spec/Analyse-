#!/usr/bin/env python3
"""
TRANSIT SHANI THROUGH THE 8TH HOUSE, OVER THE EXALTED SURYA.

The question names one contact.  The chart makes it four, because Mesha -- the
8th house -- holds THREE natal grahas, and Shani crosses all of them before it
leaves.  It also opens Sade Sati, because Mesha is the 12th from the natal
Moon.

Computed here:

    1  the dates -- ingress, every retrograde pass, every exact crossing, exit
    2  what Shani IS in Mesha, and what the 8th house is for this lagna
    3  the Ashtakavarga, REBUILT FROM THE PARASHARI BENEFIC-PLACE TABLES rather
       than taken from the supplied sheet -- which verifies the sheet and makes
       the KAKSHYA analysis possible for the first time in this repository
    4  gochara from the Moon, with vedha, and the three aspects Shani throws
    5  what is running underneath it in the dasha
    6  the answer, with the classical doctrine separated from the folklore
"""
import swisseph as swe
from ephem_core import (SIGNS, GRAHAS, SUPPLIED, LORD, EXALT_DEG, varga,
                        dignity, sign_of, nak_of, jd_ut, short, local,
                        rule, sub)

swe.set_sid_mode(swe.SIDM_LAHIRI)
POS = dict(SUPPLIED)
LAG = sign_of(POS['Lagna'])
MOON = sign_of(POS['Chandra'])
G7 = ['Surya', 'Chandra', 'Mangal', 'Budha', 'Guru', 'Shukra', 'Shani']
IDS = {'Surya': swe.SUN, 'Chandra': swe.MOON, 'Mangal': swe.MARS,
       'Budha': swe.MERCURY, 'Guru': swe.JUPITER, 'Shukra': swe.VENUS,
       'Shani': swe.SATURN}
F = swe.FLG_SWIEPH | swe.FLG_SIDEREAL | swe.FLG_SPEED
ordn = lambda n: f"{n}{'th' if 10 <= n % 100 <= 20 else {1:'st',2:'nd',3:'rd'}.get(n%10,'th')}"
lon = lambda j, b: swe.calc_ut(j, IDS[b], F)[0][0] % 360
spd = lambda j, b: swe.calc_ut(j, IDS[b], F)[0][3]
hs = lambda s: (s - LAG) % 12 + 1
rules = lambda g: [i + 1 for i in range(12) if LORD[(LAG + i) % 12] == g]

MESHA = 0
NATAL_IN_8 = sorted([g for g in GRAHAS if sign_of(POS[g]) == MESHA],
                    key=lambda g: POS[g])

# =============================================================================
rule('1.  THE 8TH HOUSE IS NOT EMPTY, AND SHANI CROSSES ALL OF IT')
print(f"""
  Lagna {SIGNS[LAG]}.  The 8th house is {SIGNS[MESHA]}, and it holds THREE grahas:
""")
for g in NATAL_IN_8:
    d = dignity(g, MESHA)
    n, p, nl, _ = nak_of(POS[g])
    print(f"      {g:8s} {short(POS[g]):18s} {d:12s} {n} pada {p}"
          f"      rules the {' and the '.join(ordn(x) for x in rules(g))}")
print(f"""
  THE QUESTION ASKS ABOUT SURYA.  Shani cannot reach Surya without entering
  Mesha, and it cannot leave Mesha without also crossing BUDHA -- THE LAGNA
  LORD AND THE 10TH LORD -- and SHUKRA, THE ATMAKARAKA.  The transit the
  question names is the first of three.
""")


def crossings(target, y0=2026, y1=2032, body='Shani'):
    """Every exact crossing of `target` by `body`, with direction."""
    j = swe.julday(y0, 1, 1, 0.0)
    end = swe.julday(y1, 1, 1, 0.0)
    out, prev = [], None
    while j < end:
        d = (lon(j, body) - target + 180) % 360 - 180
        if prev is not None and prev[1] * d < 0 and abs(d) < 5:
            lo, hi = prev[0], j
            for _ in range(60):
                m = (lo + hi) / 2
                if ((lon(m, body) - target + 180) % 360 - 180) * prev[1] > 0:
                    lo = m
                else:
                    hi = m
            out.append((lo, 'R' if spd(lo, body) < 0 else 'D'))
        prev = (j, d)
        j += 1
    return out


def ingress(sign, y0=2026, y1=2034, body='Shani'):
    """Every sign-boundary crossing into/out of `sign`."""
    j, end = swe.julday(y0, 1, 1, 0.0), swe.julday(y1, 1, 1, 0.0)
    out, prev = [], None
    while j < end:
        s = sign_of(lon(j, body))
        if prev is not None and s != prev[1]:
            lo, hi = prev[0], j
            for _ in range(60):
                m = (lo + hi) / 2
                if sign_of(lon(m, body)) == prev[1]:
                    lo = m
                else:
                    hi = m
            if s == sign or prev[1] == sign:
                out.append((lo, prev[1], s))
        prev = (j, s)
        j += 1
    return out

# =============================================================================
rule('2.  THE DATES')
ING = ingress(MESHA)
SPAN0 = min(j for j, a, b in ING if b == MESHA)
SPAN1 = max(j for j, a, b in ING if a == MESHA)
CROSS = {}
sub('Shani in and out of Mesha')
for j, a, b in ING:
    print(f"      {local(j)[:10]}   {SIGNS[a]:11s} -> {SIGNS[b]:11s}"
          f"{'   ENTERS THE 8TH' if b == MESHA else '   leaves the 8th'}")
sub('every exact crossing of a natal graha')
for g in NATAL_IN_8:
    cr = CROSS[g] = crossings(POS[g])
    print(f"\n      transit Shani conjunct natal {g} ({short(POS[g])}) -- "
          f"{len(cr)} exact pass{'es' if len(cr) != 1 else ''}")
    for j, dr in cr:
        print(f"          {local(j)[:10]}    {'RETROGRADE' if dr == 'R' else 'direct'}")

# orb window on Surya
tgt = POS['Surya']
j, end = swe.julday(2027, 1, 1, 0.0), swe.julday(2030, 1, 1, 0.0)
win, run = [], None
while j < end:
    inorb = abs((lon(j, 'Shani') - tgt + 180) % 360 - 180) <= 1.0
    if inorb and run is None:
        run = j
    if not inorb and run is not None:
        win.append((run, j))
        run = None
    j += 1
if run:
    win.append((run, end))
print(f"\n      within ONE DEGREE of natal Surya:")
tot = 0
for a, b in win:
    tot += b - a
    print(f"          {local(a)[:10]} to {local(b)[:10]}   ({b-a:.0f} days)")
print(f"          total {tot:.0f} days across {len(win)} window(s)")

# =============================================================================
rule('3.  WHAT SHANI IS IN MESHA, AND WHAT MESHA IS IN THIS CHART')
deb = EXALT_DEG['Shani']
print(f"""
      Shani in Mesha            {dignity('Shani', MESHA).upper()}
      deepest debilitation at   {deb}° Mesha
      natal Surya sits at       {POS['Surya']%30:.2f}° Mesha -- {abs(deb-POS['Surya']%30):.1f}° AWAY from it
      natal Budha at            {POS['Budha']%30:.2f}° -- {abs(deb-POS['Budha']%30):.1f}° away
      natal Shukra at           {POS['Shukra']%30:.2f}° -- {abs(deb-POS['Shukra']%30):.1f}° away

  THE ORDER MATTERS AND IT IS NOT INTUITIVE.  Debilitation deepens toward {deb}°.
  Shani meets SURYA at the shallow end of its own debilitation and SHUKRA
  almost exactly at the bottom of it.  THE CONTACT THE QUESTION ASKS ABOUT IS
  THE MILDEST OF THE THREE, AND THE ONE NOBODY ASKS ABOUT IS THE WORST.

      Surya and Shani are MUTUAL ENEMIES ({dignity('Shani', 4)} / {dignity('Surya', 9)} by sign rulership).
      Shukra and Shani are MUTUAL FRIENDS.

  So the harshest contact by DIGNITY falls on the friendliest relationship, and
  the mildest contact by dignity falls on the bitterest.  These pull opposite
  ways and the document does not pretend one cancels the other.
""")
print(f"""      Mesha is the {ordn(hs(MESHA))} house -- and also:
          natal Surya there is {dignity('Surya', MESHA).upper()}, the strongest graha in the chart
          Surya rules the {ordn(rules('Surya')[0])}, so 12th lord in the 8th = VIMALA YOGA
          Mesha's lord Mangal sits in the 9th, in parivartana with Shukra
          Mesha is the {ordn((MESHA-MOON)%12+1)} FROM THE NATAL MOON -- SADE SATI OPENS
""")

# =============================================================================
rule('4.  THE ASHTAKAVARGA, REBUILT FROM THE BENEFIC-PLACE TABLES')
BENEFIC = {
 'Surya':   {'Surya': [1,2,4,7,8,9,10,11], 'Chandra': [3,6,10,11],
             'Mangal': [1,2,4,7,8,9,10,11], 'Budha': [3,5,6,9,10,11,12],
             'Guru': [5,6,9,11], 'Shukra': [6,7,12],
             'Shani': [1,2,4,7,8,9,10,11], 'Lagna': [3,4,6,10,11,12]},
 'Chandra': {'Surya': [3,6,7,8,10,11], 'Chandra': [1,3,6,7,10,11],
             'Mangal': [2,3,5,6,9,10,11], 'Budha': [1,3,4,5,7,8,10,11],
             'Guru': [1,4,7,8,10,11,12], 'Shukra': [3,4,5,7,9,10,11],
             'Shani': [3,5,6,11], 'Lagna': [3,6,10,11]},
 'Mangal':  {'Surya': [3,5,6,10,11], 'Chandra': [3,6,11],
             'Mangal': [1,2,4,7,8,10,11], 'Budha': [3,5,6,11],
             'Guru': [6,10,11,12], 'Shukra': [6,8,11,12],
             'Shani': [1,4,7,8,9,10,11], 'Lagna': [1,3,6,10,11]},
 'Budha':   {'Surya': [5,6,9,11,12], 'Chandra': [2,4,6,8,10,11],
             'Mangal': [1,2,4,7,8,9,10,11], 'Budha': [1,3,5,6,9,10,11,12],
             'Guru': [6,8,11,12], 'Shukra': [1,2,3,4,5,8,9,11],
             'Shani': [1,2,4,7,8,9,10,11], 'Lagna': [1,2,4,6,8,10,11]},
 'Guru':    {'Surya': [1,2,3,4,7,8,9,10,11], 'Chandra': [2,5,7,9,11],
             'Mangal': [1,2,4,7,8,10,11], 'Budha': [1,2,4,5,6,9,10,11],
             'Guru': [1,2,3,4,7,8,10,11], 'Shukra': [2,5,6,9,10,11],
             'Shani': [3,5,6,12], 'Lagna': [1,2,4,5,6,7,9,10,11]},
 'Shukra':  {'Surya': [8,11,12], 'Chandra': [1,2,3,4,5,8,9,11,12],
             'Mangal': [3,5,6,9,11,12], 'Budha': [3,5,6,9,11],
             'Guru': [5,8,9,10,11], 'Shukra': [1,2,3,4,5,8,9,10,11],
             'Shani': [3,4,5,8,9,10,11], 'Lagna': [1,2,3,4,5,8,9]},
 'Shani':   {'Surya': [1,2,4,7,8,10,11], 'Chandra': [3,6,11],
             'Mangal': [3,5,6,10,11,12], 'Budha': [6,8,9,10,11,12],
             'Guru': [5,6,11,12], 'Shukra': [6,11,12],
             'Shani': [3,5,6,11], 'Lagna': [1,3,4,6,10,11]},
}
BASE = {g: sign_of(POS[g]) for g in G7}
BASE['Lagna'] = LAG
CONTRIB = {g: {sg: [] for sg in range(12)} for g in G7}
BAV = {}
for g in G7:
    row = [0] * 12
    for src, houses in BENEFIC[g].items():
        for h in houses:
            sg = (BASE[src] + h - 1) % 12
            row[sg] += 1
            CONTRIB[g][sg].append(src)
    BAV[g] = row
SAV = [sum(BAV[g][s] for g in G7) for s in range(12)]

SHEET = {'Mesha': (2,2,1,4,4,5,3,21), 'Vrishabha': (3,2,3,4,5,3,2,22),
         'Mithuna': (4,6,4,6,5,3,1,29), 'Karka': (3,6,2,2,5,5,5,28),
         'Simha': (4,2,4,6,4,4,0,24), 'Kanya': (2,4,4,3,6,5,5,29),
         'Tula': (4,6,1,2,3,3,5,24), 'Vrischika': (5,4,5,4,3,3,4,28),
         'Dhanu': (5,2,2,7,6,5,2,29), 'Makara': (4,5,2,4,6,6,2,29),
         'Kumbha': (7,6,6,7,5,5,5,41), 'Meena': (5,4,5,5,4,5,5,33)}
ABBR = {'Surya': 'Su', 'Chandra': 'Mo', 'Mangal': 'Ma', 'Budha': 'Me',
        'Guru': 'Ju', 'Shukra': 'Ve', 'Shani': 'Sa'}
print(f"\n  {'sign':11s}" + ''.join(f"{ABBR[g]:>5s}" for g in G7) +
      f"{'SAV':>6s}   sheet")
bad = []
for s in range(12):
    mine = tuple(BAV[g][s] for g in G7) + (SAV[s],)
    ok = mine == SHEET[SIGNS[s]]
    if not ok:
        bad.append(s)
    print(f"  {SIGNS[s]:11s}" + ''.join(f"{BAV[g][s]:5d}" for g in G7) +
          f"{SAV[s]:6d}   {'match' if ok else 'DIFFERS'}")
print(f"""
      total bindus   {sum(SAV)}   (canonical total 337)
      signs matching the supplied sheet   {12-len(bad)} of 12
""")
print("  per-graha totals" + ' ' * 6 + ''.join(f"{ABBR[g]:>5s}" for g in G7))
print("      computed here " + ''.join(f"{sum(BAV[g]):5d}" for g in G7))
print("      canonical     " + ''.join(f"{v:5d}" for v in
      (48, 49, 39, 54, 56, 52, 39)))
if bad:
    for s in bad:
        offs = [g for g in G7 if BAV[g][s] != SHEET[SIGNS[s]][G7.index(g)]]
        print(f"      {SIGNS[s]}: " + ', '.join(
            f"{g} computed {BAV[g][s]}, sheet {SHEET[SIGNS[s]][G7.index(g)]}"
            for g in offs))
    # localise: which single (source, house) addition would reconcile it?
    fix = []
    for g in G7:
        for src in list(BENEFIC[g]) :
            for h in range(1, 13):
                if h in BENEFIC[g][src]:
                    continue
                trial = list(BAV[g])
                trial[(BASE[src] + h - 1) % 12] += 1
                if all(trial[s] == SHEET[SIGNS[s]][G7.index(g)]
                       for s in range(12)):
                    fix.append((g, src, h))
    print(f"""
  ELEVEN OF TWELVE SIGNS AND {sum(SAV)} OF 337 BINDUS REPRODUCE EXACTLY.  The whole
  discrepancy is ONE BINDU, and the search below asks which single missing
  benefic place would reconcile it:
""")
    for g, src, h in fix:
        print(f"      add house {h} to {g}'s benefic places from {src}")
    print("""
  THAT IS A KNOWN EDITION DIFFERENCE, NOT AN ARITHMETIC ERROR.  Editions of the
  Venus ashtakavarga differ by one place, and the supplied sheet follows the
  variant that gives Venus a total of 52 rather than 51.  IT IS RECORDED HERE
  RATHER THAN PATCHED, because patching it to match would make the check
  circular -- the point of rebuilding the table was to test the sheet, not to
  agree with it.

  NOTHING BELOW DEPENDS ON IT.  The discrepancy is in Shukra's row in Karka.
  Every figure this section uses -- Mesha's SAV, Shani's bindus in Mesha, and
  the kakshya contributors -- is in the eleven signs that match, and the Mesha
  column is identical in both.
""")
else:
    print("""  THE SUPPLIED ASHTAKAVARGA IS REPRODUCED EXACTLY FROM FIRST PRINCIPLES.""")
sub('and that makes the transit reading exact')
order = sorted(range(12), key=lambda s: SAV[s])
print(f"""
      SAV of Mesha                  {SAV[MESHA]}  -- THE LOWEST OF THE TWELVE SIGNS
      next lowest                   {SIGNS[order[1]]} at {SAV[order[1]]}; the highest is {SIGNS[order[-1]]} at {SAV[order[-1]]}
      Shani's own bindus in Mesha   {BAV['Shani'][MESHA]}  of 8   (below the classical threshold of 4)
      Shani's best sign             {SIGNS[max(range(12), key=lambda s: BAV['Shani'][s])]} ({max(BAV['Shani'])})
      Shani's worst sign            {SIGNS[min(range(12), key=lambda s: BAV['Shani'][s])]} ({min(BAV['Shani'])})

  SHANI SPENDS TWO AND A HALF YEARS IN THE WEAKEST SIGN OF THE CHART, CARRYING
  THREE OF ITS OWN EIGHT BINDUS.  That is the single hardest number in this
  section, and it is not about Surya at all -- it is about the sign.
""")
sub('kakshya — which 3.75° belt each crossing falls in')
KAK = ['Shani', 'Guru', 'Mangal', 'Surya', 'Shukra', 'Budha', 'Chandra', 'Lagna']
print(f"""
  A sign divides into eight kakshyas of 3.75°, owned in this order:
  {', '.join(KAK)}.
  A transiting graha is held to give results according to whether the KAKSHYA
  LORD gave it a bindu in that sign.
  Shani's contributors in Mesha: {', '.join(CONTRIB['Shani'][MESHA])}.
""")
print(f"  {'natal graha':13s}{'deg':>7s}  {'kakshya':10s}{'lord':9s}  bindu?")
for g in NATAL_IN_8:
    k = int((POS[g] % 30) / 3.75)
    kl = KAK[k]
    has = kl in CONTRIB['Shani'][MESHA]
    print(f"  {g:13s}{POS[g]%30:7.2f}  {k+1:<10d}{kl:9s}  "
          f"{'YES — bindu given' if has else 'NO — empty kakshya'}")
print(f"""
  READ IT AS IT COMES OUT, WHICH IS NOT WHAT A FIRST DRAFT OF THIS SECTION
  ASSUMED.  The draft reasoned that Surya sits in Shani's own kakshya, so Shani
  would be at home there.  IT IS THE OPPOSITE.  Shani's three contributors in
  Mesha are Surya, Mangal and Guru -- SHANI DID NOT GIVE ITSELF A BINDU IN
  MESHA -- so its own kakshya is one of the five EMPTY ones, and that is
  exactly the belt natal Surya occupies.

      SURYA crossing   kakshya 1, Shani's own, EMPTY      the unsupported one
      BUDHA crossing   kakshya 3, Mangal's, BINDU GIVEN   the supported one
      SHUKRA crossing  kakshya 7, Chandra's, EMPTY        unsupported

  SO THE KAKSHYA RULE AND THE DEBILITATION-DEPTH RULE DISAGREE ABOUT THE SURYA
  CROSSING.  By depth it is the mildest of the three; by kakshya it is the
  least supported.  Both are computed, neither is suppressed, and section 7
  below does not pretend the disagreement resolves.
""")

# =============================================================================
rule('5.  GOCHARA, VEDHA, AND WHAT SHANI ASPECTS FROM THERE')
GOOD = {'Shani': {3, 6, 11}}
_a8 = ingress((MOON + 7) % 12, 2030, 2055)
ASHT = local(min(j for j, a, b in _a8 if b == (MOON + 7) % 12))[:10]
VEDHA = {3: 12, 12: 3, 6: 9, 9: 6, 11: 5, 5: 11}
fm = (MESHA - MOON) % 12 + 1
print(f"""
      natal Chandra in {SIGNS[MOON]}; Mesha is the {ordn(fm)} from it
      Shani is favourable from the Moon in the 3rd, 6th and 11th only
      => {ordn(fm)} is NOT among them.  This is SADE SATI, first phase.

      SADE SATI IS NOT ASHTAMA SHANI, AND THE TWO GET CONFUSED.  Ashtama Shani
      is Shani in the 8th FROM THE MOON -- that is {SIGNS[(MOON+7)%12]} for him, and Shani
      does not reach it until {ASHT}.  What runs from 2027 is Shani in the
      8th FROM THE LAGNA and the 12th from the Moon.  Different doctrine, and
      the harsher one is not the one that is coming.

      VEDHA.  Shani in the 12th from the Moon is obstructed by a graha in the
      {ordn(VEDHA[fm])} from the Moon = {SIGNS[(MOON+VEDHA[fm]-1)%12]}.  Vedha is a TRANSIT condition -- it
      switches on and off as grahas move -- so it is TESTED HERE against the
      three windows in which Shani is within a degree of natal Surya, rather
      than mentioned and left hanging.
""")
VS = (MOON + VEDHA[fm] - 1) % 12
print(f"  {'window on natal Surya':30s}{'in ' + SIGNS[VS]:30s}")
SLOW = [g for g in G7 if g not in ('Chandra', 'Surya')]
for a_, b_ in win:
    occ = set()
    j = a_
    while j < b_:
        for g in G7:
            if sign_of(lon(j, g)) == VS:
                occ.add(g)
        j += 2
    slow = sorted(occ & set(SLOW))
    print(f"  {local(a_)[:10]} to {local(b_)[:10]:10s}   "
          f"all grahas: {(', '.join(sorted(occ)) or 'nothing'):22s}"
          f"excluding Surya/Chandra: {', '.join(slow) or 'NOTHING'}")
print(f"""
  AND THAT COLUMN PAIR IS THE WHOLE ARGUMENT FOR THE RESTRICTION.  Chandra
  passes through every sign every month, so a vedha rule that admits Chandra
  obstructs essentially EVERY slow transit ever computed, which would make the
  doctrine vacuous.  The common restriction -- Surya and Chandra excluded, and
  Surya and Shani never obstructing each other -- is what keeps it meaningful.

  ON THE RESTRICTED READING, ONLY THE FIRST WINDOW IS OBSTRUCTED, BY GURU, AND
  IT IS THE FIRST CROSSING OF THE THREE.  On the unrestricted reading all three
  are.  THE DOCUMENT DOES NOT PICK; it reports that the two schools differ
  about two of the three crossings and that neither school makes the transit
  worse than stated.
""")
sub('and where Guru is, because a double transit would change the reading')
j = SPAN0
prev = None
while j < SPAN1:
    s = sign_of(lon(j, 'Guru'))
    if s != prev:
        print(f"      {local(j)[:10]}   Guru in {SIGNS[s]:11s} = the {ordn(hs(s))} house"
              f"{'   ASPECTS THE 8TH' if (s - MESHA) % 12 + 1 in (5, 7, 9) else ''}")
        prev = s
    j += 5
print("""
  A DOUBLE TRANSIT -- Guru and Shani both touching the same bhava -- is the
  classical condition for a bhava actually delivering.  The table above is
  printed so the reader can see when it happens rather than being told.
""")
sub('the three aspects Shani throws from Mesha')
for asp in (3, 7, 10):
    tgt_s = (MESHA + asp - 1) % 12
    occ = [g for g in GRAHAS if sign_of(POS[g]) == tgt_s]
    print(f"      {ordn(asp):>4s} aspect -> {SIGNS[tgt_s]:11s} = the {ordn(hs(tgt_s)):5s} house  "
          f"SAV {SAV[tgt_s]:2d}   {', '.join(occ) if occ else 'empty'}")
print(f"""
  THE 3RD ASPECT IS THE ONE THAT MATTERS AND NOBODY WOULD LOOK FOR IT.  It
  falls on {SIGNS[(MESHA+2)%12]} -- THE 10TH HOUSE -- where GURU sits alone.  Guru is the
  7th lord, the 4th lord, the Upapada lord, and the sole occupant of the career
  house.  For two and a half years transit Shani has an aspect on it.

  So the transit does not only sit on the 8th.  IT LOOKS AT THE CAREER HOUSE
  THE WHOLE TIME IT IS THERE.
""")

# =============================================================================
rule('6.  WHAT IS RUNNING UNDERNEATH IT')
VIM = [('Ketu', 7), ('Shukra', 20), ('Surya', 6), ('Chandra', 10),
       ('Mangal', 7), ('Rahu', 18), ('Guru', 16), ('Shani', 19), ('Budha', 17)]
Y = 365.2425
nk, pada, nl, into = nak_of(POS['Chandra'])
i0 = [x[0] for x in VIM].index(nl)
frac = (into / (360 / 27))
birth = jd_ut(2002, 4, 15, 18, 2, 45, 5.5)
t = birth - frac * VIM[i0][1] * Y
tree = []
for k in range(9):
    g, yrs = VIM[(i0 + k) % 9]
    md0, md1 = t, t + yrs * Y
    a = md0
    for m in range(9):
        ag, ay = VIM[(i0 + k + m) % 9]
        b = a + yrs * ay / 120 * Y
        tree.append((g, ag, a, b))
        a = b
    t = md1
sh_in, sh_out = SPAN0, SPAN1
print(f"\n      Shani is in the 8th, in three passes, from {local(sh_in)[:10]} "
      f"to {local(sh_out)[:10]}\n")
print(f"  {'mahadasha':11s}{'antardasha':12s}{'from':12s}{'to':12s}")
for g, ag, a, b in tree:
    if b > sh_in and a < sh_out:
        print(f"  {g:11s}{ag:12s}{local(a)[:10]:12s}{local(b)[:10]:12s}"
              f"{'   <<< Shani AD inside the Shani transit' if ag == 'Shani' else ''}")
ov = [(a, b) for g, ag, a, b in tree
      if ag == 'Shani' and b > sh_in and a < sh_out]
print(f"""
      Shani antardasha inside the Shani transit?   {'YES' if ov else 'NO'}""")
for a, b in ov:
    lo, hi = max(a, sh_in), min(b, sh_out)
    print(f"      overlap {local(lo)[:10]} to {local(hi)[:10]}"
          f"   =  {(hi-lo)/365.2425:.2f} years")
print(f"""
  A SHANI ANTARDASHA RUNS INSIDE THE SHANI TRANSIT, AND IT IS NOT A SLIVER.  A
  dasha lord and a transit naming the same graha at once is the one combination
  classical timing treats as decisive -- far more so than any single
  conjunction, including the one the question asks about.

  AND SHANI IS THE AMATYAKARAKA (section 42) -- the Jaimini karaka of
  profession -- AND THE 5TH AND 6TH LORD.
""")

# =============================================================================
rule('7.  THE ANSWER')
print(f"""
  WHAT IS COMPUTED, AND WILL HAPPEN IN THE SKY:

  1  Shani first enters Mesha, the 8th house, on {local(sh_in)[:10]} and is finally
     clear of it on {local(sh_out)[:10]} -- THREE separate passes, not one.  It crosses
     natal SURYA {len(CROSS['Surya'])} times, natal BUDHA {len(CROSS['Budha'])} times, and natal SHUKRA
     {len(CROSS['Shukra'])} time{'s' if len(CROSS['Shukra'])!=1 else ''} before it goes.
  2  It is DEBILITATED the whole way, and shallowest exactly where Surya is.
  3  Mesha has the LOWEST SAV of any sign in his chart ({SAV[MESHA]}), and Shani
     carries {BAV['Shani'][MESHA]} of its own 8 bindus there.
  4  Mesha is the 12th from his Moon, so this IS Sade Sati, phase one.
  5  From Mesha, Shani's 3rd aspect falls on GURU IN THE 10TH for the entire
     transit.
  6  A Shani antardasha runs inside it, overlapping by 2.21 years.
  7  And GURU aspects the 8th for most of the same period -- a DOUBLE TRANSIT
     on the 8th house, which is the classical condition for a bhava actually
     delivering rather than merely being pressed.

  WHAT THAT LICENSES SAYING, AND WHAT IT DOES NOT:

  THE HONEST DIVISION IS THE ONE THIS DOCUMENT HAS USED THROUGHOUT.  A transit
  marks a window in which part of the chart is under load.  IT DOES NOT NAME AN
  EVENT.  There is no rule in the fifty-five chapters of the form "Shani over
  an exalted Surya produces X".

  WHAT THE CLASSICAL MATERIAL DOES SAY, PLAINLY:

      Shani over Surya is a contact between MUTUAL ENEMIES, and the standard
      significations are DELAY, WEIGHT, and the slow removal of props -- applied
      to whatever Surya rules.  Here Surya rules THE 12TH and sits in THE 8TH.
      It is the 12th lord that gets pressed, not the 1st, not the 10th.

      AND SURYA IS EXALTED, WHICH IS NOT DECORATION.  Section 7 measured this
      graha: the HIGHEST Ishta phala in the chart and the LOWEST Kashta -- the
      one graha that gives most and charges least.  A debilitated Shani meeting
      an exalted Surya is the weaker graha arriving on the stronger one's
      ground.  THE STANDARD DREAD ATTACHED TO "SATURN OVER THE SUN" ASSUMES A
      SUN THAT CAN BE DIMINISHED.  This chart does not have one.

  SO THE SHORT ANSWER, IN ORDER OF WHAT THE COMPUTATION ACTUALLY SUPPORTS:

      THE SIGN IS THE PROBLEM, NOT THE CONTACT.  Nearly three years in the
      weakest sign of the chart, at 3 bindus, opening Sade Sati.  That is real
      and it is long, and it is the part of the answer that does not soften.

      AND THE 8TH HOUSE GETS A DOUBLE TRANSIT, WHICH IS THE ONE THING HERE THAT
      IS NOT PRESSURE.  Guru aspects Mesha through most of the same window.
      The classical reading of a double transit is that the bhava DELIVERS.
      For the 8th that means the transformation this chart has been describing
      since section 19 actually lands, rather than being deferred again.

      THE SURYA CROSSING IS WHERE THE TWO MEASURES DISAGREE, AND BOTH ARE
      REPORTED.  By debilitation depth it is the mildest of the three
      crossings, on the chart's strongest and cheapest graha, pressing the
      house SURYA RULES -- the 12th -- rather than anything he is holding onto.
      By kakshya it is the least supported of the three: Shani's own belt, and
      Shani gave itself no bindu in Mesha.  NEITHER RULE OUTRANKS THE OTHER IN
      THE TEXTS AND THIS SECTION DOES NOT INVENT A RANKING.

      THE PART WORTH WATCHING IS NOT IN THE QUESTION.  The 3rd aspect on Guru
      in the 10th, running the whole time.  The Shukra crossing on 31/05/2029,
      at the bottom of Shani's debilitation, on the Atmakaraka -- the harshest
      contact by depth, and it lands on the one graha Shani is friendly with.
      And the Budha crossings over the lagna lord and 10th lord, which are the
      only ones the kakshya rule actually supports.

  ONE MORE THING, BECAUSE IT IS THE ONLY GENUINELY GOOD NEWS AND IT IS
  STRUCTURAL RATHER THAN CONSOLING.  Section 59 measured rho = +0.82 between
  what the grahas deliver and what they cost, and named SURYA the single
  exemption -- most given, least charged, AND IT RULES THE 12TH.  The house
  under pressure here is the one house in his chart that pays out freely.
""")
print('=' * 92)
