#!/usr/bin/env python3
"""
Career and earning through employment -- how it grows from a job held now.

Section 44 already settled the MODE: this chart is built for employment inside
an institution, not for proprietorship.  That leaves the question actually
asked, which is different and has never been computed:

    if he is in a job now, what does the chart say about how it GROWS,
    and what does it say about the MONEY?

Four things get separated here, because the chart treats them differently and
lumping them together is how readings go vague:

    STANDING   the 10th -- position, title, what the work is
    SERVICE    the 6th  -- the employment relation itself, competition
    INCOME     the 11th -- gains arriving, the flow
    RETENTION  the 2nd  -- what stays, accumulated wealth

Nothing here is a new dasha.  Every date is already in the document.  What is
new is the separation of the four channels and the growth curve across them.
"""
import swisseph as swe
from ephem_core import (SIGNS, GRAHAS, SUPPLIED, LORD, VIM, EXALT, IDS, FLAG,
                        varga, sign_of, jd_ut, rule, sub)

POS = dict(SUPPLIED)
LAG = sign_of(POS['Lagna'])
BIRTH_Y = 2002 + (31 + 28 + 31 + 15) / 365.25
NOW = 2026 + (31 + 28 + 31 + 30 + 31 + 30 + 31 + 19) / 365.25   # 19 Aug 2026

hs = lambda g: (sign_of(POS[g]) - LAG) % 12 + 1
house_sign = lambda n: (LAG + n - 1) % 12
occupants = lambda n: [g for g in GRAHAS if hs(g) == n]
rules_of = lambda g: [i for i in range(1, 13) if LORD[(LAG + i - 1) % 12] == g]

SAV = {'Mesha': 21, 'Vrishabha': 22, 'Mithuna': 29, 'Karka': 28, 'Simha': 24,
       'Kanya': 29, 'Tula': 24, 'Vrischika': 28, 'Dhanu': 29, 'Makara': 29,
       'Kumbha': 41, 'Meena': 33}
BRANK = [5, 3, 8, 2, 6, 10, 4, 12, 7, 9, 11, 1]
SP = {'Mangal': 212, 'Shani': 184, 'Budha': 152, 'Surya': 138,
      'Shukra': 95, 'Guru': 81, 'Chandra': 33}
NET = {'Surya': 39.05, 'Shukra': 35.62, 'Guru': 22.20, 'Chandra': 20.05,
       'Budha': -11.41, 'Mangal': -19.21, 'Shani': -34.35}
CAREER = {'Shani': 7.96, 'Guru': 5.89, 'Shukra': 4.53, 'Budha': 3.77,
          'Surya': 3.25, 'Mangal': 2.36, 'Ketu': 2.36, 'Rahu': 1.53,
          'Chandra': 0.14}
MATURE = {'Guru': 16, 'Surya': 22, 'Chandra': 24, 'Shukra': 25,
          'Mangal': 28, 'Budha': 32, 'Shani': 36}
DISP = {'Rahu': 'Shukra', 'Ketu': 'Mangal'}          # shadow -> sign dispositor
val = lambda d, g, dflt=0.0: d.get(g, d.get(DISP.get(g, ''), dflt))


def ymd(t):
    y = int(t)
    doy = (t - y) * 365.25
    m, cum = 1, [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
    for i in range(12):
        if doy >= cum[i]:
            m = i + 1
    return f"{['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][m-1]} {y}"


# --------------------------------------------------------------- dasha tree
span = 360 / 27
ni = int(POS['Chandra'] // span)
into = (POS['Chandra'] - ni * span) / span
lord0 = ['Ketu', 'Shukra', 'Surya', 'Chandra', 'Mangal',
         'Rahu', 'Guru', 'Shani', 'Budha'][ni % 9]
bal = dict(VIM)[lord0] * (1 - into)
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
rule('1.  WHERE HE STANDS RIGHT NOW')
here = [(m, l, a, b) for m, l, a, b in AD if a <= NOW < b][0]
m, l, a, b = here
print(f"""
  Today is 19 August 2026.  Age {NOW - BIRTH_Y:.1f}.

      mahadasha     {m}      {ymd([x for g, x, y in MD if g == m][0])} – """
      f"""{ymd([y for g, x, y in MD if g == m][0])}
      antardasha    {m}–{l}   {ymd(a)} – {ymd(b)}
""")
pd = subs(l, a, b)
cur = [(g, x, y) for g, x, y in pd if x <= NOW < y][0]
print("  Pratyantardashas of the antardasha he is in:\n")
for g, x, y in pd:
    mark = '  <-- now' if (g, x, y) == cur else ''
    print(f"      {m}–{l}–{g:8s}  {ymd(x)} – {ymd(y)}{mark}")
print(f"""
  A JOB TAKEN NOW ATTACHES TO {m}–{l}.  That matters, because {l} is not a
  neutral marker in this chart:

      {l} occupies the 10th house and forms AMALA YOGA there
      {l} rules the 7th and the 4th
      {l} career score {CAREER['Guru']}  — rank 2 of 9 as a career agent
      {l} net Ishta−Kashta {NET['Guru']:+.2f}  — rank 3, and cheap
      {l} matured at age {MATURE['Guru']}, so it runs at full strength

  So the entry point is good, and it is the LAST antardasha of its kind before
  the structural window opens.  This is the on-ramp, not the destination.
""")

# =============================================================================
rule('2.  THE FOUR CHANNELS ARE NOT THE SAME STRENGTH')
print("""
  Readings blur "career" and "money".  This chart separates them sharply, and
  the separation is the whole answer.
""")
CH = [(10, 'STANDING  position, title'), (6, 'SERVICE   the job itself'),
      (11, 'INCOME    gains arriving'), (2, 'RETENTION what stays')]
print(f"  {'':4s}{'channel':32s}{'sign':11s}{'SAV':>4s} {'rank':>5s}  "
      f"{'lord':8s}{'SP':>5s}{'net':>8s}  occupants")
for n, lbl in CH:
    s = house_sign(n)
    ld = LORD[s]
    print(f"  {n:2d}  {lbl:32s}{SIGNS[s]:11s}{SAV[SIGNS[s]]:4d} {BRANK[n-1]:5d}  "
          f"{ld:8s}{val(SP, ld):5.0f}{val(NET, ld):+8.2f}  "
          f"{', '.join(occupants(n)) or '-'}")

print(f"""
  READ THE ROWS AGAINST EACH OTHER:

  SERVICE is the strongest thing he owns.  SAV {SAV['Kumbha']} is the highest of any
  sign in the chart, and the D10 ascendant is the same sign.  THE EMPLOYMENT
  RELATION ITSELF IS THE STRONG PART.

  RETENTION is well served BY ONE MEASURE AND NOT THE OTHER, and that has to be
  said rather than smoothed: the 2nd ranks {BRANK[1]} of 12 by Bhava Bala and its lord
  Shukra carries the best net balance in the chart ({NET['Shukra']:+.2f}) and is the
  Atmakaraka — but its SAV is only {SAV['Tula']}, joint third-lowest of the twelve.
  STRUCTURALLY SOUND, THINLY SUPPLIED.  The vessel is well made; the bindus say
  it does not fill quickly.  Both of those are in the answer.

  INCOME is the weak link, and it is weak twice over:
      the 11th ranks {BRANK[10]} of 12 and carries BOTH Gulika and Mandi
      its lord Chandra has Shodhya Pinda {SP['Chandra']} — THE LOWEST IN THE CHART
      and career score {CAREER['Chandra']} — also the lowest

  STANDING is mid.  The 10th ranks {BRANK[9]}, and its lord Budha is combust in the
  8th, the only graha failing its Shadbala minimum.

  THE SHAPE THAT MAKES:

      he is strong at DOING the job
      he is strong at KEEPING what arrives
      he is weak at the FLOW arriving in the first place
      and the TITLE is the least supported of the four

  That is not a poor chart for earning.  It is a specific one: INCOME GROWS
  SLOWLY AND IS RETAINED WELL, rather than arriving fast and dispersing.
""")

# =============================================================================
rule('3.  SO HOW DOES THE MONEY ACTUALLY ARRIVE?')
print(f"""
  If the flow-house is the weak one, the money has to come from somewhere else.
  The chart is specific about where.

      SHUKRA — 2nd lord — sits in the 8TH HOUSE.
      Highest Ishta Phala in the chart, best net balance, Atmakaraka.

  The 8th is other people's resources, and things that arrive as EVENTS rather
  than as accrual: bonuses, equity that vests, settlements, gratuity, an
  inheritance, a payout attached to an occasion.

  Set that beside the 11th being rank {BRANK[10]} with both shadow points, and the
  prediction is not ambiguous:

      SALARY ACCRETION IS THE WEAK CHANNEL.
      LUMP ARRIVALS ATTACHED TO EVENTS ARE THE STRONG ONE.

  For a salaried person that reads very concretely:  the base rises slowly and
  unspectacularly, and the real jumps come from things that are not the annual
  increment — a switch, a vesting, a payout, a bonus tied to a specific piece
  of work.  HIS INCREMENT IS NOT WHERE HIS MONEY IS.
""")

sub('The 6th is the competition house — and it is the strongest one')
print(f"""
  This is the mechanism, and it follows from the same numbers.

  The 6th at {SAV['Kumbha']} bindus rules service, competition and rivals.  A 6th that
  strong with a 10th that ordinary says growth comes from CONTESTS WON, not
  from position held.  Applying for the thing.  Being measured against others
  and coming out ahead.  Changing employer.

  AND THE 11TH BEING WEAK SAYS THE SAME THING FROM THE OTHER SIDE:  gains do
  not flow to him because he is there.  They arrive when he goes and gets them.

      HIS RAISES COME FROM MOVING, NOT FROM WAITING.
""")

# =============================================================================
rule('4.  THE GROWTH CURVE, DATED')
print("""
  Every antardasha from now to the end of the Rahu mahadasha, scored on the two
  things asked about.  CAREER is the document's existing career score for the
  antardasha lord.  INCOME is built here, transparently:

      rules the 2nd or 11th        +3 each
      occupies the 2nd or 11th     +2 each
      Shodhya Pinda / 212           0–3
      net Ishta−Kashta              ±2 scaled
      dhana karaka (Guru)          +1

  Shadow grahas borrow their sign dispositor's figures, as everywhere else.
""")


def income(g):
    s = 0.0
    r = rules_of(g)
    s += 3 * len({2, 11} & set(r))
    s += 2 * len({2, 11} & {hs(g)}) if g in POS else 0
    s += 3 * val(SP, g) / 212
    s += 2 * val(NET, g) / 39.05
    if g == 'Guru':
        s += 1
    return s


rows = [(m, l, a, b) for m, l, a, b in AD if b > NOW and a < 2041]
print(f"  {'period':16s}{'from':10s}{'to':10s}{'career':>7s}{'income':>8s}   ")
for m, l, a, b in rows:
    c, i = val(CAREER, l), income(l)
    bar = '#' * int(round(c)) + '·' * int(round(i))
    print(f"  {m}–{l:8s}  {ymd(max(a, NOW)):10s}{ymd(b):10s}"
          f"{c:7.2f}{i:8.2f}   {bar}")

best_c = max(rows, key=lambda r: val(CAREER, r[1]))
best_i = max(rows, key=lambda r: income(r[1]))
print(f"""
  PEAK CAREER  {best_c[0]}–{best_c[1]}   {ymd(best_c[2])} – {ymd(best_c[3])}
  PEAK INCOME  {best_i[0]}–{best_i[1]}   {ymd(best_i[2])} – {ymd(best_i[3])}
""")

# =============================================================================
rule('5.  THE TWO MATURITIES THAT SET THE TIMETABLE')
print("""
  This is the finding that most changes the answer, and it needed no new
  computation -- only putting the maturity table next to the career table.

  The two grahas that actually run his career are:
""")
for g in ('Budha', 'Shani'):
    yr = BIRTH_Y + MATURE[g]
    print(f"      {g:8s} matures at {MATURE[g]}  —  {ymd(yr)}   "
          f"career score {CAREER[g]}   ({'the 10th and lagna lord, nominal' if g=='Budha' else 'the actual career engine'})")
print(f"""
  BUDHA rules the 10th and the lagna and is the chart's weakest graha.  It
  matures in {ymd(BIRTH_Y + MATURE['Budha'])}.
  SHANI is the D10 lagna lord, the Amatyakaraka, the lord of the 41-bindu 6th
  and the occupant of D9's 10th -- four career credentials, more than anything
  else in the chart carries.  It matures in {ymd(BIRTH_Y + MATURE['Shani'])}.

  NEITHER OF THEM IS MATURE YET.  He is {NOW - BIRTH_Y:.0f}.

  So the structural statement about growth is this:

      the career-defining antardasha (Rahu–Shani, {ymd(2028.08)} – {ymd(2030.93)})
      runs on a graha that will not be mature for another EIGHT YEARS

      and the identity-and-career hinge (Rahu–Budha, {ymd(2030.93)} – {ymd(2033.43)})
      runs on a graha that does NOT mature until {ymd(BIRTH_Y + MATURE['Budha'])}

  A CORRECTION TO THE DRAFT.  I had written that Budha matures INSIDE its own
  antardasha.  It does not, and the dates say so: Rahu–Budha closes
  {ymd(2033.43)} and Budha matures {ymd(BIRTH_Y + MATURE['Budha'])} — about ten months AFTER.
  The true version is worse for the period and better for what follows:

      THE CAREER HINGE IS RUN BY BUDHA AND FINISHES BEFORE BUDHA IS READY.

  THAT IS THE SHAPE OF THE GROWTH CURVE.  Work laid down before either
  instrument is ready, paying out after they are.  The chart is not describing
  a career that compounds smoothly from a job taken now.  It describes
  FOUNDATION FIRST, RETURN LATER, and it puts the crossover at
  {ymd(BIRTH_Y + MATURE['Budha'])} — which is exactly where section 4's INCOME peak begins.
""")

# =============================================================================
rule('6.  TRANSITS OVER THE FOUR CHANNELS')
print("""
  The two slow grahas crossing any of the four channels, computed as merged
  occupancy intervals rather than ingress dates.
""")
ORD = {1: '1st', 2: '2nd', 3: '3rd', 6: '6th', 10: '10th', 11: '11th'}
TAG = {2: 'RETENTION', 6: 'SERVICE', 10: 'STANDING', 11: 'INCOME'}


def occupancy(g, lo, hi, houses):
    """Merged intervals when g is in one of `houses`.  Retrograde re-entry to
    the same house must EXTEND the interval, not open a second one -- the bug
    that produced a 35-year Sade Sati earlier in this document."""
    out, y = [], lo
    while y < hi:
        jd = jd_ut(int(y), 1, 1, 0, 0, 0, 0) + (y - int(y)) * 365.25
        h = (int(swe.calc_ut(jd, IDS[g], FLAG)[0][0] // 30) - LAG) % 12 + 1
        if h in houses:
            if out and out[-1][0] == h and y - out[-1][2] < 0.75:
                out[-1][2] = y
            else:
                out.append([h, y, y])
        y += 1 / 24
    return out


for g, houses in (('Guru', (2, 6, 10, 11)), ('Shani', (2, 6, 10, 11))):
    for h, a, b in occupancy(g, 2026.63, 2041.0, houses):
        if b - a < 0.1:
            continue
        print(f"      {g:6s} in the {ORD[h]:4s} {TAG[h]:10s} "
              f"{ymd(a)} – {ymd(b)}")

sub('Where transit support and antardasha support actually coincide')
INT = [(g, h, a, b) for g, hh in (('Guru', (2, 6, 10, 11)), ('Shani', (2, 6, 10, 11)))
       for h, a, b in occupancy(g, 2026.63, 2041.0, hh) if b - a >= 0.1]
hits = []
for m, l, x, y in rows:
    ov = [(g, h, max(a, x), min(b, y)) for g, h, a, b in INT
          if min(b, y) - max(a, x) > 0.25]
    if not ov:
        continue
    sc = val(CAREER, l) + income(l)
    hits.append((sc, m, l, x, y, ov))
print(f"\n  {'antardasha':16s}{'car+inc':>8s}   overlapping transit support")
for sc, m, l, x, y, ov in sorted(hits, reverse=True):
    tags = ', '.join(f"{g} {ORD[h]}" for g, h, a, b in ov)
    print(f"  {m}–{l:9s}{sc:8.2f}   {tags}")
top = max(hits)
print(f"""
  THE CONVERGENCE IS {top[1]}–{top[2]}, {ymd(top[3])} – {ymd(top[4])}.

  Four independent things land on the same window and none of them was chosen
  to make them agree:

      the highest INCOME score of any antardasha in the visible timeline
      transit SHANI crossing the 11th, the income house, Jul 2034 – Aug 2036
      BUDHA — the 10th and lagna lord — maturing {ymd(BIRTH_Y + MATURE['Budha'])}
      and the document's existing finding, reached by other means, that
      2033–2037 is the material peak of his thirties

  THAT IS THE ANSWER TO "HOW WILL IT GROW", AND IT IS NOT THE COMFORTABLE ONE:
  the career-defining work happens 2028–2030, and THE MONEY SHOWS UP ABOUT
  FOUR YEARS AFTER IT.
""")

# =============================================================================
rule('7.  WHAT THIS DOES NOT SAY')
print("""
  1. NO AMOUNT.  Jyotisha does not produce a salary figure and this reading has
     refused numeric claims everywhere else; it refuses one here.

  2. NO GUARANTEE OF THE JOB ITSELF.  The premise -- that he holds one -- came
     from him.  The chart is being asked what happens to it, not whether it
     exists.

  3. THE WEAK 11TH IS A STATEMENT ABOUT FLOW, NOT ABOUT POVERTY.  The 2nd is
     rank 3 and its lord has the best net balance in the chart.  Retention is
     strong.  A slow-filling vessel that does not leak is not the same thing as
     an empty one, and the difference matters.

  4. AND THE READING'S STANDING ADVICE APPLIES EXACTLY HERE.  The 6th outranks
     the 10th, so CHANGING WHERE HE STANDS beats working harder in place.  He
     is built to do the second.  That will feel like the right instrument and
     will be the wrong one -- which is already listed among his blind spots.
""")
print('=' * 92)
