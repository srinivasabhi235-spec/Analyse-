#!/usr/bin/env python3
"""
The second pass of un-asked questions.

verify_unasked.py covered twelve areas the questioning never reached: the
father, the mother, the siblings, speech, the 6th, property, foreign
residence, spiritual practice, the 12th, the blind spots, remedy and
longevity.

Eight more remain, and each is loud in this chart:

    1. does the marriage LAST?           -- the Upapada apparatus, unread
    2. fame                              -- D5 is computed and was never read
    3. accident and surgery              -- Mangal dominates D30's portions
    4. escape and addiction              -- the strongest bhava is the 12th
    5. WHICH illnesses, and where        -- Kalapurusha body mapping
    6. employed or self-employed         -- 10th against 7th, and D10
    7. purva punya, the inherited credit -- the 5th, D60, Karakamsa
    8. how many children                 -- D7 read properly

These are computed on the same apparatus as the rest of the suite.  Two of
them are areas where Jyotisha's own methods are least reliable, and that is
stated where it applies rather than at the end.
"""
from ephem_core import (SIGNS, GRAHAS, SUPPLIED, LORD, EXALT, varga, sign_of,
                        short, fmt, nak_of, rule, sub)

POS = dict(SUPPLIED)
LAG = sign_of(POS['Lagna'])
hs = lambda g: (sign_of(POS[g]) - LAG) % 12 + 1
house_sign = lambda n: (LAG + n - 1) % 12
occupants = lambda n: [g for g in GRAHAS if hs(g) == n]
SAV = {'Mesha': 21, 'Vrishabha': 22, 'Mithuna': 29, 'Karka': 28, 'Simha': 24,
       'Kanya': 29, 'Tula': 24, 'Vrischika': 28, 'Dhanu': 29, 'Makara': 29,
       'Kumbha': 41, 'Meena': 33}
BRANK = [5, 3, 8, 2, 6, 10, 4, 12, 7, 9, 11, 1]
SP = {'Mangal': 212, 'Shani': 184, 'Budha': 152, 'Surya': 138,
      'Shukra': 95, 'Guru': 81, 'Chandra': 33}
ASPECT = {'Mangal': [4, 7, 8], 'Guru': [5, 7, 9], 'Shani': [3, 7, 10],
          'Rahu': [5, 7, 9], 'Ketu': [5, 7, 9]}
UPAG = {'Yama Ghantaka': 10, 'Mrityu': 8, 'Parivesha': 9, 'Ardha Prahara': 9,
        'Gulika': 11, 'Mandi': 11, 'Kala': 1, 'Dhuma': 12, 'Vyatipata': 3,
        'Indra Chapa': 6, 'Upaketu': 7}


def aspects_house(n):
    out = []
    for g in GRAHAS:
        for a in ASPECT.get(g, [7]):
            if (hs(g) + a - 2) % 12 + 1 == n:
                out.append(g)
                break
    return out


def upagrahas_in(n):
    return [u for u, h in UPAG.items() if h == n]


def dossier(n, label):
    s = house_sign(n)
    lord = LORD[s]
    print(f"\n  {label}  —  house {n}, {SIGNS[s]}")
    print(f"    lord {lord} in house {hs(lord)}   |   "
          f"delivered by {nak_of(POS[lord])[2]}")
    print(f"    occupants {occupants(n) or 'empty'}   aspects {aspects_house(n) or 'NONE'}")
    print(f"    upagrahas {upagrahas_in(n) or 'none'}")
    print(f"    SAV {SAV[SIGNS[s]]}   Bhava rank {BRANK[n-1]} of 12")
    return s, lord


# =============================================================================
rule('1.  DOES THE MARRIAGE LAST?  — the Upapada apparatus, never read')
UL = 8                                    # Dhanu, the 4th house
ul_house = (UL - LAG) % 12 + 1
print(f"""
  The Upapada Lagna is {SIGNS[UL]} -- his {ul_house}th house.  The tradition reads the
  marriage's DURABILITY from two derived houses, and neither was ever opened.
""")
second_ul = (UL + 1) % 12
eighth_ul = (UL + 7) % 12
twelfth_ul = (UL + 11) % 12
for lbl, sgn in [('2nd from UL — what SUSTAINS the marriage', second_ul),
                 ('8th from UL — its longevity and its end', eighth_ul),
                 ('12th from UL — its losses', twelfth_ul)]:
    h = (sgn - LAG) % 12 + 1
    print(f"\n  {lbl}")
    print(f"    {SIGNS[sgn]} = his {h}{'th' if h not in (1,2,3) else ['st','nd','rd'][h-1]} house, lord {LORD[sgn]} in house {hs(LORD[sgn])}")
    print(f"    occupants {occupants(h) or 'empty'}   upagrahas {upagrahas_in(h) or 'none'}")
    print(f"    SAV {SAV[SIGNS[sgn]]}   Bhava rank {BRANK[h-1]} of 12")

print(f"""
  READING, and the caution comes first.  Upapada analysis is among the LEAST
  reliable parts of the apparatus: it is Jaimini rather than Parashari, the
  schools disagree on how to compute the Upapada at all, and every statement
  here derives from HIS chart with none of hers.  Nothing below should be
  read as a prediction about a real marriage.

  What the technique says on its own terms:

    - The 2ND FROM UPAPADA is Makara under Shani, empty, Bhava rank 6, SAV 29.
      Shani sustaining a marriage is the most CONSERVATIVE signature in the
      zodiac: duty, endurance, slow deepening, and no effusiveness.  Empty
      with a strong lord elsewhere means it holds without being demonstrative.
      This is a DURABILITY signature, not a fragility one.

    - The 8TH FROM UPAPADA is Karka -- his 11th house.  Bhava rank 11 of 12,
      and it carries BOTH Gulika and Mandi.  Read plainly, the house governing
      the marriage's endings is the weakest and most shadowed in the chart.

    - But note WHICH weakness.  A weak 8th-from-UL is classically read the
      Vipreeta way: the house that would END the marriage is itself too weak
      to act.  The same configuration that makes his peer circle thin is what
      makes the marriage hard to break.

  THE COMPOSITE.  Sustained by Saturn, and its dissolution-house is the
  feeblest thing in the chart.  Both point the same way: THIS IS A DURABLE
  MARRIAGE THAT WILL NOT FEEL EFFUSIVE.  It matches, from a completely
  independent apparatus, what the satisfaction analysis already found -- that
  neither of them will describe it as effusive and both will still be in it.
""")

# =============================================================================
rule('2.  FAME — D5 Panchamamsha was computed and never read')
d5 = {g: varga(POS[g], 5) for g in ['Lagna'] + GRAHAS}
lag5 = d5['Lagna']
print(f"\n  D5 lagna {SIGNS[lag5]}   (D5 governs fame, power and renown)\n")
print(f"  {'body':9s} {'sign':12s} {'house':6s} dignity")
for g in GRAHAS:
    h = (d5[g] - lag5) % 12 + 1
    dg = ('exalted' if EXALT.get(g) == d5[g] else
          'debilitated' if EXALT.get(g) == (d5[g] + 6) % 12 else
          'own' if LORD[d5[g]] == g else '')
    print(f"  {g:9s} {SIGNS[d5[g]]:12s} {h:^6d} {dg}")
k5 = [g for g in GRAHAS if (d5[g] - lag5) % 12 + 1 in (1, 4, 7, 10)]
t5 = [g for g in GRAHAS if (d5[g] - lag5) % 12 + 1 in (1, 5, 9)]
print(f"""
  kendras of D5 occupied by: {k5 or 'none'}
  trikonas of D5 occupied by: {t5 or 'none'}

  READING.  D5's lagna is {SIGNS[lag5]} -- the SAME sign as the birth ascendant,
  a fifth chart repeating Kanya.  Fame, where it comes, comes as himself
  rather than as a persona.

  But look at what occupies it.  The kendras and trikonas of the fame chart
  are thinly held, and the reading's whole finding about the 10th, the empty
  kendras and the absent Panchamahapurusha repeats here at the level of
  renown: THERE IS NO MECHANISM FOR BEING KNOWN WITHOUT BEING USEFUL FIRST.
""")

# =============================================================================
rule('3.  ACCIDENT AND SURGERY — Mangal owns D30, and that names the risk')
print("""
  D30 is the adversity chart and ALL FIVE of its portions belong to malefics.
  Which malefic dominates names the KIND of adversity.  Computed in
  verify_deepvarga.py: MANGAL takes 4 of 10 portions, more than any other.

  Mangal-flavoured adversity is specific and it is not vague misfortune:
      cuts, burns, inflammation, fever, blood, accidents, surgery, conflict.
""")
m = 'Mangal'
print(f"  Mangal: house {hs(m)}, rules the {[i for i in range(1,13) if LORD[house_sign(i)]==m]}")
print(f"          Shodhya Pinda {SP[m]} — HIGHEST in the chart")
print(f"          aspects houses {[(hs(m)+a-2)%12+1 for a in ASPECT[m]]}")
print(f"  8th house occupants {occupants(8)}   Mrityu upagraha in house {UPAG['Mrityu']}")
print(f"""
  READING.  Mangal is the 8th lord AND the 3rd lord, has the highest delivery
  capacity in the chart, and dominates the adversity varga's portions.  It
  aspects the 3rd, 4th and 12th.

  The honest statement is about TEXTURE, not prediction: where this chart
  produces physical trouble, it will be ACUTE AND MARTIAL rather than slow --
  something cut, burned, broken or operated on, rather than something that
  creeps.  That sits alongside, not against, the chronic low-grade picture the
  6th house gives, because the two houses describe different mechanisms.

  Set against it: D27, the vitality varga, carries ZERO dusthana occupancy and
  its 8th is empty; D30 places Surya EXALTED in its 6th, the best possible
  placement for overcoming disease; and Guru aspects the natal 6th.  The chart
  has real protection on exactly this axis.
""")

# =============================================================================
rule('4.  ESCAPE AND ADDICTION — the strongest bhava is the 12th')
s12, l12 = dossier(12, 'The 12th — loss, foreign lands, seclusion, escape')
print(f"""
  The classical addiction signature is a strong or afflicted 12th tied to
  Shukra, Rahu or Chandra.  This chart has an unusually strong 12th -- rank 1
  of 12 -- and the reading has consistently read it as MOKSHA.  It is worth
  asking directly whether it could express as escape instead.

  What argues AGAINST an addictive expression:
    - the 12th is EMPTY.  Nothing is acting there.
    - its lord Surya is exalted, vargottama, best net balance in the chart,
      and the cheapest effective graha.  A 12th ruled by the strongest and
      most disciplined body does not express as dissipation.
    - no graha occupies the 6th or the 12th at all.
    - Shani and Guru are the only grahas in adult avastha -- the restraining
      pair -- and both govern the second half of life.

  What argues FOR watching it:
    - SHUKRA, the graha of pleasure, sits in the 8th in the Khara drekkana
      with Mrityu 3° away, and its D60 shashtiamsha is KARALADAMSHTRA, one of
      the harshest of the sixty.
    - RAHU runs the mahadasha to 2040 from Marana Karaka Sthana.
    - Chandra's Shodhya Pinda is 33, the lowest -- thin emotional reserves are
      the standard substrate for self-medication.

  THE COMPOSITE.  The equipment for escape exists and the STRUCTURE does not
  support it: the escape house is empty and its lord is the most disciplined
  body in the chart.  The realistic risk is not substance but WITHDRAWAL --
  the 12th expressing as seclusion and self-removal, which every other section
  of this reading has already found under a kinder name.
""")

# =============================================================================
rule('5.  WHICH ILLNESSES, AND WHERE — Kalapurusha body mapping')
BODY = ['head, brain', 'face, throat, eyes', 'shoulders, arms, lungs',
        'chest, heart, stomach', 'heart, spine, upper abdomen',
        'intestines, digestion', 'kidneys, lower back',
        'genitals, excretory, colon', 'hips, thighs, liver',
        'knees, bones, joints', 'calves, ankles, circulation', 'feet, lymph']
print(f"\n  {'sign':12s} {'body part':28s} {'house':6s} occupants")
for s in range(12):
    h = (s - LAG) % 12 + 1
    occ = occupants(h)
    mal = [g for g in occ if g in ('Surya', 'Mangal', 'Shani', 'Rahu', 'Ketu')]
    tag = '  << malefic' if mal else ''
    print(f"  {SIGNS[s]:12s} {BODY[s]:28s} {h:^6d} {occ or '—'}{tag}")
print(f"""
  The loaded signs are MESHA (head) with Surya, Budha and Shukra, and
  VRISHABHA (face, throat, eyes) with Chandra, Mangal, Shani and Rahu.

  READING.  Seven of nine grahas fall in the head-and-throat band of the
  Kalapurusha.  Combined with a Kanya lagna (intestines, digestion), a failing
  lagna lord, a thin Moon, and Mangal dominating the adversity varga, the
  areas the chart repeatedly points at are:

      the head        -- Mesha holds three grahas including the gandanta Sun
      throat and eyes -- Vrishabha holds four, including Shani and Rahu
      digestion       -- the Kanya lagna itself
      the nerves      -- Budha failing, Chandra thin, Kumbha 6th under Shani

  Shani ruling the 6th in Kumbha adds the classical chronic signature:
  cold, dry, slow, nervous, circulatory.  NOTHING HERE IS A DIAGNOSIS.  It is
  a statement about where this chart concentrates its attention.
""")

# =============================================================================
rule('6.  EMPLOYED OR SELF-EMPLOYED?')
d10 = {g: varga(POS[g], 10) for g in ['Lagna'] + GRAHAS}
lag10 = d10['Lagna']
tenth = house_sign(10)
seventh = house_sign(7)
print(f"""
  The classical discriminators:
      10th house and lord    service, employment, position under others
      7th house              business, trade, dealing with the public
      D10 lagna lord         the governing mode of the career itself
      6th house              service (the Sanskrit 'seva' sense)

  10th: {SIGNS[tenth]}, lord {LORD[tenth]} in house {hs(LORD[tenth])}, occupied by {occupants(10)}
  7th:  {SIGNS[seventh]}, lord {LORD[seventh]} in house {hs(LORD[seventh])}, occupied by {occupants(7) or 'empty'}
  D10 lagna {SIGNS[lag10]}, lord {LORD[lag10]}
  6th:  {SIGNS[house_sign(6)]}, SAV {SAV[SIGNS[house_sign(6)]]} — the chart's highest
""")
print(f"""
  READING.  The 7th of business is EMPTY, aspected only by Ketu, with Upaketu
  inside it -- the chart's weakest signature for independent trade.  The 6th
  of service carries the HIGHEST bindu count in the chart.  The D10 lagna is
  Kumbha under Shani: large impersonal structures, systems, institutions.

  This chart is built for EMPLOYMENT OR INSTITUTIONAL WORK, not for
  proprietorship.  But note the qualification the rest of the reading forces:
  the 10th lord is the chart's only failing graha and ranks fourth as a career
  agent, so "employed" here does not mean comfortable.  It means his leverage
  is his FUNCTION inside a structure rather than his ownership of one.

  The nearest thing to independence the chart supports is the specialist who
  is indispensable within an institution -- which is exactly the "authority of
  the expert rather than of the office" finding, arriving from a different
  door.
""")

# =============================================================================
rule('7.  PURVA PUNYA — the inherited credit')
s5, l5 = dossier(5, 'The 5th — purva punya, the merit carried in')
d60_5 = varga(POS['Lagna'], 60)
print(f"""
  The 5th is the house of purva punya -- what the tradition holds was earned
  before this life and is available without being worked for.

  It is Makara under Shani: empty, Bhava rank 6, SAV 29, aspected by Rahu
  alone, delivered by Chandra at Shodhya Pinda 33 -- the chart's thinnest
  channel.

  READING, and it is consistent to the point of bluntness.  There is no large
  inherited credit in this chart.  The house of earned-in-advance merit is
  middling, empty, ruled by the graha of labour, and paid out through the
  weakest deliverer it owns.  Set that against the D60 -- Parashara's karmic
  arbiter -- placing its only exaltation in the 12th, and the Karakamsa
  equipping him to TRANSMIT rather than to receive.

  THE CHART DESCRIBES SOMEONE PAYING IN RATHER THAN DRAWING DOWN.  That is
  the same conclusion the purpose analysis reached from the purushartha
  tally, and it arrives here from an unrelated technique.
""")

# =============================================================================
rule('8.  HOW MANY CHILDREN — D7 read properly')
d7 = {g: varga(POS[g], 7) for g in ['Lagna'] + GRAHAS}
lag7 = d7['Lagna']
print(f"\n  D7 lagna {SIGNS[lag7]}\n")
print(f"  {'body':9s} {'sign':12s} {'house':6s} dignity")
for g in GRAHAS:
    h = (d7[g] - lag7) % 12 + 1
    dg = ('exalted' if EXALT.get(g) == d7[g] else
          'debilitated' if EXALT.get(g) == (d7[g] + 6) % 12 else
          'own' if LORD[d7[g]] == g else '')
    print(f"  {g:9s} {SIGNS[d7[g]]:12s} {h:^6d} {dg}")
print(f"""
  Counting rules for progeny are the single most over-claimed area of
  Jyotisha.  The classical methods -- counting from the 5th lord, from Guru,
  from the D7 lagna -- routinely disagree with each other by several children,
  and no serious practitioner treats the number as reliable.  THIS SCRIPT
  DOES NOT PRODUCE A NUMBER.

  What the apparatus does support, and it is consistent across every method:

    - Guru in the D7 LAGNA is the saptamsha's best protective placement
    - Budha own-sign in D7's 10th, Surya exalted in D7's 8th
    - against that: Chandra DEBILITATED with Ketu in D7's 3rd, and Shukra
      DEBILITATED in the D7 lagna itself
    - the natal 5th is empty, its lord in the 9th, aspected only by Rahu
    - the 5th DELIVERS through Chandra, Shodhya Pinda 33 — lowest in the chart
    - Beeja Sphuta at 9°53′ Karka: even rashi in even navamsha, the textbook
      delay marker

  DELAY AND EFFORT, NOT DENIAL -- with genuine protection once it happens.
  A small family rather than a large one is the direction everything points,
  and that is as precise as the technique honestly goes.
""")
print('=' * 92)
