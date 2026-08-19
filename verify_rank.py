#!/usr/bin/env python3
"""
"When will he become diamond" -- a named rank tier in a selling organisation.

FIRST, WHAT JYOTISHA CAN AND CANNOT DO WITH THIS.

It cannot name a company's ladder.  No chart contains the word Diamond, no
chart knows one firm's tiers from another's, and any reading that hands back a
date for a specific corporate rank is inventing it.  That has to be said before
anything else, because this is exactly the kind of question a reading gets
flattering about.

What it CAN do is three things, and they are worth having:

    1. translate the question into houses -- a named rank in a selling
       organisation is an 11th-house event with 3rd, 7th and 10th support
    2. test whether this chart supports THAT MODE OF EARNING at all
    3. date the windows when the apparatus is actually activated

Section 44 already found this chart is built for employment inside an
institution rather than proprietorship, so question 2 is not a formality.  It
is the real question, and the answer is not the encouraging one.

Placement-first throughout, per his instruction: no bindu counts, no Shadbala,
no constructed scores.  Dasha dates are timing, not scoring.
"""
from ephem_core import (SIGNS, GRAHAS, SUPPLIED, LORD, VIM, dignity,
                        sign_of, short, rule, sub)

POS = dict(SUPPLIED)
LAG = sign_of(POS['Lagna'])
BIRTH_Y = 2002 + (31 + 28 + 31 + 15) / 365.25
hs = lambda g: (sign_of(POS[g]) - LAG) % 12 + 1
house_sign = lambda n: (LAG + n - 1) % 12
occupants = lambda n: [g for g in GRAHAS if hs(g) == n]
rules_of = lambda g: [i for i in range(1, 13) if LORD[(LAG + i - 1) % 12] == g]
ASPECT = {'Mangal': (4, 7, 8), 'Guru': (5, 7, 9), 'Shani': (3, 7, 10),
          'Rahu': (5, 7, 9), 'Ketu': (5, 7, 9)}
UPAGRAHA = {11: ['Gulika', 'Mandi'], 7: ['Upaketu']}   # from section 16
MATURE = {'Guru': 16, 'Surya': 22, 'Chandra': 24, 'Shukra': 25,
          'Mangal': 28, 'Budha': 32, 'Shani': 36}


def ymd(t):
    y = int(t)
    doy = (t - y) * 365.25
    cum = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 366]
    m = max(i for i in range(12) if doy >= cum[i]) + 1
    return f"{['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][m-1]} {y}"


aspects_to = {}
for g in GRAHAS:
    for a in ASPECT.get(g, (7,)):
        aspects_to.setdefault((hs(g) + a - 2) % 12 + 1, []).append(g)

# --------------------------------------------------------------- dasha tree
span = 360 / 27
ni = int(POS['Chandra'] // span)
lord0 = ['Ketu', 'Shukra', 'Surya', 'Chandra', 'Mangal',
         'Rahu', 'Guru', 'Shani', 'Budha'][ni % 9]
bal = dict(VIM)[lord0] * (1 - (POS['Chandra'] - ni * span) / span)
i0 = [g for g, _ in VIM].index(lord0)
MD, t = [(lord0, BIRTH_Y, BIRTH_Y + bal)], BIRTH_Y + bal
for k in range(1, 9):
    g, y = VIM[(i0 + k) % 9]
    MD.append((g, t, t + y)); t += y


def subs(lord, a, b):
    i = [g for g, _ in VIM].index(lord)
    out, t = [], a
    for k in range(9):
        g, y = VIM[(i + k) % 9]
        d = (b - a) * y / 120
        out.append((g, t, t + d)); t += d
    return out


AD = [(m, l, x, y) for m, a, b in MD for l, x, y in subs(m, a, b)]

# =============================================================================
rule('1.  TRANSLATING THE QUESTION INTO HOUSES')
print("""
  A named rank in a selling organisation is not one house.  It is four, and
  they have to be separated because this chart treats them very differently.

      11th   GAINS, NETWORKS, LARGE GROUPS, ATTAINMENT OF DESIRES
             This is the house.  "Labha" literally means attainment, and a
             rank tier is an attainment conferred by a network.

      3rd    SELF-DRIVEN EFFORT, INITIATIVE, PERSUASION, COMMUNICATION
             Direct selling is a 3rd-house activity before it is anything
             else -- you go out and you ask.

      7th    THE PUBLIC, TRADE, DEALING ACROSS A TABLE
             Recruiting and selling to strangers is 7th-house work.

      10th   STANDING, RECOGNITION, THE TITLE ITSELF
""")

print(f"  {'house':6s}{'sign':11s}{'lord':9s}{'lord in':9s}"
      f"{'occupants':16s}{'aspected by':22s}upagrahas")
for n in (11, 3, 7, 10):
    s = house_sign(n)
    ld = LORD[s]
    print(f"  {n:2d}    {SIGNS[s]:11s}{ld:9s}{hs(ld):3d}      "
          f"{', '.join(occupants(n)) or '—':16s}"
          f"{', '.join(aspects_to.get(n, [])) or 'NOTHING':22s}"
          f"{', '.join(UPAGRAHA.get(n, [])) or '—'}")

# =============================================================================
rule('2.  THE KAMA TRIKONA — AND THIS IS THE FINDING')
kama = [3, 7, 11]
occ = {n: occupants(n) for n in kama}
allocc = [g for n in kama for g in occ[n]]
print(f"""
  The 3rd, 7th and 11th are the KAMA TRIKONA -- the three houses of desire,
  ambition and attainment.  They are precisely the machinery a rank ladder
  runs on.  Here is what occupies them:

      3rd  {', '.join(occ[3]) or 'empty'}
      7th  {', '.join(occ[7]) or 'empty'}
      11th {', '.join(occ[11]) or 'empty'}

  THE ONLY OCCUPANT OF ALL THREE HOUSES OF DESIRE IS {', '.join(allocc).upper()}.

  Ketu is the graha of detachment, severance and the removal of wanting.  It is
  the one body in the sky whose function is to make a thing stop mattering.
  And it is sitting alone in his houses of ambition -- in the 3rd, the house of
  going out and asking, IN THE SEVEREST GANDANTA PADA.

  This is not a new finding.  It is the central mechanism section 37 identified
  when asked why he walks away from what he wanted most.  WHAT IS NEW IS THAT
  THE RANK QUESTION LANDS EXACTLY ON IT.
""")

sub('And the rest of the kama trikona is thin in the same direction')
print(f"""
      the 7th  — the house of dealing with the public — is EMPTY, is aspected
                 by NOTHING except Ketu, and contains UPAKETU, a shadow point.
                 Section 44 called it the weakest signature in the chart.

      the 11th — the house of gains and networks — is EMPTY of grahas, and
                 carries BOTH GULIKA AND MANDI, the two harshest upagrahas in
                 the scheme.  It receives Shani's aspect and Ketu's.  NO
                 BENEFIC REACHES IT.

      the 3rd  — holds Ketu, and receives four aspects: {', '.join(aspects_to[3])}.
                 THREE OF THOSE FOUR ARE MALEFIC.

  So all three houses of desire are either empty, shadow-occupied, or reached
  only by malefics.  THAT IS A COHERENT STRUCTURE AND IT IS NOT AN ENCOURAGING
  ONE FOR A LADDER BUILT ON RECRUITING PEOPLE.
""")

# =============================================================================
rule('3.  BUT THE 11TH LORD IS EXALTED — SO WHAT IS THE REAL READING?')
el = LORD[house_sign(11)]
print(f"""
  The counterweight is real and section 23 found it: {el}, the 11th lord,
  stands EXALTED in the 9th.  A weak house with an exalted lord is a specific
  configuration, not a contradiction.  It says:

      THE HOUSE IS POORLY BUILT   — the machinery of networks and tiers
      THE LORD IS WELL PLACED     — but the gains themselves are strong,
                                    and they arrive FROM WHERE THE LORD SITS

  {el} sits in the NINTH: fortune, elders, teachers, mentors, the father,
  people senior to him who are well disposed toward him.

  PUT THE TWO TOGETHER AND THE ANSWER IS UNUSUALLY PRECISE:

      HIS GAINS COME THROUGH PEOPLE WHO RESPECT HIM.
      NOT THROUGH PEOPLE HE RECRUITS.

  Those are different mechanisms and this chart is emphatic about which one it
  owns.  A rank conferred by a network he has to build sits on his weakest
  structure.  A position handed to him by a senior who rates him sits on an
  exalted lord in the house of elders -- and that is the SAME finding section
  21 reached from a completely different direction when it concluded he becomes
  "the one things are handed to" rather than the one whose name is on the door.
""")

# =============================================================================
rule('4.  IF HE PURSUES IT ANYWAY — WHEN THE APPARATUS IS ACTUALLY LIVE')
print(f"""
  {el} matured at {MATURE[el]}, in {ymd(BIRTH_Y + MATURE[el])}.  THE 11TH LORD IS ALREADY MATURE --
  the only one of the four relevant lords that is.  So the gains-house
  instrument is available now, which was not true even two years ago.

  The windows where the 11th apparatus is genuinely activated:
""")
KEY = [g for g in (el, 'Guru', 'Shukra')]
for m, l, a, b in AD:
    if b < 2026.6 or a > 2052:
        continue
    why = []
    if l == el:
        why.append(f'{el} — THE 11TH LORD ITSELF')
    if m == el:
        why.append(f'{el} mahadasha')
    if l == 'Guru':
        why.append('Guru — karaka of expansion and groups')
    if l == 'Shukra' and m == 'Guru':
        why.append('Shukra under Guru')
    if why:
        print(f"      {m}–{l:8s} {ymd(a)} – {ymd(b):9s}  {'; '.join(why)}")

print(f"""
  READ THAT LIST HONESTLY, INCLUDING THE FIRST ROW.

  RAHU–GURU IS RUNNING NOW, to January 2028, and Guru is the natural karaka of
  expansion and of groups — and it rules the 7th, the house of dealing with the
  public.  So the current window is NOT dead for this.  It is the karaka
  support without the lord support, which classically shows as a good period to
  BEGIN and a poor one to expect the tier from.

  But the single cleanest activation of the gains house in his whole visible
  timeline is RAHU–CHANDRA, the 11th lord's OWN antardasha, and it does not
  arrive until 2038 — age 36.

  And the natural karaka of expansion, Guru, opens its MAHADASHA in Dec 2040
  and runs sixteen years.  Section 34 had already called December 2040 the
  step, reached by a different route entirely.

  SO THE DATED ANSWER, WITH THE CAVEAT THAT NO CHART NAMES A COMPANY'S TIERS:

      A START IS SUPPORTED NOW; THE TIER IS NOT DATED BEFORE 2038.

      The gains apparatus is weakly built and does not come under its own
      lord's period until Jun 2038, with the real expansion from Dec 2040.
      The stretch in between — 2028 to 2033 — is pointed somewhere else
      entirely: at the career foundation (2028–30) and at identity (2030–33).
      Effort routed into a rank ladder across those years is competing with
      what the chart is actually doing.
""")

# =============================================================================
rule('5.  WHAT THE CHART OFFERS INSTEAD')
print("""
  This reading does not get to just say no, so here is the constructive form.

  1. THE MECHANISM IS BACKWARDS FOR HIM.  A tier ladder pays you for RECRUITING
     BREADTH.  His chart pays him for BEING RATED BY SENIORS.  The same effort
     routed through mentors, institutions and people who already respect his
     work converts; routed through building a downline it runs into an empty
     11th with both harsh upagrahas in it.

  2. THE 6TH AND THE D10 SAY EMPLOYMENT.  Section 44's finding stands: the
     house of service is his strongest, the house of independent trade his
     weakest.  A rank inside an EMPLOYER'S structure — a grade, a band, a
     promotion — sits on completely different houses than a rank inside a
     selling network, and those houses are the ones he actually owns.

  3. AND SECTION 37 IS THE WARNING.  The one occupant of his three houses of
     desire is the graha that removes wanting.  The chart's repeated pattern is
     that he pursues something in the kama trikona, reaches it, and finds the
     wanting has gone out of it.  IF HE CLIMBS THIS LADDER, THE STRUCTURAL
     PREDICTION IS NOT THAT HE FAILS.  IT IS THAT HE ARRIVES AND STOPS CARING.

     That is worth knowing BEFORE the effort rather than after it.
""")

# =============================================================================
rule('6.  THE LIMITS, PLAINLY')
print("""
  1. NO CHART NAMES A CORPORATE RANK.  There is no Diamond in any horoscope.
     What is dated above is the activation of the houses such a rank belongs
     to, which is a different and weaker claim.

  2. THIS DOES NOT SAY HE CANNOT.  Charts describe where effort converts
     cheaply and where it converts expensively.  A weak 11th means the ladder
     costs him more per rung than it costs someone else — not that the rung is
     unreachable.  People succeed against their charts constantly.

  3. AND IF HE HAS ALREADY STARTED, THE READING CHANGES SHAPE.  Everything
     above is about whether to route effort this way.  If he is already in it,
     the useful part is section 4's dates and the warning in section 5.3 —
     not the structural verdict, which is now behind him.
""")
print('=' * 92)
