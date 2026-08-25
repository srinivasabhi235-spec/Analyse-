#!/usr/bin/env python3
"""
THE FIELD — WHEN HE FINDS IT, AND WHEN HE STARTS GOING DEEP IN IT.

The question sharpened: not "a job" and not "standing", but A FIELD -- a domain
he settles into -- and then DEEPENING it.

THOSE ARE TWO DIFFERENT QUESTIONS AND THE CHART ANSWERS THEM WITH DIFFERENT
APPARATUS.

    FINDING A FIELD    the 10th house and its lord; the Amatyakaraka; the
                       10th from Karakamsa; the D10
    DEEPENING IT       the 5th house (discernment, purva punya, mastery);
                       the D24, which is the varga of LEARNING; Guru as
                       knowledge and Shani as depth-through-time

Section 38 already judged the 10th and section 41 already ranked "place".  This
adds what neither did: the VOCATION karakas, the LEARNING varga, and a timeline
that separates FINDING from DEEPENING instead of merging them.
"""
from ephem_core import (SIGNS, GRAHAS, SUPPLIED, LORD, VIM, varga, dignity,
                        sign_of, jd_ut, rule, sub)
import swisseph as swe

POS = dict(SUPPLIED)
LAG = sign_of(POS['Lagna'])
JD0 = jd_ut(2002, 4, 15, 18, 2, 45, 5.5)
MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
       'Nov', 'Dec']
hs = lambda g: (sign_of(POS[g]) - LAG) % 12 + 1
hsign = lambda si: (si - LAG) % 12 + 1
ordn = lambda n: f"{n}{'th' if 10 <= n % 100 <= 20 else {1:'st',2:'nd',3:'rd'}.get(n%10,'th')}"
occ = lambda si: [g for g in GRAHAS if sign_of(POS[g]) == si]
show = lambda j: (lambda y, m, d, _: f"{int(d):>2d} {MON[m-1]} {y}")(*swe.revjul(j + 5.5 / 24))
RUPAS = {'Surya': 11.39, 'Chandra': 6.42, 'Mangal': 6.33, 'Budha': 6.46,
         'Guru': 8.21, 'Shukra': 6.68, 'Shani': 6.39}
MINREQ = {'Surya': 5.0, 'Chandra': 6.0, 'Mangal': 5.0, 'Budha': 7.0,
          'Guru': 6.5, 'Shukra': 5.5, 'Shani': 5.0}
KASHTA = {'Surya': 7.83, 'Chandra': 4.49, 'Mangal': 38.87, 'Budha': 30.32,
          'Guru': 15.10, 'Shukra': 11.87, 'Shani': 46.83}
BRANK = [5, 3, 8, 2, 6, 10, 4, 12, 7, 9, 11, 1]

# =============================================================================
rule('1.  WHO OWNS THE FIELD — FOUR INDEPENDENT INDICATORS')
S10 = (LAG + 9) % 12
L10 = LORD[S10]
deg = {g: (30 - (POS[g] % 30) if g == 'Rahu' else POS[g] % 30)
       for g in GRAHAS if g != 'Ketu'}
KAR = sorted(deg, key=lambda g: -deg[g])
NAMES = ['Atmakaraka', 'Amatyakaraka', 'Bhratrikaraka', 'Matrikaraka',
         'Pitrikaraka', 'Putrakaraka', 'Gnatikaraka', 'Darakaraka']
AK, AmK = KAR[0], KAR[1]
KA = varga(POS[AK], 9)
T10K = (KA + 9) % 12
print(f"""
  THE PARASHARI INDICATOR
      10th house       {SIGNS[S10]}, holding {', '.join(occ(S10))} alone, UNASPECTED
      10th lord        {L10}, in the 8th, combust, ratio {RUPAS[L10]/MINREQ[L10]:.2f} -- FAILS

  THE JAIMINI INDICATOR -- computed here for the first time in this reading
""")
for n, g in zip(NAMES, KAR):
    mark = '   <<<' if n in ('Atmakaraka', 'Amatyakaraka') else ''
    print(f"      {n:15s}{g:9s}{deg[g]:6.2f} deg in sign{mark}")
print(f"""
      AMATYAKARAKA = {AmK}.  In Jaimini this is THE karaka of profession --
      the minister, the one who executes the Atmakaraka's purpose.

  THE KARAKAMSA INDICATOR
      Atmakaraka       {AK}, whose navamsa is {SIGNS[KA]}
      KARAKAMSA        {SIGNS[KA]} = his natal {ordn(hsign(KA))} house
      10th from it     {SIGNS[T10K]}, lord {LORD[T10K]} -- his natal {ordn(hsign(T10K))} house
                       occupants: {', '.join(occ(T10K)) or 'EMPTY'}

  THE VARGA INDICATOR
""")
for n in (10, 24):
    d = {g: varga(POS[g], n) for g in list(GRAHAS) + ['Lagna']}
    t = (d['Lagna'] + 9) % 12
    print(f"      D{n} lagna {SIGNS[d['Lagna']]:11s} its 10th {SIGNS[t]:11s}"
          f" occupants {', '.join(g for g in GRAHAS if d[g] == t) or 'empty'}")
print(f"""
  AND THE FIRST REAL CONVERGENCE OF THIS SECTION:

      SHUKRA OCCUPIES THE 10TH HOUSE OF BOTH THE D10 AND THE D24 --
      the career varga AND the learning varga.

  Shukra is the Atmakaraka and carries the highest Ishta phala in the chart.
  It is the ONLY occupant of the 10th in either varga, and it occupies both --
  the professional house of the chart that shows the WORK and of the chart that
  shows the LEARNING.
""")

# =============================================================================
rule('2.  WHAT THE FIELD LOOKS LIKE — THE FOUR INDICATORS COMPARED')
print(f"""
  {'indicator':26s}{'points to':16s}what that signifies

  {'10th lord':26s}{L10 + ' / Mithuna':16s}analysis, language, transaction, the
  {'':26s}{'':16s}handling of information
  {'10th occupant':26s}{'Guru / enemy':16s}counsel, teaching, knowledge-work --
  {'':26s}{'':16s}but uncomfortable in an enemy sign
  {'Amatyakaraka':26s}{AmK:16s}structure, endurance, systems, the long
  {'':26s}{'':16s}patient grind; also the 5th and 6th lord
  {'10th from Karakamsa':26s}{SIGNS[T10K] + ' / ' + LORD[T10K]:16s}authority and the visible position --
  {'':26s}{'':16s}but it IS his 12th house

  THE FOUR DO NOT NAME ONE PROFESSION AND JYOTISHA DOES NOT PRETEND TO.  What
  they agree on is a SHAPE:

      the material is INFORMATION or KNOWLEDGE (Budha lord, Guru occupant)
      the mode is STRUCTURED AND PATIENT (Shani as Amatyakaraka)
      the position is BEHIND THE VISIBLE (10th from Karakamsa lands in the 12th)

  A field where the work is with knowledge or systems, done slowly and
  thoroughly, in a place where the practitioner is not the front of the house.
  THAT IS AS SPECIFIC AS THE METHOD HONESTLY GETS.
""")

# =============================================================================
rule('3.  DEPTH — AND IT IS ONE GRAHA')
S5 = (LAG + 4) % 12
print(f"""
  Depth, mastery and discernment belong to the 5TH HOUSE; the capacity to go
  deep over time belongs to SHANI; formal learning belongs to the D24.

      the 5th house    {SIGNS[S5]}, EMPTY and UNASPECTED, Bhava Bala rank {BRANK[4]} of 12
      its lord         {LORD[S5]}
      Amatyakaraka     {AmK}
      D24 lagna        {SIGNS[varga(POS['Lagna'], 24)]}

  THE SECOND CONVERGENCE, AND IT IS THE ANSWER TO "DEEPENING":

      THE LORD OF THE 5TH AND THE AMATYAKARAKA ARE THE SAME GRAHA: SHANI.

  So in this chart the faculty of going deep and the karaka of vocation are one
  body.  DEPTH IS NOT A SEPARATE PROJECT FROM HIS CAREER -- it is the same
  graha wearing two hats.

      Shani in the 9th, friendly sign, with Chandra, Mangal and Rahu
      Shadbala ratio {RUPAS['Shani']/MINREQ['Shani']:.2f} -- the best in the chart after Surya
      Kashta {KASHTA['Shani']:.2f} -- THE HIGHEST COST OF ANY GRAHA HE OWNS

  DEPTH IS AVAILABLE, IT IS WELL RESOURCED, AND IT IS THE MOST EXPENSIVE THING
  IN THE CHART.  That is a coherent statement rather than a contradiction:
  mastery by Shani is bought with time and discomfort, and this chart prices it
  accordingly.
""")

sub('The D24, the varga of learning — never used in this reading until now')
d24 = {g: varga(POS[g], 24) for g in list(GRAHAS) + ['Lagna']}
l24 = d24['Lagna']
print(f"      D24 lagna {SIGNS[l24]}\n")
for g in GRAHAS:
    h = (d24[g] - l24) % 12 + 1
    dg = dignity(g, d24[g])
    mark = '   <<<' if dg in ('exalted', 'own') or h == 10 else ''
    print(f"      {g:9s}{SIGNS[d24[g]]:11s}H{h:<3d}{dg:12s}{mark}")
print(f"""
  TWO THINGS STAND OUT AND THEY POINT THE SAME WAY.

      GURU IS EXALTED IN THE D24 -- the only exaltation in the learning chart.
      Guru is knowledge itself, and it is at its best in the varga that shows
      how deeply a person learns.

      BUDHA, THE CAREER LORD, IS IN THE D24 TWELFTH -- with BOTH NODES.
      The graha that runs his profession is in the house of loss in the
      learning chart, flanked by Rahu and Ketu.

  READ TOGETHER: THE CAPACITY TO GO DEEP IS EXCELLENT AND IT DOES NOT ARRIVE
  THROUGH THE CAREER LORD.  Formal credentialing through the professional
  channel is the weak route; knowledge held for its own sake is the strong one.
""")

# =============================================================================
rule('4.  THE TIMELINE — FINDING SEPARATED FROM DEEPENING')
span = 360 / 27
ni = int(POS['Chandra'] // span)
lord0 = ['Ketu', 'Shukra', 'Surya', 'Chandra', 'Mangal',
         'Rahu', 'Guru', 'Shani', 'Budha'][ni % 9]
bal = dict(VIM)[lord0] * (1 - (POS['Chandra'] - ni * span) / span)
i0 = [g for g, _ in VIM].index(lord0)
MD, t = [(lord0, 0.0, bal)], bal
for k in range(1, 9):
    g, y = VIM[(i0 + k) % 9]
    MD.append((g, t, t + y))
    t += y


def subs(lord, a, b):
    i = [g for g, _ in VIM].index(lord)
    out, tt = [], a
    for k in range(9):
        g, y = VIM[(i + k) % 9]
        d = (b - a) * y / 120
        out.append((g, tt, tt + d))
        tt += d
    return out


AD = subs('Rahu', *[x[1:] for x in MD if x[0] == 'Rahu'][0])
ROLE = {
    'Guru': 'the 10th-house OCCUPANT; exalted in the D24',
    'Shani': 'the AMATYAKARAKA and the 5th lord -- vocation and depth',
    'Budha': 'the 10th LORD -- and the graha that fails its minimum',
    'Shukra': 'Atmakaraka; holds the 10th of BOTH the D10 and the D24',
    'Surya': 'lord of the sign the 10th-from-Karakamsa falls in',
}
print(f"  {'period':22s}{'from':14s}{'to':14s}{'ages':>12s}   what it activates")
for g, a, b in AD:
    if g in ROLE:
        print(f"  Rahu-{g:17s}{show(JD0+a*365.2425):14s}"
              f"{show(JD0+b*365.2425):14s}{a:5.1f} - {b:4.1f}   {ROLE[g]}")
for g, a, b in MD:
    if g in ('Guru', 'Shani', 'Budha') and b > 24:
        print(f"  {g + ' MAHADASHA':22s}{show(JD0+a*365.2425):14s}"
              f"{show(JD0+b*365.2425):14s}{a:5.1f} - {b:4.1f}   {ROLE[g]}")
print("""
  AND THAT TABLE SEPARATES CLEANLY INTO TWO ERAS.

  THE FINDING ERA -- 2028 to 2037, ages 26 to 35
      Rahu-SHANI    Jan 2028 - Dec 2030   the Amatyakaraka.  Vocation karaka
                                          under period for the first time.
      Rahu-BUDHA    Dec 2030 - Jun 2033   the 10th lord's own period, run by
                                          the weakest graha in the chart.
      Rahu-SHUKRA   Jul 2034 - Jul 2037   the graha holding the 10th of both
                                          the career and the learning varga.

      THREE SEPARATE PROFESSIONAL ACTIVATIONS IN NINE YEARS, BY THREE DIFFERENT
      GRAHAS, AND NONE OF THEM IS THE 10TH-HOUSE OCCUPANT.  That is a decade of
      trying things rather than a decade of settling into one.

  THE DEEPENING ERA -- from December 2040, age 38.7
      GURU MAHADASHA  Dec 2040 - Dec 2056, SIXTEEN YEARS
          Guru is the sole occupant of the 10th house, and Guru is EXALTED in
          the D24.  The graha that sits in his career house and learns best
          runs the entire show for sixteen years.
      SHANI MAHADASHA Dec 2056 - Dec 2075, NINETEEN YEARS
          The Amatyakaraka and the 5th lord.  Vocation and depth, in their own
          mahadasha, for nineteen years.

      THIRTY-FIVE CONSECUTIVE YEARS, FROM 38 TO 73, RUN BY THE TWO GRAHAS THAT
      MEAN KNOWLEDGE AND DEPTH.
""")

# =============================================================================
rule('5.  THE ANSWER')
print("""
  FINDING THE FIELD AND DEEPENING IT ARE NOT THE SAME EVENT IN THIS CHART, AND
  THEY ARE ABOUT TWELVE YEARS APART.

  WHEN HE FINDS IT.  The chart does not show a clean settling before 2028.
  What it shows is JANUARY 2028 TO DECEMBER 2030 -- Rahu-Shani, the first time
  the vocation karaka runs a period -- as the first serious candidate, and
  section 38 already calls that window "the foundation".

  BUT THE FINDING IS CONTESTED FOR NINE YEARS AFTER IT.  Three different grahas
  activate the profession between 2028 and 2037 and none of them is the graha
  actually sitting in his 10th house.  The middle one, Rahu-Budha (Dec 2030 -
  Jun 2033), hands the career to the only graha in the chart that fails its own
  strength minimum.  THAT IS THE PERIOD MOST LIKELY TO LOOK LIKE A FALSE START,
  and this document has called it the hinge since section 17.

  WHEN THE DEEPENING BEGINS.  DECEMBER 2040, AND IT IS NOT SUBTLE.  Guru --
  sole occupant of his career house, exalted in the varga of learning -- takes
  the mahadasha for sixteen years, and Shani -- the Amatyakaraka and the lord
  of the 5th -- takes the following nineteen.

      THE CHART PUTS THIRTY-FIVE CONSECUTIVE YEARS OF KNOWLEDGE-AND-DEPTH
      PERIODS BETWEEN THE AGES OF 38 AND 73.

  IT IS A LATE CHART FOR THIS, AND THAT IS THE FINDING RATHER THAN A HEDGE.
  The career house is sealed, its lord is combust and failing, and the two
  grahas equipped to make a field deep do not get their own periods until he is
  nearly forty.  What runs before then is capable and scattered.

  ONE THING THAT IS AVAILABLE NOW AND IS WORTH MORE THAN IT LOOKS.  Guru is the
  10th-house occupant AND runs the current antardasha to 31 January 2028.  This
  is the ONLY period before 2040 in which the graha actually standing in his
  career house is in charge.  It is short, it is running, and it will not
  repeat for thirteen years.

  AND THE CAVEAT.  A dasha activates a capacity; it does not choose a subject.
  Nothing here names an industry.  What the chart says is the SHAPE -- knowledge
  or systems, handled patiently, from a position behind the visible one -- and
  WHEN that shape gets period support.  The choosing is not in the chart.
""")
print('=' * 92)
