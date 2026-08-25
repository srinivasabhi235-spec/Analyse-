#!/usr/bin/env python3
"""
THE CLASSICAL SEQUENCE, RUN IN ORDER, ON THE 10TH HOUSE.

A methodological correction was put to this reading:

    "If you want to follow BPHS, I would not say D1 = 35%, Varga = 25%,
     Shadbala = 8%.  That is not a classical prescription.  Instead the Bhava
     and its lord are central, and the other techniques are progressively used
     to qualify, strengthen, corroborate and time the result."

    Subject -> Bhava -> Bhava Lord -> Karaka -> Varga -> Planetary Strength
    -> Bhava Strength -> Yogas/Afflictions -> Dasha -> Transit/Ashtakavarga

TWO SEPARATE CLAIMS, AND THEY NEED SEPARATE ANSWERS.

THE WEIGHTS.  This document has never assigned a percentage weight to a
technique.  Checked programmatically: zero occurrences.  The only percentages
in it are Vimshopaka's own varga weights -- which are classical, and come from
the very chapter (7) that defines the measure -- and rarity frequencies from an
explicit null model in section 38.  SO THE CORRECTION IS RIGHT IN GENERAL AND
DOES NOT APPLY HERE.  Recorded rather than accepted.

THE ORDER.  THAT ONE LANDS.  This reading computed everything first and
synthesised afterwards, which is not the same as judging in sequence.  The
sequence subordinates strength to bhava, lord and karaka; this document reached
for Shadbala early and often.

SO THE TEST IS: RUN THE CLASSICAL SEQUENCE IN STRICT ORDER ON THE 10TH HOUSE,
RECORD THE RUNNING VERDICT AFTER EVERY STEP, AND SEE WHERE IT MOVES.

If the verdict is stable from step 3, the reading's conclusions are robust to
method-order.  If it flips at step 6, then computing strength early was doing
work the classical method would not have let it do.
"""
from ephem_core import (SIGNS, GRAHAS, SUPPLIED, LORD, varga, dignity,
                        sign_of, rule, sub)

POS = dict(SUPPLIED)
LAG = sign_of(POS['Lagna'])
G7 = [g for g in GRAHAS if g not in ('Rahu', 'Ketu')]
hs = lambda g: (sign_of(POS[g]) - LAG) % 12 + 1
occ = lambda h: [g for g in GRAHAS if hs(g) == h]
ordn = lambda n: f"{n}{'th' if 10 <= n % 100 <= 20 else {1:'st',2:'nd',3:'rd'}.get(n%10,'th')}"

H = 10
HSIGN = (LAG + H - 1) % 12
HLORD = LORD[HSIGN]

# supplied strength tables (verify_bala.py)
RUPAS = {'Surya': 11.39, 'Chandra': 6.42, 'Mangal': 6.33, 'Budha': 6.46,
         'Guru': 8.21, 'Shukra': 6.68, 'Shani': 6.39}
MINREQ = {'Surya': 5.0, 'Chandra': 6.0, 'Mangal': 5.0, 'Budha': 7.0,
          'Guru': 6.5, 'Shukra': 5.5, 'Shani': 5.0}
SRANK = {'Surya': 1, 'Chandra': 6, 'Mangal': 3, 'Budha': 7,
         'Guru': 4, 'Shukra': 5, 'Shani': 2}
ISHTA = {'Surya': 46.88, 'Chandra': 24.54, 'Mangal': 19.66, 'Budha': 18.91,
         'Guru': 37.30, 'Shukra': 47.49, 'Shani': 12.48}
BRUP = [8.39, 9.18, 7.49, 9.28, 7.91, 7.21, 8.86, 7.00, 7.61, 7.39, 7.08, 12.59]
BRANK = [5, 3, 8, 2, 6, 10, 4, 12, 7, 9, 11, 1]
SAV = {'Mesha': 21, 'Vrishabha': 22, 'Mithuna': 29, 'Karka': 28, 'Simha': 24,
       'Kanya': 29, 'Tula': 24, 'Vrischika': 28, 'Dhanu': 29, 'Makara': 29,
       'Kumbha': 41, 'Meena': 33}

VERDICT = []


def verdict(step, text):
    changed = ' ' if (VERDICT and VERDICT[-1][1] == text) else '<<< MOVED'
    if not VERDICT:
        changed = '<<< SET'
    VERDICT.append((step, text))
    print(f"\n  RUNNING VERDICT after step {step}:  {text}   {changed}")


# =============================================================================
rule('STEP 1.  WHAT THE BHAVA REPRESENTS')
print(f"""
  The 10th house.  Profession, authority, status, action in the world, the
  karma one is seen doing.  For this nativity the 10th is {SIGNS[HSIGN]}, and its
  lord is {HLORD}.

  NOTHING IS JUDGED YET.  The subject is fixed and nothing else.
""")

# =============================================================================
rule('STEP 2.  JUDGE THE BHAVA ITSELF — SIGN, OCCUPANTS, ASPECTS')
ASPECTS = {'Surya': [7], 'Chandra': [7], 'Budha': [7], 'Shukra': [7],
           'Mangal': [4, 7, 8], 'Guru': [5, 7, 9], 'Shani': [3, 7, 10],
           'Rahu': [], 'Ketu': []}
inc = []
for g in GRAHAS:
    for a in ASPECTS[g]:
        if (sign_of(POS[g]) + a - 1) % 12 == HSIGN:
            inc.append((g, a))
print(f"""      sign            {SIGNS[HSIGN]} — dual, air, ruled by {HLORD}
      occupants       {', '.join(occ(H)) or 'none'}
      aspects onto it {', '.join(f'{g} ({ordn(a)})' for g, a in inc) or 'NONE'}
""")
print(f"""  THE 10TH HOUSE OF THIS CHART RECEIVES NO ASPECT FROM ANY GRAHA.

  Section 10 found this and section 23 confirmed it: the 10th is one of only
  two houses in the chart that nothing reaches.  It holds one graha, GURU, and
  no influence of any kind arrives from outside.

  ON THE BHAVA ALONE, BEFORE ANY LORD OR STRENGTH IS CONSULTED: a benefic sits
  in the career house, unaspected by malefics AND unaspected by benefics.  No
  affliction and no help.  A SEALED CHAMBER.
""")
verdict(2, 'career house occupied by a benefic, sealed from all outside influence')

# =============================================================================
rule('STEP 3.  JUDGE THE BHAVA LORD')
lp = hs(HLORD)
ld = dignity(HLORD, sign_of(POS[HLORD]))
comb = abs(POS[HLORD] - POS['Surya'])
comb = min(comb, 360 - comb)
withl = [g for g in GRAHAS if g != HLORD and hs(g) == lp]
inc2 = [(g, a) for g in GRAHAS for a in ASPECTS[g]
        if (sign_of(POS[g]) + a - 1) % 12 == sign_of(POS[HLORD])]
print(f"""      lord            {HLORD}
      placed in       the {ordn(lp)} house — {SIGNS[sign_of(POS[HLORD])]}
      house quality   DUSTHANA (the 8th), lowest SAV in the chart ({SAV[SIGNS[sign_of(POS[HLORD])]]})
      dignity         {ld}
      combustion      {comb:.2f} deg from Surya — COMBUST
      conjoined with  {', '.join(withl) or 'none'}
      aspected by     {', '.join(f'{g} ({ordn(a)})' for g, a in inc2) or 'NONE'}
      also rules      the {ordn(1)} house — it is the LAGNA LORD as well
""")
print(f"""  THIS IS THE HEART OF THE JUDGMENT AND IT IS BAD.

  The lord of the career house is in a dusthana, in the weakest bhava of the
  chart, COMBUST, in a neutral sign, unaspected, and it is simultaneously the
  lagna lord -- so the self and the career run through one compromised graha.

  ONE COUNTERWEIGHT, AND IT IS REAL: {HLORD} sits with SHUKRA, the 9th lord.
  10th lord with 9th lord is the DHARMA-KARMADHIPATI YOGA, the strongest raja
  yoga in Parashari astrology.  IT FORMS IN THE 8TH HOUSE.

  So the promise is genuine and its channel is damaged.  THE BHAVA IS SEALED
  AND ITS LORD IS BURIED IN THE HOUSE OF UPHEAVAL, WITH A RAJA YOGA ATTACHED.
""")
verdict(3, 'real promise, damaged channel — delivery only through upheaval')

# =============================================================================
rule('STEP 4.  JUDGE THE KARAKA')
KAR = {'Surya': 'authority, status, the visible position',
       'Budha': 'commerce, intellect, transaction',
       'Guru': 'counsel, teaching, knowledge-work',
       'Shani': 'service, labour, the long grind'}
print("  The classical karakas of the 10th, each judged on its own:\n")
for g, what in KAR.items():
    print(f"      {g:8s} house {ordn(hs(g)):5s} {dignity(g, sign_of(POS[g])):12s}"
          f" Ishta {ISHTA[g]:5.2f}   {what}")
print(f"""
  THE KARAKAS SPLIT, AND THE SPLIT IS THE FINDING.

      SURYA is EXALTED, and it is the strongest graha in the chart on every
      measure -- but it sits in the 8th and rules the 12th.
      GURU is in the career house itself, but in an ENEMY sign.
      BUDHA is combust and is the damaged lord already judged in step 3.
      SHANI is in the 9th, and carries the lowest Ishta phala in the chart.

  SO THE AUTHORITY KARAKA IS SPLENDID AND PLACED IN LOSS AND UPHEAVAL; THE
  COUNSEL KARAKA IS PRESENT BUT UNCOMFORTABLE; THE TRANSACTION KARAKA IS BURNT;
  THE SERVICE KARAKA DELIVERS LEAST OF ANYTHING HE OWNS.

  This CORROBORATES step 3 rather than altering it: capacity is real, the
  channel is obstructed, and what does arrive arrives through the 8th and 9th.
""")
verdict(4, 'real promise, damaged channel — delivery only through upheaval')

# =============================================================================
rule('STEP 5.  CHECK THE RELEVANT VARGA — D10')
d10 = {g: varga(POS[g], 10) for g in list(GRAHAS) + ['Lagna']}
d10lag = d10['Lagna']
d10h = lambda g: (d10[g] - d10lag) % 12 + 1
tenth_d10 = (d10lag + 9) % 12
print(f"""      D10 lagna       {SIGNS[d10lag]}
      D10 10th house  {SIGNS[tenth_d10]}
      its occupants   {', '.join(g for g in GRAHAS if d10[g] == tenth_d10) or 'none'}
""")
print(f"  {'graha':9s}{'D10 sign':12s}{'D10 house':11s}dignity")
for g in G7:
    print(f"  {g:9s}{SIGNS[d10[g]]:12s}{ordn(d10h(g)):11s}{dignity(g, d10[g])}")
print(f"""
  I DRAFTED THIS STEP EXPECTING THE D10 TO FLATTER THE CHART -- the usual
  caution that a varga carries sign dignity but not affliction, so a graha that
  is combust and buried in the D1 can look clean in the D10.  THE COMPUTATION
  SAYS THE OPPOSITE HERE.

      {HLORD}, the D1 career lord, is in the {ordn(d10h(HLORD))} of the D10 in an ENEMY sign.
      Guru, the D1 10th-house occupant, is in the {ordn(d10h('Guru'))} of the D10, ALSO an enemy sign.

  THE D10 IS HARSHER ON THE CAREER LORD THAN THE D1 IS, not kinder.  Budha
  moves from neutral-and-combust to an enemy sign in a dusthana of the career
  varga.  THE VARGA CORROBORATES THE DAMAGE.

  AND IT ADDS ONE THING THE D1 DOES NOT SHOW:

      the D10 10th house is {SIGNS[tenth_d10]}, and SHUKRA occupies it.

  Shukra is the 9th lord, the Atmakaraka, and the highest Ishta phala in the
  chart.  The career house OF THE CAREER VARGA is held by the best deliverer he
  owns -- which is the same finding step 3 reached from the other direction,
  since Shukra is also the graha sitting with Budha and forming the raja yoga.

  SO THE D10 REFINES WITHOUT OVERTURNING, WHICH IS WHAT THE SEQUENCE ASKS OF
  IT.  Had it been read first, the Shukra placement alone could have carried a
  career story that the sealed house and the buried lord do not support.
""")
verdict(5, 'real promise, damaged channel — delivery only through upheaval')

# =============================================================================
rule('STEP 6.  PLANETARY STRENGTH — SHADBALA')
print(f"  {'graha':9s}{'rupas':>8s}{'required':>10s}{'ratio':>8s}{'rank':>6s}   verdict")
for g in ('Budha', 'Guru', 'Surya', 'Shani'):
    r = RUPAS[g] / MINREQ[g]
    print(f"  {g:9s}{RUPAS[g]:8.2f}{MINREQ[g]:10.2f}{r:8.4f}{SRANK[g]:6d}   "
          f"{'FAILS ITS MINIMUM' if r < 1 else 'passes'}")
print(f"""
  BUDHA IS THE ONLY GRAHA IN THE CHART THAT FAILS ITS SHADBALA MINIMUM, and it
  is the career lord and the lagna lord.  Rank 7 of 7.

  NOTE WHAT THIS STEP DID AND DID NOT DO.  It did not discover the problem --
  step 3 already had the lord combust in a dusthana.  IT MEASURED HOW BAD THE
  PROBLEM IS, which is precisely the role the sequence assigns it.

  Had strength been consulted FIRST, the reading would have started from
  "Budha rank 7, Surya rank 1" and been tempted to build the career story on
  SURYA, which is the strongest graha but rules the TWELFTH and is only a
  karaka here, not the lord.  THE SEQUENCE PREVENTS THAT SUBSTITUTION.
""")
verdict(6, 'real promise, damaged channel — delivery only through upheaval')

# =============================================================================
rule('STEP 7.  BHAVA STRENGTH — BHAVA BALA OF THE 10TH')
print(f"""      10th house rupas   {BRUP[9]:.2f}
      rank               {BRANK[9]} of 12
      strongest bhava    the 12th, {max(BRUP):.2f}
      weakest bhava      the 8th, {min(BRUP):.2f}

  THE CAREER HOUSE IS RANK {BRANK[9]} OF TWELVE -- below the middle, not catastrophic.

  AND HERE IS WHERE THE TWO STRENGTH MEASURES DISAGREE, WHICH IS THE WHOLE
  POINT OF KEEPING THEM SEPARATE: the HOUSE is mediocre while its LORD is the
  worst graha in the chart.  Bhava Bala is built largely from the lord's own
  Shadbala plus aspect and directional terms, so a house whose lord is failing
  can still rank mid-table when the other terms carry it.

  THE HOUSE IS ORDINARY.  THE MAN WHO RUNS IT IS NOT WELL.
""")
verdict(7, 'real promise, damaged channel — delivery only through upheaval')

# =============================================================================
rule('STEP 8.  BENEFIC / MALEFIC INFLUENCE, AFFLICTION, YOGAS')
print(f"""      on the BHAVA        no aspect at all — neither benefic nor malefic
      occupant            Guru, natural benefic, in an ENEMY sign
      kendradhipati       Guru rules the 4th and 7th, two kendras — the dosha
                          section 36 prices as the most expensive unread rule
      on the LORD         combust; conjoined Surya (malefic) and Shukra (benefic)
      yoga present        Dharma-Karmadhipati — 9th lord with 10th lord
      where it forms      the 8th house, lowest SAV in the chart
      also present        Amala — a benefic alone in the 10th
      Amala qualified by  enemy sign, sushupti avastha, kendradhipati dosha,
                          badhakesh, Yama Ghantaka contact, lowest Drik Bala

  THE AFFLICTION LAYER ADDS NO NEW DAMAGE AND REMOVES NO OLD DAMAGE.

  It sharpens one thing: BOTH of the chart's career-positive yogas -- the raja
  yoga and Amala -- are real and BOTH are compromised in the same direction.
  The raja yoga fires through the 8th; Amala runs through a graha that is
  uncomfortable, asleep, and possibly a functional malefic.
""")
verdict(8, 'real promise, damaged channel — delivery only through upheaval')

# =============================================================================
rule('STEP 9.  ONLY NOW — TIMING')
print("""      current       Rahu mahadasha to Dec 2040
      antardasha    Rahu–GURU to 31 Jan 2028   — the 10th-house occupant
      then          Rahu–Shani  Jan 2028 – Dec 2030
      then          Rahu–BUDHA  Dec 2030 – Jun 2033  — THE CAREER LORD ITSELF
      later         Rahu–Shukra Jul 2034 – Jul 2037  — highest Ishta in the chart

  THE PROMISE IS FIXED BY STEPS 2 TO 8.  TIMING ONLY SAYS WHEN IT IS ACTIVATED.

  AND THE SCHEDULE IS UNCOMFORTABLE IN A SPECIFIC WAY: the period that most
  directly activates the career house is RAHU-BUDHA, and Budha is the graha
  step 6 found failing its minimum.  The career lord gets its own period and
  arrives at it as the weakest body in the chart.

  Section 34 recorded that an unrelated dasha system, Yogini, hands Budha the
  same moment within eighteen days.  THAT AGREEMENT IS ABOUT WHEN, NOT ABOUT
  WHAT -- and the classical order is what keeps those two questions apart.
""")
verdict(9, 'real promise, damaged channel — delivery only through upheaval')

# =============================================================================
rule('STEP 10.  ASHTAKAVARGA AND TRANSIT, LAST')
print(f"""      SAV of the 10th ({SIGNS[HSIGN]})     {SAV[SIGNS[HSIGN]]}
      SAV of the lord's sign ({SIGNS[sign_of(POS[HLORD])]})   {SAV[SIGNS[sign_of(POS[HLORD])]]} — LOWEST IN THE CHART
      highest SAV in the chart      Kumbha {SAV['Kumbha']}

  THE CAREER HOUSE ITSELF IS WELL SUPPORTED AT {SAV[SIGNS[HSIGN]]} BINDUS.  ITS LORD SITS IN
  THE WORST-SUPPORTED SIGN HE OWNS.

  Used last and used for transits -- which is what section 29 did when it found
  Shani crossing the natal 10th on a single bindu in the 2032-2034 window --
  Ashtakavarga qualifies the timing.  IT DOES NOT AND SHOULD NOT DECIDE THE
  PROMISE.
""")
verdict(10, 'real promise, damaged channel — delivery only through upheaval')

# =============================================================================
rule('WHAT THE SEQUENCE PROVED')
print("  Running verdict, step by step:\n")
prev = None
for s, v in VERDICT:
    tag = 'SET' if prev is None else ('MOVED' if v != prev else 'unchanged')
    print(f"      after step {s:2d}   {tag:9s}  {v}")
    prev = v
after3 = sum(1 for i in range(1, len(VERDICT))
             if VERDICT[i][0] > 3 and VERDICT[i][1] != VERDICT[i-1][1])
print(f"""
  THE VERDICT WAS SET AT STEP 3 AND MOVED {after3} TIMES ACROSS THE SEVEN STEPS AFTER IT.

  THAT IS THE RESULT, AND IT CUTS BOTH WAYS.

  IN THIS READING'S FAVOUR: the conclusion is ROBUST TO METHOD ORDER.  Steps 5
  to 10 -- varga, Shadbala, Bhava Bala, yogas, dasha, Ashtakavarga -- qualified
  and dated the judgment without changing it.  The career conclusions in
  sections 22, 23, 29 and 30 survive being rebuilt in strict classical
  sequence.

  AGAINST IT: THE JUDGMENT WAS SETTLED BY STEP 3, AND THIS DOCUMENT SPENT
  THIRTY SECTIONS GETTING THERE.  The bhava is sealed and its lord is combust
  in a dusthana while carrying a raja yoga.  Everything after that is
  refinement.  A reading built in classical order would have said the essential
  thing on its first page.

  AND ONE PLACE THE ORDER WOULD GENUINELY HAVE CHANGED SOMETHING -- though not
  the place I expected when drafting.  I assumed the D10 would flatter the
  chart and that reading it early was the risk.  IT DOES NOT FLATTER: Budha and
  Guru are BOTH in enemy signs there, and the varga is harsher than the D1.

  The risk is narrower and sharper.  THE D10 CONTAINS EXACTLY ONE FLATTERING
  FACT -- SHUKRA, the Atmakaraka and highest Ishta in the chart, sitting in the
  D10's own 10th house.  Read early and on its own, that single placement will
  carry a confident career story.  Read at step 5, it arrives after the sealed
  bhava and the buried lord and can only qualify them.

  SECTION 11 READ THE D10 EARLY AND AT LENGTH.  It did not in fact overreach --
  but nothing in the document's method was stopping it.  THE SEQUENCE IS THAT
  MISSING GUARD.

  ON THE WEIGHTS: nothing to retract.  No percentage weight is assigned to any
  technique anywhere in this document -- verified by search, zero occurrences.
  The correction is sound as general method and simply does not describe this
  reading.
""")
print('=' * 92)
