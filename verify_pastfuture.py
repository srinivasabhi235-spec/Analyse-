#!/usr/bin/env python3
"""
Past against future, in detail -- and specifically how the RESULTS differ.

Section 19 compared the two 8th-house windows by INSTRUMENT and concluded they
are different tools on the same target.  It never asked the next question:
if the instruments differ, HOW DO THE OUTPUTS DIFFER?

This compares them on eight dimensions that can all be computed:

    1. which houses actually get activated, and by what
    2. delivery capacity, duration-weighted
    3. cost, duration-weighted
    4. THE PAYOUT CHANNEL -- who the nakshatra dispositor is
    5. career productivity, on the reading's own career score
    6. what matures inside each
    7. the transit load, and what it targets
    8. the sub-period arc

The fourth turns out to be the sharpest difference and the reading had never
noticed it.
"""
import swisseph as swe
from ephem_core import (SIGNS, GRAHAS, SUPPLIED, LORD, VIM, EXALT, varga,
                        sign_of, nak_of, short, rule, sub, FLAG)

POS = dict(SUPPLIED)
LAG = sign_of(POS['Lagna'])
MOON = sign_of(POS['Chandra'])
EIGHTH = (LAG + 7) % 12
BIRTH_Y = 2002 + (31 + 28 + 31 + 15) / 365.25
hs = lambda g: (sign_of(POS[g]) - LAG) % 12 + 1
rules = lambda g: [i for i in range(1, 13) if LORD[(LAG + i - 1) % 12] == g]
ASPECT = {'Mangal': [4, 7, 8], 'Guru': [5, 7, 9], 'Shani': [3, 7, 10],
          'Rahu': [5, 7, 9], 'Ketu': [5, 7, 9]}
SP = {'Mangal': 212, 'Shani': 184, 'Budha': 152, 'Surya': 138,
      'Shukra': 95, 'Guru': 81, 'Chandra': 33, 'Rahu': 95, 'Ketu': 212}
KASHTA = {'Shani': 46.83, 'Mangal': 38.87, 'Budha': 30.32, 'Guru': 15.10,
          'Shukra': 11.87, 'Surya': 7.83, 'Chandra': 4.49,
          'Rahu': 11.87, 'Ketu': 38.87}
NET = {'Surya': 39.05, 'Shukra': 35.62, 'Guru': 22.20, 'Chandra': 20.05,
       'Budha': -11.41, 'Mangal': -19.21, 'Shani': -34.35,
       'Rahu': 35.62, 'Ketu': -19.21}
CAREER = {'Shani': 7.96, 'Guru': 5.89, 'Shukra': 4.53, 'Budha': 3.77,
          'Surya': 3.25, 'Mangal': 2.36, 'Ketu': 2.36, 'Rahu': 1.53,
          'Chandra': 0.14}
HOUSE = ['self', 'wealth, family, speech', 'effort, siblings, skill',
         'home, mother, schooling', 'children, romance', 'adversity, health',
         'partnership', 'transformation', 'dharma, father, fortune',
         'career, standing', 'gains, networks', 'loss, foreign, moksha']
MATURE = {'Guru': 16, 'Surya': 22, 'Chandra': 24, 'Shukra': 25,
          'Mangal': 28, 'Budha': 32, 'Shani': 36}

# --------------------------------------------------------------- dasha tree
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


def ads(md, a, b):
    i = [g for g, _ in VIM].index(md)
    out, t = [], a
    for k in range(9):
        g, y = VIM[(i + k) % 9]
        d = (b - a) * y / 120
        out.append((g, t, t + d)); t += d
    return out


ALL_AD = []
for g, a, b in MD:
    ALL_AD += [(g, l, x, y) for l, x, y in ads(g, a, b)]


def slice_ad(lo, hi):
    """(md, ad, from, to, weight) for every antardasha overlapping [lo,hi)."""
    out = []
    for md, ad, a, b in ALL_AD:
        x, y = max(a, lo), min(b, hi)
        if y > x:
            out.append((md, ad, x, y, y - x))
    return out


PAST = (2015.978, 2022.978)
FUT = (2027.0, 2033.5)


def wmean(win, tbl):
    s = slice_ad(*win)
    num = sum(tbl[ad] * w for _, ad, _, _, w in s)
    den = sum(w for *_, w in s)
    return num / den


def jd_of(y):
    return swe.julday(int(y), 1, 1, 0) + (y % 1) * 365.25


def tsign(y, body):
    return sign_of(swe.calc_ut(jd_of(y), body, FLAG)[0][0] % 360)


rule('1.  THE TWO WINDOWS')
print(f"""
  PAST    Mangal mahadasha        {PAST[0]:.1f} – {PAST[1]:.1f}   ages {PAST[0]-BIRTH_Y:.1f} – {PAST[1]-BIRTH_Y:.1f}   ({PAST[1]-PAST[0]:.1f} years)
  FUTURE  the 8th-house window    {FUT[0]:.1f} – {FUT[1]:.1f}   ages {FUT[0]-BIRTH_Y:.1f} – {FUT[1]-BIRTH_Y:.1f}   ({FUT[1]-FUT[0]:.1f} years)
""")
for lbl, win in [('PAST', PAST), ('FUTURE', FUT)]:
    print(f"  {lbl} sub-periods:")
    for md, ad, a, b, w in slice_ad(*win):
        print(f"      {md}–{ad:9s} {a-BIRTH_Y:5.1f} – {b-BIRTH_Y:5.1f}  ({w*12:4.1f} months)")

# =============================================================================
rule('2.  WHICH HOUSES ACTUALLY GET ACTIVATED')


def activated(win):
    """Houses touched by the period lords -- ruled, occupied or aspected."""
    hits = {}
    for md, ad, a, b, w in slice_ad(*win):
        for g in {md, ad}:
            for h in rules(g):
                hits[h] = hits.get(h, 0) + w
            hits[hs(g)] = hits.get(hs(g), 0) + w
            for asp in ASPECT.get(g, [7]):
                hh = (hs(g) + asp - 2) % 12 + 1
                hits[hh] = hits.get(hh, 0) + w * 0.5
    return hits


ap, af = activated(PAST), activated(FUT)
print(f"\n  {'house':>5s}  {'signifies':28s} {'PAST':>8s} {'FUTURE':>8s}   shift")
for h in range(1, 13):
    p, f = ap.get(h, 0), af.get(h, 0)
    d = f - p
    mark = ''
    if d > 2:
        mark = '  <<< MUCH MORE in the future'
    elif d < -2:
        mark = '  <<< MUCH MORE in the past'
    print(f"  {h:5d}  {HOUSE[h-1]:28s} {p:8.1f} {f:8.1f}   {d:+5.1f}{mark}")
print(f"""
  THE TARGET MOVES.  The past window loaded the 3rd, 4th, 8th, 9th and 12th --
  effort, HOME, transformation, the FATHER, and loss.  The future window loads
  the 1st, 8th, 9th and 10th -- SELF, transformation, dharma and CAREER.

  Same house at the centre.  COMPLETELY DIFFERENT PERIPHERY.
      the past reached into the FAMILY
      the future reaches into the SELF AND THE WORK
""")

# =============================================================================
rule('3.  DELIVERY AND COST, DURATION-WEIGHTED')
print("""
  Two weightings, because they answer different questions.

    AD    weight only the ANTARDASHA lord -- what is running right now
    MD+AD weight the mahadasha lord and the antardasha lord equally --
          the period's overall colour
""")


def wmean2(win, tbl, blend=False):
    sl = slice_ad(*win)
    den = sum(w for *_, w in sl)
    if not blend:
        return sum(tbl[ad] * w for _, ad, _, _, w in sl) / den
    return sum((tbl[md] + tbl[ad]) / 2 * w for md, ad, _, _, w in sl) / den


print(f"  {'measure':30s} {'PAST(AD)':>9s} {'FUT(AD)':>9s}  "
      f"{'PAST(MD+AD)':>11s} {'FUT(MD+AD)':>11s}")
for lbl, tbl in [('Shodhya Pinda — delivery', SP), ('Kashta — cost', KASHTA),
                 ('net Ishta−Kashta', NET), ('career score', CAREER)]:
    print(f"  {lbl:30s} {wmean2(PAST, tbl):9.2f} {wmean2(FUT, tbl):9.2f}  "
          f"{wmean2(PAST, tbl, 1):11.2f} {wmean2(FUT, tbl, 1):11.2f}")

pD, fD = wmean2(PAST, SP), wmean2(FUT, SP)
pK, fK = wmean2(PAST, KASHTA), wmean2(FUT, KASHTA)
pN, fN = wmean2(PAST, NET), wmean2(FUT, NET)
pC, fC = wmean2(PAST, CAREER), wmean2(FUT, CAREER)
rev = []
for lbl, tbl in [('delivery', SP), ('cost', KASHTA), ('net', NET),
                 ('career', CAREER)]:
    d1 = wmean2(FUT, tbl) - wmean2(PAST, tbl)
    d2 = wmean2(FUT, tbl, 1) - wmean2(PAST, tbl, 1)
    rev.append((lbl, d1, d2, (d1 > 0) == (d2 > 0)))
print(f"\n  {'measure':12s} {'AD diff':>10s} {'MD+AD diff':>11s}   same direction?")
for lbl, d1, d2, same in rev:
    print(f"  {lbl:12s} {d1:+10.2f} {d2:+11.2f}   "
          f"{'YES' if same else 'NO — REVERSES'}")

robust = [l for l, _, _, sm in rev if sm]
print(f"""
  THIS IS THE RESULT, AND IT IS NOT THE ONE THE SCRIPT SET OUT TO FIND.

  THREE OF THE FOUR MEASURES REVERSE depending on which weighting you use.
  Only ONE survives the choice: {robust[0].upper()}.

  Why they reverse is not mysterious.  The past window's MAHADASHA lord is
  MANGAL -- highest delivery in the chart (212), second-worst cost, net
  -19.21.  The future window's is RAHU, which borrows Shukra's numbers --
  modest delivery (95), lowest cost bracket, net +35.62.  So weighting the
  mahadasha lord pulls the past UP on delivery and cost and DOWN on net, and
  does the exact opposite to the future.

  THE HONEST STATEMENT:

      Whether the past or the future window is "heavier" depends on whether
      you weight the CONTINUOUS BACKGROUND (the mahadasha lord, running for
      seven and eighteen years respectively) or the ACTIVE FOREGROUND (the
      antardasha lord, changing every year or two).  BOTH ARE LEGITIMATE
      READINGS.  This document does not get to pick the one it prefers.

  That is the same methodological shape section 19 found when it scored the
  two windows, and it points the same way: THE TWO PERIODS ARE COMPARABLE IN
  WEIGHT AND DIFFERENT IN KIND.

  BUT THE CAREER SCORE IS ROBUST, and that makes it the one number in this
  file worth leaning on:

      career conversion   AD weighting     past {pC:.2f}  ->  future {fC:.2f}
                          MD+AD weighting  past {wmean2(PAST, CAREER, 1):.2f}  ->  future {wmean2(FUT, CAREER, 1):.2f}

  HIGHER IN THE FUTURE ON BOTH.  However you weight it, the coming window
  converts into position and standing in a way the past one structurally
  could not.
""")

# =============================================================================
rule('4.  THE PAYOUT CHANNEL — the difference the reading had missed')
print("""
  Every graha works in one field (its sign lord) and is PAID OUT by another
  (its nakshatra lord).  So the question "what does a period actually hand
  you" is answered by the STAR LORD of its ruling graha, not by the graha.
""")
print(f"\n  {'period lord':12s} {'nakshatra':14s} {'PAID OUT BY':12s} {'Kashta':>7s}  what that channel is")
CH = {
    'Mangal': 'the 12th lord — release, healing, authority',
    'Rahu': 'the 8th lord itself — force, at maximum cost',
    'Budha': 'a SHADOW — no Shadbala figures at all',
    'Shani': 'exalted but Mrita — the thinnest supply in the chart',
    'Guru': 'the Avayogi, from Marana Karaka Sthana',
    'Shukra': 'ITSELF — self-disposited, the only fixed point',
}
for g in ['Mangal', 'Rahu', 'Guru', 'Shani', 'Budha', 'Shukra']:
    n = nak_of(POS[g])
    print(f"  {g:12s} {n[0]:14s} {n[2]:12s} {KASHTA.get(n[2], 0):7.2f}  {CH[g]}")
print(f"""
  NOW APPLY IT.

  THE PAST WINDOW was governed by MANGAL for all seven years.  Mangal stands
  in Krittika, whose lord is SURYA -- Kashta 7.83, the cheapest effective
  graha in the chart, ruler of the 12th, exalted in the 8th, forming Vimala.
      -> everything that period produced was PAID OUT THROUGH RELEASE.

  THE FUTURE WINDOW is governed by RAHU, and its central antardasha from
  December 2030 is RAHU–BUDHA.  Budha stands in Ashwini, whose lord is KETU --
  a shadow with NO strength figures at all.
      -> the hinge of the coming window PAYS OUT THROUGH DISSOLUTION.

  THAT IS THE SHARPEST DIFFERENCE BETWEEN THE TWO PERIODS AND IT IS NOT IN
  THE DOCUMENT ANYWHERE.

      past:    burned by Mangal, collected by SURYA   -> loss that heals
      future:  pressed by Shani, collected by KETU    -> loss that empties

  Surya gives back.  Ketu does not give back -- it removes the wanting.  Those
  are different outcomes from a structurally similar amount of pressure, and
  it is why the past window reads as FORMATIVE and the coming one is described
  throughout this reading as a hinge.
""")

# =============================================================================
rule('5.  WHAT MATURES INSIDE EACH')
print(f"\n  {'graha':9s} {'matures':>7s} {'year':>6s}  PAST?  FUTURE?  what it is")
WHAT = {'Guru': 'the one kendra benefic, Amala giver',
        'Surya': 'exalted, vargottama, 12th lord',
        'Chandra': 'exalted but Mrita',
        'Shukra': 'the ATMAKARAKA',
        'Mangal': 'THE 8TH LORD ITSELF',
        'Budha': 'lagna and 10th lord',
        'Shani': 'Amatyakaraka'}
for g, m in sorted(MATURE.items(), key=lambda x: x[1]):
    y = BIRTH_Y + m
    p = 'yes' if PAST[0] <= y <= PAST[1] else '—'
    f = 'yes' if FUT[0] <= y <= FUT[1] else '—'
    star = '  <<<' if f == 'yes' else ''
    print(f"  {g:9s} {m:7d} {y:6.0f}  {p:>5s}  {f:>6s}   {WHAT[g]}{star}")
print("""
  ONE matured in the past window: Guru, the protective graha.
  TWO mature in the coming one: SHUKRA (2027) and MANGAL (2030) -- the
  Atmakaraka and the 8th lord itself.

  So the past window ran an IMMATURE 8th lord and had the protective graha
  come online inside it.  The coming window runs a MATURE 8th lord and has the
  soul-significator come online at its start.  Structurally that is a period
  with more capacity and less shelter.
""")

# =============================================================================
rule('6.  THE TRANSIT LOAD, AND WHAT IT TARGETS')
print(f"\n  {'':10s} {'PAST 2016-2022':34s} {'FUTURE 2027-2033'}")
T = [('Saturn sign path', 'Vrischika -> Dhanu -> Makara', 'Meena -> Mesha -> Vrishabha -> Mithuna'),
     ('from the LAGNA', '3rd, 4th, 5th', '7th, 8TH, 9th, 10TH'),
     ('from the MOON', '7th, 8TH, 9th', '12th, 1ST, 2ND — Sade Sati'),
     ('Ashtama Shani', 'YES — 3 years, from the Moon', 'no'),
     ('Sade Sati', 'no', 'YES — from 3 Jun 2027'),
     ('Saturn in the natal 8th', 'no', 'YES — 3 passes, Jun 2027 to Apr 2030'),
     ('Saturn return', 'no', 'YES — 2 Jun 2031'),
     ('Rahu return', 'YES — 20 Nov 2020', 'no (half-return ~2030)'),
     ('Bhrigu Bindu', 'no', 'YES — 3 Sep 2030, 3 passes')]
for a, b, c in T:
    print(f"  {a:10s} {b:34s} {c}")
print("""
  THE PAST WINDOW'S SATURN WORKED FROM THE MOON.  Ashtama Shani is a transit
  over the 8th from Chandra -- it presses the MIND and the emotional supply,
  and it does not touch the ascendant.

  THE FUTURE WINDOW'S SATURN WORKS FROM THE LAGNA AND THE MOON AT ONCE.  Sade
  Sati is over the Moon; transit Saturn is simultaneously in the natal 8th;
  and the Saturn return falls inside it.  Three separate Saturn mechanisms
  where the past had one.

  That is the clearest answer to "how do the results differ":
      PAST     pressure on the INNER LIFE, with the outer world unchanged
      FUTURE   pressure on the OUTER STRUCTURE, with the inner life already
               built
""")

# =============================================================================
rule('7.  THE ARC, SIDE BY SIDE')
print("""
                PAST  2016 – 2022                FUTURE  2027 – 2033
  ------------  ---------------------------  ---------------------------------
  opens with    Rahu — a break with the      Guru — the 7th and 4th lord.
                inherited.  Nothing chosen.  MARRIAGE, and it is chosen.

  the middle    Guru, Shani, Budha under     Shani — the D10 lagna lord and
                three years of Ashtama       Amatyakaraka.  THE CAREER
                Shani.  Endurance.           FOUNDATION.  Construction.

  the hinge     Budha at 17-18 — the         Budha from Dec 2030 — the same
                who-are-you question,        graha, now with a career and a
                answered by the chart's      family attached, under the
                weakest graha, with          Saturn return and Sade Sati
                nothing at stake             at peak.  EVERYTHING at stake.

  closes with   Shukra — the Atmakaraka.     Ketu then Shukra (2033-2037) —
                THE TURN, at the end.        withdrawal, then the material
                                             peak.

  net effect    FORMATION                    CONVERSION
                something burned away        something built, tested to
                before anything was built    destruction, and what survives
                                             is load-bearing for thirty years
""")

# =============================================================================
rule('8.  HOW THE RESULTS DIFFER — the summary')
print(f"""
  Eight dimensions, and they line up into one distinction.

  {'':26s} {'PAST':>22s}   {'FUTURE':>22s}
  {'-'*26} {'-'*22}   {'-'*22}
  {'target':26s} {'family, home, father':>22s}   {'self, career, marriage':>22s}
  {'delivery — AD / MD+AD':26s} {f'{wmean2(PAST,SP):.0f} / {wmean2(PAST,SP,1):.0f}':>22s}   {f'{wmean2(FUT,SP):.0f} / {wmean2(FUT,SP,1):.0f}':>22s}
  {'cost — AD / MD+AD':26s} {f'{wmean2(PAST,KASHTA):.1f} / {wmean2(PAST,KASHTA,1):.1f}':>22s}   {f'{wmean2(FUT,KASHTA):.1f} / {wmean2(FUT,KASHTA,1):.1f}':>22s}
  {'career — AD / MD+AD':26s} {f'{wmean2(PAST,CAREER):.2f} / {wmean2(PAST,CAREER,1):.2f}':>22s}   {f'{wmean2(FUT,CAREER):.2f} / {wmean2(FUT,CAREER,1):.2f}':>22s}
  {'paid out through':26s} {'SURYA — release':>22s}   {'KETU — dissolution':>22s}
  {'grahas maturing':26s} {'1 (Guru)':>22s}   {'2 (Shukra, Mangal)':>22s}
  {'Saturn mechanisms':26s} {'1 (Ashtama Shani)':>22s}   {'3 (SS, 8th, return)':>22s}
  {'what is at stake':26s} {'nothing external':>22s}   {'marriage, child, work':>22s}

  DELIVERY AND COST DO NOT SETTLE IT -- they reverse with the weighting, and
  section 3 says so rather than picking a favourite.  THREE THINGS DO SETTLE
  IT, because none of them depends on a scoring choice:

      THE TARGET MOVED.  Family, home and father in the past; self, career and
      marriage in the future.  Computed in section 2 from lordship, occupancy
      and aspect, not from weighting.

      THE PAYOUT CHANNEL INVERTED.  Surya then, Ketu now.  A fact about
      nakshatra dispositors, with no arithmetic in it at all.

      CAREER CONVERSION IS HIGHER AHEAD ON BOTH WEIGHTINGS.  The one measure
      robust to the choice.

  THE PAST PRODUCED A PERSON.  Aimed at the family, paid out through the graha
  of release, with nothing external to lose and almost no conversion into the
  world.  It burned things away and left someone who works alone under load.
  That is FORMATION.

  THE FUTURE PRODUCES A LIFE.  Aimed at the self and the work, three Saturn
  mechanisms instead of one, a marriage and a child and a career attached to
  the outcome, and the highest career conversion of anything before 2040.
  That is CONVERSION.

  AND THE PAYOUT CHANNELS ARE OPPOSITE, which is the deepest difference:

      what the past took, SURYA gave back as authority and healing
      what the future takes, KETU does not give back -- it removes the wanting

  So the honest answer to "how do the results differ" is NOT that one is
  harder.  Section 19 established they are comparable in weight.  It is that

      THE PAST COST HIM THINGS HE HAD NOT CHOSEN AND RETURNED A SELF.
      THE FUTURE COSTS HIM THINGS HE WILL HAVE CHOSEN AND RETURNS A ROLE.

  One built the instrument.  The other plays it, and charges admission.
""")
print('=' * 92)
