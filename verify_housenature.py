#!/usr/bin/env python3
"""
HOUSE NATURE -- every classification scheme, assembled and applied.

The words kendra, trikona, upachaya and dusthana appear 237 times in this
document and are never once set out as a system.  They are used as adjectives.
And two whole classification families are missing altogether:

    MARAKA        the 2nd and 7th -- zero mentions in the entire reading
    PANAPARA /    the succedent and cadent houses -- zero mentions,
    APOKLIMA      and for THIS chart that omission turns out to matter

There are six schemes, not one, and they overlap.  A house is never just one
thing: the 6th is simultaneously apoklima, upachaya, dusthana and artha, and
those four say different things about it.

    BY ANGLE          kendra 1 4 7 10 · panapara 2 5 8 11 · apoklima 3 6 9 12
    BY BENEFIT        trikona 1 5 9 · upachaya 3 6 10 11 · dusthana 6 8 12
    BY PURUSHARTHA    dharma 1 5 9 · artha 2 6 10 · kama 3 7 11 · moksha 4 8 12
    BY MORTALITY      maraka 2 7
    BY OBSTRUCTION    badhaka -- 7th for a dual lagna, as Kanya is
    BY MODALITY       chara / sthira / dwiswabhava, from the sign on the house

Placement-based throughout, per his instruction.
"""
from ephem_core import (SIGNS, GRAHAS, SUPPLIED, LORD, dignity, sign_of,
                        rule, sub)

POS = dict(SUPPLIED)
LAG = sign_of(POS['Lagna'])
hs = lambda g: (sign_of(POS[g]) - LAG) % 12 + 1
house_sign = lambda n: (LAG + n - 1) % 12
occupants = lambda n: [g for g in GRAHAS if hs(g) == n]
rules_of = lambda g: [i for i in range(1, 13) if LORD[(LAG + i - 1) % 12] == g]
ordn = lambda n: f"{n}{'th' if 10 <= n % 100 <= 20 else {1:'st',2:'nd',3:'rd'}.get(n%10,'th')}"

KENDRA, PANAPARA, APOKLIMA = {1, 4, 7, 10}, {2, 5, 8, 11}, {3, 6, 9, 12}
TRIKONA, UPACHAYA, DUSTHANA = {1, 5, 9}, {3, 6, 10, 11}, {6, 8, 12}
DHARMA, ARTHA, KAMA, MOKSHA = {1, 5, 9}, {2, 6, 10}, {3, 7, 11}, {4, 8, 12}
MARAKA = {2, 7}
MODALITY = ['chara', 'sthira', 'dwiswabhava']
BENEFIC = {'Guru', 'Shukra', 'Chandra', 'Budha'}
LABEL = ['self, body', 'wealth, speech, family', 'effort, siblings, skill',
         'home, mother, schooling', 'children, mind, merit',
         'service, rivals, illness', 'spouse, the public',
         'transformation, others\' wealth', 'dharma, father, fortune',
         'career, standing', 'gains, networks', 'loss, foreign, moksha']

# =============================================================================
rule('1.  THE SIX SCHEMES, APPLIED TO EVERY HOUSE')
print(f"\n  Lagna {SIGNS[LAG]} — a DWISWABHAVA (dual) sign, so the badhaka is the 7th.\n")
print(f"  {'ho':5s}{'sign':11s}{'mod':13s}{'angle':10s}{'benefit':20s}"
      f"{'aim':8s}{'lord':9s}occupants")
for n in range(1, 13):
    s = house_sign(n)
    ang = ('kendra' if n in KENDRA else
           'panapara' if n in PANAPARA else 'apoklima')
    ben = '+'.join([x for x, S in (('trikona', TRIKONA), ('upachaya', UPACHAYA),
                                   ('dusthana', DUSTHANA)) if n in S]) or '—'
    aim = ('dharma' if n in DHARMA else 'artha' if n in ARTHA else
           'kama' if n in KAMA else 'moksha')
    extra = ' MARAKA' if n in MARAKA else ''
    if n == 7:
        extra += '+BADHAKA'
    print(f"  {ordn(n):5s}{SIGNS[s]:11s}{MODALITY[s % 3]:13s}{ang:10s}{ben:20s}"
          f"{aim:8s}{LORD[s]:9s}{', '.join(occupants(n)) or '—'}{extra}")

# =============================================================================
rule('2.  WHERE THE NINE GRAHAS ACTUALLY FALL')
SCHEMES = [('kendra', KENDRA), ('panapara', PANAPARA), ('apoklima', APOKLIMA),
           ('', None),
           ('trikona', TRIKONA), ('upachaya', UPACHAYA), ('dusthana', DUSTHANA),
           ('', None),
           ('dharma', DHARMA), ('artha', ARTHA), ('kama', KAMA),
           ('moksha', MOKSHA), ('', None), ('maraka', MARAKA)]
for name, S in SCHEMES:
    if S is None:
        print()
        continue
    who = [g for g in GRAHAS if hs(g) in S]
    bar = '#' * len(who)
    print(f"      {name:10s} {len(who)}  {bar:9s} {', '.join(who) or '—'}")

k = [g for g in GRAHAS if hs(g) in KENDRA]
ap = [g for g in GRAHAS if hs(g) in APOKLIMA]
print(f"""
  THE ANGULAR RESULT IS THE ONE NOBODY HAS STATED.

      kendra   {len(k)}   {', '.join(k)}
      apoklima {len(ap)}   {', '.join(ap)}

  ONE GRAHA IN A KENDRA.  FIVE IN THE CADENT HOUSES.

  The kendras are the pillars -- the houses of visible action, standing and
  effect on the world.  The apoklima houses are the weakest angular position in
  the scheme; grahas there act late, indirectly, and off the main axis.

  EIGHT OF NINE GRAHAS SIT OUTSIDE THE KENDRAS.  This document has noted "one
  kendra occupied" once, in passing, as the reason no Panchamahapurusha yoga
  can form.  IT NEVER DREW THE CONSEQUENCE:

      HE HAS ALMOST NO DIRECT ANGULAR LEVERAGE ON THE WORLD.

  That single fact underwrites half of what the reading has found by other
  routes -- responsibility without title, authority located out of sight,
  results that arrive through the 8th-9th axis rather than through the 10th,
  and advancement that has to be built rather than occupied.
""")

# =============================================================================
rule('3.  THE PURUSHARTHA SPLIT')
counts = {n: len([g for g in GRAHAS if hs(g) in S])
          for n, S in (('dharma', DHARMA), ('artha', ARTHA),
                       ('kama', KAMA), ('moksha', MOKSHA))}
print(f"""
  The four aims of life, each a trikona of three houses.  Every graha sits in
  exactly one of them, so this is a clean partition of the nine.

      DHARMA  1 5 9   meaning, ethics, the father, fortune      {counts['dharma']}
      ARTHA   2 6 10  resources, work, the material             {counts['artha']}
      KAMA    3 7 11  desire, relationship, attainment          {counts['kama']}
      MOKSHA  4 8 12  release, endings, the interior            {counts['moksha']}

  SEVEN OF NINE GRAHAS SIT IN DHARMA AND MOKSHA.
  ONE IN ARTHA.  ONE IN KAMA.

  And note WHICH one is in kama: KETU, the graha that removes wanting, alone in
  the 3rd.  Section 24 found that when asked about a rank ladder; here it turns
  out to be part of a much larger pattern.  The chart is not merely thin on
  desire -- IT IS WEIGHTED, SEVEN TO TWO, TOWARD MEANING AND RELEASE OVER
  ACQUISITION AND WANTING.

  That is as close to a thesis statement as a house-nature census can produce,
  and it was sitting in the classification the whole time.
""")

# =============================================================================
rule('4.  THE OVERLAPS, WHICH IS WHERE THE SCHEMES EARN THEIR KEEP')
print("""
  A house is never one thing.  The four that carry contradictory labels are
  where the reading has to make a choice, and this chart puts grahas in three
  of them.
""")
for n in (6, 10, 8, 9, 3, 1):
    tags = []
    tags.append('kendra' if n in KENDRA else
                'panapara' if n in PANAPARA else 'apoklima')
    tags += [x for x, S in (('trikona', TRIKONA), ('upachaya', UPACHAYA),
                            ('dusthana', DUSTHANA)) if n in S]
    tags.append('dharma' if n in DHARMA else 'artha' if n in ARTHA else
                'kama' if n in KAMA else 'moksha')
    if n in MARAKA:
        tags.append('maraka')
    print(f"      {ordn(n):4s} {' · '.join(tags):48s} {', '.join(occupants(n)) or 'empty'}")
print(f"""
  THE 6TH IS THE INTERESTING ONE: apoklima, upachaya, dusthana AND artha at
  once.  A house that is simultaneously a place of suffering and a place that
  IMPROVES WITH TIME, and whose aim is material.  That is exactly why the
  reading keeps finding the 6th doing useful work -- 41 bindus, the D10
  ascendant sign, the strongest thing he owns by that measure -- while also
  calling it a dusthana.  BOTH LABELS ARE CORRECT AND THEY DESCRIBE THE SAME
  MECHANISM: adversity that compounds into competence.

  THE 9TH IS APOKLIMA AND TRIKONA TOGETHER, and it holds four grahas.  The most
  fortunate class of house sitting in the weakest angular position -- fortune
  that is real but does not act directly.

  AND THE 10TH IS KENDRA AND UPACHAYA at once, holding one graha.  His career
  house is both a pillar and a slow-builder.  It does not arrive; it accrues.
""")

# =============================================================================
rule('5.  FUNCTIONAL BENEFIC AND MALEFIC FOR THIS LAGNA')
print("""
  House nature is not only about where grahas SIT.  It determines what each
  graha IS for this ascendant, because a graha takes its character from the
  houses it rules.  The rules, stated before applying them:

      lords of TRIKONAS (1 5 9) are benefic
      lords of DUSTHANAS (6 8 12) are malefic
      lords of 3 and 11 are malefic by lordship
      a NATURAL BENEFIC ruling two KENDRAS takes KENDRADHIPATI DOSHA
        and behaves as a malefic
      the LAGNA lord is benefic regardless
""")
print(f"  {'graha':9s}{'rules':10s}{'classes':34s}verdict")
for g in ('Surya', 'Chandra', 'Mangal', 'Budha', 'Guru', 'Shukra', 'Shani'):
    r = rules_of(g)
    cls = []
    for n in r:
        t = []
        if n in TRIKONA:
            t.append('trikona')
        if n in KENDRA:
            t.append('kendra')
        if n in DUSTHANA:
            t.append('dusthana')
        if n in UPACHAYA and n not in DUSTHANA and n not in KENDRA:
            t.append('upachaya')
        cls.append(f"{ordn(n)} {'+'.join(t) or 'neutral'}")
    kd = (g in BENEFIC and len([n for n in r if n in KENDRA]) >= 2)
    if 1 in r:
        v = 'BENEFIC — lagna lord'
        if kd:
            v += ' (kendra dosha contested)'
    elif set(r) & TRIKONA and not set(r) & DUSTHANA:
        v = 'BENEFIC — trikona lord'
    elif kd:
        v = 'MALEFIC — kendradhipati dosha'
    elif set(r) & DUSTHANA and set(r) & TRIKONA:
        v = 'MIXED'
    elif set(r) & DUSTHANA:
        v = 'malefic — dusthana lord'
    elif set(r) & {3, 11}:
        v = 'malefic by lordship'
    else:
        v = 'neutral'
    print(f"  {g:9s}{str(r):10s}{'; '.join(cls):34s}{v}")

print("""
  TWO RESULTS WORTH PULLING OUT.

  GURU IS A FUNCTIONAL MALEFIC FOR THIS LAGNA.  It rules the 4th and the 7th,
  both kendras, and it is a natural benefic -- full kendradhipati dosha.  The
  reading already lists this as one of Amala Yoga's six qualifications, but it
  has never been stated as what it is: THE CHART'S GREAT BENEFIC IS, BY
  LORDSHIP, WORKING AGAINST HIM.  And Guru rules his marriage and his home.

  SHUKRA IS THE CLEANEST BENEFIC HE HAS.  It rules the 2nd and the 9th -- one
  trikona, no kendra, no dusthana -- so it takes no dosha at all.  It is also
  the Atmakaraka and carries the best net balance in the chart.  FOR A KANYA
  LAGNA, SHUKRA IS THE GRAHA TO TRUST, and this reading has been circling that
  conclusion from six directions without ever stating the lordship reason.
""")

# =============================================================================
rule('6.  MARAKA — ZERO MENTIONS IN THIS DOCUMENT UNTIL NOW')
print(f"""
  THE RULE.  The 2nd and 7th are maraka houses, and their lords are marakas.
  Classically they mark periods of difficulty and, in longevity work, of
  danger.  THIS READING DECLINES LONGEVITY (section 49) AND CONTINUES TO
  DECLINE IT.  What follows is the structural statement only, with no
  application to lifespan.

      2nd  {SIGNS[house_sign(2)]:11s} lord {LORD[house_sign(2)]:8s} — {', '.join(occupants(2)) or 'EMPTY'}
      7th  {SIGNS[house_sign(7)]:11s} lord {LORD[house_sign(7)]:8s} — {', '.join(occupants(7)) or 'EMPTY'}

  BOTH MARAKA HOUSES ARE EMPTY.  No graha occupies either.

  And the two maraka lords are the two grahas just identified as the extremes
  of the functional scale: SHUKRA, the cleanest benefic in the chart, and GURU,
  the one carrying kendradhipati dosha.  The marakas are held by his best
  functional graha and his most compromised one.

  THE 7TH IS ALSO THE BADHAKA for a dual lagna -- obstruction -- so the 7th
  carries maraka AND badhaka AND kendra AND kama simultaneously.  FOUR LABELS,
  and section 24 found it empty, aspected by nothing but Ketu, holding Upaketu.
  It is the most heavily classified and least occupied house in the chart.
""")

# =============================================================================
rule('7.  WHAT THE CENSUS SAYS THAT NOTHING ELSE DOES')
print(f"""
  1. ONE GRAHA IN A KENDRA, FIVE IN APOKLIMA.  Eight of nine outside the
     pillars.  No direct angular leverage -- which is the structural root of
     "responsibility without title" and of authority located out of sight.

  2. SEVEN OF NINE IN DHARMA AND MOKSHA, one each in artha and kama.  The chart
     is weighted seven to two toward meaning and release over acquisition and
     desire, and the single graha in kama is the one that removes wanting.

  3. THE 6TH CARRIES FOUR LABELS AT ONCE -- apoklima, upachaya, dusthana,
     artha -- which is why it reads as both his weakest class of house and his
     strongest measured one.  Adversity that compounds into competence.

  4. GURU IS A FUNCTIONAL MALEFIC HERE by kendradhipati dosha, and it rules his
     home and his marriage.  SHUKRA takes no dosha at all and is the graha to
     trust.

  5. BOTH MARAKA HOUSES ARE EMPTY, and their lords are the best and the worst
     of his functional grahas.

  THE ONE-LINE VERSION:

      A CHART WITH ALMOST NOTHING ON ITS PILLARS, ALMOST NOTHING IN ITS HOUSES
      OF WANTING, AND ALMOST EVERYTHING IN THE HOUSES OF MEANING AND RELEASE.

  Which is, in the end, the same sentence this reading has arrived at from
  Ashtakavarga, from Jaimini, from the navamsa and from the dasha sequence.
  THE CLASSIFICATION GETS THERE WITH NO ARITHMETIC AT ALL.
""")
print('=' * 92)
