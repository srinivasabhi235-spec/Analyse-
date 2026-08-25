#!/usr/bin/env python3
"""
GURU THROUGH ASHLESHA — AND THE CLAIM THAT IT BRINGS FEARS INTO DREAMS.

The question: does Jupiter transiting Ashlesha bring up deepest fears or
traumas in dreams?

THIS IS A TRANSIT QUESTION, AND THE SEQUENCE THIS READING NOW FOLLOWS PUTS
TRANSIT AT STEP 10 -- last, and as a MODIFIER.  A transit cannot originate a
promise; it can only act on what the natal chart already holds.  So the honest
shape of the answer is:

    1  is the premise true?  (dates, computed)
    2  what does the transit actually touch?
    3  what does the NATAL chart hold for dreams and fear -- steps 1 to 8,
       done properly, for the houses that own this subject
    4  does gochara call this transit favourable or not?
    5  and does the classical method support the claim at all?

Step 3 is the part that decides it, and it is not where the question pointed.
"""
import swisseph as swe
from ephem_core import (SIGNS, GRAHAS, SUPPLIED, LORD, jd_ut, nak_of,
                        sign_of, dignity, rule, sub)

swe.set_sid_mode(swe.SIDM_LAHIRI)
F = swe.FLG_SWIEPH | swe.FLG_SIDEREAL | swe.FLG_SPEED
POS = dict(SUPPLIED)
LAG = sign_of(POS['Lagna'])
NOW = jd_ut(2026, 8, 25, 12, 0, 0, 5.5)
MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
       'Nov', 'Dec']
hs = lambda g: (sign_of(POS[g]) - LAG) % 12 + 1
hsign = lambda si: (si - LAG) % 12 + 1
ordn = lambda n: f"{n}{'th' if 10 <= n % 100 <= 20 else {1:'st',2:'nd',3:'rd'}.get(n%10,'th')}"
occ = lambda si: [g for g in GRAHAS if sign_of(POS[g]) == si]
# Guru's own Bhinnashtakavarga, from the supplied table
GURU_BAV = {'Mesha': 4, 'Vrishabha': 5, 'Mithuna': 5, 'Karka': 5, 'Simha': 4,
            'Kanya': 6, 'Tula': 3, 'Vrischika': 3, 'Dhanu': 6, 'Makara': 6,
            'Kumbha': 5, 'Meena': 4}
SAV = {'Mesha': 21, 'Vrishabha': 22, 'Mithuna': 29, 'Karka': 28, 'Simha': 24,
       'Kanya': 29, 'Tula': 24, 'Vrischika': 28, 'Dhanu': 29, 'Makara': 29,
       'Kumbha': 41, 'Meena': 33}


def show(j):
    y, m, d, _ = swe.revjul(j + 5.5 / 24)
    return f"{int(d)} {MON[m-1]} {y}"


def jup(j):
    return swe.calc_ut(j, swe.JUPITER, F)[0][0]


# =============================================================================
rule('1.  THE PREMISE — TRUE, AND FIVE DAYS OLD')
l, _ = swe.calc_ut(NOW, swe.JUPITER, F)
nk = nak_of(l[0])
print(f"""
      transit Guru   {l[0]:.4f}  =  {SIGNS[sign_of(l[0])]} {l[0]%30:.2f}
      nakshatra      {nk[0]} pada {nk[1]}, lord {nk[2]}
      motion         {l[3]:+.4f} deg/day (direct)
      the sign Karka is his {ordn(hsign(sign_of(l[0])))} HOUSE
""")
lo, hi = 106.6667, 120.0
prev, j, evts = None, jd_ut(2025, 1, 1, 0, 0, 0, 5.5), []
while j < jd_ut(2028, 6, 1, 0, 0, 0, 5.5):
    cur = lo <= jup(j) < hi
    if prev is not None and cur != prev:
        evts.append(('enters' if cur else 'leaves', j))
    prev = cur
    j += 1.0
print("      THE PASSAGE, computed with the retrograde loop included:\n")
for what, j in evts:
    print(f"        {what} Ashlesha   {show(j)}")
print(f"""
  TWO PASSES, NOT ONE.  Guru entered Ashlesha on 20 August 2026 -- FIVE DAYS
  BEFORE THIS QUESTION WAS ASKED -- and left it FORWARD on 1 November 2026.  It
  then turned retrograde, came BACK into Ashlesha on 26 January 2027, and
  finally cleared it on 27 June 2027.

  ABOUT TEN MONTHS OF OCCUPANCY SPLIT ACROSS TWO WINDOWS, WITH THE SECOND ONE
  ENTERED BACKWARDS.  Anyone quoting a single continuous span for this transit
  is quoting it wrong.
""")

# =============================================================================
rule('2.  WHAT ASHLESHA IS IN THIS CHART')
print(f"""
      Ashlesha spans     106 40' to 120 00'  =  Karka 16 40' to 30 00'
      nakshatra lord     BUDHA
      sign               Karka, his {ordn(hsign(3))} house -- gains, income, networks
      natal occupants of Karka    {', '.join(occ(3)) or 'EMPTY'}
      anything natal in Ashlesha? {[g for g in GRAHAS if lo <= POS[g] < hi] or 'NOTHING'}

  TWO FACTS MATTER AND THE SECOND IS THE SHARPER ONE.

  FIRST, THE NAKSHATRA LORD IS BUDHA -- and Budha in this chart is the lord of
  the 1st AND the 10th, combust at 9 degrees in the 8th house, and the only
  graha that fails its Shadbala minimum.  A transit through Budha's asterism
  routes through the weakest body he owns.

  SECOND, AND THIS IS THE ONE NOBODY MENTIONS: ASHLESHA ENDS AT 120 DEGREES,
  WHICH IS THE KARKA/SIMHA BOUNDARY -- ONE OF THE THREE GANDANTA JUNCTIONS.

      leaving Ashlesha and entering Magha IS crossing the water-fire gandanta.

  And Simha is his TWELFTH HOUSE.
""")

# =============================================================================
rule('3.  WHAT THE TRANSIT ACTUALLY TOUCHES')
ks = 3   # Karka
print(f"  Guru in Karka aspects, by the 5th, 7th and 9th:\n")
for a in (5, 7, 9):
    t = (ks + a - 1) % 12
    print(f"      {ordn(a)} aspect -> {SIGNS[t]:11s} = his {ordn(hsign(t)):5s} house,"
          f" occupants {', '.join(occ(t)) or 'empty'}")
print(f"""
  THE FIRST ROW IS THE FINDING.

  Guru's 5th aspect falls on VRISCHIKA -- his 3rd house -- which holds KETU in
  the severest gandanta pada in the zodiac.  So for ten months a benefic is
  throwing its most creative aspect onto the chart's single most unstable
  point, and that point is a node of dissolution sitting in the house of
  courage and initiative.

  IF THE QUESTION IS ABOUT MATERIAL RISING FROM SOMEWHERE BENEATH DELIBERATE
  CONTROL, THAT ASPECT IS A BETTER REASON THAN THE NAKSHATRA IS.
""")

# =============================================================================
rule('4.  GOCHARA — AND IT IS UNFAVOURABLE')
from_moon = (ks - sign_of(POS['Chandra'])) % 12 + 1
from_lagna = hsign(ks)
GOOD_GURU = (2, 5, 7, 9, 11)
print(f"""
      from the natal CHANDRA (Vrishabha)   the {ordn(from_moon)}
      from the natal LAGNA (Kanya)         the {ordn(from_lagna)}

  THE CLASSICAL TABLE.  Guru is favourable in the 2nd, 5th, 7th, 9th and 11th
  from Chandra, and unfavourable everywhere else.

      the {ordn(from_moon)} from Chandra is {'FAVOURABLE' if from_moon in GOOD_GURU else 'NOT among them -- UNFAVOURABLE'}

  So the standard method calls this transit BAD from the Moon and GOOD from the
  lagna, and gochara is read from the MOON.

      Guru's own bindus in Karka        {GURU_BAV['Karka']} of 8
      Sarvashtakavarga of Karka         {SAV['Karka']}

  {GURU_BAV['Karka']} bindus is middling -- neither the single-bindu crossing section 29 flags
  for Shani over the 10th, nor a well-supported passage.
""")

# =============================================================================
rule('5.  THE ONE THING THAT MAKES THIS TRANSIT WORTH ANYTHING')
print("""
  GURU IS THE RUNNING ANTARDASHA LORD.

      Rahu mahadasha, Dec 2022 - Dec 2040
      RAHU-GURU antardasha, Sep 2025 - 31 JANUARY 2028

  The whole Ashlesha passage -- both windows, August 2026 to June 2027 -- sits
  INSIDE Guru's own antardasha.

  THAT IS THE CLASSICAL CONDITION FOR A TRANSIT TO MATTER AT ALL.  A gochara
  over a graha that owns no period is weather.  A gochara BY the period lord is
  the period expressing itself.  Section 38's step 9 exists precisely to keep
  these apart, and here they coincide.
""")

# =============================================================================
rule('6.  THE NATAL DREAM AND FEAR APPARATUS — WHICH IS WHERE THE ANSWER IS')
sub('The 12th house — bed, sleep, dreams, the unconscious')
s12 = (LAG + 11) % 12
print(f"""      sign            {SIGNS[s12]}
      occupants       {', '.join(occ(s12)) or 'EMPTY'}
      lord            {LORD[s12]} -- {dignity(LORD[s12], sign_of(POS[LORD[s12]]))}, in the {ordn(hs(LORD[s12]))}
      Bhava Bala      12.59 rupas -- RANK 1 OF 12, THE STRONGEST BHAVA IN THE CHART
      SAV             {SAV[SIGNS[s12]]}

  THE HOUSE OF DREAMS IS THE BEST-MADE HOUSE HE OWNS, and its lord is EXALTED.
""")
sub('Chandra — the mind itself')
print(f"""      {POS['Chandra']:.2f} = Vrishabha {POS['Chandra']%30:.2f}, EXALTED, in the 9th
      avastha         MRITA -- 'dead' by the Baladi scheme
      Kashta          4.49, the lowest cost of any graha in the chart

  AN EXALTED MOON IN A DEAD AVASTHA IS THE SINGLE MOST IMPORTANT FACT IN THIS
  CHART FOR THE QUESTION ASKED.  The mind is dignified and it is not awake.
  Whatever the inner life does, it does at low wattage and without the ordinary
  daytime governor.
""")
sub('The 8th — fear, the hidden, what surfaces unbidden')
s8 = (LAG + 7) % 12
print(f"""      occupants       {', '.join(occ(s8))} -- three grahas
      aspects onto it NONE
      Bhava Bala      7.00, RANK 12 OF 12 -- the weakest bhava
      SAV             {SAV[SIGNS[s8]]}, the lowest in the chart

  Three grahas sealed in the weakest, least-supported house, reached by nothing.
""")
sub('Ketu — dissolution, and it is in gandanta')
print(f"""      {POS['Ketu']:.2f} = Vrischika {POS['Ketu']%30:.2f}, Jyeshtha pada 4
      the severest gandanta pada in the zodiac, in the 3rd house
      AND IT IS WHAT TRANSIT GURU'S 5TH ASPECT IS ON, for ten months.
""")

# =============================================================================
rule('7.  DOES THE CLASSICAL METHOD SUPPORT THE CLAIM?')
print("""
  DIRECTLY: NO, AND THIS HAS TO BE SAID PLAINLY.

  Parashara's transit material -- chapters 8 and 26 for aspects, the gochara
  and Ashtakavarga chapters for transit judgment -- gives transit results in
  terms of gain, loss, illness, honour, travel, conflict and the like.  IT DOES
  NOT ASSIGN DREAM CONTENT TO A GRAHA CROSSING A NAKSHATRA.  Nowhere in the
  fifty-five chapters this reading has enumerated is there a rule of the form
  "graha X in nakshatra Y produces fears in sleep".

  "ASHLESHA BRINGS UP THE SUBCONSCIOUS" IS A MODERN NAKSHATRA-ASTROLOGY
  ASSOCIATION, built out of the asterism's symbolism -- the coiled serpent, the
  Sarpa deity, the clinging embrace.  It is coherent and it is widely taught.
  IT IS NOT A PARASHARI RULE, and this reading does not have a text for it.

  WHAT THE METHOD DOES SUPPORT, AND IT IS NOT NOTHING:

      the 12th house governs sleep, the bed and what happens there
      Chandra governs the mind
      the 8th governs fear and what is hidden
      Ketu governs dissolution and what surfaces without a cause

  SO THE QUESTION IS ANSWERABLE.  IT IS JUST NOT ANSWERABLE FROM ASHLESHA.
""")

# =============================================================================
rule('8.  THE DATES THAT ACTUALLY MATTER — AND I HAD THIS WRONG FIRST')
print("""
  I DRAFTED THIS SECTION SAYING "GURU LEAVES ASHLESHA ON 27 JUNE 2027, AND THAT
  CROSSING IS THE EVENT."  The ingress computation says there are THREE
  crossings, not one, and the middle one goes BACKWARDS.
""")
prev, j, ing = None, jd_ut(2026, 1, 1, 0, 0, 0, 5.5), []
while j < jd_ut(2028, 6, 1, 0, 0, 0, 5.5):
    x, _ = swe.calc_ut(j, swe.JUPITER, F)
    s = sign_of(x[0])
    if prev is not None and s != prev:
        ing.append((show(j), SIGNS[prev], SIGNS[s], x[3]))
    prev = s
    j += 1.0
print(f"  {'date':16s}{'from':12s}{'to':12s}{'motion':>9s}   what it is")
for d, a_, b_, sp in ing:
    what = ''
    if {a_, b_} == {'Karka', 'Simha'}:
        what = ('GANDANTA crossing, RETROGRADE' if sp < 0 else 'GANDANTA crossing, direct')
        what += ' — into the 12th' if b_ == 'Simha' else ' — out of the 12th'
    elif {a_, b_} == {'Simha', 'Kanya'}:
        what = 'into the LAGNA' if b_ == 'Kanya' else 'back out of the lagna'
    print(f"  {d:16s}{a_:12s}{b_:12s}{sp:+9.4f}   {what}")
print("""
  SO THE PICTURE IS THIS, AND IT IS BETTER THAN THE QUESTION'S VERSION.

  GURU CROSSES THE ASHLESHA-MAGHA GANDANTA THREE TIMES IN THIRTEEN MONTHS --
  forward on 1 November 2026, BACKWARD AND RETROGRADE on 26 January 2027, and
  forward again on 27 June 2027.  A retrograde passage back through a gandanta
  is not a common event and nothing in this reading had noticed it.

  AND WHAT LIES ON THE FAR SIDE IS THE TWELFTH HOUSE -- sleep, the bed, dreams,
  retreat, foreign residence, release.

      in the 12th    1 Nov 2026 - 26 Jan 2027   (first pass, cut short)
      back in Karka  26 Jan 2027 - 27 Jun 2027  (the second Ashlesha window)
      in the 12th    27 Jun 2027 - 27 Nov 2027  (the full pass)
      then           27 Nov 2027 -> KANYA, the natal LAGNA

  THE TRANSIT THE QUESTION ASKS ABOUT IS THE WAITING ROOM.  Ashlesha is the
  last quarter of Karka; what it is the approach TO is the twelfth house, and
  Guru reaches it three separate times.

  AND ONE COOLING FACT TO SET AGAINST ALL OF IT.  Guru enters the 12th as a
  BENEFIC, into the BEST-BUILT HOUSE IN THE CHART -- rank 1 of 12 by Bhava Bala
  -- ruled by an EXALTED Surya, the strongest graha he owns.  The classical
  reading of a benefic transiting a strong 12th is retreat, pilgrimage, foreign
  residence, expenditure on good account, and undisturbed sleep.

      NOT NIGHTMARES.  THE OPPOSITE OF NIGHTMARES.

  If the last ten months have in fact brought difficult material into his
  dreams, THE CHART DOES NOT LOCATE THE CAUSE IN THIS TRANSIT, and the honest
  answer is to say so rather than to find a rule that fits after the fact.
""")
print('=' * 92)
