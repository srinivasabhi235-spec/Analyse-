#!/usr/bin/env python3
"""
"WHEN WILL HE MEET HIS LIFE PARTNER?"

FIRST, WHAT THE METHOD CAN AND CANNOT ANSWER, because the question and the
apparatus are not quite the same shape.

Jyotisha times VIVAHA -- the activation of the 7th house promise, conventionally
read as marriage.  THERE IS NO CLASSICAL EVENT CALLED "MEETING".  No chapter
gives a rule for when two people first encounter each other, and any reading
that produces a date for that is going beyond what the method supports.  What
CAN be computed is when the 7th house is under simultaneous dasha and transit
pressure, which is the window in which the tradition expects the matter to move.

Computed here:

    1  the significators, and one thing about this 7th house that is unusual
    2  the dasha windows -- every remaining period of the grahas that carry it
    3  the double transit, scanned month by month rather than by ingress
    4  where the two agree
    5  the answer, with the limit stated rather than implied
"""
import swisseph as swe

import ground as G
from ephem_core import SIGNS, GRAHAS, short, nak_of, dignity, rule, sub

swe.set_sid_mode(swe.SIDM_LAHIRI)
F = G.FACTS
V = lambda k: F[k]['value']
ORD = {1: 'st', 2: 'nd', 3: 'rd'}
ordn = lambda n: f"{n}{ORD.get(n, 'th') if n < 21 else 'th'}"
MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
       'Nov', 'Dec']
IDS = {'Guru': swe.JUPITER, 'Shani': swe.SATURN}
FL = swe.FLG_SWIEPH | swe.FLG_SIDEREAL
NOW = swe.julday(2026, 9, 5, 0.0)
Y = G.Y


def date(j):
    y, m, d, _ = swe.revjul(j + 5.5 / 24)
    return f"{int(d):2d} {MON[m-1]} {y}"


def ym(j):
    y, m, _, _ = swe.revjul(j + 5.5 / 24)
    return f"{MON[m-1]} {y}"


def age(j):
    return (j - G.BIRTH_JD) / Y


lon = lambda j, b: swe.calc_ut(j, IDS[b], FL)[0][0] % 360

L7 = V('house7.lord')
UP = V('upapada')
UPL = G.LORD[SIGNS.index(UP)]
DK = V('karaka.Darakaraka')
AK = V('karaka.Atmakaraka')
S7 = G.sign_in_house(7)
S_UP = SIGNS.index(UP)
S7M = (G.MOON_SIGN + 6) % 12

# =============================================================================
rule('1.  THE SIGNIFICATORS — AND WHAT IS UNUSUAL ABOUT THIS 7TH HOUSE')
print(f"""
      the 7th house          {SIGNS[S7]}
      its occupants          {', '.join(V('house7.occupants')) or 'EMPTY'}
      grahas aspecting it    {', '.join(G.aspected_by(7, nodes=False)) or 'NONE'}
      its lord               {L7}, in the {ordn(G.house_of(L7))}, {dignity(L7, G.sign_of(G.POS[L7]))}
      Upapada                {UP} -- the {ordn((S_UP - G.LAG) % 12 + 1)} house, lord {UPL}
      Darakaraka (Jaimini)   {DK}, in the {ordn(G.house_of(DK))}, {dignity(DK, G.sign_of(G.POS[DK]))}
      Shukra, natural karaka in the {ordn(G.house_of('Shukra'))}, Atmakaraka,
                             Ishta {G.ISHTA['Shukra']:.2f} -- the highest in the chart
      7th from the Moon      {SIGNS[S7M]} -- the {ordn((S7M - G.LAG) % 12 + 1)} house

  TWO THINGS ABOUT THIS HOUSE PULL IN OPPOSITE DIRECTIONS AND BOTH ARE REAL.

      IT IS WELL SUPPLIED.  Sarvashtakavarga {V('house7.sav')} -- the second
      highest of the twelve signs -- and Bhava Bala rank {V('house7.bhavarank')} of 12.
      Materially this is one of the better houses in the chart.

      AND NOTHING TOUCHES IT.  No graha sits in it and, on this reading's
      declared drishti rule, no graha aspects it.  It is one of the three
      wholly untouched houses.  (Counting node aspects, Ketu would reach it --
      that is the one dependency, and it is declared.)

  SO THE HOUSE IS NOT WEAK.  IT IS UNATTENDED.  Everything that happens to it
  happens through its lord, because there is no other channel in.

  AND THE LORD IS THE SAME GRAHA TWICE OVER:
""")
print(f"      {L7} is the 7TH LORD and {UPL} is the UPAPADA LORD -- "
      f"{'THE SAME GRAHA' if L7 == UPL else 'different grahas'}.")
print(f"""
  TWO INDEPENDENT SIGNIFICATORS OF MARRIAGE -- one Parashari, one Jaimini --
  RESOLVE TO ONE GRAHA.  That is not the usual case, and it makes the timing
  unusually sharp: whatever {L7} does, the marriage does.  {L7} sits in the
  {ordn(G.house_of(L7))} as the sole occupant, Shadbala {G.SHADBALA_RUPAS[L7]:.2f}
  against a minimum of {G.SHADBALA_MIN[L7]:.1f} -- comfortably passing, and the
  second strongest graha in the chart.
""")

# =============================================================================
rule('2.  THE DASHA WINDOWS')
CARRIERS = {L7: '7th lord and Upapada lord', 'Shukra': 'natural karaka, Atmakaraka',
            DK: 'Darakaraka'}
print(f"""
  A bhava is held to deliver in the periods of the grahas that carry it.  For
  the 7th those are: {', '.join(f'{g} ({w})' for g, w in CARRIERS.items())}.
""")
rows = []
for g, ag, a, b in G.ANTARDASHA:
    if b < NOW or a > G.BIRTH_JD + 60 * Y:
        continue
    w = (2 if ag == L7 else 0) + (1 if ag in CARRIERS else 0) \
        + (1 if g in CARRIERS else 0)
    if w:
        rows.append((w, g, ag, a, b))
print(f"  {'mahadasha':11s}{'antardasha':12s}{'from':13s}{'to':13s}{'age':>5s}"
      f"{'yrs':>7s}   what carries it")
for w, g, ag, a, b in rows:
    tags = []
    if ag in CARRIERS:
        tags.append(f'AD {ag} = {CARRIERS[ag]}')
    if g in CARRIERS:
        tags.append(f'MD {g} = {CARRIERS[g]}')
    live = '  <<< RUNNING NOW' if a <= NOW < b else ''
    print(f"  {g:11s}{ag:12s}{date(a):13s}{date(b):13s}{age(a):5.0f}"
          f"{(b-a)/Y:7.2f}   {'; '.join(tags)}{live}")
cur = [r for r in rows if r[3] <= NOW < r[4]]
print(f"""
  THE STRONGEST DASHA SIGNAL IN THIS CHART IS RUNNING RIGHT NOW.

      {cur[0][1]}-{cur[0][2]}, to {date(cur[0][4]).strip()}.

  {L7} IS THE 7TH LORD AND THE UPAPADA LORD, AND THIS IS ITS ONLY ANTARDASHA IN
  AN EIGHTEEN-YEAR MAHADASHA.  There is not another one until the {L7}
  mahadasha itself opens in {ym([x for x in G.MAHADASHA if x[0] == L7][0][1])},
  at age {age([x for x in G.MAHADASHA if x[0] == L7][0][1]):.0f}.
""")

# =============================================================================
rule('3.  THE DOUBLE TRANSIT, SCANNED MONTH BY MONTH')
ASP = {'Guru': [5, 7, 9], 'Shani': [3, 7, 10]}


def touches(j, body, sign):
    """Does `body` occupy or aspect `sign` at time j?"""
    s = G.sign_of(lon(j, body))
    if s == sign:
        return 'in'
    for a in ASP[body]:
        if (s + a - 1) % 12 == sign:
            return f'{ordn(a)}'
    return None


TARGETS = [('the 7th house', S7), ('the Upapada', S_UP),
           ('the 7th from the Moon', S7M)]
print("""
  A DOUBLE TRANSIT -- Guru AND Shani both occupying or aspecting the same bhava
  -- is the classical condition for that bhava actually delivering.

  SCANNED BY ASPECT, NOT BY INGRESS.  Counting only the months a graha SITS in
  the target throws away most of the evidence, because Guru's 5th and 9th
  aspects and Shani's 3rd and 10th reach two thirds of the chart.  The earlier
  version of this reading made exactly that mistake and its ranking inverted
  once the aspects were included.
""")
hits = {}
j = NOW
while j < G.BIRTH_JD + 45 * Y:
    for name, sg in TARGETS:
        a, b = touches(j, 'Guru', sg), touches(j, 'Shani', sg)
        if a and b:
            hits.setdefault(name, []).append((j, a, b))
    j += 15
for name, sg in TARGETS:
    sub(f'double transit on {name} ({SIGNS[sg]})')
    hs = hits.get(name, [])
    if not hs:
        print('      none in the window scanned')
        continue
    runs, start, prev = [], hs[0][0], hs[0]
    for h in hs[1:]:
        if h[0] - prev[0] > 40:
            runs.append((start, prev[0], prev[1], prev[2]))
            start = h[0]
        prev = h
    runs.append((start, prev[0], prev[1], prev[2]))
    for s, e, ga, sa in runs:
        print(f"      {ym(s):9s} to {ym(e):9s}   {(e-s)/Y*12:5.1f} months"
              f"   Guru {ga}, Shani {sa}   age {age(s):.0f}")

# =============================================================================
rule('4.  WHERE DASHA AND TRANSIT AGREE')
score = {}
j = NOW
while j < G.BIRTH_JD + 45 * Y:
    n = sum(1 for name, sg in TARGETS
            if touches(j, 'Guru', sg) and touches(j, 'Shani', sg))
    if n:
        ad = [x for x in G.ANTARDASHA if x[2] <= j < x[3]]
        if ad:
            g, ag = ad[0][0], ad[0][1]
            w = (2 if ag == L7 else 0) + (1 if ag in CARRIERS else 0) \
                + (1 if g in CARRIERS else 0)
            if w:
                key = (g, ag, ad[0][2], ad[0][3])
                score[key] = score.get(key, 0) + n
    j += 15
print(f"""
  Months in which a double transit falls INSIDE a period carried by a 7th-house
  graha.  This is the intersection, and it is where the tradition would look.
""")
print(f"  {'period':24s}{'window':28s}{'age':>5s}   weighted months")
for (g, ag, a, b), n in sorted(score.items(), key=lambda x: x[0][2]):
    live = '  <<< NOW' if a <= NOW < b else ''
    print(f"  {g + '-' + ag:24s}{date(a) + ' to ' + date(b):28s}"
          f"{age(a):5.0f}   {n * 0.5:5.1f}{live}")

# =============================================================================
rule('4b.  INSIDE THE WINDOW THAT IS RUNNING')
VIM = [('Ketu', 7), ('Shukra', 20), ('Surya', 6), ('Chandra', 10),
       ('Mangal', 7), ('Rahu', 18), ('Guru', 16), ('Shani', 19), ('Budha', 17)]
_g, _ag, _a, _b = cur[0][1], cur[0][2], cur[0][3], cur[0][4]
i0 = [x[0] for x in VIM].index(_ag)
span = _b - _a
print(f"""
  {_g}-{_ag} runs {date(_a).strip()} to {date(_b).strip()}.  Resolving it one level
  further -- the pratyantardasha -- narrows a two-year window to months, and
  the sub-periods of the CARRIER grahas are the ones that matter.
""")
print(f"  {'pratyantardasha':18s}{'from':13s}{'to':13s}{'months':>8s}"
      f"{'DT':>5s}   ")
tt = _a
for k in range(9):
    pg, py = VIM[(i0 + k) % 9]
    pe = tt + span * py / 120
    n = 0
    jj = max(tt, NOW)
    while jj < pe:
        n += sum(1 for _nm, sg in TARGETS
                 if touches(jj, 'Guru', sg) and touches(jj, 'Shani', sg))
        jj += 15
    tag = ''
    if pg in CARRIERS:
        tag = f'   <<< {CARRIERS[pg]}'
    if pe < NOW:
        tag += '   (past)'
    elif tt <= NOW < pe:
        tag += '   <<< NOW'
    print(f"  {pg:18s}{date(tt):13s}{date(pe):13s}{(pe-tt)/Y*12:8.1f}"
          f"{n*0.5:5.1f}{tag}")
    tt = pe
print("""
  READ THE LAST TWO COLUMNS TOGETHER.  A pratyantardasha of a carrier graha
  that ALSO catches double-transit months is the tightest thing this method
  produces, and it is the only level at which a window measured in months
  rather than years can honestly be named.
""")

# =============================================================================
rule('5.  THE ANSWER')
best = sorted(score.items(), key=lambda x: -x[1])[:3]
_nxt = sorted((r for r in rows if r[3] > cur[0][4]), key=lambda r: r[3])[0][1:]
print(f"""
  WHAT THE METHOD ACTUALLY ANSWERS, SAID FIRST SO NOTHING BELOW IS OVERSOLD.

      JYOTISHA TIMES THE ACTIVATION OF THE 7TH HOUSE PROMISE.  There is no
      classical rule for when two people first meet -- not in the fifty-five
      chapters, not anywhere.  What follows are windows in which the 7th is
      under simultaneous dasha and transit pressure.  THAT IS A MARKED PERIOD,
      NOT A DATE, AND IT IS NOT A GUARANTEE THAT ANYTHING HAPPENS IN IT.

  THE STRUCTURE, WHICH MATTERS MORE THAN ANY DATE:

      THE 7TH HOUSE IS WELL SUPPLIED AND COMPLETELY UNATTENDED.  SAV {V('house7.sav')}, the
      second highest in the chart; Bhava Bala rank {V('house7.bhavarank')} of 12; and no graha
      either sits in it or looks at it.  Nothing about the marriage is
      negotiated in public view of the rest of the chart -- it is run entirely
      by its lord, from the {ordn(G.house_of(L7))}.

      AND THE LORD IS DOUBLED.  {L7} is the 7th lord AND the Upapada lord.
      Parashari and Jaimini point at the same graha, which is uncommon, and it
      means the timing question has one answer rather than two competing ones.

  THE WINDOWS, IN ORDER OF WHAT THE COMPUTATION SUPPORTS:
""")
for i, ((g, ag, a, b), n) in enumerate(best, 1):
    print(f"      {i}.  {g}-{ag}   {date(a).strip()} to {date(b).strip()}   "
          f"age {age(a):.0f}-{age(b):.0f}   ({n * 0.5:.1f} weighted months)")
print(f"""
  AND THE HONEST READING OF THAT TABLE:

      THE FIRST WINDOW IS OPEN NOW AND CLOSES {date(cur[0][4]).strip().upper()}.
      {cur[0][1]}-{cur[0][2]} is the only antardasha of the 7th-and-Upapada lord in an
      eighteen-year mahadasha.  If the chart has a near-term answer, this is it,
      and it is not a long window.

      AND THE GAP AFTER IT IS LONG, MEASURED RATHER THAN ESTIMATED.  The next
      period carried by ANY 7th-house graha is {_nxt[0]}-{_nxt[1]}, opening
      {date(_nxt[2]).strip()} -- {(_nxt[2]-cur[0][4])/Y:.1f} years after this one closes, at age
      {age(_nxt[2]):.0f}.  The next period carried by {L7} ITSELF is the {L7} mahadasha,
      opening {ym([x for x in G.MAHADASHA if x[0] == L7][0][1])} -- {([x for x in G.MAHADASHA if x[0] == L7][0][1]-cur[0][4])/Y:.1f} years after.  What lies between is
      carried by Shukra and Surya, which are real significators but second
      order: neither owns the 7th house or the Upapada.

  SO THE ANSWER IS A SHAPE, NOT A DAY:

      THE CHART PUTS ITS STRONGEST MARRIAGE SIGNAL IN THE PERIOD RUNNING RIGHT
      NOW, AND NOTHING OF COMPARABLE WEIGHT ARRIVES FOR OVER A DECADE AFTER
      IT.  That is an unusual profile and it is worth saying
      plainly rather than smoothing into "sometime in your thirties".

      AND WHAT IT WILL NOT SAY: whether the window produces a meeting, a
      marriage, or nothing at all.  A marked window is a window.  Anyone
      offering a date for a first meeting is not reading this chart -- they are
      reading the person in front of them.
""")
print('=' * 92)
