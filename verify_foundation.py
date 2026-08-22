#!/usr/bin/env python3
"""
CHAPTERS 1 TO 41 — THE HALF OF THE BOOK WITH NO CONTENTS PAGE.

Two contents pages have been supplied: Volume 2 (chapters 46-96) and the tail
of Volume 1 (chapters 42-45).  Section 35 assigned a state to all fifty-five
of those.

CHAPTERS 1 TO 41 HAVE NEVER BEEN SUPPLIED IN ANY FORM.

And that is the half that matters most, because it is the foundation: signs,
grahas, houses, the divisional charts, aspects, strengths, and the yogas.
Almost everything this reading does lives there.

I WILL NOT RECONSTRUCT THAT CONTENTS PAGE FROM MEMORY.  Section 31 refused to
invent citations and that refusal stands; a chapter list recalled rather than
read would be indistinguishable from a fabricated one.

SO THIS SCRIPT DOES THE PART THAT DOES NOT NEED THE PAGE.

Section 31 flagged eight rules as school-dependent and located all eight in
chapters 1-41.  It never asked the obvious follow-up:

    HOW MUCH OF THE READING ACTUALLY MOVES IF EACH ONE GOES THE OTHER WAY?

That is computable now, without the book.  It converts "we do not have the
chapter" into "here is exactly what the chapter would decide".
"""
from ephem_core import (SIGNS, GRAHAS, SUPPLIED, LORD, EXALT, varga,
                        dignity, sign_of, rule, sub)

POS = dict(SUPPLIED)
LAG = sign_of(POS['Lagna'])
G7 = [g for g in GRAHAS if g not in ('Rahu', 'Ketu')]
hs = lambda g: (sign_of(POS[g]) - LAG) % 12 + 1
ordn = lambda n: f"{n}{'th' if 10 <= n % 100 <= 20 else {1:'st',2:'nd',3:'rd'}.get(n%10,'th')}"
rules_of = lambda g: [i + 1 for i in range(12) if LORD[(LAG + i) % 12] == g]

# =============================================================================
rule('1.  WHAT IS MISSING, MEASURED')
V1_HAVE, V1_TOTAL, BOOK = 4, 45, 96
print(f"""
  The volume split is fixed by the two pages in hand: Volume 1 runs to chapter
  45, Volume 2 opens at 46.

      chapters in the work                     {BOOK}
      Volume 2, contents supplied              51   (46-96)
      Volume 1 tail, contents supplied          {V1_HAVE}   (42-45)
      ------------------------------------------------
      SUPPLIED                                 {51+V1_HAVE}   ({(51+V1_HAVE)/BOOK*100:.0f}% of the work)
      NEVER SUPPLIED                           {BOOK-51-V1_HAVE}   (1-41, {(BOOK-51-V1_HAVE)/BOOK*100:.0f}% of the work)

  SO THE READING HAS AN ADDRESS FOR 57 PERCENT OF PARASHARA AND NONE AT ALL FOR
  THE OTHER 43 PERCENT -- and the 43 percent is the foundational half.

  WHAT LIVES THERE, stated as techniques rather than as guessed chapter
  numbers.  Every item below is used by this reading and none of it can be
  anywhere except chapters 1-41, because 42-96 is now fully enumerated and does
  not contain it:
""")
FOUND = [
    ('the twelve rasis and their attributes', 'every section'),
    ('the grahas, their natures and karakatwas', 'every section'),
    ('house significations (bhava vichara)', '§9, §27'),
    ('THE SHODASHAVARGA — construction of all sixteen', '§11, §12, §13'),
    ('exaltation, debilitation, moolatrikona, own sign', '§4'),
    ('friendship — natural, temporal and compound', '§4, §6'),
    ('DRISHTI — the aspect rules and their strengths', '§10'),
    ('SHADBALA — all six strength components', '§7'),
    ('Bhava Bala', '§8'),
    ('Ishta and Kashta phala', '§7'),
    ('the raja yogas, dhana yogas, and the rest', '§14'),
    ('viparita raja yoga', '§25'),
    ('kendradhipati dosha', '§27'),
    ('combustion (astangata)', '§4, §25'),
    ('vargottama, pushkara, gandanta', '§5, §13, §16'),
    ('the upagrahas', '§16'),
    ('Jaimini karakas, arudhas, argala', '§15, §30'),
    ('Kuja dosha', '§25'),
    ('Kemadruma and the Chandra yogas', '§25'),
]
for t, w in FOUND:
    print(f"      {t:52s}{w}")
print(f"""
  NINETEEN TECHNIQUE FAMILIES, AND THE READING USES ALL NINETEEN.

  Compare that with what the supplied half gave: the dasha apparatus, the
  Ashtakavarga chain, Sudarshana Chakra, Panchamahapurusha, longevity, maraka,
  avasthas, and the remedial chapters.  IMPORTANT, BUT DOWNSTREAM.

  THE PAGE THIS DOCUMENT STILL NEEDS IS THE ONE IT HAS BEEN ASKING FOR SINCE
  SECTION 31: the Shodashavarga chapter.  What follows measures exactly how
  much rests on it.
""")

# =============================================================================
rule('2.  THE DISPUTE NOBODY NOTICED — IT IS INSIDE THE SHODASHAVARGA')
print("""
  Section 12 declined six divisional charts because "schools disagree on the
  starting sign": D5, D6, D15, D18, D22, D36.  That was the right call.

  BUT IT STOPPED THERE, AND IT SHOULD NOT HAVE.

  The starting-sign convention is not a defect peculiar to those six.  It is a
  property of any varga built as "pick a base sign, then count".  AND FIVE
  MEMBERS OF THE SHODASHAVARGA ARE BUILT EXACTLY THAT WAY -- plus the Hora,
  whose two competing forms are the oldest dispute in the subject.

  Those six are not declined.  They are load-bearing: they feed VIMSHOPAKA
  BALA, which section 7 uses as one of its four strength measures.
""")
VARGAS = [(1, 'D1', 3.5), (2, 'D2', 1), (3, 'D3', 1), (4, 'D4', 0.5),
          (7, 'D7', 0.5), (9, 'D9', 3), (10, 'D10', 0.5), (12, 'D12', 0.5),
          (16, 'D16', 2), (20, 'D20', 0.5), (24, 'D24', 0.5), (27, 'D27', 0.5),
          (30, 'D30', 1), (40, 'D40', 0.5), (45, 'D45', 0.5), (60, 'D60', 4)]
DISPUTED = {2, 16, 20, 24, 40, 45}
SCORE = {'exalted': 20, 'own': 20, 'friend': 15, 'neutral': 10,
         'enemy': 7, 'debilitated': 3}
wd = sum(w for n, _, w in VARGAS if n in DISPUTED)
wt = sum(w for _, _, w in VARGAS)
print(f"  {'varga':7s}{'weight':>8s}   construction        start convention")
for n, nm, w in VARGAS:
    if n in DISPUTED:
        how = {2: 'Simha/Karka by parity — vs the Kashinatha hora',
               16: 'movable Mesha / fixed Simha / dual Dhanu',
               20: 'movable Mesha / fixed Dhanu / dual Simha',
               24: 'odd from Simha / even from Karka',
               40: 'odd from Mesha / even from Tula',
               45: 'movable Mesha / fixed Simha / dual Dhanu'}[n]
        print(f"  {nm:7s}{w:8.1f}   DISPUTED START      {how}")
print(f"""
      disputed weight  {wd:.1f} of {wt:.0f}  =  {wd/wt*100:.0f}% OF VIMSHOPAKA BALA

  A QUARTER OF THAT MEASURE RESTS ON RULES THIS READING HAS ITSELF FLAGGED AS
  SCHOOL-DEPENDENT -- and section 12 declined six OTHER vargas for that very
  reason while never noticing these six.
""")

# =============================================================================
rule('3.  HOW FAR CAN VIMSHOPAKA MOVE?  A COMPLETE BOUND')
print("""
  THE BOUND IS EXACT, AND IT DOES NOT REQUIRE GUESSING ANY RIVAL RULE.

  Whatever the true convention is, a base rule assigns SOME starting sign, and
  the resulting varga sign is (base + part) mod 12.  So sweeping all twelve
  possible bases covers EVERY POSSIBLE RULE, including ones nobody has
  proposed.  A base rule may also assign different bases to different rasis, so
  each graha is allowed its own extreme -- which makes this a strict upper
  bound on the disagreement rather than an estimate.
""")
base = {}
lo = {}
hi = {}
for g in G7:
    fixed = sum(w * SCORE[dignity(g, varga(POS[g], n))]
                for n, _, w in VARGAS if n not in DISPUTED)
    b = fixed
    mn = fixed
    mx = fixed
    for n, _, w in VARGAS:
        if n not in DISPUTED:
            continue
        cur = varga(POS[g], n)
        vals = [SCORE[dignity(g, (cur + k) % 12)] for k in range(12)]
        b += w * vals[0]
        mn += w * min(vals)
        mx += w * max(vals)
    base[g], lo[g], hi[g] = b / 20, mn / 20, mx / 20
band = lambda s: ('EXCELLENT' if s >= 15 else 'good' if s >= 10
                  else 'moderate' if s >= 7 else 'weak')
print(f"  {'graha':9s}{'as built':>10s}{'min':>8s}{'max':>8s}{'range':>8s}   band as built -> band range")
for g in sorted(G7, key=lambda x: -base[x]):
    bl, bh = band(lo[g]), band(hi[g])
    flag = '   <<< BAND CAN CHANGE' if bl != bh else ''
    print(f"  {g:9s}{base[g]:10.2f}{lo[g]:8.2f}{hi[g]:8.2f}{hi[g]-lo[g]:8.2f}   "
          f"{band(base[g]):9s} -> {bl}/{bh}{flag}")
ordb = sorted(G7, key=lambda x: -base[x])
print(f"""
  EVERY RANGE IS THE SAME, 4.25, AND THAT IS NOT A COINCIDENCE.  The disputed
  weight is {wd:.0f} of {wt:.0f} and the dignity scale runs 3 to 20, so the largest possible
  swing is {wd:.0f} x 17 / {wt:.0f} = 4.25 for any graha whatever.  WHICH MEANS THE RISK IS NOT
  TO ANY ONE FIGURE.  IT IS TO THE ORDER.

  AND THE ORDER NEEDS A TIGHTER TEST THAN THE COLUMNS ABOVE.  A starting-sign
  rule assigns a base to a RASI, not to a graha -- so grahas sharing a D1 sign
  must move TOGETHER:
""")
byrasi = {}
for g in G7:
    byrasi.setdefault(sign_of(POS[g]), []).append(g)
for s, gs in sorted(byrasi.items()):
    print(f"      {SIGNS[s]:11s} {', '.join(gs)}")


def maxdiff(x, y):
    """Largest achievable base[x] - base[y] over all start-sign rules, with
    grahas in one rasi forced to share a base."""
    same = sign_of(POS[x]) == sign_of(POS[y])
    d = sum(w * (SCORE[dignity(x, varga(POS[x], n))]
                 - SCORE[dignity(y, varga(POS[y], n))])
            for n, _, w in VARGAS if n not in DISPUTED)
    for n, _, w in VARGAS:
        if n not in DISPUTED:
            continue
        cx, cy = varga(POS[x], n), varga(POS[y], n)
        if same:
            d += w * max(SCORE[dignity(x, (cx + k) % 12)]
                         - SCORE[dignity(y, (cy + k) % 12)] for k in range(12))
        else:
            d += w * (max(SCORE[dignity(x, (cx + k) % 12)] for k in range(12))
                      - min(SCORE[dignity(y, (cy + k) % 12)] for k in range(12)))
    return d / 20


print(f"""
  THE EXACT TEST.  For each graha, can it overtake the one above it under SOME
  starting-sign rule?  The maximum of a difference of sums is the sum of the
  per-varga maxima, so this is computed exactly rather than sampled.
""")
print(f"  {'challenger':11s}{'incumbent':11s}{'gap as built':>14s}{'best case':>12s}   verdict")
flips = 0
for i in range(1, len(ordb)):
    y, x = ordb[i - 1], ordb[i]
    md = maxdiff(x, y)
    ok = md > 0
    flips += ok
    print(f"  {x:11s}{y:11s}{base[x]-base[y]:14.2f}{md:12.2f}   "
          f"{'CAN OVERTAKE' if ok else 'cannot'}")
top = [g for g in G7 if g == ordb[0] or maxdiff(g, ordb[0]) > 0]
gap = {g: maxdiff(g, ordb[0]) for g in G7 if g != ordb[0]}
near = min((g for g in G7 if g not in top), key=lambda g: -gap[g])
print(f"""
  {flips} OF SIX ADJACENT PAIRS CAN SWAP.  EVERY SINGLE ADJACENCY IN THE ORDER IS
  REVERSIBLE by a starting-sign rule this document does not have the page for.

  I DRAFTED THE NEXT LINE EXPECTING THE EXACT TEST TO SHORTEN THE LIST OF
  POSSIBLE LEADERS, ON THE REASONING THAT SHUKRA SHARES MESHA WITH SURYA AND
  CANNOT MOVE INDEPENDENTLY OF IT.  IT DOES NOT.  Shukra clears Surya by
  {maxdiff('Shukra', ordb[0]):.2f} even with the base forced to be shared.  Both tests name the same
  three:

      {', '.join(top)}

  SO THE EXACT TEST CONFIRMS THE LOOSE BOUND RATHER THAN NARROWING IT -- but it
  is not redundant, because it turns up something the loose bound could not:

      {near} FALLS SHORT OF FIRST PLACE BY {-gap[near]:.2f} OF A POINT.

  A graha whose functional nature is itself disputed (see part 4) misses the
  top of this reading's strength order by seven hundredths, on a rule nobody
  has read.  THAT IS AS CLOSE TO A COIN TOSS AS THIS DOCUMENT CONTAINS.

  WHAT SURVIVES REGARDLESS: Surya and Chandra cannot be displaced to LAST under
  any rule, and Mangal, Budha, Guru and Shani cannot reach FIRST.  The top of
  the order is a closed set of three and the bottom is a closed set of four.
  EVERYTHING INSIDE THOSE TWO SETS IS UNDETERMINED.
""")

# =============================================================================
rule('4.  THE OTHER SEVEN DISPUTES, EACH PRICED')
sub('Dispute 1 — D8 and D11 construction.  SETTLED, AND NOT BY THE BOOK')
print("""
  Section 11 rebuilt D8 and D11 from scratch and reproduced the SUPPLIED charts
  10 of 10 placements each, nodes included.

  THIS IS THE ONE DISPUTE THE MISSING CHAPTER CANNOT REOPEN.  A rule that
  reproduces twenty independent placements exactly is confirmed by data, and a
  contents page could only tell us what to call it.  RECORDED AS CLOSED.
""")

sub('Dispute 2 — viparita raja yoga cancelled by strength')
DUST = (6, 8, 12)
vip = [(g, rules_of(g), hs(g)) for g in G7
       if any(h in DUST for h in rules_of(g)) and hs(g) in DUST]
for g, r, h in vip:
    print(f"      {g:8s} rules {r}  sits in the {ordn(h)}  "
          f"dignity: {dignity(g, sign_of(POS[g]))}")
print(f"""
  {len(vip)} viparita yoga in the chart, and it is SURYA -- 12th lord in the 8th,
  which is Vimala yoga.  AND SURYA IS EXALTED.

      SCHOOL A   the yoga stands; a dusthana lord in a dusthana destroys the
                 bad it would otherwise do, and strength helps it do so
      SCHOOL B   the yoga is CANCELLED; viparita needs an afflicted graha and
                 an exalted 12th lord is not an afflicted one

  SECTION 25 TOOK SCHOOL B AND SAID SO.  What it did not say is the size of
  the bet: Surya is the ONLY viparita yoga this chart has, so School A would
  hand the chart a raja yoga it currently does not have, formed by the graha
  section 7 already calls the cheapest deliverer it owns.

  PRICE OF THE DISPUTE: one raja yoga, on the 12th lord.  NOT SETTLEABLE HERE.
""")

sub('Dispute 3 — kendradhipati dosha, and this is the expensive one')
KEN = (1, 4, 7, 10)
NAT_BEN = ('Guru', 'Shukra', 'Budha', 'Chandra')
for g in G7:
    r = rules_of(g)
    k = [h for h in r if h in KEN]
    if len(k) == 2 and g in NAT_BEN:
        print(f"      {g:8s} rules {r} — kendras {k} — natural benefic  "
              f"=> DOSHA{'  (lagna lord: exemption disputed)' if 1 in k else ''}")
print(f"""
  TWO GRAHAS QUALIFY AND THEY ARE THE TWO THE READING LEANS ON HARDEST.

      BUDHA rules the 1st and the 10th.  Most schools exempt the lagna lord.
      GURU rules the 4th and the 7th.  No exemption is available.

  SECTION 27 APPLIED THE DOSHA TO GURU AND CALLS IT A FUNCTIONAL MALEFIC.
  THAT IS A LARGE CLAIM TO REST ON A CHAPTER NOBODY HAS READ, because:
""")
print(f"""      Guru is the only occupant of the 10th house
      Guru runs the antardasha now in force, to January 2028
      Guru holds the 7th lordship the marriage window is read from
      Guru's mahadasha, Dec 2040 to Dec 2056, is called the best in the chart

  IF THE DOSHA IS REJECTED OR MODIFIED, GURU IS A BENEFIC IN THE CAREER HOUSE
  RUNNING THE CURRENT PERIOD.  If it is upheld, Guru is a malefic doing the
  same three jobs.  THE READING TOOK ONE SIDE WITHOUT MARKING IT AS A CHOICE.

  PRICE OF THE DISPUTE: the functional nature of the most active graha in the
  chart.  THIS IS THE SINGLE MOST EXPENSIVE UNREAD RULE IN THE DOCUMENT.
""")

sub('Dispute 4 — a graha ruling both a trikona and a dusthana')
TRIK = (1, 5, 9)
for g in G7:
    r = rules_of(g)
    if any(h in TRIK for h in r) and any(h in DUST for h in r):
        print(f"      {g:8s} rules {r} — trikona {[h for h in r if h in TRIK]}"
              f" AND dusthana {[h for h in r if h in DUST]}")
print("""
  ONE GRAHA, AND IT IS SHANI: lord of the 5th (trikona) and the 6th (dusthana).

      SCHOOL A   the trikona lordship prevails; Shani is a benefic for Kanya
      SCHOOL B   the dusthana lordship spoils it; Shani stays mixed

  Shani sits in the 9th with Chandra, Mangal and Rahu, and section 17 gives it
  the antardasha Jan 2028 - Dec 2030, the window the reading calls THE
  FOUNDATION.  So the same ambiguity attaches to the graha running the
  foundation period.

  PRICE: the functional nature of the 5th and 6th lord during a period this
  reading has already dated and described in detail.
""")

sub('Dispute 5 — drishti applied inside a divisional chart')
d9 = {g: varga(POS[g], 9) for g in list(GRAHAS) + ['Lagna']}
d9h = lambda g: (d9[g] - d9['Lagna']) % 12 + 1
print(f"""      D9 lagna {SIGNS[d9['Lagna']]}; D9 10th house = {SIGNS[(d9['Lagna']+9) % 12]}

  Section 26 read aspects INSIDE the navamsa and found the D9 10th receives
  Guru's 5th and Mangal's 4th.  Section 33 then DECLINED to run transits inside
  a varga, on the ground that a varga maps dignity rather than a sky.

  THOSE TWO POSITIONS ARE IN TENSION and the document has never reconciled
  them.  If a varga is not a sky, an aspect cast across it is as questionable
  as a transit through it.

  PRICE: section 26's finding that the D9 career house is aspected -- which was
  itself a CORRECTION of an earlier claim that it was unaspected.  If drishti
  does not apply inside a varga, neither statement is meaningful.
""")

sub('Dispute 6 — Kuja dosha reckoned from Shukra')
KUJA = (1, 2, 4, 7, 8, 12)
for ref in ('Lagna', 'Chandra', 'Shukra'):
    h = (sign_of(POS['Mangal']) - sign_of(POS[ref])) % 12 + 1
    print(f"      from {ref:8s} Mangal is in the {ordn(h):5s} "
          f"{'DOSHA' if h in KUJA else 'clean'}")
print("""
  ALREADY COMPUTED FROM ALL THREE REFERENCES IN SECTION 25, which is the right
  treatment: it reports the dosha as absent from the lagna and present from
  Chandra and Shukra rather than picking a reference and hiding the others.

  PRICE: none.  THE READING HANDLED THIS ONE CORRECTLY BY REFUSING TO CHOOSE.
""")

sub('Dispute 7 — argala and its counter-houses')
ARG = {2: 'the 2nd', 4: 'the 4th', 11: 'the 11th'}
CTR = {2: 12, 4: 10, 11: 3}
occ = lambda si: [g for g in GRAHAS if sign_of(POS[g]) == si]
tenth = (LAG + 9) % 12
print(f"      argala on the 10th house ({SIGNS[tenth]}):")
for k, lbl in ARG.items():
    a = (tenth + k - 1) % 12
    c = (tenth + CTR[k] - 1) % 12
    oa = ', '.join(occ(a)) or 'empty'
    oc = ', '.join(occ(c)) or 'empty'
    print(f"        {lbl:8s} = {SIGNS[a]:11s} {oa:30s} counter {SIGNS[c]:11s} {oc}")
print("""
  Section 30 computed this and found ONE argala, unopposed: the three grahas in
  the 8th intervene on the career house and nothing blocks them.

  I DRAFTED THE VERDICT AS "SMALL, BECAUSE THE ONE ARGALA HERE IS ON THE 2ND-
  FROM AND THE CONTESTED VARIANTS DO NOT TOUCH IT."  THE TABLE ABOVE SAYS
  OTHERWISE.  The 2nd-from and the 4th-from are both EMPTY.  The single argala
  in this chart is the 11TH-FROM -- and the contested rule is precisely whether
  the 3rd counters the 11th.  I had it exactly backwards: this is the one
  argala the dispute governs, not one it misses.

  SO THE DISPUTE IS LIVE AND THEN IT DIES ON THE FACTS.  The 3rd from the 10th
  is SIMHA, and Simha is empty.  Whether or not the 3rd is allowed to counter
  the 11th, THERE IS NOTHING IN IT TO DO THE COUNTERING.

  PRICE: none -- but by accident rather than by design.  Had one graha been in
  Simha, this dispute would have decided whether the chart's only intervention
  on the career house stands or is blocked.
""")

# =============================================================================
rule('5.  THE PRICE LIST')
print("""
  Eight rules, each priced by what it would change:

      SETTLED BY DATA, chapter cannot reopen it
          D8 and D11 construction — 20 of 20 placements reproduced

      HANDLED CORRECTLY ALREADY, by refusing to choose
          Kuja dosha from three references (section 25)

      LIVE BUT MOOT ON THE FACTS
          argala counter-houses — the contested rule governs the chart's only
              argala after all, but the counter-house is empty either way

      MEDIUM
          viparita cancelled by strength — one raja yoga, on the 12th lord
          trikona-and-dusthana lordship — Shani's nature in the 2028-2030 window
          drishti inside a varga — section 26's D9 aspect finding, and its
              tension with section 33's refusal to run transits in a varga

      LARGE
          the Shodashavarga starting signs — 25% of Vimshopaka Bala, and the
              rank order of the strength measure is not stable under it

      LARGEST
          KENDRADHIPATI DOSHA — decides whether GURU, the sole occupant of the
              10th, the current antardasha lord, the 7th lord read for
              marriage, and the lord of the best mahadasha in the chart, is a
              functional benefic or a functional malefic

  THE HONEST SUMMARY, AND I HAD TO CORRECT IT TWICE WHILE WRITING IT.

      I FIRST WROTE "NOTHING IN CHAPTERS 1-41 CAN CHANGE A COMPUTED POSITION."
      THAT IS FALSE, and part 3 above is the refutation: the starting-sign rule
      IS the construction, so six of the sixteen Shodashavarga charts have
      positions that move with it.

      WHAT IS ACTUALLY IMMUNE, and it is most of the document:

          every longitude              fixed by the ephemeris
          every dasha date             fixed by the Moon's longitude
          every Ashtakavarga figure    built from D1 signs only
          D1 D3 D4 D7 D9 D10 D12       construction not in dispute
          D27 D30 D60                  construction not in dispute
          houses, aspects, lordships   fixed by the D1

      WHAT IS NOT IMMUNE:

          D2 D16 D20 D24 D40 D45       positions themselves can move
          Vimshopaka Bala              25% of its weight, and its rank order
          five named interpretive rules

      I ALSO FIRST WROTE "SIX RULES UNRESOLVED."  IT IS FIVE: of the eight,
      D8/D11 is settled by data, Kuja dosha was handled correctly by refusing
      to choose, and the argala dispute dies on an empty house.

      SO THE ANSWER TO "WHAT ABOUT 1 TO 41" IS NOT "THEY ARE MISSING."  IT IS
      THIS: they are missing, they are the more important half, FIVE specific
      rules in them are unresolved, six divisional charts and one strength
      measure move with one of those five, and exactly one -- THE
      KENDRADHIPATI RULE -- would require rewriting sections of this document
      rather than annotating them.
""")
print('=' * 92)
