#!/usr/bin/env python3
"""
"9TH LORD IN 8TH / 8TH LORD IN 9TH — UNEXPECTED CHANGE OF FORTUNE THROUGH
SOMETHING INITIALLY PERCEIVED AS A CRISIS."

THAT IS THIS CHART'S CENTRAL STRUCTURE, NAMED FROM OUTSIDE.  Shukra rules the
9th and sits in the 8th; Mangal rules the 8th and sits in the 9th.  Section 49
calls it the single configuration everything else restates.

THE DESCRIPTION IS ACCURATE AS A DESCRIPTION AND THE VALENCE CLAIM IS THE PART
THAT NEEDS TESTING, because section 14 has classified this exchange DAINYA --
the type the tradition calls wretched -- and the pasted claim reads it as
fortune.  BOTH CANNOT BE TAKEN ON TRUST.

Computed here:

    1  the exchange exactly, including one thing sixteen prior mentions missed
    2  the two classical readings, and what each actually rests on
    3  the six named significations, tested ONE BY ONE against the chart
    4  WHEN it fires -- and the dasha arithmetic gives a hard answer
    5  the parivartana substitution, applied and measured
    6  the answer
"""
import swisseph as swe
from ephem_core import (SIGNS, GRAHAS, SUPPLIED, LORD, EXALT, varga, dignity,
                        sign_of, nak_of, jd_ut, short, local, rule, sub)

swe.set_sid_mode(swe.SIDM_LAHIRI)
POS = dict(SUPPLIED)
LAG = sign_of(POS['Lagna'])
G7 = ['Surya', 'Chandra', 'Mangal', 'Budha', 'Guru', 'Shukra', 'Shani']
ordn = lambda n: f"{n}{'th' if 10 <= n % 100 <= 20 else {1:'st',2:'nd',3:'rd'}.get(n%10,'th')}"
hs = lambda g: (sign_of(POS[g]) - LAG) % 12 + 1
rules = lambda g: [i + 1 for i in range(12) if LORD[(LAG + i) % 12] == g]
occ = lambda h: [g for g in GRAHAS if hs(g) == h]

ASPECTS = {'Surya': [7], 'Chandra': [7], 'Mangal': [4, 7, 8], 'Budha': [7],
           'Guru': [5, 7, 9], 'Shukra': [7], 'Shani': [3, 7, 10],
           'Rahu': [5, 7, 9], 'Ketu': [5, 7, 9]}
BRUP = [8.39, 9.18, 7.49, 9.28, 7.91, 7.21, 8.86, 7.00, 7.61, 7.39, 7.08, 12.59]
BRANK = [5, 3, 8, 2, 6, 10, 4, 12, 7, 9, 11, 1]
SAV = [21, 22, 29, 28, 24, 29, 24, 28, 29, 29, 41, 33]
RUPAS = {'Surya': 11.39, 'Chandra': 6.42, 'Mangal': 6.33, 'Budha': 6.46,
         'Guru': 8.21, 'Shukra': 6.68, 'Shani': 6.39}
MINREQ = {'Surya': 5.0, 'Chandra': 6.0, 'Mangal': 5.0, 'Budha': 7.0,
          'Guru': 6.5, 'Shukra': 5.5, 'Shani': 5.0}
ISHTA = {'Surya': 46.88, 'Chandra': 24.54, 'Mangal': 19.66, 'Budha': 18.91,
         'Guru': 37.30, 'Shukra': 47.49, 'Shani': 12.48}
KASHTA = {'Surya': 7.83, 'Chandra': 4.49, 'Mangal': 38.87, 'Budha': 30.32,
          'Guru': 15.10, 'Shukra': 11.87, 'Shani': 46.83}
A, B = 'Mangal', 'Shukra'          # 8th lord, 9th lord

# =============================================================================
rule('1.  THE EXCHANGE, EXACTLY')
print(f"""
      {B:8s} rules the {' and the '.join(ordn(x) for x in rules(B))}   sits in the {ordn(hs(B))}  ({SIGNS[sign_of(POS[B])]}, {dignity(B, sign_of(POS[B]))})
      {A:8s} rules the {' and the '.join(ordn(x) for x in rules(A))}   sits in the {ordn(hs(A))}  ({SIGNS[sign_of(POS[A])]}, {dignity(A, sign_of(POS[A]))})

  THE PASTED DESCRIPTION MATCHES THE CHART EXACTLY.  9th lord in the 8th, 8th
  lord in the 9th, a complete mutual exchange.  This is the configuration
  section 50 identifies as the one everything else in the reading restates.
""")
sub('and one thing sixteen prior mentions of it never checked')
sep = abs(POS[A] - POS[B])
aspect_ab = [(g, a) for g in (A, B) for a in ASPECTS[g]
             if (sign_of(POS[g]) + a - 1) % 12 == sign_of(POS[B if g == A else A])]
print(f"""
      longitude gap between them   {sep:.2f}°  -- they are {sep:.0f} degrees apart
      but they are in ADJACENT SIGNS, a 2/12 axis
      does {A} aspect {B}?     {'yes' if any(g == A for g, _ in aspect_ab) else 'NO'}
      does {B} aspect {A}?     {'yes' if any(g == B for g, _ in aspect_ab) else 'NO'}

  THE TWO LORDS DO NOT SEE EACH OTHER.  A 2/12 relationship carries no drishti
  in any scheme, and {A}'s special aspects (4th, 7th, 8th) miss as well.  They
  are {sep:.0f} degrees apart in longitude and completely unaspected by one another.

  THAT MATTERS FOR THE CLAIM BEING TESTED.  A parivartana is a bond of
  OWNERSHIP, not of sight.  Each holds the other's house and neither looks at
  it.  The exchange is real and it is administrative, not collaborative.
""")

# =============================================================================
rule('2.  THE TWO CLASSICAL READINGS, AND WHAT EACH RESTS ON')
DUST = {6, 8, 12}
both = set(rules(A)) | set(rules(B))
kind = 'DAINYA' if both & DUST else ('KHALA' if 3 in both else 'MAHA')
print(f"""
  READING ONE -- THE PARIVARTANA TYPOLOGY (section 14).

      the pair's lordships       {sorted(both)}
      dusthana in the pair?      {sorted(both & DUST)}  -- the 8TH
      3rd lordship in the pair?  {'yes' if 3 in both else 'no'}
      => {kind} parivartana, and Khala as well.

      Dainya means poverty, wretchedness, dependency.  ON THIS TYPOLOGY THE
      EXCHANGE IS THE BAD KIND, AND IT IS NOT CLOSE.

  READING TWO -- THE TRIKONA/DUSTHANA READING, WHICH IS WHAT WAS PASTED.

      {B} also rules the 9TH -- the strongest trikona, the house of fortune.
      So this is not a plain dusthana exchange.  It is a DUSTHANA LORD AND A
      TRIKONA LORD SWAPPING SEATS, and the trikona lord goes INTO the dusthana.

      THAT IS A REAL DISTINCTION AND THE TYPOLOGY DOES NOT CAPTURE IT.  The
      Dainya rule fires on the presence of a dusthana lordship anywhere in the
      pair; it does not ask what else the pair owns.  Here the pair owns the
      2nd, 3rd, 8th and 9th -- the worst dusthana and the best trikona at once.

  AND A DRAFT OF THIS SECTION GOT THE PROVENANCE WRONG, SO THE CORRECTION IS
  PRINTED RATHER THAN QUIETLY MADE.

      THE DRAFT SAID the fortune reading is "a later elaboration, not textual."
      THAT IS TOO STRONG.  Section 37's contents page lists BPHS CHAPTER 24 --
      "Effects of the bhava lords, 144 combinations" -- which is precisely a
      chapter of results for EVERY lord in EVERY house.  So "9th lord in the
      8th" and "8th lord in the 9th" are BOTH classical entries with stated
      results.  The placements are textual.

      WHAT IS NOT TEXTUAL IS THE JOINT CLAIM.  Chapter 24 gives two separate
      results, one per placement.  It does not give a combined result for the
      EXCHANGE, and no chapter in the fifty-five enumerated in sections 35 and
      37 states "the 8th-9th parivartana produces an unexpected change of
      fortune."  THAT SYNTHESIS -- two placements read as one mechanism with
      one outcome -- IS THE LATER PART.

      AND CHAPTER 24 IS ON THIS DOCUMENT'S OWN UNFINISHED LIST.  Section 37
      marks it "§6, §9, throughout", which means used in passing and never
      worked systematically.  SO THE HONEST POSITION IS: the tradition has a
      specific answer for each half of this exchange, THIS READING HAS NEVER
      LOOKED IT UP, and parts 3 to 5 below test the claim against the chart
      instead of against the chapter.
""")

# =============================================================================
rule('3.  THE SIX NAMED SIGNIFICATIONS, TESTED ONE BY ONE')
print(f"""
      8th house  {SIGNS[(LAG+7)%12]:11s} Bhava Bala {BRUP[7]:5.2f} rupas -- RANK {BRANK[7]} OF 12, THE WEAKEST BHAVA
                             SAV {SAV[(LAG+7)%12]} -- THE LOWEST OF THE TWELVE SIGNS
                             occupants: {', '.join(occ(8))}
      9th house  {SIGNS[(LAG+8)%12]:11s} Bhava Bala {BRUP[8]:5.2f} rupas -- rank {BRANK[8]} of 12
                             SAV {SAV[(LAG+8)%12]}
                             occupants: {', '.join(occ(9))}

  THE HOUSE THE FORTUNE IS SUPPOSED TO ARRIVE THROUGH IS THE WEAKEST BHAVA IN
  THE CHART AND THE WEAKEST SIGN BY ASHTAKAVARGA.  That is not a refutation --
  a weak bhava can still deliver in the right dasha -- but it is the first
  thing an honest test returns and it is not in the pasted description.
""")
CHECK = [
 ('INHERITANCE',
  '8th house and its lord; the 2nd from the 8th (the 9th) for what is received',
  lambda: [
    f"8th lord {A} in the 9th -- what the 8th yields, placed in the house of",
    "the father.  THE CLASSICAL SIGNATURE IS PRESENT.",
    f"but {A}'s Shadbala is {RUPAS[A]} against a minimum of {MINREQ[A]} -- it PASSES,",
    f"and its Kashta phala is {KASHTA[A]:.2f}, THE SECOND HIGHEST IN THE CHART.",
    f"the 2nd house (family wealth) is ruled by {B}, which is in the 8th.",
    "VERDICT: the significature is there and it is expensive.  Nothing in the",
    "chart dates it, and no computation in this document can name an amount.",
  ]),
 ('MARRIAGE',
  '7th house, 7th lord, Upapada, Shukra as karaka',
  lambda: [
    f"7th lord Guru is the SOLE OCCUPANT OF THE 10TH; Upapada is Dhanu, lord Guru.",
    f"Shukra -- the marriage karaka AND the 9th lord in this exchange -- carries",
    f"the HIGHEST Ishta phala in the chart at {ISHTA[B]:.2f}, cost {KASHTA[B]:.2f}.",
    "and section 40 already timed this from the Upapada and the double transit.",
    "VERDICT: STRONGEST OF THE SIX.  The karaka of the thing named is one of the",
    "two grahas in the exchange, and it is the best-conditioned graha in the chart.",
  ]),
 ('RESEARCH AND OCCULT KNOWLEDGE',
  '8th house, its lord in the 9th, Ketu, Shani, the 5th of mantra',
  lambda: [
    f"8TH LORD IN THE 9TH IS THE TEXTBOOK RESEARCH PLACEMENT -- the house of",
    f"hidden things governed from the house of knowledge and doctrine.",
    f"Shani is the Amatyakaraka AND the 5th lord (mantra, purva punya).",
    f"Ketu sits in the 3rd; the 8th holds three grahas including the exalted Surya.",
    "VERDICT: SECOND STRONGEST.  This one is structural, not incidental -- it is",
    "the exchange itself, read forwards.",
  ]),
 ('TAX, INSURANCE, OTHER PEOPLE\'S MONEY',
  '8th house, 6th (debt), 2nd and 11th for what accrues',
  lambda: [
    f"the 8th is the weakest bhava (rank {BRANK[7]}) and lowest SAV ({SAV[(LAG+7)%12]}).",
    f"the 6th -- debt and obligation -- has SAV {SAV[(LAG+5)%12]}, THE HIGHEST IN THE CHART,",
    f"and its lord is Shani, the Amatyakaraka.",
    "VERDICT: the DEBT side of this signification is far better supported than",
    "the RECEIPT side.  The chart is built to carry obligation, not to be handed",
    "windfalls.  THAT IS THE OPPOSITE WEIGHTING TO THE PASTED CLAIM.",
  ]),
 ('INSTITUTIONAL CONNECTIONS',
  '6th (service), 10th (office), 11th (networks), 12th (large institutions)',
  lambda: [
    f"6th SAV {SAV[(LAG+5)%12]} (highest), 10th SAV {SAV[(LAG+9)%12]}, 11th SAV {SAV[(LAG+10)%12]},",
    f"12th SAV {SAV[(LAG+11)%12]} with Bhava Bala {BRUP[11]} -- RANK {BRANK[11]} OF 12, THE STRONGEST.",
    f"the 12th's lord is Surya, exalted, and it sits IN THE 8TH.",
    "VERDICT: STRONG, and it arrives through the 12th rather than the 11th --",
    "large institutions and elsewhere, not networks and contacts.  Sections 41",
    "and 45 reached the same place from different directions.",
  ]),
 ('A CHANGE IN FORTUNE ITSELF',
  '9th house, 9th lord, and whether the 9th can deliver from the 8th',
  lambda: [
    f"9th house Bhava Bala {BRUP[8]} -- rank {BRANK[8]} of 12, MIDDLING.",
    f"9th lord {B} is in the 8th, Shadbala {RUPAS[B]} against minimum {MINREQ[B]} -- PASSES.",
    f"{B} is also the ATMAKARAKA and carries the chart's highest Ishta phala.",
    f"but the 9th's own occupants are {', '.join(occ(9))} -- four grahas, including",
    f"Shani ({dignity('Shani', sign_of(POS['Shani']))}) and Rahu.",
    "VERDICT: the fortune is REAL and it is ROUTED.  The 9th lord does not sit in",
    "the 9th; it administers fortune from the house of crisis.  THAT IS EXACTLY",
    "WHAT THE PASTED CLAIM SAYS, AND IT IS THE ONE PART THAT SURVIVES INTACT.",
  ]),
]
for name, basis, fn in CHECK:
    sub(name)
    print(f"      tested against: {basis}\n")
    for line in fn():
        print(f"      {line}")

# =============================================================================
rule('4.  WHEN IT FIRES — AND THE DASHA ARITHMETIC IS BLUNT')
VIM = [('Ketu', 7), ('Shukra', 20), ('Surya', 6), ('Chandra', 10),
       ('Mangal', 7), ('Rahu', 18), ('Guru', 16), ('Shani', 19), ('Budha', 17)]
Y = 365.2425
nk, pada, nl, into = nak_of(POS['Chandra'])
i0 = [x[0] for x in VIM].index(nl)
birth = jd_ut(2002, 4, 15, 18, 2, 45, 5.5)
t = birth - (into / (360 / 27)) * VIM[i0][1] * Y
MD, AD = [], []
for k in range(9):
    g, yrs = VIM[(i0 + k) % 9]
    MD.append((g, t, t + yrs * Y))
    a = t
    for m in range(9):
        ag, ay = VIM[(i0 + k + m) % 9]
        b = a + yrs * ay / 120 * Y
        AD.append((g, ag, a, b))
        a = b
    t += yrs * Y
NOW = swe.julday(2026, 9, 2, 0.0)
print(f"""
  A PARIVARTANA IS HELD TO FIRE IN THE DASHAS OF ITS TWO LORDS.  So the whole
  question of WHEN reduces to: when do {A} and {B} run?
""")
print(f"  {'mahadasha':10s}{'from':13s}{'to':13s}{'age at start':>13s}   ")
for g, a, b in MD:
    tag = ''
    if g in (A, B):
        tag = ('   <<< ALREADY SPENT' if b < NOW else
               '   <<< STILL TO COME' if a > NOW else '   <<< RUNNING NOW')
    print(f"  {g:10s}{local(a)[:10]:13s}{local(b)[:10]:13s}"
          f"{(a-birth)/Y:13.1f}{tag}")
mmd = [x for x in MD if x[0] == A][0]
smd = [x for x in MD if x[0] == B][0]
print(f"""
  READ THOSE TWO ROWS TOGETHER, BECAUSE NOBODY IN THIS DOCUMENT HAS:

      {A} mahadasha  ended {local(mmd[2])[:10]}, at age {(mmd[2]-birth)/Y:.0f}.  SPENT.
      {B} mahadasha  begins {local(smd[1])[:10]}, at age {(smd[1]-birth)/Y:.0f}.  UNREACHABLE.

  THE MAHADASHAS OF BOTH LORDS OF THE EXCHANGE ARE OUT OF PLAY.  One is behind
  him and the other is past any plausible lifespan.  Krittika's Vimshottari
  order puts Shukra LAST of the nine.

  SO THE EXCHANGE NEVER GETS A MAHADASHA AGAIN.  It fires only at antardasha
  level and below, for the rest of his life.  THAT IS THE SINGLE MOST IMPORTANT
  FACT ABOUT THIS CONFIGURATION AND IT IS PURE ARITHMETIC.
""")
sub(f'every remaining antardasha of {A} or {B}, to age 80')
lim = birth + 80 * Y
rows = [(g, ag, a, b) for g, ag, a, b in AD
        if ag in (A, B) and b > NOW and a < lim]
print(f"  {'mahadasha':11s}{'antardasha':12s}{'from':13s}{'to':13s}{'age':>6s}{'years':>8s}")
for g, ag, a, b in rows:
    print(f"  {g:11s}{ag:12s}{local(max(a,NOW))[:10]:13s}{local(b)[:10]:13s}"
          f"{(a-birth)/Y:6.0f}{(b-a)/Y:8.2f}")
tot = sum(b - max(a, NOW) for _, _, a, b in rows) / Y
print(f"""
      total remaining time under a lord of the exchange, to age 80: {tot:.1f} years
      as a fraction of the {(lim-NOW)/Y:.0f} years to age 80: {tot/((lim-NOW)/Y)*100:.0f}%

  AND THE NEAREST ONE IS THE ONE THAT MATTERS:""")
nxt = min(rows, key=lambda r: r[2] if r[2] > NOW else 1e9)
run = [r for r in rows if r[2] <= NOW < r[3]]
if run:
    g, ag, a, b = run[0]
    print(f"      RUNNING NOW: {g}-{ag}, to {local(b)[:10]}")
print(f"      NEXT: {nxt[0]}-{nxt[1]}, {local(nxt[2])[:10]} to {local(nxt[3])[:10]}, "
      f"age {(nxt[2]-birth)/Y:.0f}, lasting {(nxt[3]-nxt[2])/Y:.2f} years")

# =============================================================================
rule('5.  THE PARIVARTANA SUBSTITUTION, APPLIED AND MEASURED')
print(f"""
  ONE CLASSICAL TREATMENT OF A COMPLETE EXCHANGE IS THAT EACH LORD IS READ AS
  IF IT WERE IN ITS OWN SIGN, because it owns the ground it stands on through
  its partner.  THAT IS A SCHOOL POSITION, NOT A UNIVERSAL RULE, and it has
  never been applied in this document.  Applied here:
""")
print(f"  {'graha':9s}{'actual sign':13s}{'actual dignity':16s}"
      f"{'as-if sign':13s}{'as-if dignity':14s}")
for g in (A, B):
    act = sign_of(POS[g])
    asif = sign_of(POS[B if g == A else A])
    print(f"  {g:9s}{SIGNS[act]:13s}{dignity(g, act):16s}"
          f"{SIGNS[asif]:13s}{dignity(g, asif):14s}")
print(f"""
  BOTH GO FROM NEUTRAL TO OWN SIGN.  That is the entire effect of the
  substitution, and it is worth being precise about how small it is:

      NEITHER BECOMES EXALTED.  Neither was debilitated to begin with.  The
      upgrade is one step, neutral -> own, for two grahas.

      IT CHANGES NO HOUSE PLACEMENT.  {A} is still in the 9th and {B} is still
      in the 8th under every reading.  The substitution is about DIGNITY only.

      AND IT DOES NOT TOUCH THE MEASURED STRENGTHS.  Shadbala {A} {RUPAS[A]},
      {B} {RUPAS[B]} -- both computed from the actual positions, both PASSING
      their minimum, both in the bottom half of the chart.  Section 8's ranking
      is unaffected because Shadbala never used the substitution.

  SO THE SUBSTITUTION IS A GENUINE UPGRADE AND A SMALL ONE.  It does not turn a
  Dainya exchange into a Maha one, and no school claims it does.
""")

# =============================================================================
rule('6.  THE ANSWER')
print(f"""
  THE DESCRIPTION IS RIGHT ABOUT THE MECHANISM AND OVERSTATED ABOUT THE PAYOUT,
  AND THE CHART IS SPECIFIC ABOUT WHICH PARTS LAND.

  WHAT IS CONFIRMED, WITHOUT QUALIFICATION:

      THE CONFIGURATION IS EXACTLY AS DESCRIBED.  9th lord in the 8th, 8th lord
      in the 9th, complete exchange.  Section 50 already calls it the one
      structure the whole reading restates.

      "FORTUNE ROUTED THROUGH CRISIS" IS LITERALLY WHAT THE CHART DOES.  The
      9th lord does not sit in the 9th.  Bhagya is administered from the house
      of upheaval, and there is no other channel for it.

      OF THE SIX NAMED SIGNIFICATIONS, THREE ARE STRONGLY SUPPORTED:
          MARRIAGE -- the karaka of it IS one of the two exchanging grahas, and
              it is the best-conditioned graha in the chart
          RESEARCH AND OCCULT KNOWLEDGE -- this is the exchange read forwards;
              the 8th lord governing hidden things from the house of doctrine
          INSTITUTIONAL CONNECTIONS -- but through the 12TH, the strongest bhava
              in the chart, not through the 11th of networks

  WHAT THE COMPUTATION DOES NOT SUPPORT:

      "COMPLETELY UNEXPECTED CHANGE IN FORTUNE" AS A PROMISE OF SCALE.  The 8th
      house is the WEAKEST BHAVA in this chart (rank {BRANK[7]} of 12) and Mesha is the
      LOWEST SAV of the twelve signs ({SAV[0]}).  The channel is real; the channel is
      also the thinnest thing in the chart.

      THE TAX/INSURANCE/OTHER-PEOPLE'S-MONEY SIGNIFICATION INVERTS.  The debt
      side is the best-supported house in the chart ({SAV[(LAG+5)%12]} bindus in the 6th, the
      highest) and the receipt side is the worst.  He is built to CARRY
      obligation, not to be handed windfalls.

      AND THE TYPOLOGY DISAGREES WITH THE CLAIM OUTRIGHT.  Section 14 classes
      this exchange DAINYA -- wretched -- and Khala on top.  Both halves of the
      placement are covered individually by BPHS chapter 24; what the texts do
      not carry is a JOINT result for the exchange, which is the form the claim
      takes.  THIS DOCUMENT REPORTS BOTH READINGS AND PICKS NEITHER, because the
      texts do not settle it and pretending otherwise would be inventing
      authority.

  AND THE HARD FACT NOBODY MENTIONS WHEN THEY DESCRIBE THIS YOGA:

      A PARIVARTANA FIRES IN THE DASHAS OF ITS TWO LORDS.  {A}'s mahadasha
      ENDED at age {(mmd[2]-birth)/Y:.0f}.  {B}'s mahadasha BEGINS at age {(smd[1]-birth)/Y:.0f}.

      THE EXCHANGE WILL NEVER HOLD A MAHADASHA AGAIN IN HIS LIFE.  Whatever it
      delivers, it delivers in antardashas and below -- about {tot:.0f} years spread
      across the next fifty, in pieces of a year or two.

      SO THE ANSWER TO "WHEN" IS: NOT AS ONE EVENT.  The description imagines a
      hinge.  The arithmetic gives instalments.

  ONE LAST THING, AND IT IS THE PART THAT IS ACTUALLY GOOD.

      The two lords are {sep:.0f} degrees apart and DO NOT ASPECT EACH OTHER.  They
      hold each other's houses and never look at each other.  That is not a
      defect -- it is why the arrangement is STABLE rather than volatile.  The
      crisis house and the fortune house are permanently bonded by ownership
      and permanently out of each other's sight.

      SECTION 50 PUT IT IN ONE SENTENCE AND THE COMPUTATION HAS NOT MOVED IT:
      every crisis is routed through meaning, and every belief is tested by
      crisis.  He does not get to hold a philosophy that has not been through
      something.  THAT IS THE YOGA.  NOT A WINDFALL -- A WIRING.
""")
print('=' * 92)
