#!/usr/bin/env python3
"""
CAREER FROM D1 AND D9 ONLY -- every technique the two charts support.

THE CONSTRAINT, STATED PLAINLY BECAUSE IT SHAPES EVERYTHING.

He asked for both charts read deeply with every career concept applied, and
for nothing else to be brought in.  So this uses THE RASHI CHART AND THE
NAVAMSA AND NOTHING ELSE:

    NO D10, the dedicated career varga -- which is a real cost and is
      acknowledged rather than hidden
    NO Ashtakavarga, no Shadbala, no Shodhya Pinda, no constructed scores
      (his earlier instruction, kept)
    NO transits, no dasha timing -- those are not "career concepts", they
      are timing, and he asked about the charts

What is LEFT is larger than it sounds, and four of the techniques below have
never been applied in this document at all:

    the 10th from the LAGNA, from CHANDRA and from SURYA -- three references
    ARGALA on the 10th -- intervention and its obstruction
    the ARUDHA OF THE 10TH (A10) -- the career as others perceive it
    the D1 10th lord's own navamsa, read as the fate of the career
"""
from ephem_core import (SIGNS, GRAHAS, SUPPLIED, LORD, EXALT, dignity,
                        varga, sign_of, nak_of, short, rule, sub)

POS = dict(SUPPLIED)
LAG = sign_of(POS['Lagna'])
D9 = {g: varga(POS[g], 9) for g in GRAHAS + ['Lagna']}
L9 = D9['Lagna']
hs = lambda g: (sign_of(POS[g]) - LAG) % 12 + 1
h9 = lambda g: (D9[g] - L9) % 12 + 1
hsign = lambda n: (LAG + n - 1) % 12
s9 = lambda n: (L9 + n - 1) % 12
occ = lambda n: [g for g in GRAHAS if hs(g) == n]
occ9 = lambda n: [g for g in GRAHAS if h9(g) == n]
rules = lambda g: [i for i in range(1, 13) if LORD[(LAG + i - 1) % 12] == g]
ordn = lambda n: f"{n}{'th' if 10 <= n % 100 <= 20 else {1:'st',2:'nd',3:'rd'}.get(n%10,'th')}"
dg = lambda g, s: 'shadow' if g in ('Rahu', 'Ketu') else dignity(g, s)
ASPECT = {'Mangal': (4, 7, 8), 'Guru': (5, 7, 9), 'Shani': (3, 7, 10),
          'Rahu': (5, 7, 9), 'Ketu': (5, 7, 9)}
asp_d1, asp_d9 = {}, {}
for g in GRAHAS:
    for a in ASPECT.get(g, (7,)):
        asp_d1.setdefault((hs(g) + a - 2) % 12 + 1, []).append(g)
        asp_d9.setdefault((h9(g) + a - 2) % 12 + 1, []).append(g)

# =============================================================================
rule('1.  THREE CAREER REFERENCES, NOT ONE')
print("""
  Parashara reads a house from the lagna, from CHANDRA and from SURYA.  Most
  readings use only the first.  This document has used only the first.  Doing
  all three is the single largest thing that was missing, and it resolves an
  argument the reading has been having with itself for many sections.
""")
print(f"  {'reference':22s}{'10th from it':13s}{'lord':9s}{'natal house':13s}occupants")
for ref, lbl in (('Lagna', 'the LAGNA'), ('Chandra', 'CHANDRA — the mind'),
                 ('Surya', 'SURYA — the soul')):
    s = sign_of(POS[ref])
    t = (s + 9) % 12
    nh = (t - LAG) % 12 + 1
    print(f"  {lbl:22s}{SIGNS[t]:13s}{LORD[t]:9s}{ordn(nh) + ' house':13s}"
          f"{', '.join(occ(nh)) or 'empty'}")
print(f"""
  BUDHA IS THE CAREER LORD FROM THE LAGNA ONLY.
  SHANI IS THE CAREER LORD FROM BOTH CHANDRA AND SURYA.

  That is the whole of the argument this reading kept running into: section 21
  found the 10th lord ranks fourth as a career agent behind Shani, section 23
  found the same thing from placement, section 29 found the career vulnerability
  is entirely in Budha.  ALL OF IT FOLLOWS FROM ONE PLACEMENT FACT, and here it
  is without a single score:

      TWO OF THE THREE CLASSICAL CAREER REFERENCES ARE RULED BY SHANI.
      ONLY THE LAGNA GIVES THE JOB TO BUDHA.

  His nominal profession is Budha's -- analysis, communication, commerce.  His
  ACTUAL working life belongs to Shani: structure, service, endurance, time.
""")

# =============================================================================
rule('2.  THE 10TH HOUSE IN D1 — EVERYTHING THAT TOUCHES IT')
t10 = hsign(10)
l10 = LORD[t10]
print(f"""
      sign            {SIGNS[t10]} — dwiswabhava, an air sign
      lord            {l10}, in the {ordn(hs(l10))}, {dg(l10, sign_of(POS[l10]))}
      occupants       {', '.join(occ(10)) or 'empty'}
      aspects on it   {', '.join(asp_d1.get(10, [])) or 'NONE'}
      house class     kendra + upachaya + artha
""")

sub('Argala — intervention on the career house, never computed here')
print("""
  THE RULE.  Grahas in the 2nd, 4th and 11th from a house intervene in its
  affairs -- ARGALA.  Each argala has a specific counter-house whose occupants
  obstruct it -- VIRODHA ARGALA: the 12th counters the 2nd, the 10th counters
  the 4th, the 3rd counters the 11th.  An argala with an empty counter-house
  operates unopposed.

  THE TEST, from the 10th house:
""")
for a, v, lbl in ((2, 12, '2nd'), (4, 10, '4th'), (11, 3, '11th')):
    ah = (10 + a - 2) % 12 + 1
    vh = (10 + v - 2) % 12 + 1
    A, V = occ(ah), occ(vh)
    verdict = ('no argala' if not A else
               'UNOBSTRUCTED' if not V else f'obstructed by {", ".join(V)}')
    print(f"      argala from the {lbl:4s} = house {ah:2d}  {', '.join(A) or 'empty':28s}"
          f"counter house {vh:2d}  {verdict}")
print(f"""
  ONE ARGALA EXISTS AND IT IS UNOPPOSED.

      THREE GRAHAS IN THE 8TH HOUSE -- Surya, Budha, Shukra -- INTERVENE IN HIS
      CAREER, AND THE HOUSE THAT WOULD BLOCK THEM IS EMPTY.

  This is the sharpest statement in the whole section.  Everything that acts on
  his career acts THROUGH THE 8TH HOUSE: crisis, research, other people's
  resources, what is hidden, what is inherited, what is transformed.  Not
  through the 11th of networks, which is empty, and not through the 1st of
  self-assertion, which is also empty.

  AND NOTHING OBSTRUCTS IT.  The 12th from the 10th is vacant.

  So the career is reached by exactly one route and that route is wide open.
""")

# =============================================================================
rule('3.  THE 10TH LORD, IN FULL')
nk, pd = nak_of(POS[l10])[0], nak_of(POS[l10])[1]
NAKL = {'Ashwini': 'Ketu', 'Bharani': 'Shukra', 'Krittika': 'Surya',
        'Rohini': 'Chandra', 'Mrigashira': 'Mangal', 'Ardra': 'Rahu',
        'Punarvasu': 'Guru', 'Pushya': 'Shani', 'Ashlesha': 'Budha',
        'Magha': 'Ketu', 'Jyeshtha': 'Budha', 'Revati': 'Budha'}
print(f"""
      {l10} at {short(POS[l10])}
      house           the {ordn(hs(l10))} — a dusthana, and the weakest bhava
      dignity         {dg(l10, sign_of(POS[l10]))} in {SIGNS[sign_of(POS[l10])]}
      combust         YES, 9.00° from Surya, no exemption available
      nakshatra       {nk} pada {pd}, lord {NAKL.get(nk, '?')}
      rules           the {ordn(rules(l10)[0])} and the {ordn(rules(l10)[1])}
      sits with       {', '.join(g for g in occ(hs(l10)) if g != l10)}

  THE PAYOUT CHANNEL IS THE THING TO NOTICE.  A graha works in its sign lord's
  field but is PAID OUT by its nakshatra lord.  Budha stands in ASHWINI, whose
  lord is KETU.

      THE LORD OF HIS CAREER IS PAID OUT BY A SHADOW GRAHA.

  Ketu owns no sign, has no substance, and its function is severance.  So the
  10th lord's results are delivered through the one body in the chart that
  specialises in things ceasing to matter -- which is exactly the mechanism
  section 29 found for job loss, arrived at here by a completely different
  route and using only the nakshatra table.
""")

# =============================================================================
rule('4.  THE ARUDHA OF THE 10TH — HOW THE CAREER IS PERCEIVED')
lp = sign_of(POS[l10])
dist = (lp - t10) % 12 + 1
a10 = (lp + dist - 1) % 12
if (a10 - t10) % 12 + 1 in (1, 7):
    a10 = (a10 + 9) % 12
print(f"""
  THE RULE.  Count from the house to its lord, then the same distance again
  from the lord.  The resulting sign is the ARUDHA -- not what the house IS,
  but WHAT IT LOOKS LIKE FROM OUTSIDE.  The document computed the Arudha Lagna
  and the Upapada and never computed A10, the career arudha.

      from the 10th ({SIGNS[t10]}) to its lord in {SIGNS[lp]}   = {dist} signs
      the same {dist} again from {SIGNS[lp]}              = {SIGNS[a10]}

      A10 = {SIGNS[a10]}, which is his natal {ordn((a10 - LAG) % 12 + 1)} HOUSE.

  AND NOW PUT IT BESIDE SECTION 1 OF THIS SCRIPT:

      the 10th from CHANDRA  = {SIGNS[(sign_of(POS['Chandra']) + 9) % 12]}
      the ARUDHA of the 10th = {SIGNS[a10]}

  THE SAME SIGN, REACHED BY TWO COMPLETELY UNRELATED TECHNIQUES -- one a
  house-count from the Moon, the other a reflection formula from the lord.

  {SIGNS[a10]} is the 6TH HOUSE: service, employment, the daily work, contest,
  and the resolution of other people's problems.

      WHAT HIS CAREER IS: the 10th, ruled by a combust Budha in the 8th.
      WHAT HIS CAREER LOOKS LIKE: the 6th — the man who does the work.

  The reading has said "responsibility without title" and "the authority of the
  expert" from four other directions.  THIS IS THE PLACEMENT REASON, and it
  needed no strength measure at all.
""")

# =============================================================================
rule('5.  THE SAME APPARATUS IN THE NAVAMSA')
t10n = s9(10)
l10n = LORD[t10n]
print(f"""
      D9 lagna        {SIGNS[L9]} — VARGOTTAMA with the D1 lagna
      D9 10th sign    {SIGNS[t10n]}
      D9 10th lord    {l10n}, in D9 house {h9(l10n)}, {dg(l10n, D9[l10n])}
      D9 10th holds   {', '.join(occ9(10)) or 'empty'}
      aspects on it   {', '.join(asp_d9.get(10, [])) or 'NONE'}
""")
print(f"""  THE NAVAMSA GIVES THE CAREER HOUSE THE SAME SIGN AS THE RASHI CHART.

  Mithuna is the 10th in BOTH charts.  That is not vargottama in the technical
  sense -- which applies to a graha or the lagna, not to a house -- but it is
  the same structural statement: THE CAREER DOES NOT CHANGE SHAPE BETWEEN THE
  OUTER LIFE AND THE INNER ONE.

  AND SHANI OCCUPIES IT.

  In the rashi chart the 10th holds GURU and Shani is absent.  In the navamsa
  the 10th holds SHANI and Guru is absent.  The two charts hand the career
  house to different grahas -- and the navamsa's choice agrees with section 1
  of this script, where Shani rules the 10th from both Chandra and Surya.

      D1 SAYS THE CAREER IS GURU'S: reputation, counsel, standing, Amala.
      D9 SAYS THE CAREER IS SHANI'S: structure, service, endurance, time.

  THREE OF THE FOUR INDICATORS POINT AT SHANI AND ONE POINTS AT GURU.
""")

sub('And where the rashi 10th lord goes in the navamsa')
print(f"""
      {l10} in D1   {SIGNS[sign_of(POS[l10])]}, the {ordn(hs(l10))} house, combust
      {l10} in D9   {SIGNS[D9[l10]]}, D9 house {h9(l10)}, {dg(l10, D9[l10])}

  A graha's navamsa is classically read as the FATE of what it rules.  The lord
  of his career goes from a dusthana in the rashi chart to an ENEMY SIGN in the
  navamsa.

      IT DOES NOT RECOVER INSIDE.

  Section 26 found this for Budha generally; applied to the career specifically
  it says the profession itself never becomes comfortable.  Not that it fails --
  that it never stops costing effort.

  BY CONTRAST, look at the two grahas the navamsa favours for career:

      SHANI    D1 {SIGNS[sign_of(POS['Shani'])]:11s} {dg('Shani', sign_of(POS['Shani'])):8s} -> D9 {SIGNS[D9['Shani']]:11s} {dg('Shani', D9['Shani'])}, IN THE D9 10TH
      GURU     D1 {SIGNS[sign_of(POS['Guru'])]:11s} {dg('Guru', sign_of(POS['Guru'])):8s} -> D9 {SIGNS[D9['Guru']]:11s} {dg('Guru', D9['Guru'])}

  Shani holds friendly dignity in BOTH charts and occupies the navamsa 10th.
  Guru IMPROVES from enemy to neutral but leaves the career house.
""")

# =============================================================================
rule('6.  THE CAREER KARAKAS ACROSS BOTH CHARTS')
KAR = [('Surya', 'authority, the soul of the work, government'),
       ('Shani', 'karma, labour, service, duration'),
       ('Budha', 'commerce, skill, communication'),
       ('Guru', 'counsel, teaching, the advisory function'),
       ('Mangal', 'technical force, engineering, contest')]
print(f"  {'karaka':9s}{'D1 house':10s}{'D1 dignity':13s}{'D9 house':10s}{'D9 dignity':13s}what it signifies")
for g, what in KAR:
    print(f"  {g:9s}{ordn(hs(g)):10s}{dg(g, sign_of(POS[g])):13s}"
          f"{ordn(h9(g)):10s}{dg(g, D9[g]):13s}{what}")
print(f"""
  SURYA IS THE KARAKA OF AUTHORITY AND IT IS EXALTED IN BOTH CHARTS -- the only
  graha that is.  But it sits in the 8TH in D1 and the 8TH in D9.

      THE SIGNIFICATOR OF AUTHORITY IS THE BEST-MADE BODY IN THE CHART AND IT
      STANDS IN THE HOUSE OF CRISIS IN BOTH CHARTS.

  That is as exact a statement of "authority that is real and not visible" as
  the two charts can produce, and it required no technique beyond looking.
""")

# =============================================================================
rule('7.  WHAT THE TWO CHARTS AGREE AND DISAGREE ON')
print("""
  AGREED BY BOTH CHARTS

      the career house is MITHUNA in both -- the profession does not change
        shape between the outer life and the inner one
      BUDHA, its lord, is compromised in both -- combust in a dusthana outside,
        an enemy sign inside
      SURYA, the karaka of authority, is exalted in both and in the 8th in both
      the career sits on an 8TH-HOUSE axis in both charts

  DISAGREED

      D1 puts GURU in the 10th and forms Amala -- reputation, counsel, clean
        standing
      D9 puts SHANI there instead -- structure, service, endurance

  AND ONE PLACE WHERE I HAD TO CORRECT THE DRAFT.  I wrote that the D9 10th is
  unaspected like the D1 10th.  IT IS NOT:

      D1 10th   aspected by NOTHING
      D9 10th   aspected by GURU (its 5th, from the D9 6th) and MANGAL
                (its 4th, from the D9 7th)

  So the career house is SEALED IN THE OUTER CHART AND CONTACTED IN THE INNER
  ONE -- and one of the two contacts is the great benefic.  Guru leaves the
  career house in the navamsa but keeps aspecting it, which is a better outcome
  than the draft assumed: AMALA'S GIVER STILL REACHES THE CAREER FROM INSIDE.
  Mangal, the other contact, is in a friendly sign in D9 -- friction that is
  competent.

  AND THE THREE-REFERENCE TEST BREAKS THE TIE.  Shani rules the 10th from
  Chandra and from Surya; Budha rules it only from the lagna; Shani occupies
  the navamsa 10th.  GURU HOLDS ONE POSITION OUT OF FOUR.

  THE SYNTHESIS, USING NOTHING BUT THESE TWO CHARTS:

      HIS PROFESSION IS NOMINALLY BUDHA'S AND ACTUALLY SHANI'S.
      IT IS REACHED ONLY THROUGH THE 8TH HOUSE, BY AN ARGALA NOTHING BLOCKS.
      IT IS PERCEIVED AS THE 6TH -- the man who does the work, not the man who
        holds the post.
      ITS LORD IS PAID OUT BY KETU, so results arrive and then stop mattering.
      AND AMALA YOGA EXISTS IN THE RASHI CHART ONLY -- though Guru still
        ASPECTS the career house from inside the navamsa.

  THE LAST LINE IS THE ONE WORTH SITTING WITH.  The yoga of spotless reputation
  is an outer-chart fact.  Inside, Guru no longer occupies the career house; it
  only looks at it.  He will be well thought of, and from the inside it will
  feel like something observed rather than something held.
""")

# =============================================================================
rule('8.  WHAT THE CONSTRAINT COST')
print("""
  Stated honestly, because the exclusion was his instruction and not a
  limitation of the material:

  1. THE D10 IS THE DEDICATED CAREER VARGA and it is excluded here.  Its
     ascendant is Kumbha -- the SAME sign A10 and the 10th-from-Chandra both
     returned -- so it would have agreed rather than added.  That agreement is
     worth knowing and is not used above.

  2. NO TIMING.  Nothing here dates anything.  The windows are in sections 22,
     28 and 29.

  3. NO STRENGTH MEASURES.  Everything above is placement, lordship, aspect,
     dignity, nakshatra and arudha.  A reading that needs its own scoring to
     work is not a reading -- and this one did not need it.
""")
print('=' * 92)
