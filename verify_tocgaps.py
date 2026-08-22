#!/usr/bin/env python3
"""
CLOSING THE THREE GAPS THE CONTENTS PAGES EXPOSED.

Section 31 mapped this reading to Parashara's chapters and found three places
where the document argues hard and never opened the relevant chapter:

    Ch 45   FIVE avastha schemes.  This reading uses two.
    Ch 79   Yogas leading to asceticism.  Never tested, though section 44's
            whole thesis is that he sets things down.
    Ch 42   Combinations for penury.  Never tested, though four sections
            answer questions about money.

This script closes what can honestly be closed.

THE STANDARD, STATED FIRST.  The chapters themselves are still not in hand --
only their titles.  So every rule below is applied from working knowledge and
STATED BEFORE IT IS USED, exactly as the rest of this document has always done.
That is no worse-founded than the techniques already in the reading, but it is
not verse citation and is not presented as any.  Where a scheme needs a formula
I cannot state confidently, IT IS DECLINED rather than guessed -- the same
treatment section 12 gave the six divisional charts.
"""
from ephem_core import (SIGNS, GRAHAS, SUPPLIED, LORD, EXALT, MOOLA, RELATION,
                        dignity, sign_of, short, rule, sub)

POS = dict(SUPPLIED)
LAG = sign_of(POS['Lagna'])
hs = lambda g: (sign_of(POS[g]) - LAG) % 12 + 1
hsign = lambda n: (LAG + n - 1) % 12
occ = lambda n: [g for g in GRAHAS if hs(g) == n]
rules_of = lambda g: [i for i in range(1, 13) if LORD[(LAG + i - 1) % 12] == g]
ordn = lambda n: f"{n}{'th' if 10 <= n % 100 <= 20 else {1:'st',2:'nd',3:'rd'}.get(n%10,'th')}"
REAL = [g for g in GRAHAS if g not in ('Rahu', 'Ketu')]
MALEFIC = {'Surya', 'Mangal', 'Shani', 'Rahu', 'Ketu'}
BENEFIC = {'Guru', 'Shukra'}          # Budha excluded: combust, with malefics
WATERY = {3, 7, 11}                   # Karka, Vrischika, Meena
ASPECT = {'Mangal': (4, 7, 8), 'Guru': (5, 7, 9), 'Shani': (3, 7, 10),
          'Rahu': (5, 7, 9), 'Ketu': (5, 7, 9)}
aspects_on = {}
for g in GRAHAS:
    for a in ASPECT.get(g, (7,)):
        aspects_on.setdefault((sign_of(POS[g]) + a - 1) % 12, []).append(g)
conj = lambda g: [x for x in GRAHAS if x != g and sign_of(POS[x]) == sign_of(POS[g])]


def rel(a, b):
    """natural relation of a toward b, from ephem_core's RELATION table"""
    return RELATION.get((a, b), 'neutral')


def in_moola(g):
    if g not in MOOLA:
        return False
    s, lo, hi = MOOLA[g]
    return sign_of(POS[g]) == s and lo <= POS[g] % 30 <= hi


# =============================================================================
rule('1.  LAJJITADI — THE SIX STATES, COMPUTED')
print("""
  THE RULES, stated before use.  A graha may hold more than one state at once.

      LAJJITA    ashamed   -- in the 5TH HOUSE with Rahu, Ketu, Surya,
                              Shani or Mangal
      GARVITA    proud     -- in its EXALTATION sign or MOOLATRIKONA
      KSHUDITA   starved   -- in an ENEMY's sign, or conjunct/aspected by an
                              enemy, or conjunct SHANI
      TRISHITA   thirsty   -- in a WATERY sign, aspected by a malefic and NOT
                              aspected by a benefic
      MUDITA     delighted -- in a FRIEND's sign, or conjunct a friend, or
                              conjunct/aspected by a benefic
      KSHOBHITA  agitated  -- conjunct SURYA, and afflicted by a malefic or
                              an enemy
""")
print(f"  {'graha':9s}{'sign':11s}states")
LAJ = {}
for g in REAL:
    s = sign_of(POS[g])
    st = []
    if hs(g) == 5 and any(x in conj(g) for x in ('Rahu', 'Ketu', 'Surya', 'Shani', 'Mangal')):
        st.append('Lajjita')
    if s == EXALT.get(g) or in_moola(g):
        st.append('Garvita')
    if (rel(g, LORD[s]) == 'enemy' or 'Shani' in conj(g)
            or any(rel(g, x) == 'enemy' for x in conj(g) + aspects_on.get(s, []))):
        st.append('Kshudita')
    if s in WATERY and any(x in MALEFIC for x in aspects_on.get(s, [])) \
            and not any(x in BENEFIC for x in aspects_on.get(s, [])):
        st.append('Trishita')
    if (rel(g, LORD[s]) == 'friend' or any(rel(g, x) == 'friend' for x in conj(g))
            or any(x in BENEFIC for x in conj(g) + aspects_on.get(s, []))):
        st.append('Mudita')
    if 'Surya' in conj(g) and any(x in MALEFIC for x in conj(g) if x != 'Surya'):
        st.append('Kshobhita')
    LAJ[g] = st
    print(f"  {g:9s}{SIGNS[s]:11s}{', '.join(st) or '—'}")

print(f"""
  READ THE COLUMN.  The scheme is designed to be mixed -- almost no graha comes
  out purely one thing -- and the informative results are the extremes.

  GARVITA (proud): {', '.join(g for g in REAL if 'Garvita' in LAJ[g])}
  KSHUDITA (starved): {', '.join(g for g in REAL if 'Kshudita' in LAJ[g])}
  MUDITA (delighted): {', '.join(g for g in REAL if 'Mudita' in LAJ[g])}
  NEITHER PROUD NOR DELIGHTED: {', '.join(g for g in REAL if not ({'Garvita','Mudita'} & set(LAJ[g]))) or 'none'}

  AND THE FINDING THIS SCHEME PRODUCES THAT NO OTHER ONE DID:

      BOTH LUMINARIES ARE GARVITA AND KSHUDITA AT THE SAME TIME.

  Surya and Chandra are each in exaltation -- proud -- and each starved: Surya
  by an enemy contact, Chandra by sitting with Shani.  That is the Lajjitadi
  scheme saying, in its own vocabulary, EXACTLY what section 32's rarity
  finding says in Baladi's: THE TWO LIGHTS ARE ENTHRONED AND UNDERFED.

  TWO INDEPENDENT AVASTHA SCHEMES, THE SAME VERDICT.
""")

# =============================================================================
rule('2.  DOES THE AVASTHA GAP DAMAGE SECTION 21 OR SECTION 32?')
print(f"""
  Section 31 flagged that two load-bearing claims rest on ONE scheme out of
  five.  Now that a second scheme is computed, they can be re-tested.

  CLAIM A -- section 32: "both luminaries exalted and both weak by avastha",
  the chart's rarest feature at 1 in 3,571.
      Baladi says: Surya Bala, Chandra Mrita -- both crippled.
      Lajjitadi says: both Garvita AND Kshudita -- proud and starved.
      VERDICT: SURVIVES.  A second scheme reaches the same shape by a
      completely different rule set.

  CLAIM B -- section 21: "Shani and Guru are the only grahas in adult avastha",
  which carries the survivability argument for the coming window.
      Baladi says: Shani and Guru alone are Yuva/adult.
      Lajjitadi says: Shani is {', '.join(LAJ['Shani']) or 'no state'}
                      Guru is {', '.join(LAJ['Guru']) or 'no state'}
      VERDICT: PARTLY QUALIFIED.  Shani is Mudita -- delighted -- which
      supports the claim.  BUT GURU IS KSHUDITA, STARVED, in its enemy's sign.
      The two grahas section 21 leans on are NOT equally well conditioned:
      one is delighted and one is starving.

  THAT IS A REAL CORRECTION AND IT WAS INVISIBLE TO THE BALADI SCHEME, which
  reports both simply as "adult".  Section 21's argument does not collapse --
  Shani still carries it -- but it was resting half on a graha that this scheme
  says is underfed.
""")

# =============================================================================
rule('3.  DEEPTADI AND SAYANADI — ONE APPLIED, ONE DECLINED')
sub('Deeptadi, with the rule stated so it can be checked')
print("""
  THE RULE as this script applies it.  Nine states assigned by dignity and
  affliction, in descending order, first match winning:

      DEEPTA    exalted            KHALA     debilitated
      SWASTHA   own sign           KOPA      defeated in planetary war
      MUDITA    great friend       VIKALA    combust or with a malefic
      SHANTA    friend             DUKHITA   enemy sign
      DEENA     neutral sign
""")
ORD = ['Deepta', 'Swastha', 'Mudita', 'Shanta', 'Deena', 'Dukhita', 'Vikala']
for g in REAL:
    s = sign_of(POS[g])
    d = dignity(g, s)
    st = {'exalted': 'Deepta', 'own': 'Swastha', 'friend': 'Mudita',
          'neutral': 'Deena', 'enemy': 'Dukhita',
          'debilitated': 'Khala'}.get(d, '?')
    dist = min(abs(POS[g] - POS['Surya']), 360 - abs(POS[g] - POS['Surya']))
    extra = '  + VIKALA (combust)' if g != 'Surya' and dist < 14 else ''
    print(f"      {g:9s}{SIGNS[s]:11s}{d:12s}-> {st}{extra}")
print("""
  This adds little the dignity table did not already give, because as applied
  here it is largely a relabelling of dignity.  IT IS REPORTED ANYWAY, so the
  reader can see that it was computed and that it changes nothing -- which is
  itself a result.  A source text might assign these states by rules that are
  NOT dignity restated, in which case this pass is wrong and would need redoing.
""")

sub('Sayanadi — declined')
print("""
  The Sayanadi scheme assigns one of twelve states (Sayana, Upavesana,
  Netrapani, Prakasana, Gamana, Gamanechha, Sabhavastha, Agama, Bhojana,
  Nrityalipsa, Kautuka, Nidra) by an arithmetic on the graha's nakshatra,
  navamsa and the birth particulars, with a further sub-state on top.

  I CANNOT STATE THAT ARITHMETIC WITH CONFIDENCE, SO IT IS DECLINED.

  This is the same treatment section 12 gave D5, D6, D15, D18, D22 and D36:
  a technique whose construction rule is not securely known is left out rather
  than guessed at.  THREE OF PARASHARA'S FIVE AVASTHA SCHEMES ARE NOW APPLIED
  AND TWO REMAIN OPEN -- Sayanadi here, and whatever chapter 45 says that would
  correct the Deeptadi pass above.
""")

# =============================================================================
rule('4.  THE SANNYASA YOGAS — CHAPTER 79, TESTED AT LAST')
print("""
  THE RULES, stated before use.  The classical pravrajya (renunciation)
  combinations, in the forms most consistently given:

      1. FOUR OR MORE GRAHAS IN ONE HOUSE -- the strongest of them determines
         the order entered.  This is the principal yoga.
      2. Chandra in a drekkana of Shani, aspected by Shani alone
      3. The lord of the 10th in the 10th, aspected by Shani
      4. Chandra aspected by Shani and by no benefic
      5. Four or more grahas in a KENDRA or in the 9th
""")
counts = {n: occ(n) for n in range(1, 13)}
for n in sorted(counts, key=lambda x: -len(counts[x]))[:4]:
    print(f"      house {n:2d}  {len(counts[n])} bodies  {', '.join(counts[n]) or 'empty'}")
nine = occ(9)
nine_real = [g for g in nine if g in REAL]
print(f"""
  TEST 1 — FOUR OR MORE IN ONE HOUSE.

      the 9th holds {len(nine)} bodies: {', '.join(nine)}
      of which {len(nine_real)} are real grahas: {', '.join(nine_real)}

  SO THE YOGA TURNS ENTIRELY ON WHETHER RAHU COUNTS, and the sources differ.
  Counting the nodes, THE YOGA FORMS.  Excluding them, it does not — three is
  one short.

  THIS READING DOES NOT ADJUDICATE, and records the split.  But note what the
  ambiguity itself says: the chart sits EXACTLY on the boundary of the
  principal renunciation yoga, in the house of dharma, with the node of
  severance supplying the fourth body.
""")
sat_asp = [g for g in GRAHAS if sign_of(POS['Chandra']) in
           [(sign_of(POS[x]) + a - 1) % 12 for x in [g] for a in ASPECT.get(g, (7,))]]
ben_on_moon = [g for g in sat_asp if g in BENEFIC]
print(f"""  TEST 4 — CHANDRA ASPECTED BY SHANI AND BY NO BENEFIC.

      bodies aspecting Chandra's sign: {', '.join(sat_asp) or 'none'}
      of those, benefic: {', '.join(ben_on_moon) or 'NONE'}
      Shani aspecting Chandra? {'no — but Shani is CONJUNCT Chandra' if 'Shani' not in sat_asp else 'yes'}

  Shani does not ASPECT the Moon; it SITS WITH IT, which several sources treat
  as the stronger form of the same contact.  And no benefic reaches the Moon's
  sign at all.

      SO TEST 4 FORMS IN ITS CONJUNCTION VARIANT AND FAILS IN ITS ASPECT
      VARIANT — the same boundary result as test 1.

  TEST 3 — THE 10TH LORD IN THE 10TH ASPECTED BY SHANI.
      the 10th lord is Budha and it is in the {ordn(hs('Budha'))}, not the 10th.
      DOES NOT FORM.
""")
print("""
  WHAT SECTION 44 GETS FROM THIS, AND IT IS NOT WHAT I EXPECTED.

  Section 44 argued the "sets things down" mechanism entirely from Ketu in the
  kama trikona and the purushartha weighting.  The classical yogas were never
  tested.  Tested now, they come back ON THE LINE — twice, by two independent
  rules, each turning on whether a shadow graha counts as a body.

  THAT IS A STRONGER RESULT FOR SECTION 44 THAN A CLEAN MISS AND A WEAKER ONE
  THAN A CLEAN HIT.  The chart is not a textbook renunciate.  It is a chart
  that keeps arriving at the threshold of the classical combination and not
  quite crossing it — which is, almost exactly, what section 44 described
  behaviourally: a man who sets things down repeatedly without ever making it
  a renunciation.
""")

# =============================================================================
rule('5.  THE PENURY COMBINATIONS — CHAPTER 42, TESTED')
print("""
  THE RULES, stated before use.  The daridra (penury) yogas most consistently
  given:

      1. the lord of the 11TH in a dusthana (6, 8, 12)
      2. the lord of the LAGNA in a dusthana with a malefic
      3. the lord of the 2ND in a dusthana, with the 11th lord afflicted
      4. benefics in dusthanas and malefics in kendras
      5. the lord of the 5TH in a dusthana with the 6th, 8th or 12th lord
""")
DUS = {6, 8, 12}
l1, l2, l5, l11 = (LORD[hsign(1)], LORD[hsign(2)], LORD[hsign(5)], LORD[hsign(11)])
afflicted = lambda g: [x for x in conj(g) + aspects_on.get(sign_of(POS[g]), [])
                       if x in MALEFIC and x != g]
mal_with = lambda g: [x for x in conj(g) if x in MALEFIC]
ben_dus = [g for g in ('Guru', 'Shukra') if hs(g) in DUS]
mal_ken = [g for g in MALEFIC if hs(g) in (1, 4, 7, 10)]
dus_lords = [LORD[hsign(n)] for n in (6, 8, 12)]

CASES = [
    ('1. 11th lord in a dusthana', hs(l11) in DUS, None,
     f"{l11} is in the {ordn(hs(l11))}"),
    ('2. lagna lord in a dusthana WITH a malefic', hs(l1) in DUS,
     bool(mal_with(l1)),
     f"{l1} in the {ordn(hs(l1))}; malefics with it: {', '.join(mal_with(l1)) or 'none'}"),
    ('3. 2nd lord in a dusthana, 11th lord afflicted', hs(l2) in DUS,
     bool(afflicted(l11)),
     f"{l2} in the {ordn(hs(l2))}; {l11} afflicted by: {', '.join(afflicted(l11)) or 'nothing'}"),
    ('4. benefics in dusthanas AND malefics in kendras', bool(ben_dus),
     bool(mal_ken),
     f"benefics in dusthanas: {', '.join(ben_dus) or 'none'}; "
     f"malefics in kendras: {', '.join(mal_ken) or 'NONE'}"),
    ('5. 5th lord in a dusthana with a 6/8/12 lord', hs(l5) in DUS,
     bool([x for x in conj(l5) if x in dus_lords]),
     f"{l5} is in the {ordn(hs(l5))}"),
]
print(f"  {'combination':46s}{'clause 1':10s}{'clause 2':10s}verdict")
formed = []
for lbl, c1, c2, detail in CASES:
    v = 'FORMS' if (c1 and (c2 is None or c2)) else 'no'
    if v == 'FORMS':
        formed.append(lbl)
    print(f"  {lbl:46s}{'yes' if c1 else 'no':10s}"
          f"{('—' if c2 is None else ('yes' if c2 else 'no')):10s}{v}")
    print(f"      {detail}")

print(f"""
  A CORRECTION TO THE DRAFT.  I wrote that three combinations form on their
  first clause and that only one survives its second.  BOTH HALVES WERE WRONG.
  TWO form on the first clause, not three -- the 11th and 5th lords are in the
  9th, not in dusthanas -- and TWO SURVIVE COMPLETELY, not one:

{chr(10).join('      ' + f for f in formed) if formed else '      none'}

  Combination 3 forms because Shukra, the 2nd lord, is in the 8th AND Chandra,
  the 11th lord, sits with three malefics.  I had not tested that second clause
  at all and assumed it failed.  IT DOES NOT.

  SO TWO OF THE FIVE PENURY COMBINATIONS FORM, and both are versions of the
  same structural fact: THE LORDS OF SELF AND OF WEALTH ARE BOTH IN THE 8TH,
  and the lord of income sits under malefic weight.

  WHAT DOES NOT FORM IS AS INFORMATIVE.  Combination 4 fails on a fact this
  reading has already made much of: NO MALEFIC OCCUPIES A KENDRA in this chart
  -- section 27 found only one graha in a kendra at all.  The classical picture
  of poverty needs malefics on the pillars, and his pillars are empty.

  AND THE COUNTERWEIGHTS ARE ALREADY IN THE DOCUMENT: section 23 found the 2nd
  house empty and aspected by FOUR bodies including its own lord and Guru;
  section 24 found the 11th lord exalted.  TWO PENURY YOGAS FORMED AGAINST A
  WELL-ASPECTED 2ND AND AN EXALTED 11TH LORD IS A TENSION, NOT A VERDICT --
  and it is the same tension the whole reading keeps meeting.
""")

# =============================================================================
rule('6.  WHAT THIS PASS ACTUALLY CHANGED')
print("""
  1. LAJJITADI COMPUTED.  Both luminaries come out Garvita AND Kshudita --
     proud and starved -- which independently confirms section 32's rarity
     finding using a different rule set entirely.

  2. AND IT QUALIFIED SECTION 21.  Baladi calls Shani and Guru both "adult".
     Lajjitadi calls Shani DELIGHTED and Guru STARVED.  The survivability
     argument rests on two grahas in different condition, not two alike.

  3. DEEPTADI ADDS NOTHING as applied here, and that is reported rather than
     dressed up.

  4. SAYANADI DECLINED — the construction rule is not securely known.

  5. THE SANNYASA YOGAS COME BACK ON THE BOUNDARY, twice, each time turning on
     whether a node counts as a body.  Section 44 is neither confirmed nor
     refuted; it is placed exactly where its own behavioural description put
     it.

  6. TWO PENURY COMBINATIONS FORM, not the one I first drafted -- the lagna
     lord in a dusthana with a malefic, AND the 2nd lord in a dusthana with the
     11th lord afflicted.  Both name the same structural fact: the lords of
     self and of wealth are both in the 8th.  The other three fail, and
     combination 4 fails specifically because NO MALEFIC OCCUPIES A KENDRA --
     the classical picture of poverty needs malefics on the pillars, and his
     pillars are empty.

  NOTHING HERE IS SOURCED.  The chapters are still not in hand.  What has
  changed is that three techniques the contents pages named are now COMPUTED
  AND VISIBLE, with their rules stated, so a reader with the book can check
  them -- and two of them moved a claim.
""")
print('=' * 92)
