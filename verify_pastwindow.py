#!/usr/bin/env python3
"""
The transformation he has already been through, against the one ahead.

Section 18 found that the Mangal mahadasha ran ages 13.7 to 20.7 -- the lord
of the 8th house governing seven years -- and concluded that the 8th-house
life did not begin in 2027 but around age fourteen.

That raises the obvious next question, and it is not rhetorical: IF A MAJOR
8TH-HOUSE PASSAGE HAS ALREADY HAPPENED, DOES THAT CHANGE WHAT 2028-2033 IS?

Three answers are possible and only one of them is right:

  (a) it discharges it   -- the karma is spent, the coming window is lighter
  (b) it repeats it      -- the same thing again, and he should expect a rerun
  (c) it is a different  -- same house, different instrument, different
      instrument on the     capacity to respond
      same target

This scores both windows on the SAME eight markers the reading used for its
forward transformation-window table, extends that scoring backwards to birth
so past and future sit on one scale, and then examines what differed.
"""
import swisseph as swe
from ephem_core import (BIRTH, JD, SIGNS, GRAHAS, COMPUTED, SUPPLIED, LORD,
                        VIM, sign_of, short, local, rule, sub, FLAG)

POS = dict(SUPPLIED)
LAG = sign_of(POS['Lagna'])
MOON_SIGN = sign_of(POS['Chandra'])
EIGHTH = (LAG + 7) % 12
BIRTH_Y = 2002 + (31 + 28 + 31 + 15) / 365.25
TODAY = 2026.63
SP = {'Mangal': 212, 'Shani': 184, 'Budha': 152, 'Surya': 138,
      'Shukra': 95, 'Guru': 81, 'Chandra': 33}
MATURE = {'Guru': 16, 'Surya': 22, 'Chandra': 24, 'Shukra': 25,
          'Mangal': 28, 'Budha': 32, 'Shani': 36}
EIGHTH_LORD = LORD[EIGHTH]
EIGHTH_OCC = [g for g in GRAHAS if sign_of(POS[g]) == EIGHTH]

# ------------------------------------------------------------ dasha sequence
span = 360 / 27
ni = int(POS['Chandra'] // span)
into = (POS['Chandra'] - ni * span) / span
lord0 = ['Ketu', 'Shukra', 'Surya', 'Chandra', 'Mangal',
         'Rahu', 'Guru', 'Shani', 'Budha'][ni % 9]
bal = dict(VIM)[lord0] * (1 - into)
MD, t = [], BIRTH_Y
i0 = [g for g, _ in VIM].index(lord0)
MD.append((lord0, t, t + bal))
t += bal
for k in range(1, 9):
    g, y = VIM[(i0 + k) % 9]
    MD.append((g, t, t + y))
    t += y


def antardashas(md, a, b):
    """(lord, from, to) for every antardasha inside one mahadasha."""
    tot = b - a
    i = [g for g, _ in VIM].index(md)
    out, t = [], a
    for k in range(9):
        g, y = VIM[(i + k) % 9]
        d = tot * y / 120
        out.append((g, t, t + d))
        t += d
    return out


def md_at(y):
    for g, a, b in MD:
        if a <= y < b:
            return g, a, b
    return None, None, None


def ad_at(y):
    g, a, b = md_at(y)
    if not g:
        return None
    for l, x, z in antardashas(g, a, b):
        if x <= y < z:
            return l
    return None


def jd_of(y):
    return swe.julday(int(y), 1, 1, 0) + (y % 1) * 365.25


def lon(y, body):
    return swe.calc_ut(jd_of(y), body, FLAG)[0][0] % 360


# --------------------------------------------------------------- the scoring
def score(y):
    """The reading's eight transformation markers, applied at year y."""
    s, why = 0, []
    md, _, _ = md_at(y)
    ad = ad_at(y)
    if md == EIGHTH_LORD:
        s += 3
        why.append('8th lord MAHADASHA')
    if ad == EIGHTH_LORD:
        s += 2
        why.append('8th lord antardasha')
    if md in EIGHTH_OCC:
        s += 1
        why.append(f'8th occupant MD ({md})')
    if ad in EIGHTH_OCC:
        s += 1
        why.append(f'8th occupant AD ({ad})')
    sat = sign_of(lon(y, swe.SATURN))
    if sat == EIGHTH:
        s += 2
        why.append('transit Shani in natal 8th')
    if sat == (MOON_SIGN + 7) % 12:
        s += 1
        why.append('Ashtama Shani from Chandra')
    if sat in ((MOON_SIGN - 1) % 12, MOON_SIGN, (MOON_SIGN + 1) % 12):
        s += 1
        why.append('Sade Sati')
    if abs(((lon(y, swe.SATURN) - POS['Shani'] + 180) % 360) - 180) < 8:
        s += 2
        why.append('SATURN RETURN')
    r = lon(y, swe.MEAN_NODE)
    dr = abs(((r - POS['Rahu'] + 180) % 360) - 180)
    if dr < 8:
        s += 1
        why.append('Rahu return')
    elif abs(dr - 180) < 8:
        s += 1
        why.append('Rahu half-return')
    for _, a, _ in MD:
        if abs(y - a) < 0.75:
            s += 2
            why.append('mahadasha junction')
            break
    return s, why


rule('1.  THE SAME SCORING, EXTENDED BACKWARDS TO BIRTH')
print(f"""
  8th house       {SIGNS[EIGHTH]}, lord {EIGHTH_LORD}, occupants {EIGHTH_OCC}
  natal Chandra   {SIGNS[MOON_SIGN]}
""")
print(f"  {'year':>6s} {'age':>5s} {'MD-AD':16s} {'score':>5s}  markers")
rows = []
for i in range(0, 56):
    y = 2002.5 + i
    sc, why = score(y)
    rows.append((y, sc, why))
    if sc >= 3 or y < 2024:
        md, _, _ = md_at(y)
        bar = '█' * sc
        print(f"  {int(y):6d} {y-BIRTH_Y:5.1f} {str(md)+'-'+str(ad_at(y)):16s} "
              f"{sc:5d}  {bar:12s} {', '.join(why[:3])}")

sub('the two windows, year by year')
W1 = [r for r in rows if 2015.9 <= r[0] <= 2023.0]
W2 = [r for r in rows if 2027.0 <= r[0] <= 2033.5]
print(f"  {'PAST — Mangal MD':38s}     {'AHEAD — the 2028-2033 window'}")
for a, b in zip(W1, W2):
    print(f"  {int(a[0])}  age {a[0]-BIRTH_Y:4.1f}  score {a[1]}  {'█'*a[1]:6s}"
          f"      {int(b[0])}  age {b[0]-BIRTH_Y:4.1f}  score {b[1]}  {'█'*b[1]}")
t1, t2 = sum(r[1] for r in W1), sum(r[1] for r in W2)
print(f"\n  {'total':14s} {t1:3d}                            {t2:3d}")
print(f"  {'mean':14s} {t1/len(W1):4.1f}                           {t2/len(W2):4.1f}")

sub('THE RESULT CONTRADICTS WHAT THIS SCRIPT EXPECTED, so state it plainly')
print(f"""
  ON THE READING'S OWN MARKERS, THE WINDOW ALREADY LIVED SCORES HIGHER THAN
  THE ONE AHEAD: {t1} against {t2}, mean {t1/len(W1):.1f} against {t2/len(W2):.1f}.

  Before that is believed, one methodological problem has to be admitted.
  The marker "8th lord MAHADASHA" worth 3 points is one THIS SCRIPT ADDED in
  order to extend the scoring backwards.  The document's original forward
  table had no such marker, because no FUTURE mahadasha belongs to Mangal --
  so the marker exists only to describe the past window, and it is worth
  3 points in every one of its seven years.
""")
bias = sum(3 for r in W1 if md_at(r[0])[0] == EIGHTH_LORD)
print(f"      that marker contributes {bias} of the past window's {t1} points")
print(f"      strip it out and the past window scores {t1-bias}, against {t2} ahead")
print(f"""
  SO BOTH READINGS ARE DEFENSIBLE AND THEY DISAGREE:

      counting the 8th lord's mahadasha    past {t1:2d}  vs  ahead {t2:2d}   past is heavier
      not counting it                      past {t1-bias:2d}  vs  ahead {t2:2d}   ahead is heavier

  The honest statement is that THE TWO WINDOWS ARE COMPARABLE IN WEIGHT, and
  which one measures heavier depends entirely on whether you count a
  seven-year mahadasha of the 8th lord as a transformation marker.

  Classical practice does count it.  A mahadasha of the 8th lord is one of the
  standard descriptions of an 8th-house life-phase, and it ran for seven
  straight years where the coming window's transit markers come and go.

  WHAT IS NOT DEFENSIBLE IS THE DOCUMENT'S EXISTING LANGUAGE.  Calling
  2028-2033 "the defining transformation" implied it was both the first and
  the largest.  IT IS NEITHER CLEARLY THE LARGEST NOR THE FIRST.
""")

# ---------------------------------------------------------------------------
rule('2.  SO WAS IT DISCHARGED, REPEATED, OR SOMETHING ELSE?')
print("""
  (a) DISCHARGED -- the karma is spent and the coming window is lighter.
      NO.  Nothing in Parashari says a house is consumed by being activated.
      The 8th fires whenever its lord or occupants are active or transits
      reach it.  And the scoring above shows the coming window is NOT lighter
      than the one already lived -- on one defensible reading it is heavier,
      on the other it is lighter, and neither is negligible.

  (b) REPEATED -- the same thing again.
      NO, and this is the more tempting error.  The two windows are driven by
      COMPLETELY DIFFERENT INSTRUMENTS.
""")
print(f"  {'':30s} {'PAST (2016-2022)':34s} {'AHEAD (2028-2033)'}")
COMPARE = [
    ('what activates the 8th',
     'its own LORD, as mahadasha',
     'TRANSIT Shani, plus Rahu-Budha'),
    ('governing graha',
     'Mangal — SP 212, the highest',
     'Rahu, then Budha — the failing lord'),
    ('Saturn return',
     'no',
     'YES — 2 June 2031'),
    ('Sade Sati',
     'no',
     'YES — from 3 June 2027'),
    ('Ashtama Shani from Chandra',
     'YES — Saturn in Dhanu 2017-20',
     'no'),
    ('Rahu return',
     'YES — 20 Nov 2020, age 18.6',
     'no (half-return ~2030)'),
    ('Bhrigu Bindu crossing',
     'no',
     'YES — 3 Sep 2030, three passes'),
]
for a, b, c in COMPARE:
    print(f"  {a:30s} {b:34s} {c}")
print("""
  Read the first row twice.  In the past window the EIGHTH HOUSE'S OWN LORD
  was running the whole show from the inside.  In the coming one the 8th is
  being worked on FROM OUTSIDE by transit, while the dasha is held by Rahu and
  then by the chart's only failing graha.

  Those are not the same event.  One is the house acting; the other is the
  house being acted upon.
""")

# ---------------------------------------------------------------------------
rule('3.  THE DECISIVE ASYMMETRY — maturity')
print(f"\n  {'graha':9s} {'matures':>8s} {'year':>6s}  during the PAST window?  during the window AHEAD?")
for g, m in sorted(MATURE.items(), key=lambda x: x[1]):
    y = BIRTH_Y + m
    p = 'YES' if 2015.9 <= y <= 2023.0 else '—'
    f = 'YES' if 2027.0 <= y <= 2033.5 else '—'
    star = '   <<<' if g in ('Mangal', 'Shukra') else ''
    print(f"  {g:9s} {m:8d} {y:6.0f}  {p:>22s}  {f:>22s}{star}")
print(f"""
  THE MANGAL MAHADASHA RAN BEFORE MANGAL ITSELF MATURED.

  Mangal matures at 28, in 2030.  Its mahadasha ran ages 13.7 to 20.7, which
  ended more than SEVEN YEARS BEFORE the graha came into its own strength.
  The 8th lord governed seven years of his life while it was still, in the
  classical sense, not yet itself.

  And Mangal's maturation falls INSIDE the coming window -- 2030, the exact
  peak year the forward scoring already identified independently.

  One graha did mature inside the past window -- GURU, in 2018 -- and it is
  the one benefic in a kendra, the Amala giver.  Which is worth noting: the
  only maturation available to him during his hardest early stretch was the
  graha of protection and reputation.

  TWO mature inside or beside the coming one: SHUKRA in 2027 and MANGAL in
  2030 -- the Atmakaraka and the 8th lord itself.
""")

# ---------------------------------------------------------------------------
rule('4.  THE OTHER ASYMMETRY — what he had to respond with')
print("""
  Jyotisha describes structure, not agency, so this part is stated as what it
  is: an observation about the person rather than a computation.

      PAST WINDOW   ages 13.7 to 20.7.  No position, no resources, no
                    independent household, no professional standing.  The 8th
                    arrived and there was nothing to do but undergo it.

      WINDOW AHEAD  ages 25.1 to 31.0.  By the chart's own timeline: married
                    by early 2028, a career foundation antardasha opening the
                    same week, a child around 2029, and Shukra matured in 2027.

  The same house, at an age with something to lose and something to steer.
""")

# ---------------------------------------------------------------------------
rule('5.  WHAT THIS CHANGES IN THE READING')
print("""
  1.  THE COMING WINDOW IS NOT HIS FIRST, AND THE DOCUMENT SHOULD STOP
      IMPLYING IT IS.  Language like "the defining transformation" was written
      as though 2028-2033 were the opening encounter.  It is the second pass.

  2.  IT IS NOT CLEARLY THE HARDER OF THE TWO.  Section 1 scores them as
      comparable, and which is heavier depends on a scoring choice that can
      go either way.  What IS certain is that the coming window carries three
      markers the past one did not -- the Saturn return, Sade Sati and the
      Bhrigu Bindu crossing -- while the past one carried two the coming one
      does not: the 8th lord's own mahadasha and the Rahu return.

  3.  A SEVENTH BLIND SPOT, AND IT IS NEW.  He has survived an 8th-house
      passage already.  The natural inference from that -- "I have been through
      this, I know what it feels like" -- IS WRONG HERE, because the
      instruments differ.  The past window was the 8th lord acting from
      inside, at maximum delivery capacity, with little at stake externally.
      The coming one is transit pressure on a matured apparatus with a
      marriage, a child and a career attached.
      PATTERN-MATCHING THE SECOND TO THE FIRST WILL UNDERSTATE IT.

  4.  IT STRENGTHENS ONE PIECE OF COUNSEL AND WEAKENS NONE.  "Change position,
      don't just push harder" was written for a man who, at fourteen, had no
      position to change.  At twenty-eight he will have one.  The instruction
      becomes actionable for the first time exactly when the chart most needs
      it to be.

  5.  AND ONE GENUINE REASSURANCE, EARNED RATHER THAN OFFERED.  He came
      through seven years governed by the 8th lord at the highest delivery
      capacity in the chart, with only Guru matured and with no resources of
      his own.  D27's zero dusthana occupancy said the transformations were
      survivable.  THE PAST WINDOW IS THE FIRST EVIDENCE THAT THEY ACTUALLY
      WERE -- and it is the only evidence in this document that comes from
      his life rather than from the chart.
""")
print('=' * 92)
