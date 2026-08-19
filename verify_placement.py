#!/usr/bin/env python3
"""
The same question, from PLACEMENT ONLY.

Section 22 answered career and earning using Shodhya Pinda, Ashtakavarga
bindus, Bhava Bala ranks, a career score and an income score I built myself.
That is a fair thing to object to.  Half of those are constructed rather than
classical, and a reading that only works with its own scoring is not a reading.

So this script throws ALL of it away.  Nothing below uses:

    no Shadbala          no Ashtakavarga / SAV bindus
    no Shodhya Pinda     no Bhava Bala or house ranks
    no Ishta / Kashta    no career score, no income score
    no Vimshopaka        no rarity model

What is left is what Parashara actually works from:

    WHICH GRAHA IS IN WHICH HOUSE
    WHAT IT RULES
    WHAT CONDITION IT IS IN     (sign dignity, combustion, retrogression)
    WHAT IT ASPECTS
    WHO IT SITS WITH

and the divisional charts, which are also just placement at another
magnification.  Everything here is countable off the chart by hand.

The test at the end is the one that matters: DOES THE ANSWER SURVIVE?
"""
from ephem_core import (SIGNS, GRAHAS, SUPPLIED, LORD, EXALT, dignity,
                        varga, sign_of, nak_of, short, rule, sub)

POS = dict(SUPPLIED)
LAG = sign_of(POS['Lagna'])
hs = lambda g: (sign_of(POS[g]) - LAG) % 12 + 1
house_sign = lambda n: (LAG + n - 1) % 12
occupants = lambda n: [g for g in GRAHAS if hs(g) == n]
rules_of = lambda g: [i for i in range(1, 13) if LORD[(LAG + i - 1) % 12] == g]

HOUSE = ['self, body', 'wealth, family, speech', 'effort, siblings, skill',
         'home, mother, schooling', 'children, mind', 'service, rivals, health',
         'partnership', 'transformation, others\' resources',
         'dharma, father, fortune', 'career, standing', 'gains, income',
         'loss, foreign, moksha']
# Parashari graha drishti: house-counts each graha aspects from its own house.
ASPECT = {'Mangal': (4, 7, 8), 'Guru': (5, 7, 9), 'Shani': (3, 7, 10),
          'Rahu': (5, 7, 9), 'Ketu': (5, 7, 9)}
DEFAULT_ASPECT = (7,)

# =============================================================================
rule('1.  THE CHART AS PLACEMENT — NOTHING ELSE')
print(f"\n  Lagna {short(POS['Lagna'])} {SIGNS[LAG]}, lord {LORD[LAG]}\n")
print(f"  {'graha':9s}{'position':22s}{'ho':>3s}  {'dignity':12s}"
      f"{'nakshatra':16s}rules")
for g in GRAHAS:
    s = sign_of(POS[g])
    nk, pada = nak_of(POS[g])[0], nak_of(POS[g])[1]
    dg = dignity(g, s) if g not in ('Rahu', 'Ketu') else 'shadow'
    r = ', '.join(str(x) for x in rules_of(g)) or '—'
    print(f"  {g:9s}{short(POS[g]):22s}{hs(g):3d}  "
          f"{dg:12s}{nk + ' ' + str(pada):16s}{r}")

sub('Combustion — a placement fact, not a score')
sun = POS['Surya']
LIMIT = {'Chandra': 12, 'Mangal': 17, 'Budha': 14, 'Guru': 11,
         'Shukra': 10, 'Shani': 15}
for g, lim in LIMIT.items():
    d = abs(POS[g] - sun)
    d = min(d, 360 - d)
    if d < lim:
        print(f"      {g} is {d:.2f}° from Surya (limit {lim}°) — COMBUST")
print("      no other graha is within its limit")

# =============================================================================
rule('2.  WHERE EVERY HOUSE LORD SITS')
print("""
  This is the single most informative table you can build without a number in
  it, and for this chart it produces something startling.
""")
print(f"  {'house':6s}{'sign':11s}{'lord':9s}{'sits in':9s}  what that reads as")
targets = {}
for n in range(1, 13):
    ld = LORD[house_sign(n)]
    at = hs(ld)
    targets.setdefault(at, []).append(n)
    print(f"  {n:2d}    {SIGNS[house_sign(n)]:11s}{ld:9s}{at:2d}       "
          f"{HOUSE[n-1]} → {HOUSE[at-1]}")
print(f"""
  EVERY ONE OF THE TWELVE LORDS SITS IN THE 8TH, THE 9TH OR THE 10TH.

      into the 8th : houses {', '.join(str(x) for x in sorted(targets.get(8, [])))}
      into the 9th : houses {', '.join(str(x) for x in sorted(targets.get(9, [])))}
      into the 10th: houses {', '.join(str(x) for x in sorted(targets.get(10, [])))}

  Three houses out of twelve receive the entire chart.  You do not need a
  strength measure to see what that means: WHATEVER HAPPENS IN THIS LIFE IS
  ROUTED THROUGH TRANSFORMATION, FORTUNE, AND WORK.  There is no other address.
""")

# =============================================================================
rule('3.  CAREER, READ ONLY FROM PLACEMENT')
tenth = LORD[house_sign(10)]
print(f"""
  THE 10TH LORD IS {tenth.upper()}, AND IT SITS IN THE 8TH.

  Classically that is unambiguous and it does not need a score: the house of
  career is owned by a graha standing in the house of crisis, research, hidden
  things and other people's resources.  It says the WORK ITSELF is
  investigative, and that the CAREER IS NOT STABLE IN FORM -- it changes shape,
  it involves what is not visible, and it is entangled with other people's
  money or other people's problems.

  AND THAT SAME GRAHA IS COMBUST.

  A combust 10th lord means the career significator is swallowed by the Sun --
  the classical reading is that his OWN position is obscured by the authority
  he stands next to.  Work done under someone else's name.  Credit that lands
  elsewhere.  That is placement, not opinion.

  BUT THE 10TH ITSELF IS NOT EMPTY.
""")
for g in occupants(10):
    s = sign_of(POS[g])
    print(f"      {g} occupies the 10th, in {SIGNS[s]} — {dignity(g, s)}, "
          f"ruling {', '.join(str(x) for x in rules_of(g))}")
print("""
  Guru in the 10th from the lagna is AMALA YOGA by placement alone: a natural
  benefic in the house of career gives lasting reputation and clean standing.
  This is one of the few classical yogas that needs no strength test.

  AND THE QUALIFICATION IS ALSO PURE PLACEMENT: Guru is in Mithuna, the sign of
  its enemy Budha.  So the reputation is real and the instrument is
  uncomfortable.  He is respected doing work that does not sit naturally.
""")

# =============================================================================
rule('4.  EARNING, READ ONLY FROM PLACEMENT')
second, eleventh = LORD[house_sign(2)], LORD[house_sign(11)]
print(f"""
  TWO HOUSES CARRY MONEY.  The 2nd is what is held; the 11th is what comes in.

      2nd  {SIGNS[house_sign(2)]:10s} lord {second:8s} sits in the {hs(second)}th
      11th {SIGNS[house_sign(11)]:10s} lord {eleventh:8s} sits in the {hs(eleventh)}th

  THE 2ND LORD IN THE 8TH.  Wealth held is ruled by a graha in the house of
  other people's resources.  Classically: money through inheritance, through
  partners, through what is transferred rather than earned in increments;
  and money that arrives in events rather than in a steady line.

  THE 11TH LORD IN THE 9TH, EXALTED.  Income is ruled by a graha standing
  exalted in the house of fortune, elders and dharma.  This is a GOOD placement
  and it says something specific: GAINS COME THROUGH SENIORS, MENTORS,
  TEACHERS AND WELL-DISPOSED ELDERS -- through people who favour him, not
  through mechanism.
""")

sub('And now the thing that only appears if you count aspects')


def ordn(n):
    return f"{n}{'th' if 10 <= n % 100 <= 20 else {1:'st',2:'nd',3:'rd'}.get(n%10,'th')}"


inc = {}
for g in GRAHAS:
    for a in ASPECT.get(g, DEFAULT_ASPECT):
        tgt = (hs(g) + a - 2) % 12 + 1
        inc.setdefault(tgt, []).append(f"{g}'s {ordn(a)}")
print(f"  {'house':5s}{'':18s}{'occupants':28s}aspects received")
for n in range(1, 13):
    who = inc.get(n, [])
    flag = '   <-- NOTHING REACHES IT' if not who else ''
    print(f"  {ordn(n):5s}{HOUSE[n-1][:17]:18s}"
          f"{', '.join(occupants(n)) or '—':28s}"
          f"{', '.join(who) or 'none'}{flag}")
empty = [n for n in range(1, 13) if not inc.get(n)]
print(f"""
  A CORRECTION TO SECTION 10.  That section reports that nothing aspects the
  8th and treats it as the one sealed house in the chart.  Counted properly,
  {len(empty)} HOUSES RECEIVE NO ASPECT AT ALL: the {' and the '.join(ordn(n) for n in empty)}.

  THE CAREER HOUSE IS THE OTHER SEALED CHAMBER, and section 10 missed it.

  That is a substantial statement about the question actually asked.  The 10th
  holds Guru and receives NOTHING from outside -- no help, no interference, no
  correction.  His career runs on ITS SINGLE OCCUPANT and on nothing else.
  Whatever Guru is worth in the 10th is the whole of what the career house has.

  THE 2ND HOUSE IS EMPTY AND RECEIVES {len(inc.get(2, []))} ASPECTS -- the most of any house
  in the chart.  Among them is GURU, the most benefic aspect in Jyotisha, and
  SHUKRA, its own lord aspecting its own house from the 8th.

  A house that is empty but aspected by its own lord and by Jupiter is
  classically WELL PROTECTED.  No strength table shows this.

  SO THE PLACEMENT READING OF MONEY IS:

      what he KEEPS is protected — the 2nd is empty, unafflicted by occupancy,
      and aspected by both its own lord and the great benefic

      what he EARNS comes through people — the 11th lord is exalted in the
      house of elders and fortune

      and how it ARRIVES is lumpy — because the lord of what-he-keeps stands
      in the 8th, the house of transfers, and not in an earning house
""")

# =============================================================================
rule('5.  THE EXCHANGE, AND THE YOGAS THAT ARE PURE PLACEMENT')
sub('Parivartana — mutual exchange')
for a in range(1, 13):
    for b in range(a + 1, 13):
        la, lb = LORD[house_sign(a)], LORD[house_sign(b)]
        if la != lb and hs(la) == b and hs(lb) == a:
            print(f"      the {a}th lord {la} is in the {b}th, and the "
                  f"{b}th lord {lb} is in the {a}th — EXCHANGE")
print("""
      The 8th and the 9th trade rulers outright.  Transformation and fortune
      are not two departments in this chart; they are one mechanism wearing two
      names, and neither can be reached except through the other.
""")

sub('Viparita — a dusthana lord standing in a dusthana')
NAMES = {6: 'Harsha', 8: 'Sarala', 12: 'Vimala'}
for n in (6, 8, 12):
    ld = LORD[house_sign(n)]
    if hs(ld) in (6, 8, 12):
        print(f"      {NAMES[n]} yoga: the {n}th lord {ld} stands in the "
              f"{hs(ld)}th — present by placement")

sub('Raja yoga — a kendra lord conjunct a trikona lord')
KEN, TRI = (1, 4, 7, 10), (1, 5, 9)
for n in range(1, 13):
    occ = occupants(n)
    for i in range(len(occ)):
        for j in range(i + 1, len(occ)):
            g1, g2 = occ[i], occ[j]
            k1 = set(rules_of(g1)) & set(KEN)
            t2 = set(rules_of(g2)) & set(TRI)
            k2 = set(rules_of(g2)) & set(KEN)
            t1 = set(rules_of(g1)) & set(TRI)
            if (k1 and t2) or (k2 and t1):
                print(f"      {g1} + {g2} in the {n}th — kendra lord with "
                      f"trikona lord")

sub('Dhana — the 11th lord conjunct a trikona lord')
for n in range(1, 13):
    occ = occupants(n)
    if eleventh in occ:
        for g in occ:
            if g != eleventh and set(rules_of(g)) & set(TRI):
                print(f"      {eleventh} (11th) with {g} "
                      f"({', '.join(str(x) for x in rules_of(g))}) in the {n}th")

print("""
  ONE QUALIFICATION, AND IT IS ALSO PURE PLACEMENT: Shani rules the 5th AND the
  6th here -- a trikona and a dusthana on one body.  Schools differ on whether
  the trikona lordship prevails or the dusthana taints it.  This reading does
  not adjudicate; it records that the chart's income combination is built on a
  graha with divided loyalties.

  NOTE WHERE THEY SIT.  The raja yoga is in the 8TH.  The income combination is
  in the 9TH.  Neither is in a career house, and that is a placement fact with
  a direct consequence: HIS ELEVATION AND HIS GAINS BOTH ARRIVE THROUGH THE
  8TH-9TH AXIS -- through upheaval and through fortune -- RATHER THAN THROUGH
  THE 10TH.  He is not promoted into things. He is delivered into them.
""")

# =============================================================================
rule('6.  THE CAREER VARGA, STILL ONLY PLACEMENT')
d10 = {g: varga(POS[g], 10) for g in GRAHAS + ['Lagna']}
dl = d10['Lagna']
print(f"\n  D10 lagna: {SIGNS[dl]}, lord {LORD[dl]}\n")
for g in GRAHAS:
    h = (d10[g] - dl) % 12 + 1
    tag = ''
    if h in (1, 4, 7, 10):
        tag = 'kendra'
    elif h in (5, 9):
        tag = 'trikona'
    elif h in (6, 8, 12):
        tag = 'dusthana'
    print(f"      {g:9s} D10 house {h:2d}  {SIGNS[d10[g]]:11s} {tag}")
print(f"""
  Three grahas hold good D10 houses by placement alone: SHUKRA IN THE D10 10TH
  ITSELF, and GURU and SHANI in D10 trikonas.  And BUDHA -- the birth chart's
  10th lord -- falls in a D10 DUSTHANA, which is the same verdict the rashi
  chart gave, arrived at independently in the career varga.

  Read only for placement: the D10 ascendant is {SIGNS[dl]} and its lord is
  {LORD[dl]}.  Whatever else is true, THE SHAPE OF HIS WORKING LIFE IS OWNED BY
  {LORD[dl].upper()} — the graha of structure, patience, service and long
  institutional time.  Not by the 10th lord of the birth chart.
""")

# =============================================================================
rule('7.  SO DOES THE ANSWER SURVIVE WITHOUT THE NUMBERS?')
print("""
  Section 22's four claims, tested against placement alone:

  1. "THE EMPLOYMENT RELATION IS THE STRONG PART, NOT THE TITLE."
     SURVIVES, and by a different route.  Placement says the 10th lord is
     combust in the 8th while the D10 ascendant is owned by Shani, the graha of
     service inside structures.  No bindu count required.

  2. "INCOME IS THE WEAK CHANNEL."
     DOES NOT SURVIVE IN THAT FORM — and this is the correction.
     By placement the 11th lord is EXALTED.  That is not weakness.  What the
     placement says instead is that income is CONDITIONAL RATHER THAN WEAK: it
     comes through the 9th, which means through elders, mentors and fortune,
     and it does not come through mechanism or accumulation.
     The score-based reading called that "weak flow".  Placement calls it
     "flow that depends on people".  THOSE ARE DIFFERENT CLAIMS AND PLACEMENT
     IS THE MORE CLASSICAL ONE.

  3. "MONEY ARRIVES AS EVENTS, NOT AS INCREMENTS."
     SURVIVES CLEANLY.  The 2nd lord in the 8th says it on its own, and the
     8th-9th exchange reinforces it.  This was never a scoring claim.

  4. "RAISES COME FROM MOVING, NOT WAITING."
     PARTLY SURVIVES, WITH A CHANGED REASON.  It rested on the 6th's bindu
     count, which is now discarded.  What placement supports is different: the
     raja yoga sits in the 8th and the income combination in the 9th, so
     ADVANCEMENT DOES NOT COME THROUGH THE 10TH HOUSE AT ALL.  Change is the
     mechanism, but the reason is that his elevation is not located in his
     career house — not that he wins competitions.

  AND ONE THING PLACEMENT SAYS THAT THE SCORES NEVER DID:

      THE 2ND HOUSE IS EMPTY, ASPECTED BY ITS OWN LORD AND BY GURU.
      THE 11TH LORD IS EXALTED.

  Read without a single strength figure, THIS IS A BETTER WEALTH CHART THAN
  SECTION 22 DESCRIBED.  The bindus were dragging the reading pessimistic.
""")
print('=' * 92)
