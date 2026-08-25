#!/usr/bin/env python3
"""
WHEN — THE MARRIAGE QUESTION, TIMED IN CLASSICAL ORDER.

"When will he find his soulmate or girl?"

Section 38 fixed where timing belongs: STEP 9, after the bhava, its lord, the
karaka, the varga, both strengths and the afflictions have all been judged.
Steps 1 to 8 for the 7th house are already done in bhava-krama.md and are
recapped here in four lines, not redone.

WHAT THIS SCRIPT ADDS IS THE PART THAT WAS NEVER COMPUTED: the UPAPADA, the
sub-period structure inside the current window, and every classical
marriage-transit trigger with real dates.

ONE THING SAID UP FRONT.  Jyotisha times the ACTIVATION of a promise.  It does
not name a person, guarantee an event, or distinguish "meeting someone" from
"marrying them".  Every window below is a period in which the 7th house is
under period-and-transit pressure.  What is done inside it is not in the chart.
"""
import swisseph as swe
from ephem_core import (SIGNS, GRAHAS, SUPPLIED, LORD, VIM, jd_ut, nak_of,
                        sign_of, dignity, rule, sub)

swe.set_sid_mode(swe.SIDM_LAHIRI)
F = swe.FLG_SWIEPH | swe.FLG_SIDEREAL | swe.FLG_SPEED
POS = dict(SUPPLIED)
LAG = sign_of(POS['Lagna'])
MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
       'Nov', 'Dec']
JD0 = jd_ut(2002, 4, 15, 18, 2, 45, 5.5)
hs = lambda g: (sign_of(POS[g]) - LAG) % 12 + 1
hsign = lambda si: (si - LAG) % 12 + 1
ordn = lambda n: f"{n}{'th' if 10 <= n % 100 <= 20 else {1:'st',2:'nd',3:'rd'}.get(n%10,'th')}"
occ = lambda si: [g for g in GRAHAS if sign_of(POS[g]) == si]


def show(j):
    y, m, d, _ = swe.revjul(j + 5.5 / 24)
    return f"{int(d):>2d} {MON[m-1]} {y}"


def age(j):
    return (j - JD0) / 365.2425


def ingress(body, target_sign, a, b):
    """All entries into target_sign between jd a and b, with motion."""
    out, prev, j = [], None, a
    while j < b:
        x, _ = swe.calc_ut(j, body, F)
        s = sign_of(x[0])
        if prev is not None and s == target_sign and prev != target_sign:
            out.append((j, x[3]))
        prev = s
        j += 1.0
    return out


# =============================================================================
rule('STEPS 1-8, RECAPPED — WHAT IS PROMISED, BEFORE ANY DATE')
S7 = (LAG + 6) % 12
L7 = LORD[S7]
print(f"""
      the bhava     {SIGNS[S7]} — EMPTY, and NO aspect from any graha
      the lord      {L7}, in the {ordn(hs(L7))} — a kendra — in an ENEMY sign, alone
      the karaka    Shukra, in the 8th, Ishta 47.49 — THE HIGHEST IN THE CHART
      the varga     D9 7th is Meena and holds MANGAL and KETU — two malefics
      strength      Bhava Bala 8.86, rank 4 of 12; SAV 33, second-highest
      affliction    lord is badhakesh for a dual lagna, and carries
                    kendradhipati dosha

  A STRONG HOUSE WITH A SPECIFIC AFFLICTION, AND THE AFFLICTION IS IN THE
  NAVAMSA RATHER THAN THE RASHI.  That judgment is fixed before any date is
  named, and nothing below can change it -- only say when it is active.
""")

# =============================================================================
rule('THE UPAPADA — NEVER COMPUTED IN THIS READING UNTIL NOW')
s12 = (LAG + 11) % 12
l12 = LORD[s12]
d = (sign_of(POS[l12]) - s12) % 12
UL = (sign_of(POS[l12]) + d) % 12
if UL == s12 or (UL - s12) % 12 == 6:
    UL = (UL + 9) % 12
ULL = LORD[UL]
UL2 = (UL + 1) % 12
print(f"""
  THE RULE.  The Upapada Lagna is the arudha of the 12th house: count from the
  12th to its lord, then the same distance again from the lord.  It is the
  single most specific marriage indicator Jaimini gives.

      12th house        {SIGNS[s12]}, lord {l12} in {SIGNS[sign_of(POS[l12])]}
      distance          {d} signs
      UPAPADA           {SIGNS[UL]} — his {ordn(hsign(UL))} house
      its lord          {ULL}
      2nd from Upapada  {SIGNS[UL2]}, lord {LORD[UL2]} — the house of the marriage's survival
      occupants of UL   {', '.join(occ(UL)) or 'empty'}

  AND HERE IS THE CONVERGENCE THAT DECIDES THIS QUESTION.

      the 7TH LORD is {L7}.
      the UPAPADA LORD is {ULL}.

  THEY ARE THE SAME GRAHA.  Two independent systems -- Parashari house
  lordship and Jaimini arudha -- hand the marriage to ONE body.  Nothing else
  in this chart has that property.

  Guru also rules the 4th, and the Upapada FALLS in the 4th.  So Guru owns the
  7th, owns the Upapada, and owns the sign the Upapada sits in.
""")

# =============================================================================
rule('STEP 9 — THE DASHA STRUCTURE')
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
        dd = (b - a) * y / 120
        out.append((g, tt, tt + dd))
        tt += dd
    return out


md = [x for x in MD if x[0] == 'Rahu'][0]
AD = subs('Rahu', md[1], md[2])
print("  The Rahu mahadasha, Dec 2022 - Dec 2040, and which antardashas own\n"
      "  the marriage significators:\n")
print(f"  {'antardasha':14s}{'from':14s}{'to':14s}{'age':>12s}   relevance")
for g, a, b in AD:
    rel = ''
    if g == L7:
        rel = '<<< 7TH LORD *AND* UPAPADA LORD'
    elif g == 'Shukra':
        rel = '<<< KARAKA of marriage, highest Ishta'
    elif g == LORD[UL2]:
        rel = '(lord of the 2nd from Upapada)'
    print(f"  Rahu-{g:9s}{show(JD0+a*365.2425):14s}{show(JD0+b*365.2425):14s}"
          f"{a:5.1f} - {b:4.1f}   {rel}")
gu = [x for x in AD if x[0] == L7][0]
sk = [x for x in AD if x[0] == 'Shukra'][0]
print(f"""
  TWO PERIODS CARRY THIS QUESTION AND THEY ARE FAR APART.

      RAHU-GURU    {show(JD0+gu[1]*365.2425)} to {show(JD0+gu[2]*365.2425)}   ages {gu[1]:.1f} to {gu[2]:.1f}
                   the 7th lord AND the Upapada lord.  RUNNING NOW.
      RAHU-SHUKRA  {show(JD0+sk[1]*365.2425)} to {show(JD0+sk[2]*365.2425)}   ages {sk[1]:.1f} to {sk[2]:.1f}
                   the karaka, and the strongest deliverer in the chart.
""")
sub('Inside Rahu-Guru — where Shukra sub-periods fall')
PD = subs(L7, gu[1], gu[2])
for g, a, b in PD:
    mark = '   <<<' if g in ('Shukra', L7) else ''
    print(f"      Rahu-{L7}-{g:9s}{show(JD0+a*365.2425):14s}{show(JD0+b*365.2425):14s}{mark}")
skpd = [x for x in PD if x[0] == 'Shukra'][0]
print(f"""
  THE TIGHTEST DASHA WINDOW THIS CHART OFFERS FOR MARRIAGE:

      RAHU - GURU - SHUKRA        {show(JD0+skpd[1]*365.2425)}  to  {show(JD0+skpd[2]*365.2425)}
      the 7th-and-Upapada lord running the karaka, ages {skpd[1]:.1f} to {skpd[2]:.1f}

  Roughly five months long, and as of the date this was asked (25 August 2026)
  IT HAS NOT STARTED -- it opens in about eleven weeks.
""")

# =============================================================================
rule('STEP 10 — THE DOUBLE TRANSIT, SCANNED MONTH BY MONTH')
print("""
  I FIRST BUILT THIS AS A LIST OF INGRESS DATES -- when Guru ENTERS the 7th,
  the Upapada, the 7th from the Moon.  THAT WAS WRONG AND IT MISSED THE ANSWER.

  A graha influences a bhava by OCCUPYING it OR ASPECTING it, and Guru's 5th,
  7th and 9th aspects reach three signs it never enters.  Scanning occupancy
  only threw away most of the evidence -- including the configuration running
  at this moment.

  SO THIS SCANS EVERY MONTH FROM 2026 TO 2040 AND ASKS: do GURU AND SHANI BOTH
  touch the 7th house, by occupation or aspect?  That is the classical double
  transit, and it is the standard marriage trigger.
""")
GA, SA = (5, 7, 9), (3, 7, 10)


def touches(body, asp, target, j):
    x, _ = swe.calc_ut(j, body, F)
    s = sign_of(x[0])
    if s == target:
        return 'in'
    if target in [(s + a - 1) % 12 for a in asp]:
        return 'aspect'
    return ''


def ad_at(j):
    y = (j - JD0) / 365.2425
    for g, a, b in AD:
        if a <= y < b:
            return f'Rahu-{g}'
    return '-'


j, runs, cur = jd_ut(2026, 1, 1, 0, 0, 0, 5.5), [], None
while j < jd_ut(2041, 1, 1, 0, 0, 0, 5.5):
    g = touches(swe.JUPITER, GA, S7, j)
    s = touches(swe.SATURN, SA, S7, j)
    both = bool(g) and bool(s)
    if both and cur is None:
        cur = [j, g, s]
    elif not both and cur is not None:
        runs.append((cur[0], j, cur[1], cur[2]))
        cur = None
    j += 15.0
if cur:
    runs.append((cur[0], j, cur[1], cur[2]))
print(f"  {'from':14s}{'to':14s}{'Guru':9s}{'Shani':9s}{'ages':>13s}   antardasha")
for a_, b_, gw, sw in runs:
    print(f"  {show(a_):14s}{show(b_):14s}{gw:9s}{sw:9s}"
          f"{age(a_):5.1f} - {age(b_):4.1f}   {ad_at(a_)}")
print(f"""
  THE FIRST ROW IS RUNNING RIGHT NOW.

      SHANI has been IN the 7th house since 30 March 2025.
      GURU aspects the 7th from Karka by its 9th aspect.
      RAHU-GURU -- the 7th lord and Upapada lord -- owns the period.

  DASHA AND DOUBLE TRANSIT COINCIDE, AND THEY ARE COINCIDING NOW.

  AND THE HONEST QUALIFICATION, which most statements of this rule omit: SHANI
  IN THE 7TH IS ALSO THE CLASSICAL SIGNATURE OF DELAY IN MARRIAGE.  The same
  placement that completes the double transit is the one the tradition names
  when a marriage is late.  BOTH READINGS ARE STANDARD AND THEY POINT OPPOSITE
  WAYS.  I am not going to pick one silently:

      as DOUBLE TRANSIT      the 7th is under both great grahas -- activation
      as SHANI IN THE 7TH    the 7th is under its heaviest natural obstruction

  What is NOT ambiguous is that the 7th house is under maximum attention right
  now, and that this coincides with the only antardasha in the whole mahadasha
  owned by the graha that rules both the 7th and the Upapada.
""")

rule('THE ANSWER, RANKED — AND THE RANKING CHANGED WHEN THE SCAN RAN')
ov_a = max(runs[1][0], JD0 + skpd[1] * 365.2425)
ov_b = min(runs[1][1], JD0 + skpd[2] * 365.2425)
print(f"""
  I DRAFTED THE RANKING BEFORE THE DOUBLE-TRANSIT SCAN AND HAD TO REDO IT.

  My first version ranked the windows on DASHA ALONE and gave Rahu-Shukra
  (2034-2037) as a strong second on the strength of the karaka.  The scan says
  something sharper: THREE OF THE SEVEN DOUBLE-TRANSIT WINDOWS BETWEEN NOW AND
  2040 FALL INSIDE RAHU-GURU, and the Rahu-Shukra period contains NONE.

  So the convergence is much more concentrated than the dasha table alone
  suggests.

  1  THE TIGHTEST WINDOW IN HIS CHART            {show(ov_a)} to {show(ov_b)}
     THREE THINGS AT ONCE, and this is the only time they coincide:
         antardasha      Rahu-GURU        -- 7th lord AND Upapada lord
         pratyantardasha Rahu-Guru-SHUKRA -- the karaka of marriage
         transit         DOUBLE TRANSIT on the 7th house
     About ten weeks, ages {age(ov_a):.1f} to {age(ov_b):.1f}.

  2  THE WHOLE OF RAHU-GURU                      now to 31 January 2028
     Ages {gu[1]:.1f} to {gu[2]:.1f}.  Guru is the ONLY graha in this chart that owns both
     the 7th house and the Upapada, and this is its ONLY antardasha in an
     eighteen-year mahadasha.  Two further double-transit windows sit inside it:
     {show(runs[0][0])} - {show(runs[0][1])} (running now) and {show(runs[2][0])} - {show(runs[2][1])}.

  3  APRIL TO JULY 2034                          ages 32.0 to 32.3
     Guru IN the 7th house with Shani aspecting it -- the strongest FORM of
     double transit, Guru occupying rather than aspecting.  But the antardasha
     is RAHU-KETU, and Ketu is the graha of severance sitting in gandanta.
     A strong transit under a poor period.

  4  RAHU-SHUKRA, JULY 2034 - JULY 2037          ages 32.2 to 35.2
     The karaka's own period and the chart's highest Ishta -- but NO double
     transit on the 7th falls inside it.  Strong promise, no trigger.

  WHAT THE CHART DOES NOT SAY, AND I WILL NOT PRETEND OTHERWISE:

      it does not name a person
      it does not distinguish MEETING someone from MARRYING them
      it does not promise that a window produces either
      and the D9 seventh carries MANGAL and KETU, which the krama reads as
      difficulty located INSIDE the marriage rather than in finding it

  ONE MORE THING THAT BELONGS IN AN HONEST ANSWER.  The whole of window 2 has
  SHANI SITTING IN THE 7TH HOUSE, from 30 March 2025 to June 2027 and again to
  February 2028.  That placement is what completes the double transit AND it is
  the classical signature of DELAY in marriage.  The same fact argues both ways
  and the tradition holds both readings.

  THE SENTENCE I WOULD STAND BEHIND:

      The chart's clearest marriage activation is running now and closes
      31 January 2028, with its sharpest point at {show(ov_a)} to {show(ov_b)}.
      It is distinctive not for strength but for CONVERGENCE -- the only graha
      owning both the 7th and the Upapada is running its only period in
      eighteen years, and the double transit falls inside it three times.
      If nothing comes of it, the next comparable convergence is not until
      2034, and it arrives under Ketu.
""")
print('=' * 92)
