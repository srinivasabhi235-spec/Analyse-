#!/usr/bin/env python3
"""
RAHU THROUGH DHANISHTHA, AND THE D10 LAGNA CLAIM.

The claim put to the chart: people say something will happen as Rahu moves
through Dhanishtha, because his D10 ascendant is involved.

That claim has THREE separable parts and they are not equally sound:

    1. is Rahu actually in Dhanishtha, and for how long?
    2. does Dhanishtha touch the D10 lagna at all?
    3. is "a transit over a divisional-chart ascendant" even a technique?

Part 3 is the one that decides the answer, and it is a methodological question
rather than an astrological one.  It gets settled first, before any
interpretation, because if the technique is unsound the rest is decoration.
"""
import swisseph as swe
from ephem_core import (SIGNS, GRAHAS, SUPPLIED, LORD, FLAG, jd_ut, varga,
                        sign_of, nak_of, short, rule, sub)

swe.set_sid_mode(swe.SIDM_LAHIRI)
NAT = dict(SUPPLIED)
LAG = sign_of(NAT['Lagna'])
D10L = varga(NAT['Lagna'], 10)
NOW = jd_ut(2026, 8, 21, 12, 42, 0, 5.5)
rahu = lambda jd: swe.calc_ut(jd, swe.MEAN_NODE, FLAG)[0][0]
ordn = lambda n: f"{n}{'th' if 10 <= n % 100 <= 20 else {1:'st',2:'nd',3:'rd'}.get(n%10,'th')}"
nat_house = lambda s: (s - LAG) % 12 + 1
MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def cross(target, lo, hi):
    for _ in range(60):
        mid = (lo + hi) / 2
        if ((rahu(mid) - target + 180) % 360 - 180) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def show(jd):
    y, m, d, _ = swe.revjul(jd)
    return f"{int(d)} {MON[m-1]} {y}"


# =============================================================================
rule('1.  IS THE PREMISE EVEN RIGHT?  YES — AND IT IS NEWER THAN IT SOUNDS')
r0 = rahu(NOW)
nk, pd = nak_of(r0)[0], nak_of(r0)[1]
print(f"""
      transit Rahu   {r0:.2f}   {short(r0)}
      nakshatra      {nk} pada {pd}
      sign           {SIGNS[int(r0 // 30)]} — his natal {ordn(nat_house(int(r0 // 30)))} house

  THE PREMISE HOLDS.  Rahu is in Dhanishtha, and his own supplied transit table
  says the same thing.  But the dates matter more than the fact:
""")
e_dh = cross(306.6667, NOW - 800, NOW + 400)
e_ku = cross(300.0, NOW - 100, NOW + 900)
x_dh = cross(293.3333, NOW, NOW + 1400)
print(f"      entered DHANISHTHA          {show(e_dh)}")
print(f"      leaves KUMBHA for Makara    {show(e_ku)}")
print(f"      leaves DHANISHTHA           {show(x_dh)}")
print(f"""
  SO THERE ARE TWO WINDOWS, NOT ONE, AND THEY DO NOT END TOGETHER.

      Rahu in KUMBHA        ... to {show(e_ku)}
      Rahu in DHANISHTHA    ... to {show(x_dh)}

  Dhanishtha straddles a sign boundary: its last two quarters sit in Kumbha and
  its first two in Makara.  Rahu is in the KUMBHA half now and drops into the
  Makara half in December.

  THAT DISTINCTION IS THE WHOLE QUESTION, because everything people attach to
  this transit attaches to KUMBHA, NOT TO DHANISHTHA — and the Kumbha half has
  about {round((e_ku - NOW) / 30.44)} months left, not eight.
""")

# =============================================================================
rule('2.  WHAT KUMBHA IS IN THIS CHART — AND IT IS NOT ONE THING')
print(f"""
  This is why the transit is worth taking seriously at all.  Kumbha carries
  FIVE separate identifications in this reading, arrived at in five different
  sections by five different techniques:

      1. the natal 6TH HOUSE — service, employment, competition, rivals
      2. the D10 ASCENDANT sign (section 11)
      3. the ARUDHA OF THE 10TH, A10 — how the career is perceived (section 30)
      4. the 10TH FROM CHANDRA — one of the three career references (section 30)
      5. the HIGHEST SARVASHTAKAVARGA in the chart, 41 bindus (section 8)

  FIVE CAREER-RELEVANT IDENTITIES ON ONE SIGN.  No other sign in this chart
  carries more than two.

  So the instinct behind the claim is sound even if its stated reason is not:
  A TRANSIT THROUGH KUMBHA CROSSES MORE CAREER SIGNIFICATION THAN A TRANSIT
  THROUGH ANY OTHER SIGN HE HAS.

  And the graha doing the crossing is RAHU, which is running the mahadasha
  until December 2040.  A mahadasha lord crossing the most career-loaded sign
  in its own period is a real conjunction of factors, not a coincidence of
  vocabulary.
""")

# =============================================================================
rule('3.  BUT THE D10 CLAIM ITSELF DOES NOT SURVIVE INSPECTION')
r_d10 = varga(r0, 10)
print(f"""
  THE METHODOLOGICAL QUESTION, STATED PLAINLY.  "Rahu is transiting his D10
  lagna" can mean two quite different things:

      LOOSE   Rahu is in Kumbha, and Kumbha happens to be the sign the D10
              ascendant falls in
      STRICT  Rahu's transit position, MAPPED INTO THE D10, lands on or near
              the D10 ascendant

  Those are not the same claim, and only the strict one would be a transit over
  the D10 lagna in any meaningful sense.  SO IT IS COMPUTED.

      transit Rahu          {r0:.2f}, {SIGNS[int(r0 // 30)]}
      mapped into the D10   {SIGNS[r_d10]}
      D10 ascendant         {SIGNS[D10L]}
      so transit Rahu sits in D10 house {(r_d10 - D10L) % 12 + 1}, NOT the 1st

  THE STRICT CLAIM IS FALSE.  Mapped properly into the dashamsha, transit Rahu
  is nowhere near the D10 ascendant — it falls in the {ordn((r_d10 - D10L) % 12 + 1)} house of that
  chart.  The D10 divides each sign into ten, so a transiting body sweeps a
  whole D10 sign every three degrees; being "on the D10 lagna" lasts about ten
  weeks for Rahu and has nothing to do with Dhanishtha.

  AND THE DEEPER OBJECTION IS WORSE FOR THE CLAIM.  Section 26 already recorded
  that applying transit and aspect logic INSIDE a divisional chart is done by
  many and rejected by others, on the grounds that a varga is a mapping of
  dignity rather than a sky. THIS READING HAS NEVER RUN TRANSITS THROUGH A
  VARGA and does not start now.

      SO: the D10 reason people give is the WEAK part of the claim.
      The Kumbha reason they do not give is the STRONG part.
""")

# =============================================================================
rule('4.  WHAT THE TRANSIT ACTUALLY TOUCHES — READ FROM THE RASHI CHART')
sr = int(r0 // 30)
print(f"""
  Read the ordinary way, from the birth chart, Rahu in Kumbha aspects by its
  5th, 7th and 9th — the convention this document has used throughout:
""")
for a in (5, 7, 9):
    tgt = (sr + a - 1) % 12
    occ = [g for g in GRAHAS if sign_of(NAT[g]) == tgt]
    print(f"      {a}th aspect -> {SIGNS[tgt]:11s} natal {ordn(nat_house(tgt)):5s} "
          f"{', '.join(occ) or 'empty'}")
print(f"""
  THE FIRST ROW IS THE FINDING.

      TRANSIT RAHU'S 5TH ASPECT FALLS ON MITHUNA — HIS NATAL 10TH HOUSE.

  Sections 23 and 29 established that the natal 10th is one of only two houses
  in this chart that receive NO natal aspect at all — a sealed chamber holding
  Guru and reached by nothing.

      SO A TRANSIT IS PRESENTLY REACHING A HOUSE THAT NOTHING NATAL REACHES,
      AND IT IS REACHING NATAL GURU, WHICH RUNS THE CURRENT ANTARDASHA.

  That is a far better reason to take this transit seriously than the D10
  claim, and nobody offering the D10 claim mentioned it.
""")
sub('And it changes target in December')
sm = 9   # Makara
print(f"""
  When Rahu leaves Kumbha on {show(e_ku)} the aspects move with it:
""")
for a in (5, 7, 9):
    tgt = (sm + a - 1) % 12
    occ = [g for g in GRAHAS if sign_of(NAT[g]) == tgt]
    print(f"      {a}th aspect -> {SIGNS[tgt]:11s} natal {ordn(nat_house(tgt)):5s} "
          f"{', '.join(occ) or 'empty'}")
print("""
  From Makara, Rahu's 9th aspect falls on KANYA — the natal lagna itself — and
  its 5th aspect on VRISHABHA, the 9th, where NATAL RAHU SITS with three other
  bodies.

  SO THE SECOND HALF OF THE DHANISHTHA PASSAGE IS THE HEAVIER ONE, not the
  first: it turns the aspect off the career house and onto the SELF and onto
  its own natal position.  If a claim about Dhanishtha is going to be made, it
  belongs to DECEMBER 2026 – APRIL 2027, not to now.
""")

# =============================================================================
rule('5.  THE NAKSHATRA ECHO, WHICH IS REAL AND SMALL')
nn, np_ = nak_of(NAT['Rahu'])[0], nak_of(NAT['Rahu'])[1]
print(f"""
      natal Rahu     {nn} pada {np_}   — lord MANGAL
      transit Rahu   {nk} pada {pd}   — lord MANGAL

  Both are Mangal's nakshatras.  So the transit repeats the natal condition at
  the star level without repeating it at the sign level — which is a genuine
  echo and a modest one.

  It is worth naming because MANGAL is the 8th lord in this chart and ran the
  mahadasha of ages 13.7 to 20.7 (sections 18-19).  A Rahu transit through
  Mangal's star, during a Rahu mahadasha, quietly re-involves the graha that
  governed the transformation already lived.

  THAT IS AN ECHO, NOT AN EVENT, and it is stated at that weight.
""")

# =============================================================================
rule('6.  THE VERDICT ON WHAT PEOPLE SAY')
print(f"""
  1. THE PREMISE IS CORRECT.  Rahu is in Dhanishtha, since {show(e_dh)}.

  2. THE STATED REASON IS WRONG.  "It is his D10 lagna" does not survive
     computation: mapped into the D10, transit Rahu is in that chart's
     {ordn((r_d10 - D10L) % 12 + 1)} house, not its 1st.  And this reading does not run transits
     through vargas at all.

  3. THE REAL REASON IS BETTER THAN THE STATED ONE.  Kumbha carries five
     independent career identifications — the 6th, the D10 ascendant, the A10,
     the 10th from Chandra, and the highest bindu count in the chart — and
     Rahu is the mahadasha lord crossing it.

  4. AND THE SHARPEST FACT IS ONE NOBODY MENTIONED: transit Rahu's 5th aspect
     is currently on the natal 10th, a house nothing natal can reach.

  5. THE DATES ARE NOT WHAT PEOPLE IMPLY.  The Kumbha half ends {show(e_ku)} —
     about {round((e_ku - NOW) / 30.44)} months away, not eight.  The Makara half runs to {show(x_dh)}
     and is the heavier of the two, because from Makara Rahu's aspects move
     onto the LAGNA and onto its own natal position.

  6. AND NOTHING HERE PREDICTS AN EVENT.  A transit marks a window in which a
     particular part of the chart is under pressure.  It does not say what
     happens in it, and the reading has refused that distinction consistently.

  ONE THING TO SET AGAINST ALL OF IT.  Section 28 computed the current gochara
  and found Rahu in the 6th from the lagna and the 10th from the Moon — BOTH
  FAVOURABLE positions for a node by the classical table.  Whatever this
  transit is doing, the standard method calls it well placed.
""")
print('=' * 92)
