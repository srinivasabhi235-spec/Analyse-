#!/usr/bin/env python3
"""
JOB LOSS AND CAREER DISRUPTION -- how they are structured, and when.

Never asked before, and it is a different question from "career growth"
(section 39) or "how will earning grow" (section 22).  Those ask what the
career DOES.  This asks what happens when it BREAKS.

The apparatus is specific and mostly bhavat bhavam -- reading a house from
another house:

    the 10th          the job and the standing themselves
    the 10th LORD     the instrument that carries them
    the 12th from the 10th = the 9TH     LOSS of career, expenditure of it
    the 8th from the 10th  = the 5TH     sudden upheaval of career
    the 6th           the employment relation, and service disputes
    the badhaka       obstruction -- the 7th, for a dual lagna

Then: which dasha periods activate those, which transits cross them, and
whether the chart describes loss that ARRIVES or loss that is CHOSEN.

Placement-first, with Ashtakavarga used only where the classical method
requires it (judging a transit).  Dates are timing, not scoring.
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
ordn = lambda n: f"{n}{'th' if 10 <= n % 100 <= 20 else {1:'st',2:'nd',3:'rd'}.get(n%10,'th')}"
ASPECT = {'Mangal': (4, 7, 8), 'Guru': (5, 7, 9), 'Shani': (3, 7, 10),
          'Rahu': (5, 7, 9), 'Ketu': (5, 7, 9)}
MALEFIC = {'Surya', 'Mangal', 'Shani', 'Rahu', 'Ketu'}
AV = {"Mesha": (4, 2, 2, 1, 4, 4, 5, 3, 21), "Vrishabha": (4, 3, 2, 3, 4, 5, 3, 2, 22),
      "Mithuna": (3, 4, 6, 4, 6, 5, 3, 1, 29), "Karka": (8, 3, 6, 2, 2, 5, 5, 5, 28),
      "Simha": (2, 4, 2, 4, 6, 4, 4, 0, 24), "Kanya": (3, 2, 4, 4, 3, 6, 5, 5, 29),
      "Tula": (4, 4, 6, 1, 2, 3, 3, 5, 24), "Vrischika": (5, 5, 4, 5, 4, 3, 3, 4, 28),
      "Dhanu": (2, 5, 2, 2, 7, 6, 5, 2, 29), "Makara": (2, 4, 5, 2, 4, 6, 6, 2, 29),
      "Kumbha": (7, 7, 6, 6, 7, 5, 5, 5, 41), "Meena": (5, 5, 4, 5, 5, 4, 5, 5, 33)}
COL = {'Surya': 1, 'Chandra': 2, 'Mangal': 3, 'Budha': 4, 'Guru': 5,
       'Shukra': 6, 'Shani': 7}
aspects_to = {}
for g in GRAHAS:
    for a in ASPECT.get(g, (7,)):
        aspects_to.setdefault((hs(g) + a - 2) % 12 + 1, []).append(g)


def ymd(t):
    y = int(t); doy = (t - y) * 365.25
    cum = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 366]
    m = max(i for i in range(12) if doy >= cum[i]) + 1
    return f"{['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][m-1]} {y}"


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
    out, tt = [], a
    for k in range(9):
        g, y = VIM[(i + k) % 9]
        d = (b - a) * y / 120
        out.append((g, tt, tt + d)); tt += d
    return out


AD = [(m, l, x, y) for m, a, b in MD for l, x, y in subs(m, a, b)]

# =============================================================================
rule('1.  WHICH HOUSES CARRY JOB LOSS — AND THE FIRST SURPRISE')
tenth = LORD[house_sign(10)]
print(f"""
  Bhavat bhavam: a house is read from another house.  The 12th FROM the 10th is
  the loss of career; the 8th from the 10th is its sudden upheaval.

      the 10th itself         {SIGNS[house_sign(10)]:11s} {', '.join(occupants(10)) or 'empty'}
      the 10th LORD           {tenth} — in the {ordn(hs(tenth))}, COMBUST
      12th from 10th = 9TH    {SIGNS[house_sign(9)]:11s} {', '.join(occupants(9)) or 'empty'}
      8th from 10th = 5TH     {SIGNS[house_sign(5)]:11s} {', '.join(occupants(5)) or 'empty'}
      the 6th, employment     {SIGNS[house_sign(6)]:11s} {', '.join(occupants(6)) or 'empty'}
      badhaka = 7th           {SIGNS[house_sign(7)]:11s} {', '.join(occupants(7)) or 'empty'}
""")
print(f"""  THE FIRST RESULT IS THE ONE THAT SHAPES EVERYTHING ELSE.

      ASPECTS ON THE 10TH HOUSE: {', '.join(aspects_to.get(10, [])) or 'NONE — NOTHING REACHES IT'}

  Section 23 found the 10th is one of only two houses in this chart that
  receive no aspect at all.  Applied to THIS question it says something very
  specific and rather reassuring:

      NO MALEFIC ASPECTS HIS CAREER HOUSE, BECAUSE NOTHING ASPECTS IT.

  The classical signatures of career destruction -- Shani or Mangal or Rahu
  throwing an aspect onto the 10th, a malefic sitting in it, the 10th lord
  hemmed between malefics -- ARE ALL ABSENT.  The 10th holds one graha and it
  is GURU, the great benefic, forming Amala Yoga.

  SO THE CHART CONTAINS NO STRUCTURE FOR CAREER BEING DESTROYED FROM OUTSIDE.
""")

# =============================================================================
rule('2.  THE VULNERABILITY IS THE LORD, NOT THE HOUSE')
print(f"""
  Everything fragile about his career sits in {tenth}, not in the 10th:

      combust           9.00° from Surya, with no exemption (section 25)
      placed            in the 8TH — a dusthana, the house of upheaval
      Shadbala          the only graha in the chart failing its minimum
      Dig Bala          4.28 of 60 — the lowest of any body
      D9                ENEMY sign; it gets worse inside, not better (section 26)
      D10               falls in a D10 dusthana
      career agent      ranks 4th in his own chart, behind Shani, Guru, Shukra

  THE STRUCTURE IS THEREFORE UNUSUAL AND WORTH STATING PLAINLY:

      THE CAREER HOUSE IS PROTECTED AND UNREACHABLE.
      THE CAREER LORD IS THE WEAKEST GRAHA IN THE CHART.

  Which means job loss, where it appears, does NOT arrive as an external event
  striking his position.  It arrives as THE INSTRUMENT FAILING TO HOLD -- his
  own footing, his own clarity about what he is doing, his own visibility.
""")

sub('And the 12th-from-the-10th is the crowded house')
print(f"""
  The loss-of-career house is the 9TH, and it holds {len(occupants(9))} grahas:
  {', '.join(occupants(9))} — including RAHU IN MARANA KARAKA STHANA and SHANI.

  This has to be read carefully rather than dramatically.  The 9th is ALSO the
  trikona of fortune, and the reading has treated it as such throughout.  Both
  are true at once, and the bhavat bhavam layer adds a specific nuance:

      THE SAME HOUSE THAT CARRIES HIS FORTUNE CARRIES THE EXPENDITURE OF HIS
      CAREER.

  Classically, the 12th from a house is where that house's matters are SPENT --
  not destroyed, spent.  Four grahas there says career is repeatedly POURED
  INTO something: dharma, elders, teaching, belief, the father, foreign
  concerns.  It is the structure of a man who gives his working life away to
  something he considers larger, more than once.

  And it is the SAME 9th that section 24 identified as where his gains come
  from.  Career flows out through the house his gains flow in through.
""")

# =============================================================================
rule('3.  WHAT ARGUES AGAINST SERIOUS LOSS')
print(f"""
  Five things, and they are not small:

  1. AMALA YOGA.  A natural benefic alone in the 10th from the lagna gives
     reputation that does not tarnish.  Section 25 found it diminished by an
     enemy sign but NOT cancelled.

  2. THE 10TH IS UNASPECTED.  Nothing can reach it — the point above.

  3. THE 6TH IS HIS STRONGEST HOUSE BY BINDUS ({AV['Kumbha'][8]}), and the 6th is the
     house of the employment relation itself and of winning contests.  A strong
     6th is protection in exactly the domain where jobs are lost: disputes,
     rivals, performance reviews, competition for a role.

  4. THE 10TH IS AN UPACHAYA.  Upachaya houses IMPROVE WITH TIME and are
     strengthened rather than damaged by malefic contact.  His career house is
     structurally the kind that recovers.

  5. THE LAGNA IS VARGOTTAMA (section 26).  Identity does not collapse when
     circumstances do.

  TAKEN TOGETHER: THIS IS NOT A CHART THAT DESCRIBES CAREER RUIN.  It describes
  a career that is hard to build and hard to destroy.
""")

# =============================================================================
rule('4.  THE DATED WINDOWS — WHERE THE RISK ACTUALLY CONCENTRATES')
print("""
  Two things have to coincide for a real disruption: a dasha that activates the
  career apparatus, and a transit that pressures it.  Computed separately, then
  overlapped.

  DASHA SIDE — periods run by the 10th lord, the 8th lord, or Ketu:
""")
RISK = {'Budha': 'the 10th lord itself — combust, in the 8th',
        'Mangal': 'the 8th lord — upheaval, and lord of the 3rd',
        'Ketu': 'severance; the graha that removes wanting'}
for m, l, a, b in AD:
    if b < 2026.6 or a > 2045:
        continue
    if l in RISK:
        print(f"      {m}–{l:8s} {ymd(a)} – {ymd(b):10s} {RISK[l]}")

print("""
  TRANSIT SIDE — Shani crossing the natal 10th, with its own bindu count there:
""")
print(f"""      Shani in Mithuna, the natal 10th : 31 MAY 2032 – 13 JULY 2034
      Shani's own bindus in Mithuna    : {AV['Mithuna'][COL['Shani']]} of 8

  ONE BINDU IS THE WEAKEST PLANET-SIGN CELL IN THE ENTIRE ASHTAKAVARGA OF THIS
  CHART.  Section 17 found it while dating Sade Sati and read it for the Moon;
  read for the CAREER it says something sharper — Saturn crosses his career
  house on the least support any transit in his chart ever has.

  AND IT IS THE THIRD PHASE OF SADE SATI, so the pressure on the mind and the
  pressure on the career house are the same transit.
""")

sub('The overlap, which is the answer to the question')
lo, hi = 2032.42, 2034.53
best = [(m, l, max(a, lo), min(b, hi)) for m, l, a, b in AD
        if min(b, hi) - max(a, lo) > 0.05]
print(f"""
  Shani sits in the natal 10th from {ymd(lo)} to {ymd(hi)}.
  The antardashas running inside that window:
""")
for m, l, a, b in best:
    tag = '   <-- ' + RISK[l] if l in RISK else ''
    print(f"      {m}–{l:8s} {ymd(a)} – {ymd(b)}{tag}")
print(f"""
  A CORRECTION TO THE DRAFT.  I had written the concentration as ending
  {ymd(2033.43)}.  The overlap table above says otherwise: RAHU–KETU ALSO RUNS
  ENTIRELY INSIDE THE SHANI TRANSIT, and Ketu is the more relevant graha of the
  two for this question, not the less.  The window is longer than drafted:

      {ymd(2032.42)} – {ymd(2033.43)}   Shani in the 10th + RAHU–BUDHA
                            the 10th lord's own period, and it is the
                            chart's weakest graha

      {ymd(2033.43)} – {ymd(2034.53)}   Shani in the 10th + RAHU–KETU
                            severance, under the same one-bindu transit

  TWENTY-FIVE MONTHS, IN TWO PHASES, WITH THE THIRD PHASE OF SADE SATI RUNNING
  THROUGHOUT.  Section 17 already called Rahu–Budha "the hinge" and section 44
  called it identity and career reassessment -- both reached before this
  question was asked.

  THAT IS THE CAREER-VULNERABLE STRETCH IN THIS CHART, AND THERE IS ONLY ONE.
  Nothing else in the visible timeline stacks three career-negative factors,
  and the second phase is the more exposed of the two because Ketu is what it
  is.
""")

# =============================================================================
rule('5.  WHAT KIND OF LOSS — AND THIS IS THE REAL ANSWER')
print(f"""
  The chart is unusually clear about the MECHANISM, and it is not the expected
  one.

  AGAINST BEING REMOVED:
      nothing aspects the 10th — no malefic can strike the position
      the 10th holds only Guru, and Amala stands
      the 6th, the house of disputes and rivals, is his strongest by bindus
      the 10th is upachaya — it recovers

  FOR LEAVING:
      KETU is the sole occupant of the three houses of desire (section 27),
        and Ketu's function is to make a thing stop mattering
      section 42 established the chart's central mechanism as SETTING THINGS
        DOWN, and answered "why does he walk away from what he wanted most"
      the 12th-from-the-10th holds four grahas — career is SPENT, given away
      the 10th lord sits in the 8TH, the house of transformation and of
        endings that are not endings

  PUT TOGETHER:

      JOB LOSS IN THIS CHART IS OVERWHELMINGLY LIKELY TO BE RESIGNATION
      RATHER THAN DISMISSAL.

  The structures that would show someone being fired are absent — genuinely
  absent, not weak.  The structures that show someone walking out of a role
  that has stopped meaning anything to him are the strongest signatures the
  chart owns.

  AND THE WARNING FOLLOWS FROM THAT.  In {ymd(2032.42)}–{ymd(2033.43)}, under
  Saturn in the 10th on one bindu and the 10th lord's own weak period, the
  danger is NOT that someone takes his job.  IT IS THAT HE PUTS IT DOWN, at the
  worst possible moment, and calls it a decision.

  Section 44's timeline already carries "do not resign here" against a much
  smaller window in Dec 2028.  THE SAME ADVICE BELONGS TO 2032-34 AND CARRIES
  FAR MORE WEIGHT THERE, and this reading had never put it there.
""")

# =============================================================================
rule('6.  WHAT THIS DOES NOT SAY')
print("""
  1. NO EVENT IS PREDICTED.  The chart describes what kind of pressure a period
     is built to produce and where the structural weakness lies.  Whether a job
     is lost is not something Jyotisha settles.

  2. GAPS BETWEEN JOBS ARE NOT THE SAME AS RUIN, and this chart's 10th is an
     upachaya with an unblemished benefic in it.  Interruption is much better
     supported than collapse.

  3. THE 2032–33 WINDOW IS SIX YEARS OUT.  Nothing here bears on the job he
     holds now; section 28 found the current transits are the favourable
     stretch, running to June 2027.

  4. AND THE CHART'S OWN ADVICE APPLIES.  The 6th outranks the 10th, so a
     change of position is his strongest move — but a change made FROM a
     position, not from having left one.  The distinction is the whole of it.
""")
print('=' * 92)
