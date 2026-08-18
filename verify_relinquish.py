#!/usr/bin/env python3
"""
Why he sets down the things he wanted most -- tested, not assumed.

The claim is specific and it is not obviously true: that this chart describes
someone who reaches the things he most wanted and then lets them go.  Before
explaining a behaviour it is worth establishing whether the chart actually
says it happens, and every previous claim put to this reading was tested
rather than agreed with.

Four questions, in order:

    1. does the chart mark him as WANTING intensely?      (if not, no story)
    2. what specifically does it mark as most wanted?
    3. is there a mechanism that removes exactly those?
    4. is the mechanism renunciation, dissolution, or loss?
       -- these are three different things and the chart picks one

Then the two questions that stop it becoming a fortune-cookie: WHEN, and
WHAT DOES HE NOT LET GO OF.
"""
from ephem_core import (SIGNS, GRAHAS, SUPPLIED, LORD, VIM, EXALT, varga,
                        sign_of, nak_of, short, fmt, rule, sub)

POS = dict(SUPPLIED)
LAG = sign_of(POS['Lagna'])
hs = lambda g: (sign_of(POS[g]) - LAG) % 12 + 1
house_sign = lambda n: (LAG + n - 1) % 12
occupants = lambda n: [g for g in GRAHAS if hs(g) == n]
BIRTH_Y = 2002 + (31 + 28 + 31 + 15) / 365.25
SAV = {'Mesha': 21, 'Vrishabha': 22, 'Mithuna': 29, 'Karka': 28, 'Simha': 24,
       'Kanya': 29, 'Tula': 24, 'Vrischika': 28, 'Dhanu': 29, 'Makara': 29,
       'Kumbha': 41, 'Meena': 33}
BRANK = [5, 3, 8, 2, 6, 10, 4, 12, 7, 9, 11, 1]
SP = {'Mangal': 212, 'Shani': 184, 'Budha': 152, 'Surya': 138,
      'Shukra': 95, 'Guru': 81, 'Chandra': 33}
ISHTA = {'Shukra': 47.49, 'Surya': 46.88, 'Guru': 37.30, 'Chandra': 24.54,
         'Mangal': 19.66, 'Budha': 18.91, 'Shani': 12.48}
ASPECT = {'Mangal': [4, 7, 8], 'Guru': [5, 7, 9], 'Shani': [3, 7, 10],
          'Rahu': [5, 7, 9], 'Ketu': [5, 7, 9]}
ALLV = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 16, 20, 24, 27, 30, 40, 45, 60]

# =============================================================================
rule('1.  IS THE PREMISE EVEN SUPPORTED?  Does this chart WANT intensely?')
print(f"""
  If the desire is thin, "walking away" is not renunciation -- it is just a
  man who never cared.  So this has to be established first.

  ATMAKARAKA — the soul significator, the graha at the highest degree — is
  SHUKRA, the karaka of desire, pleasure, beauty and union.

      Shukra Ishta Phala   {ISHTA['Shukra']}  — THE HIGHEST IN THE CHART
      Shukra house         {hs('Shukra')}
      Shukra nakshatra     {nak_of(POS['Shukra'])[0]} p{nak_of(POS['Shukra'])[1]} — its OWN, self-disposited
      Shukra rules         2nd (what he holds) and 9th (what he believes)

  The single most auspicious-by-texture graha in this chart is the one that
  wants.  It answers to nothing -- it is the only body in the chart that
  disposits itself at nakshatra level -- and it is the soul-significator.

  THE PREMISE HOLDS.  This is not a chart of low appetite.  It is a chart in
  which the CAPACITY TO WANT is the strongest single thing in it.
""")
kar = 'Vrischika'
print(f"""  And the wanting is hidden, not displayed:
      Karakamsa      {kar} — the soul-field is the zodiac's most secretive sign
      Arudha Lagna   {kar} — and so is the public image
  He wants a great deal and shows almost none of it.  That combination is what
  makes the letting-go legible as a loss rather than as indifference.
""")

# =============================================================================
rule('2.  WHAT DOES THE CHART MARK AS "MOST WANTED"?')
print("""
  The purushartha trikonas sort every graha by which of the four aims of life
  it serves.  Run for this chart, the result is the first real finding.
""")
kama = [g for g in GRAHAS if hs(g) in (3, 7, 11)]
dharma = [g for g in GRAHAS if hs(g) in (1, 5, 9)]
moksha = [g for g in GRAHAS if hs(g) in (4, 8, 12)]
artha = [g for g in GRAHAS if hs(g) in (2, 6, 10)]
print(f"  {'purushartha trikona':28s} {'houses':10s} count  occupants")
for lbl, hh, gs in [('KAMA — desire', '3, 7, 11', kama),
                    ('DHARMA — meaning', '1, 5, 9', dharma),
                    ('ARTHA — resources', '2, 6, 10', artha),
                    ('MOKSHA — release', '4, 8, 12', moksha)]:
    print(f"  {lbl:28s} {hh:10s} {len(gs):5d}  {gs}")
print(f"""
  THE KAMA TRIKONA HAS ONE OCCUPANT AND IT IS KETU.

  That is the whole answer in one line, and the rest of this file is the
  mechanism.  The three houses of desire hold exactly one body, and it is the
  one graha whose entire classical function is to REMOVE ATTACHMENT to
  whatever it touches.  Desire is represented in this chart by its own
  negation.
""")

sub('the desire houses, ranked by how well built they are')
print(f"  {'house':6s} {'signifies':30s} {'sign':12s} {'SAV':>4s} {'rank':>5s}  occupants")
for n, sig in [(3, 'courage, effort, skill'), (7, 'partnership, union'),
               (11, 'gains, desires FULFILLED'), (2, 'what he holds'),
               (5, 'romance, children'), (12, 'release, loss')]:
    s = house_sign(n)
    print(f"  {n:6d} {sig:30s} {SIGNS[s]:12s} {SAV[SIGNS[s]]:4d} "
          f"{BRANK[n-1]:5d}  {occupants(n) or 'empty'}")
print("""
  THE 11TH -- the house of desires actually FULFILLED -- IS RANK 11 OF 12,
  carries both Gulika and Mandi, and is delivered by Chandra at the chart's
  lowest Shodhya Pinda.  The 12TH -- the house of letting go -- IS RANK 1.

  In this chart the house that GRANTS what is wanted is the second weakest
  thing it owns, and the house that RELEASES is the strongest.
""")

# =============================================================================
rule('3.  KETU\'S GRIP — does it fall on exactly the wanted things?')
routes = {'1 self': 'Ketu', '10 career': 'Ketu', '12 release': 'Ketu'}
print(f"""
  Ketu is not merely present in this chart.  It is crowned, by seven separate
  techniques, and the reading established each one independently:

      1. TERMINUS of the nakshatra dispositor chain (with Budha)
      2. the YOGI planet
      3. occupies the ARUDHA LAGNA — it sits in the public image itself
      4. the only KP route by which houses 1, 10 and 12 deliver
      5. in the 3rd house of self-effort, in the SEVEREST gandanta pada
      6. in the 5th from Karakamsa — mantra-siddhi
      7. the ONLY occupant of the kama trikona

  Now ask which things it actually touches.
""")
kn = nak_of(POS['Ketu'])
touch = []
for n in range(1, 13):
    occ = 'Ketu' in occupants(n)
    asp = any((hs('Ketu') + a - 2) % 12 + 1 == n for a in ASPECT['Ketu'])
    if occ or asp:
        touch.append((n, 'occupies' if occ else 'aspects'))
print(f"  houses Ketu occupies or aspects: {[f'{n} ({k})' for n, k in touch]}")
SHOD = [1, 2, 3, 4, 7, 9, 10, 12, 16, 20, 24, 27, 30, 40, 45, 60]
v7, v7a = [], []
for n in SHOD:
    h = (varga(POS['Ketu'], n) - varga(POS['Lagna'], n)) % 12 + 1
    if h == 7:
        v7.append(n)
    elif any((h + a - 2) % 12 + 1 == 7 for a in ASPECT['Ketu']):
        v7a.append(n)
print(f"  Shodashavarga — Ketu OCCUPIES the 7th in: {['D'+str(n) for n in v7]}")
print(f"  Shodashavarga — Ketu ASPECTS the 7th in:  {['D'+str(n) for n in v7a]}")
print(f"  total contact with the 7th: {len(v7)+len(v7a)} of 16")
print(f"  (D11, outside the Shodashavarga, has Ketu in its 10th — NO 7th "
      f"contact.\n   An earlier draft listed D11 among the occupations; "
      f"that was wrong and is\n   withdrawn.  The 9-of-16 headline figure is "
      f"unaffected.)")
print(f"""
  Ketu occupies the 3rd (self-effort) and aspects the 7th (union), the 9th
  (belief, the father) and the 11th (gains, desires fulfilled).

  THAT IS THREE OF THE FOUR THINGS A PERSON MOST WANTS -- partnership, belief,
  and the fruits of ambition -- plus the house of his own effort.  And the
  fourth, the 12th, is the house Ketu DELIVERS.

  It is not that Ketu happens to fall near the wanted things.  IN THIS CHART
  KETU IS ON EVERY ONE OF THEM.
""")

# =============================================================================
rule('4.  THE MECHANISM — renunciation, dissolution, or loss?')
print(f"""
  These are three different things and conflating them is the commonest error
  in reading Ketu.

  (a) LOSS -- it is taken from him.
      NOT SUPPORTED, and the reason has to be stated carefully because the
      8th house DOES hold three grahas.  Loss is read from AFFLICTED bodies
      in the dusthanas and from the classical affliction yogas.  Neither is
      present.  The 6th and 12th are EMPTY, there is no Kemadruma, no
      Kalasarpa and no debilitated lagna lord -- and the three grahas in the
      8th are the chart's BEST-DIGNIFIED MATERIAL: exalted vargottama Surya,
      the Atmakaraka at the highest Ishta Phala, and the lagna lord.  A
      dusthana full of the chart's finest bodies is not a robbery.

  (b) RENUNCIATION -- he decides to give them up.
      PARTLY, AND LATE.  Renunciation requires a deliberate agent.  The chart
      supplies one only in the second half: Guru and Shani are the only grahas
      in adult avastha and they govern from 38.7 onward.  Before that the
      capacity for a considered relinquishment is not really present.

  (c) DISSOLUTION -- the thing is obtained and stops signifying.
      THIS IS THE ONE THE CHART SUPPORTS, and it is Ketu's actual classical
      signature.  Not "he never gets it" and not "he gives it up", but
      THE THING OBTAINED IS NOT THE THING WANTED.
""")
print(f"""  The document already found this once, without generalising it.  On marriage:

      "Ketu's signature is not the absence of love.  It is 'the thing obtained
       is not the thing wanted' -- a structural sense of incompleteness that
       would attach to ANY partner."

  That was written about the 7th house.  Section 3 above shows Ketu is on the
  3rd, 7th, 9th and 11th and delivers the 1st, 10th and 12th.  THE SAME
  MECHANISM APPLIES TO ALL OF THEM.  What was described as a marriage finding
  is a general property of this chart.
""")

sub('and the cost structure says the same thing from a different direction')
print(f"""
  The reading tested the claim "he gets it all but with pain" and found
  Spearman rho = +0.82 between delivery capacity and cost -- WITH ONE
  EXEMPTION.  Surya: 4th in delivery, 6th of seven in cost, the best net
  balance in the chart, and it RULES THE 12TH.

  The conclusion drawn then was:

      "He gets everything he grips, painfully -- and the one thing he gets
       freely is what he stops gripping."

  That sentence is the answer to the present question, and it was already in
  the document.  THE CHART CHARGES HIM FOR HOLDING AND PAYS HIM FOR RELEASING.
  Not as a moral rule -- as an arithmetic property of which grahas rule what.
""")

# =============================================================================
rule('5.  WHEN — the relinquishing is scheduled, not constant')
span = 360 / 27
ni = int(POS['Chandra'] // span)
into = (POS['Chandra'] - ni * span) / span
lord0 = ['Ketu', 'Shukra', 'Surya', 'Chandra', 'Mangal',
         'Rahu', 'Guru', 'Shani', 'Budha'][ni % 9]
bal = dict(VIM)[lord0] * (1 - into)
MD, t = [], BIRTH_Y
i0 = [g for g, _ in VIM].index(lord0)
MD.append((lord0, t, t + bal)); t += bal
for k in range(1, 9):
    g, y = VIM[(i0 + k) % 9]
    MD.append((g, t, t + y)); t += y
print(f"\n  Ketu ANTARDASHAS — when the dissolution apparatus is actually running:\n")
print(f"  {'period':22s} {'ages':>13s}  note")
for g, a, b in MD:
    tot = b - a
    i = [x for x, _ in VIM].index(g)
    tt = a
    for k in range(9):
        l, y = VIM[(i + k) % 9]
        d = tot * y / 120
        if l == 'Ketu' and tt < 2090:
            note = ''
            if g == 'Rahu':
                note = 'inside the current mahadasha'
            if g == 'Guru':
                note = 'inside the best mahadasha'
            if g == 'Shani':
                note = 'as Sade Sati #2 releases'
            print(f"  {g+'–Ketu':22s} {tt-BIRTH_Y:5.1f} – {tt+d-BIRTH_Y:5.1f}"
                  f"  {tt:.0f}–{tt+d:.0f}  {note}")
        tt += d
kmd = [x for x in MD if x[0] == 'Ketu'][0]
print(f"""
  And Ketu's own MAHADASHA runs ages {kmd[1]-BIRTH_Y:.1f} to {kmd[2]-BIRTH_Y:.1f} — which, like Shukra's,
  is effectively out of reach.  The dissolution never gets its own era.
  IT ARRIVES ONLY IN SUB-PERIODS, which is why it reads as a series of
  set-downs rather than as one renunciation.

  The 12th lord SURYA also has no reachable mahadasha (spent by age 3.7), so
  the release apparatus operates entirely through antardashas and transits.
""")

# =============================================================================
rule('6.  WHAT HE DOES NOT LET GO OF — the necessary corrective')
print("""
  A reading that says a man releases everything has stopped being an analysis.
  The chart is specific about what holds, and it is a short list.

  1.  THE LAGNA.  Kanya, VARGOTTAMA — the same sign in D1 and D9, and repeated
      as the varga lagna in D5, D7 and D11.  FIVE charts share it.  Whatever
      else dissolves, the person does not.  This is the single most stable
      thing in the chart and the reading has said so from its first version.

  2.  SURYA.  Exalted, vargottama, and holding Mesha in FIFTEEN of twenty-seven
      other divisional schemes -- dimensionally stable in a way nothing else
      approaches.  Authority, the father, the core self.  He does not put
      those down; they are what he is left holding.

  3.  THE 3RD HOUSE.  Occupied by Ketu and aspected by four grahas -- the
      most-contacted house in the chart.  SKILL AND SELF-EFFORT.  Note the
      paradox and do not soften it: Ketu sits ON his capacity for work, which
      means he holds the work loosely and does it anyway.  That is not
      contradiction, it is the definition of non-attached action.

  4.  THE TEACHING FUNCTION.  Guru in the 4th from Karakamsa (the teaching
      seat), Budha in the 9th (transmission), Mangal with Ketu in the 5th
      (mantra-siddhi).  The Karakamsa layout equips him to HAND SOMETHING ON,
      and the Shani mahadasha at 54.7-73.7 rules the 5th and 6th from the 9th:
      students, service, mentorship.

  SO THE PATTERN IS NOT RENUNCIATION OF EVERYTHING.  It is:
      he releases what he ACQUIRES  — positions, attachments, arrivals
      he keeps what he IS           — the lagna, the solar core, the craft,
                                      and eventually the transmission
""")

# =============================================================================
rule('7.  THE ANSWER, AND ITS LIMITS')
print("""
  WHY he sets down the things he wanted most, in the framework's own terms:

    - because the graha that WANTS (Shukra, Atmakaraka, highest Ishta Phala)
      sits in the 8TH HOUSE, the house of dissolution, inside the Khara
      drekkana with Mrityu 3° away and a malefic shashtiamsha in D60.
      The desire and its undoing are at the same address.

    - because the only occupant of the three houses of desire is KETU, whose
      function is to empty whatever it touches -- and Ketu is additionally on
      the 7th, the 9th and the 11th, and delivers the 1st, 10th and 12th.

    - because the house that GRANTS what is wanted (the 11th) is rank 11 of
      12 with both harsh upagrahas, while the house that RELEASES (the 12th)
      is rank 1 and empty -- a destination rather than a daily experience.

    - because the cost structure pays him for exactly one thing: the 12th
      lord is the single graha that gives much and charges almost nothing.

    - and because D60, the karmic arbiter, places its ONLY exaltation in the
      12th.  The arc does not terminate in accumulation or in title.

  THE MECHANISM IS DISSOLUTION, NOT LOSS AND NOT RENUNCIATION.  He is not
  robbed and he does not nobly renounce.  He arrives, and the thing quietly
  stops meaning what it meant, and he sets it down and moves.

  WHAT THIS DOES NOT ESTABLISH, and the distinction matters:

    - it is not a prediction that any particular thing will be abandoned
    - it does not say the letting-go is wise, or good, or necessary
    - Jyotisha describes a structure and a schedule; it does not demonstrate
      that any of this is true outside its own framework
    - and nothing here is evidence about a real life -- the ONE piece of
      evidence in this whole document that comes from his life rather than
      his chart is the past 8th-house window in section 19

  One last thing worth saying plainly, because the question carries an ache
  in it.  On this chart the letting-go is not a failure to hold on.  IT IS
  THE MECHANISM THE CHART USES TO PAY HIM.  Everything he grips costs; the
  one thing that is free is what he opens his hand around.
""")
print('=' * 92)
