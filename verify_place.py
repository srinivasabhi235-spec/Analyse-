#!/usr/bin/env python3
"""
"WHEN WOULD HE FIND HIS PLACE?"

THE QUESTION SPLITS FOUR WAYS AND THE CHART ANSWERS THEM DIFFERENTLY.

"His place" can mean:

    the 4TH   a home, roots, land, the ground under him, inner settledness
    the 10TH  his standing, his position in the world, what he is seen as
    the 11TH  belonging -- the circle, the network, the people he is among
    the 12TH  elsewhere -- foreign residence, retreat, the place away

RATHER THAN PICK ONE, THIS COMPUTES ALL FOUR IN THE CLASSICAL SEQUENCE AND
RANKS THEM.  The comparison is the answer: the chart is emphatic about which
kind of place it gives him, and it is not the one most people would guess.

Steps 1-8 are already done for every house in bhava-krama.md.  This adds the
part that was never done: the four "place" houses set SIDE BY SIDE, and each
one TIMED.
"""
import swisseph as swe
from ephem_core import (SIGNS, GRAHAS, SUPPLIED, LORD, VIM, jd_ut, sign_of,
                        dignity, varga, rule, sub)

swe.set_sid_mode(swe.SIDM_LAHIRI)
F = swe.FLG_SWIEPH | swe.FLG_SIDEREAL | swe.FLG_SPEED
POS = dict(SUPPLIED)
LAG = sign_of(POS['Lagna'])
JD0 = jd_ut(2002, 4, 15, 18, 2, 45, 5.5)
NOW = jd_ut(2026, 8, 25, 12, 0, 0, 5.5)
MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
       'Nov', 'Dec']
NAT_BEN, NAT_MAL = ('Guru', 'Shukra', 'Chandra'), ('Surya', 'Mangal', 'Shani',
                                                   'Rahu', 'Ketu')
ASPECTS = {'Surya': [7], 'Chandra': [7], 'Budha': [7], 'Shukra': [7],
           'Mangal': [4, 7, 8], 'Guru': [5, 7, 9], 'Shani': [3, 7, 10],
           'Rahu': [], 'Ketu': []}
BRUP = [8.39, 9.18, 7.49, 9.28, 7.91, 7.21, 8.86, 7.00, 7.61, 7.39, 7.08, 12.59]
BRANK = [5, 3, 8, 2, 6, 10, 4, 12, 7, 9, 11, 1]
SAV = {'Mesha': 21, 'Vrishabha': 22, 'Mithuna': 29, 'Karka': 28, 'Simha': 24,
       'Kanya': 29, 'Tula': 24, 'Vrischika': 28, 'Dhanu': 29, 'Makara': 29,
       'Kumbha': 41, 'Meena': 33}
RUPAS = {'Surya': 11.39, 'Chandra': 6.42, 'Mangal': 6.33, 'Budha': 6.46,
         'Guru': 8.21, 'Shukra': 6.68, 'Shani': 6.39}
MINREQ = {'Surya': 5.0, 'Chandra': 6.0, 'Mangal': 5.0, 'Budha': 7.0,
          'Guru': 6.5, 'Shukra': 5.5, 'Shani': 5.0}
hs = lambda g: (sign_of(POS[g]) - LAG) % 12 + 1
ordn = lambda n: f"{n}{'th' if 10 <= n % 100 <= 20 else {1:'st',2:'nd',3:'rd'}.get(n%10,'th')}"
occ = lambda si: [g for g in GRAHAS if sign_of(POS[g]) == si]
show = lambda j: (lambda y, m, d, _: f"{int(d):>2d} {MON[m-1]} {y}")(*swe.revjul(j + 5.5 / 24))
age = lambda j: (j - JD0) / 365.2425
asp_onto = lambda si: [(g, a) for g in GRAHAS for a in ASPECTS[g]
                       if (sign_of(POS[g]) + a - 1) % 12 == si]

PLACES = {
    4:  ('A HOME — roots, land, the ground under him, inner settledness',
         ['Chandra', 'Mangal'], 4),
    10: ('A STANDING — his position in the world, what he is seen as',
         ['Surya', 'Budha'], 10),
    11: ('BELONGING — the circle, the network, the people he is among',
         ['Guru'], 11),
    12: ('ELSEWHERE — foreign residence, retreat, the place away',
         ['Shani', 'Ketu'], 12),
}

# Vimshottari
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


def periods(g):
    out = []
    for mg, a, b in MD:
        if mg == g and b > age(NOW):
            out.append((f'{g} MAHADASHA', a, b))
    for ag, a, b in AD:
        if ag == g and b > age(NOW):
            out.append((f'Rahu-{g}', a, b))
    return sorted(out, key=lambda x: x[1])


# =============================================================================
rule('THE FOUR PLACES, SIDE BY SIDE')
rows = []
for h, (what, kar, vn) in PLACES.items():
    s = (LAG + h - 1) % 12
    lord = LORD[s]
    o = occ(s)
    inc = asp_onto(s)
    ben = sorted({g for g, _ in inc if g in NAT_BEN} | {g for g in o if g in NAT_BEN})
    mal = sorted({g for g, _ in inc if g in NAT_MAL} | {g for g in o if g in NAT_MAL})
    rows.append((h, what, s, lord, o, inc, ben, mal))
    print(f"\n  ---- THE {ordn(h).upper()}: {what}")
    print(f"       sign        {SIGNS[s]}")
    print(f"       occupants   {', '.join(o) or 'EMPTY'}")
    print(f"       aspects     {', '.join(f'{g}({ordn(a)})' for g, a in inc) or 'NONE'}"
          f"   [benefic {ben or '-'} / malefic {mal or '-'}]")
    print(f"       lord        {lord}, in the {ordn(hs(lord))}, "
          f"{dignity(lord, sign_of(POS[lord]))}"
          f"{'  RATIO ' + format(RUPAS[lord]/MINREQ[lord], '.2f') if lord in RUPAS else ''}"
          f"{'  FAILS' if lord in RUPAS and RUPAS[lord] < MINREQ[lord] else ''}")
    print(f"       karaka      " + '; '.join(
        f"{k} in the {ordn(hs(k))}, {dignity(k, sign_of(POS[k]))}" for k in kar))
    print(f"       Bhava Bala  {BRUP[h-1]:.2f} rupas, RANK {BRANK[h-1]} of 12")
    print(f"       SAV         {SAV[SIGNS[s]]}")

# =============================================================================
rule('RANKED — AND THE RANKING IS THE ANSWER')
order = sorted(PLACES, key=lambda h: BRANK[h - 1])
print(f"\n  {'place':11s}{'house':7s}{'Bhava Bala':>12s}{'rank':>6s}   lord's condition")
for h in order:
    s = (LAG + h - 1) % 12
    lord = LORD[s]
    cond = f"{lord} {dignity(lord, sign_of(POS[lord]))}, in the {ordn(hs(lord))}"
    if lord in RUPAS and RUPAS[lord] < MINREQ[lord]:
        cond += ', FAILS Shadbala'
    nm = {4: 'a home', 10: 'a standing', 11: 'belonging', 12: 'elsewhere'}[h]
    print(f"  {nm:11s}{ordn(h):7s}{BRUP[h-1]:12.2f}{BRANK[h-1]:6d}   {cond}")
print(f"""
  THE CHART IS NOT AMBIGUOUS ABOUT THIS AND THE ANSWER IS UNCOMFORTABLE.

      THE STRONGEST PLACE HE OWNS IS THE 12TH -- ELSEWHERE.
      Rank 1 of 12, by a margin of 3.31 rupas over the next house, with an
      EXALTED and UNDIVIDED lord that is also the strongest graha in the chart.

      THE SECOND IS THE 4TH -- A HOME.  Rank 2 of 12, lord in a kendra, karaka
      Chandra exalted at the lowest Kashta in the chart, and NOTHING structural
      to flag against it.

      THEN A LARGE GAP.

      HIS STANDING is rank 9 and its lord is the only graha in the chart that
      fails its own minimum.  BELONGING is rank 11, touched by a malefic and
      nothing else.

  SO "HIS PLACE" IS NOT A SINGLE QUESTION WITH ONE DATE.  The chart gives him
  TWO strong places and TWO weak ones, and the two strong ones are A HOME and
  SOMEWHERE ELSE -- which is the same tension section 54 named as walking away
  from what he wanted.
""")

# =============================================================================
rule('TIMED — WHEN EACH PLACE IS ACTIVATED')
for h in order:
    s = (LAG + h - 1) % 12
    lord = LORD[s]
    kar = PLACES[h][1]
    nm = {4: 'A HOME (4th)', 10: 'A STANDING (10th)',
          11: 'BELONGING (11th)', 12: 'ELSEWHERE (12th)'}[h]
    sub(f'{nm} — rank {BRANK[h-1]} of 12')
    seen = set()
    for g in [lord] + kar:
        if g in seen:
            continue
        seen.add(g)
        role = 'LORD' if g == lord else 'karaka'
        for label, a, b in periods(g):
            tag = ''
            if a <= age(NOW) < b:
                tag = '   <<< RUNNING NOW'
            print(f"      {g:8s} ({role:6s}) {label:18s}"
                  f"{show(JD0+a*365.2425):14s}{show(JD0+b*365.2425):14s}"
                  f" ages {a:4.1f}-{b:4.1f}{tag}")

# =============================================================================
rule('THE TRANSIT LAYER — GURU THROUGH THE FOUR PLACES')
print("""
  Guru transiting a bhava, or aspecting it, is the standard trigger for that
  bhava's matters to become live.  Guru's ingresses 2026-2041, with the house
  each sign is:
""")
prev, j = None, jd_ut(2026, 1, 1, 0, 0, 0, 5.5)
while j < jd_ut(2041, 1, 1, 0, 0, 0, 5.5):
    x, _ = swe.calc_ut(j, swe.JUPITER, F)
    s = sign_of(x[0])
    if prev is not None and s != prev and x[3] > 0:
        hh = (s - LAG) % 12 + 1
        note = ''
        if hh in PLACES:
            note = '   <<< ' + {4: 'THE HOME HOUSE', 10: 'THE STANDING HOUSE',
                                11: 'THE BELONGING HOUSE',
                                12: 'THE ELSEWHERE HOUSE'}[hh]
        if hh == 1:
            note = '   <<< over the LAGNA itself'
        print(f"      {show(j)}   Guru -> {SIGNS[s]:11s} = the {ordn(hh):5s}"
              f"  age {age(j):4.1f}{note}")
    prev = s
    j += 2.0

# =============================================================================
rule('THE ANSWER')
print("""
  1  ELSEWHERE IS ALREADY THE STRONGEST THING HE HAS, AND IT IS NOT DATED --
     IT IS STRUCTURAL.  The 12th is the best-built house in this chart by a
     margin of 3.31 rupas, and its lord is EXALTED, UNDIVIDED, and the strongest
     graha he owns.  Nothing has to happen for that to be true; it is true at
     birth.

     WHAT IS DATED IS WHEN IT BECOMES VISIBLE.  Guru enters the 12th on
     1 Nov 2026, retrogrades out, and holds it properly from 27 Jun 2027 to
     late Nov 2027 -- all of it inside Rahu-Guru.  THAT IS NOW AND THE NEXT
     FIFTEEN MONTHS.

  2  A HOME IS THE SECOND-STRONGEST AND IT HAS THREE SEPARATE WINDOWS.

         RAHU-GURU, now to 31 Jan 2028      its LORD's period.  RUNNING NOW.
         Feb 2031 - Mar 2032, ages 28.8-29.9  GURU TRANSITING THE 4TH ITSELF
         GURU MAHADASHA, Dec 2040 - Dec 2056  sixteen years under the home's
                                              lord -- the best mahadasha in
                                              the chart

     Three windows, and the middle one is a transit rather than a period, so it
     is the weakest of the three.  THE LONG ONE IS THE REAL ANSWER: from 38 to
     54, the lord of the home runs the whole show.

  3  A STANDING IS THE WEAK ONE, and its date is Dec 2030 - Jun 2033, when the
     failing lagna-and-career lord runs its antardasha.  Guru transits the 10th
     later, Sep 2036 - Apr 2037, but under Rahu-Surya rather than a career
     period.

     THE PLACE HE IS LEAST EQUIPPED TO FIND IS THE ONE MOST PEOPLE MEAN BY THE
     WORD.

  4  BELONGING IS THE WEAKEST OF THE FOUR -- rank 11 of 12, malefic aspect and
     nothing else -- AND YET ITS LORD IS EXALTED AND UNDIVIDED.  The house and
     the lord flatly contradict each other, which the krama already flagged as
     the sharpest internal disagreement in the chart.  Its period, Rahu-Chandra,
     is Jun 2038 - Dec 2039.

  AND ONE DATE THAT BELONGS TO ALL FOUR AT ONCE.

      GURU CROSSES HIS OWN LAGNA on 28 Nov 2027, retrogrades, and returns
      25 Jul 2028.

  Guru over the ascendant is the classical marker for the person themselves
  becoming established rather than a department of their life.  It falls at the
  very end of Rahu-Guru and just after it -- ages 25.6 to 26.3.

  THE ONE SENTENCE.

      He finds his place soonest in the two houses that mean A ROOF and AWAY,
      and both are live right now: the 4th's lord is running its period to
      31 January 2028, and Guru sits in the 12th for most of that span.

      The durable answer is later and larger -- the GURU MAHADASHA, Dec 2040 to
      Dec 2056, sixteen years run by the lord of the home.

      What he is least equipped to find is a STANDING, which is the sense of
      "place" the question usually carries.

  AND THE CAVEAT THAT MATTERS MOST.  A strong bhava is a CAPACITY, not an
  event.  The 12th being the best house in the chart does not mean he will
  emigrate.  It means that of everything this chart is built to do well, BEING
  SOMEWHERE OTHER THAN WHERE HE STARTED is the thing it does best.
""")
print('=' * 92)
