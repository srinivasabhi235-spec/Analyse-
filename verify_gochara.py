#!/usr/bin/env python3
"""
THE CURRENT TRANSIT -- verified against the ephemeris, then read.

He supplied a live transit table.  This document's discipline with supplied
data is to VERIFY IT FIRST (section 2 did that with the birth data and found a
constant ayanamsa offset), so the same is done here before a word of
interpretation.

Then the transits are read properly -- gochara from the natal Moon, which is
the classical reference, and from the natal lagna, with each transit weighted
by the TRANSITING GRAHA'S OWN BINDUS in the sign it occupies.  That is the
Ashtakavarga method for judging a transit and it is the one thing that
separates a real transit reading from a list of positions.
"""
import swisseph as swe
from ephem_core import (SIGNS, GRAHAS, SUPPLIED, LORD, EXALT, IDS, FLAG,
                        BIRTH, jd_ut, dignity, sign_of, short, rule, sub)

swe.set_sid_mode(swe.SIDM_LAHIRI)
NAT = dict(SUPPLIED)
LAG = sign_of(NAT['Lagna'])
MOON = sign_of(NAT['Chandra'])
JD_T = jd_ut(2026, 8, 21, 12, 42, 0, 5.5)
ordn = lambda n: f"{n}{'th' if 10 <= n % 100 <= 20 else {1:'st',2:'nd',3:'rd'}.get(n%10,'th')}"

SUP = {'Surya': 124.03, 'Chandra': 227.07, 'Mangal': 72.29, 'Budha': 117.41,
       'Guru': 107.18, 'Shukra': 169.75, 'Shani': 349.97,
       'Rahu': 305.63, 'Ketu': 125.63}
OUTER = {'Arun (Uranus)': (41.28, swe.URANUS),
         'Varun (Neptune)': (339.67, swe.NEPTUNE),
         'Yam (Pluto)': (279.11, swe.PLUTO)}
# Bhinnashtakavarga: (lagna, Su, Ch, Ma, Bu, Gu, Sk, Sa, SAV) -- from verify_bala
AV = {"Mesha": (4, 2, 2, 1, 4, 4, 5, 3, 21), "Vrishabha": (4, 3, 2, 3, 4, 5, 3, 2, 22),
      "Mithuna": (3, 4, 6, 4, 6, 5, 3, 1, 29), "Karka": (8, 3, 6, 2, 2, 5, 5, 5, 28),
      "Simha": (2, 4, 2, 4, 6, 4, 4, 0, 24), "Kanya": (3, 2, 4, 4, 3, 6, 5, 5, 29),
      "Tula": (4, 4, 6, 1, 2, 3, 3, 5, 24), "Vrischika": (5, 5, 4, 5, 4, 3, 3, 4, 28),
      "Dhanu": (2, 5, 2, 2, 7, 6, 5, 2, 29), "Makara": (2, 4, 5, 2, 4, 6, 6, 2, 29),
      "Kumbha": (7, 7, 6, 6, 7, 5, 5, 5, 41), "Meena": (5, 5, 4, 5, 5, 4, 5, 5, 33)}
COL = {'Surya': 1, 'Chandra': 2, 'Mangal': 3, 'Budha': 4, 'Guru': 5,
       'Shukra': 6, 'Shani': 7}
# Classical gochara: houses FROM THE NATAL MOON in which each graha is benefic
GOOD = {'Surya': {3, 6, 10, 11}, 'Chandra': {1, 3, 6, 7, 10, 11},
        'Mangal': {3, 6, 11}, 'Budha': {2, 4, 6, 8, 10, 11},
        'Guru': {2, 5, 7, 9, 11}, 'Shukra': {1, 2, 3, 4, 5, 8, 9, 11, 12},
        'Shani': {3, 6, 11}, 'Rahu': {3, 6, 10, 11}, 'Ketu': {3, 6, 11}}

# =============================================================================
rule('1.  VERIFYING THE SUPPLIED TRANSIT DATA')
print("""
  The Moon fixes the moment: it moves about 13 degrees a day, so a match to
  the arcminute pins the time to a couple of minutes.  Searching 18-24 August
  2026 for a Moon at 227.07 sidereal returns ONE answer.

      21 AUGUST 2026, 12:42 IST.  Which is today.

  Every graha checked against Swiss Ephemeris with Lahiri ayanamsa:
""")
print(f"  {'body':9s}{'supplied':>10s}{'computed':>10s}{'diff':>9s}   sign")
worst = 0.0
for g, v in SUP.items():
    if g in ('Rahu', 'Ketu'):
        x = swe.calc_ut(JD_T, swe.MEAN_NODE, FLAG)[0][0]
        if g == 'Ketu':
            x = (x + 180) % 360
    else:
        x = swe.calc_ut(JD_T, IDS[g], FLAG)[0][0]
    d = ((x - v + 180) % 360 - 180) * 60
    worst = max(worst, abs(d))
    print(f"  {g:9s}{v:10.2f}{x:10.2f}{d:8.1f}'   {SIGNS[int(v // 30)]}")
print(f"\n  Worst disagreement across all nine: {worst:.1f} arcminutes.")

sub('The outer planets, verified and then set aside')
for name, (v, pid) in OUTER.items():
    x = swe.calc_ut(JD_T, pid, FLAG)[0][0]
    print(f"      {name:17s} supplied {v:7.2f}  computed {x:7.2f}  "
          f"diff {((x - v + 180) % 360 - 180) * 60:+5.1f}'")
print("""
  Uranus and Neptune reproduce to half an arcminute.  PLUTO IS OUT BY 22.8',
  which is too large to be rounding -- different sources use different Pluto
  models and the discrepancy is his source's, not an error in the rest of the
  table.  It changes nothing here.

  THEY ARE NOT USED BELOW.  Parashari jyotisha works with
  nine grahas; Uranus, Neptune and Pluto have no rulership, no aspect doctrine,
  no dasha and no place in any of the techniques this reading applies.
  Including them would be borrowing from a different system mid-sentence.
""")

sub('And one row that does NOT verify')
asc = swe.houses_ex(JD_T, BIRTH['lat'], BIRTH['lon'], b'P', swe.FLG_SIDEREAL)[1][0]
print(f"""
      supplied Lagna    83.90   (Mithuna 23°54')
      Guntur ascendant  {asc:.2f}   ({SIGNS[int(asc // 30)]} {asc % 30:.2f}°) at 12:42 IST

  THAT IS NOT A SMALL DISCREPANCY -- it is most of a chart apart.  Working
  backwards: an ascendant of 83.90 occurs at Guntur at 03:02 IST, about ten
  hours earlier, at which point the Moon would be 222.27 rather than 227.07.
  Solving instead for a longitude that would give that ascendant at this
  instant returns -65°, which is the western Atlantic.

  SO THE ASCENDANT ROW DOES NOT BELONG TO THE SAME MOMENT AS THE PLANETS.
  Some transit pages render a live planetary table beside an ascendant computed
  for a stored location or a stale timestamp; that is the likeliest cause.

  AND IT DOES NOT MATTER FOR ANYTHING BELOW, which is worth saying clearly:
  GOCHARA IS READ FROM THE NATAL MOON AND THE NATAL LAGNA.  The transit
  ascendant plays no part in it.  The one row that cannot be verified is the
  one row the technique does not use.
""")

# =============================================================================
rule('2.  WHERE THE TRANSITS FALL IN HIS CHART')
print(f"""  Natal lagna {SIGNS[LAG]}.  Natal Chandra in {SIGNS[MOON]}.
""")
print(f"  {'graha':9s}{'transit sign':13s}{'dignity':13s}{'from lagna':12s}"
      f"{'from Moon':11s}{'own bindus':>11s}  gochara")
rows = []
for g in GRAHAS:
    s = int(SUP[g] // 30)
    hl = (s - LAG) % 12 + 1
    hm = (s - MOON) % 12 + 1
    b = AV[SIGNS[s]][COL[g]] if g in COL else None
    dg = dignity(g, s) if g in COL else 'shadow'
    good = hm in GOOD[g]
    rows.append((g, s, hl, hm, b, good))
    print(f"  {g:9s}{SIGNS[s]:13s}{dg:13s}{ordn(hl) + ' house':12s}"
          f"{ordn(hm):11s}{('—' if b is None else str(b)):>11s}  "
          f"{'FAVOURABLE' if good else 'not favourable'}")
nf = sum(1 for r in rows if r[5])
print(f"""
  {nf} of 9 favourable by classical gochara from the Moon.
""")

# =============================================================================
rule('3.  THE FOUR THINGS THAT ACTUALLY MATTER TODAY')
sub('1.  Guru is EXALTED, in his 11th, during its own antardasha')
print(f"""
      transit Guru   {SIGNS[3]} — its EXALTATION sign
      natal house    11th, gains and income
      own bindus     {AV['Karka'][COL['Guru']]} of 8
      and the running antardasha is RAHU–GURU, to 31 January 2028

  THREE THINGS POINT AT THE SAME GRAHA AT THE SAME TIME: the antardasha lord,
  its exaltation, and the income house.  Section 22 computed the transit window
  "Guru in the 11th, Aug 2026 – Jun 2027" from the ephemeris; this is that
  window, confirmed by his own supplied data, WITH the exaltation the section
  did not mention.

  AND THE COUNTER-READING, WHICH HAS TO BE GIVEN EQUAL WEIGHT.  Measured the
  classical way -- from the natal Moon -- Guru is in the 3RD, and the 3rd is
  NOT one of Guru's benefic gochara houses (2, 5, 7, 9, 11).  So:

      from the natal LAGNA   Guru is in the 11th, exalted, on 5 bindus  GOOD
      from the natal MOON    Guru is in the 3rd                          NOT GOOD

  THE TWO REFERENCES DISAGREE, and this reading does not get to keep only the
  favourable one.  Gochara is classically weighted from the Moon, which argues
  the transit is less helpful than the exaltation makes it look; the bindu
  count and the house-from-lagna argue the other way.

  WHAT SURVIVES BOTH READINGS: it is the antardasha lord, it is exalted, and it
  is in the income house until the window section 22 dated to June 2027.  That
  is real and it is qualified -- which is the same shape as everything else in
  this chart.
""")

sub('2.  Shani is in the 11th from the Moon — its single best position')
print(f"""
      transit Shani  {SIGNS[11]}, natal 7th house, {ordn((11 - MOON) % 12 + 1)} from the Moon
      own bindus     {AV['Meena'][COL['Shani']]} of 8

  THE 3RD, 6TH AND 11TH FROM THE MOON ARE THE ONLY PLACES SATURN IS BENEFIC IN
  GOCHARA, AND IT IS IN THE BEST OF THEM.

  AND THAT IS THE WHOLE POINT OF THIS MOMENT.  Saturn leaves Meena for Mesha on
  3 JUNE 2027 -- the 12th from his natal Moon -- AND SADE SATI BEGINS.  So the
  transit is currently in its most favourable classical position and its next
  move is into its worst.

      RIGHT NOW           Shani 11th from Moon, benefic, 5 bindus
      FROM 3 JUNE 2027    Shani 12th from Moon, SADE SATI OPENS

  Section 21 dated the marriage window's close to 3 June 2027 and section 20
  called it "the clear window".  This is what it looks like from inside: the
  clear part is running now, and it has about nine months left.
""")

sub('3.  Budha is combust, on 2 bindus, and it is running the pratyantardasha')
d = min(abs(SUP['Budha'] - SUP['Surya']), 360 - abs(SUP['Budha'] - SUP['Surya']))
print(f"""
      transit Budha  {SIGNS[3]}, natal 11th house
      {d:.2f}° from transit Surya — COMBUST (his table marks it too)
      own bindus     {AV['Karka'][COL['Budha']]} of 8 — the lowest of any transiting graha
      gochara        3rd from the Moon, which is NOT in Budha's benefic set

  AND THE CURRENT PRATYANTARDASHA IS RAHU–GURU–BUDHA, MAY TO SEPTEMBER 2026.

  So the sub-sub-period lord is, at this moment, combust, on two bindus, and in
  an unfavourable gochara house.  BUDHA IS ALSO HIS NATAL LAGNA LORD AND 10TH
  LORD, AND IT IS COMBUST NATALLY TOO -- the same affliction repeating in
  transit over the graha that already carries it.

  THIS IS THE WEAKEST FEW WEEKS IN THE CURRENT ANTARDASHA, and it ends in
  September when Rahu–Guru–Ketu takes over.  Nothing dramatic is implied.  It
  is a reason not to read the last month as representative of the window.
""")

sub('4.  Mangal is 2.5° from his natal Guru')
gap = abs(SUP['Mangal'] - NAT['Guru'])
print(f"""
      transit Mangal  {SUP['Mangal']:.2f}   ({SIGNS[2]})
      natal Guru      {NAT['Guru']:.2f}   ({short(NAT['Guru'])})
      separation      {gap:.2f}°

  Transit Mangal is passing over natal Guru -- the graha that forms Amala Yoga
  in his 10th, rules his 4th and 7th, and runs the current antardasha.  Mangal
  carries {AV['Mithuna'][COL['Mangal']]} bindus in Mithuna, which is exactly the 4-bindu threshold --
  adequate, not strong.

  A malefic transit over the antardasha lord is a short, sharp contact rather
  than a period: Mangal clears the degree within days.  It is worth noting
  because it lands on the ONE graha currently doing the most work in his chart,
  not because it forecasts anything.
""")

# =============================================================================
rule('4.  WHAT THE TRANSIT CONFIRMS FROM EARLIER SECTIONS')
print(f"""
  This is the useful part of a live chart: it TESTS dated claims made earlier
  from computation alone.

      SECTION 21 said transit Shani sits in the natal 7th until 3 June 2027.
      SUPPLIED DATA: Shani in Meena, the natal 7th.  CONFIRMED.

      SECTION 22 computed "Guru in the 11th, INCOME, Aug 2026 – Jun 2027".
      SUPPLIED DATA: Guru in Karka, the natal 11th.  CONFIRMED.

      SECTION 22 put the current antardasha as Rahu–Guru to Jan 2028 and the
      pratyantardasha as Rahu–Guru–Budha, May–Sep 2026.
      Nothing in the supplied data contradicts it.

      SADE SATI is dated to begin 3 June 2027.  Shani is presently in the 11th
      from the natal Moon and has not yet reached the 12th.  CONSISTENT.

  FOUR DATED CLAIMS, ALL MADE BEFORE THIS DATA ARRIVED, ALL HOLDING.
""")

# =============================================================================
rule('5.  THE HONEST SUMMARY OF THIS MOMENT')
print(f"""
  FAVOURABLE RIGHT NOW

      Guru exalted in the income house, running its own antardasha
      Shani in its best gochara position, 11th from the Moon
      Shukra crossing the natal lagna — though DEBILITATED in Kanya,
        which has to be said rather than glossed
      Rahu in the 6th from the lagna, an upachaya, where nodes do well

  NOT FAVOURABLE

      Budha combust on 2 bindus while running the pratyantardasha
      Surya and Ketu together in the natal 12th
      five of nine grahas outside their benefic gochara houses

  AND THE ONE SENTENCE:

      THIS IS THE GOOD STRETCH, AND IT IS DATED.  Saturn is in the best
      position it occupies in the whole cycle and moves to the worst on
      3 JUNE 2027.  Jupiter is exalted in the house of gains until it leaves
      Karka.  NINE MONTHS.

  Section 20 said "whatever is worth securing, secure it before then."  The
  supplied transit chart is that advice with the clock showing.
""")
print('=' * 92)
