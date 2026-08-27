#!/usr/bin/env python3
"""
"DOES IT TRIGGER ANY EVENTS OR SITUATIONS FOR HIM?"

The 28 August 2026 Chandra grahan is visible from the United States (section
44), so if he is there it reaches him.  The question is what that does.

THIS DOCUMENT'S STANDING POSITION, STATED BEFORE THE COMPUTATION SO IT CANNOT
BE ACCUSED OF BEING FITTED AFTERWARDS:

    a transit marks a window in which part of the chart is under pressure.
    IT DOES NOT SAY WHAT HAPPENS IN IT, and it does not create a promise the
    natal chart does not already hold.  (sections 33, 39, 43)

So the honest shape is: what does classical method actually license here, what
do the two measures that DO apply to an individual say, and what is already
scheduled in this window regardless of the eclipse.

THE RESULT IS NOT WHAT THE QUESTION EXPECTS.
"""
import swisseph as swe
from ephem_core import (SIGNS, GRAHAS, SUPPLIED, LORD, VIM, jd_ut, nak_of,
                        varga, sign_of, rule, sub)

swe.set_sid_mode(swe.SIDM_LAHIRI)
F = swe.FLG_SWIEPH | swe.FLG_SIDEREAL
POS = dict(SUPPLIED)
LAG = sign_of(POS['Lagna'])
JD0 = jd_ut(2002, 4, 15, 18, 2, 45, 5.5)
MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
       'Nov', 'Dec']
NAKS = ['Ashwini', 'Bharani', 'Krittika', 'Rohini', 'Mrigashira', 'Ardra',
        'Punarvasu', 'Pushya', 'Ashlesha', 'Magha', 'P.Phalguni', 'U.Phalguni',
        'Hasta', 'Chitra', 'Swati', 'Vishakha', 'Anuradha', 'Jyeshtha', 'Moola',
        'P.Ashadha', 'U.Ashadha', 'Shravana', 'Dhanishtha', 'Shatabhisha',
        'P.Bhadrapada', 'U.Bhadrapada', 'Revati']
TARA = ['Janma', 'Sampat', 'Vipat', 'Kshema', 'Pratyari', 'Sadhaka', 'Vadha',
        'Mitra', 'Ati-Mitra']
GOOD_TARA = {2, 4, 6, 8, 9}
hsign = lambda si: (si - LAG) % 12 + 1
ordn = lambda n: f"{n}{'th' if 10 <= n % 100 <= 20 else {1:'st',2:'nd',3:'rd'}.get(n%10,'th')}"
occ = lambda si: [g for g in GRAHAS if sign_of(POS[g]) == si]
show = lambda j: (lambda y, m, d, _: f"{int(d)} {MON[m-1]} {y}")(*swe.revjul(j + 5.5 / 24))
SAV = {'Kumbha': 41, 'Simha': 24}
BRANK = [5, 3, 8, 2, 6, 10, 4, 12, 7, 9, 11, 1]

TJ = swe.lun_eclipse_when(jd_ut(2026, 8, 24, 0, 0, 0, 5.5), swe.FLG_SWIEPH, 0, False)[1][0]
MO = swe.calc_ut(TJ, swe.MOON, F)[0][0]
ES, EH = sign_of(MO), hsign(sign_of(MO))

# =============================================================================
rule('1.  WHAT CLASSICAL METHOD ACTUALLY LICENSES HERE')
print("""
  A POINT WORTH MAKING BEFORE ANY PREDICTION.

  The classical eclipse material is overwhelmingly MUNDANE.  Where the texts
  treat grahan at length they are talking about kings, kingdoms, armies, crops,
  rainfall and the fortunes of countries -- not about what happens to a private
  individual in the months after.

  INDIVIDUAL ECLIPSE-EFFECT PREDICTION IS A LATER AND LARGELY POPULAR
  ELABORATION.  It is widely taught and this document is not sneering at it,
  but it is not what Parashara is doing, and the fifty-five chapters enumerated
  in sections 35 and 37 contain no rule of the form "an eclipse in house N
  produces event X for the native".

  WHAT DOES APPLY TO AN INDIVIDUAL, AND IS FULLY CLASSICAL:

      GOCHARA -- an eclipse is a full Moon, so the Moon's transit rules apply
      TARA BALA -- the eclipse nakshatra counted from the janma nakshatra
      THE DASHA running underneath it

  Those three are computed below.  Nothing else is invented to fill the gap.
""")

# =============================================================================
rule('2.  THE TWO MEASURES THAT APPLY — AND BOTH COME BACK FAVOURABLE')
frm = (ES - sign_of(POS['Chandra'])) % 12 + 1
GOOD_MOON = {1, 3, 6, 7, 10, 11}
en = nak_of(MO)
ei, ji = NAKS.index(en[0]), NAKS.index(nak_of(POS['Chandra'])[0])
cnt = (ei - ji) % 27 + 1
tara = (cnt - 1) % 9 + 1
sub('Gochara — the Moon transiting from the janma rashi')
print(f"""      eclipse Moon      {SIGNS[ES]} {MO%30:.2f}
      natal Chandra     {SIGNS[sign_of(POS['Chandra'])]} {POS['Chandra']%30:.2f}
      so the eclipse is the {ordn(frm)} FROM THE MOON

      Chandra's gochara is favourable in the 1st, 3rd, 6th, 7th, 10th and 11th
      from the janma rashi.

      THE {ordn(frm).upper()} IS {'AMONG THEM -- FAVOURABLE' if frm in GOOD_MOON else 'NOT AMONG THEM -- UNFAVOURABLE'}
""")
sub('Tara bala — the eclipse nakshatra from the janma nakshatra')
print(f"""      janma nakshatra   {NAKS[ji]}  (#{ji+1})
      eclipse nakshatra {NAKS[ei]}  (#{ei+1}), pada {en[1]}, lord {en[2]}
      count             {cnt}  ->  tara {tara} = {TARA[tara-1].upper()}

      {TARA[tara-1]} is {'a FAVOURABLE tara' if tara in GOOD_TARA else 'an UNFAVOURABLE tara'} -- {'well-being, safety, prosperity' if tara == 4 else ''}
""")
print(f"""
  SO BY THE TWO MEASURES THE CLASSICAL METHOD ACTUALLY GIVES FOR AN INDIVIDUAL,
  THIS ECLIPSE IS FAVOURABLY PLACED.

  THAT IS THE OPPOSITE OF WHAT THE QUESTION EXPECTS, and it is worth sitting
  with rather than explaining away.  The dread attached to grahan is real in
  practice and in ritual, and it is not what the transit tables say here.
""")

# =============================================================================
rule('3.  WHAT THE ECLIPSE ACTUALLY TOUCHES')
t7 = (ES + 6) % 12
print(f"""      falls in          {SIGNS[ES]} = his {ordn(EH).upper()} HOUSE
      what that house is  service, employment, competition, debt, illness,
                          the daily grind, and enemies
      occupants of {SIGNS[ES]}  {', '.join(occ(ES)) or 'EMPTY -- NOTHING NATAL IS BEING ECLIPSED'}
      its lord          {LORD[ES]} -- which section 42 identified as the
                        AMATYAKARAKA, the Jaimini karaka of profession
      Bhava Bala        rank {BRANK[EH-1]} of 12
      Sarvashtakavarga  {SAV['Kumbha']} -- THE HIGHEST OF ANY SIGN IN THIS CHART
      Moon's 7th aspect {SIGNS[t7]} = the {ordn(hsign(t7))}, {', '.join(occ(t7)) or 'empty'}

  ONE COINCIDENCE THAT LOOKS LIKE SOMETHING AND IS NOT.  The eclipse falls at
  {MO%30:.2f} degrees of its sign; natal Budha is at {POS['Budha']%30:.2f} degrees of ITS sign --
  {abs((MO%30)-(POS['Budha']%30)):.2f} of a degree apart.  THEY ARE IN DIFFERENT SIGNS AND DIFFERENT
  NAVAMSAS ({SIGNS[varga(MO,9)]} against {SIGNS[varga(POS['Budha'],9)]}).  Same degree-in-sign is not a
  contact in any classical scheme.  IT IS A NUMERICAL ACCIDENT AND IT IS
  REPORTED SO THAT NOBODY ELSE MISTAKES IT FOR A FINDING.
""")

# =============================================================================
rule('4.  WHAT IS ALREADY SCHEDULED IN THIS WINDOW')
span = 360 / 27
ni = int(POS['Chandra'] // span)
l0 = ['Ketu', 'Shukra', 'Surya', 'Chandra', 'Mangal',
      'Rahu', 'Guru', 'Shani', 'Budha'][ni % 9]
bal = dict(VIM)[l0] * (1 - (POS['Chandra'] - ni * span) / span)
i0 = [g for g, _ in VIM].index(l0)
MD, t = [(l0, 0.0, bal)], bal
for k in range(1, 9):
    g, y = VIM[(i0 + k) % 9]
    MD.append((g, t, t + y))
    t += y


def subs(l, a, b):
    i = [g for g, _ in VIM].index(l)
    out, tt = [], a
    for k in range(9):
        g, y = VIM[(i + k) % 9]
        d = (b - a) * y / 120
        out.append((g, tt, tt + d))
        tt += d
    return out


age = (TJ - JD0) / 365.2425
md = [x for x in MD if x[1] <= age < x[2]][0]
ad = [x for x in subs(md[0], md[1], md[2]) if x[1] <= age < x[2]][0]
pd = [x for x in subs(ad[0], ad[1], ad[2]) if x[1] <= age < x[2]][0]
sh = lambda a: show(JD0 + a * 365.2425)
print(f"""      mahadasha        {md[0]}
      antardasha       {ad[0]}    {sh(ad[1])} - {sh(ad[2])}
      pratyantardasha  {pd[0]}   {sh(pd[1])} - {sh(pd[2])}

  AND THAT IS THE REAL ANSWER TO THE QUESTION.

  RAHU-GURU is running, and Guru in this chart is:

      the SOLE OCCUPANT of the 10th house            (section 42)
      the 7TH LORD and the UPAPADA LORD              (section 40)
      the 4TH LORD -- the house of home and roots    (section 41)
      exalted in the D24, the varga of learning      (section 42)

  IT IS THE ONLY ANTARDASHA IN AN EIGHTEEN-YEAR MAHADASHA OWNED BY THE GRAHA
  THAT STANDS IN HIS CAREER HOUSE, AND IT CLOSES 31 JANUARY 2028.

  WHATEVER MOVES IN THIS PERIOD MOVES BECAUSE OF THAT.  The eclipse is a
  fortnight of sky inside a twenty-nine-month period that was already the most
  loaded stretch in his chart before anyone looked up.
""")

# =============================================================================
rule('5.  HOW LONG AN ECLIPSE IS HELD TO ACT')
prev_sol = swe.sol_eclipse_when_glob(TJ - 40, swe.FLG_SWIEPH, 0, False)[1][0]
nxt = swe.lun_eclipse_when(TJ + 10, swe.FLG_SWIEPH, 0, False)[1][0]
print(f"""      preceding solar eclipse   {show(prev_sol)}
      THIS lunar eclipse        {show(TJ)}
      next lunar eclipse        {show(nxt)}

  These two are an ECLIPSE SEASON -- a solar and a lunar sixteen days apart on
  the same nodal axis.  The common rule of thumb is that an eclipse's influence
  runs until the next one, which here means AUGUST 2026 TO FEBRUARY 2027.

  THAT RULE IS FOLKLORE RATHER THAN TEXT, and this document flags it as such
  rather than dressing it up.  What IS textual is that the Moon leaves Kumbha
  in about two days and does not return for a month.
""")

# =============================================================================
rule('6.  THE ANSWER')
print(f"""
  DOES IT TRIGGER EVENTS?

  NOT BY ITSELF, AND THE CHART GIVES NO REASON TO EXPECT IT TO.

  1  BY THE TWO CLASSICAL MEASURES THAT APPLY TO AN INDIVIDUAL, IT IS
     FAVOURABLY PLACED -- the {ordn(frm)} from his Moon, which is a good gochara
     position, and {TARA[tara-1]} tara, which is a good tara.  If you were going to
     predict anything from the transit tables alone, you would not predict
     trouble.

  2  NOTHING NATAL IS BEING ECLIPSED.  Kumbha is empty.  The eclipse conjoins
     no graha of his and its 7th aspect falls on an empty 12th.

  3  WHAT IS UNDER ATTENTION IS THE 6TH HOUSE -- service, employment,
     competition, debt, health, the daily grind.  That is a real and specific
     domain, and it is the house whose lord is the AMATYAKARAKA, so it connects
     directly to the career questions he has been asking.

     The 6th is rank {BRANK[EH-1]} of 12 by Bhava Bala and carries the HIGHEST bindu count
     in the chart.  Section 41 read that disagreement as: he wins contests he
     should not comfortably win, and the winning costs him.

  4  AND THE PERIOD UNDERNEATH IS DOING THE ACTUAL WORK.  Rahu-Guru runs to
     31 January 2028 and hands this stretch to the graha that occupies his 10th,
     rules his 7th and his 4th, owns his Upapada, and is exalted in his learning
     varga.  THAT is the live thing.  The eclipse is weather inside it.

  THE SENTENCE I WOULD STAND BEHIND:

      The eclipse marks the 6th house -- work, competition, health, obligation
      -- for a few weeks, in a favourable transit position, touching nothing
      natal.  If something moves for him between now and early 2027, the chart
      attributes it to RAHU-GURU and not to the grahan, and it would have been
      due with or without an eclipse.

  AND THE LIMIT, WHICH IS NOT A HEDGE.  Jyotisha times the activation of a
  promise.  It does not name an event, and no computation in this document can
  turn a marked window into a specific thing that happens.  Anyone telling him
  what a particular eclipse WILL DO is going beyond what the method supports.
""")
print('=' * 92)
