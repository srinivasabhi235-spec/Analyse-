#!/usr/bin/env python3
"""
The Mangal mahadasha, opened up: December 2015 to December 2022, ages 13.7 to 20.7.

Section 18 established that this was an 8th-house life-phase and section 19
scored it against the window ahead.  Neither of them said WHAT KIND.

Mangal is not a generic malefic.  In this chart it is a very specific
instrument, and the kind of transformation it produces is readable from six
things that all point the same way:

    what it RULES        the 8th and the 3rd
    where it STANDS      the 9th -- dharma, the father, fortune
    what it ASPECTS      the 12th, the 3rd and the 4th
    how much it DELIVERS Shodhya Pinda 212, the highest in the chart
    what it COSTS        Kashta 38.87, the second worst
    who PAYS IT OUT      Surya, via Krittika -- the cheapest effective channel

This computes every antardasha with dates and ages, puts the real transits
against each, and then names the texture rather than gesturing at it.

Nothing here is a claim about events.  It is what the chart says, offered so
that it can be checked against a life that has actually been lived.
"""
import swisseph as swe
from ephem_core import (BIRTH, JD, SIGNS, GRAHAS, SUPPLIED, LORD, VIM, EXALT,
                        varga, sign_of, nak_of, short, fmt, local, rule, sub,
                        FLAG)

POS = dict(SUPPLIED)
LAG = sign_of(POS['Lagna'])
MOON = sign_of(POS['Chandra'])
BIRTH_Y = 2002 + (31 + 28 + 31 + 15) / 365.25
hs = lambda g: (sign_of(POS[g]) - LAG) % 12 + 1
rules = lambda g: [i for i in range(1, 13) if LORD[(LAG + i - 1) % 12] == g]
SP = {'Mangal': 212, 'Shani': 184, 'Budha': 152, 'Surya': 138,
      'Shukra': 95, 'Guru': 81, 'Chandra': 33}
KASHTA = {'Shani': 46.83, 'Mangal': 38.87, 'Budha': 30.32, 'Guru': 15.10,
          'Shukra': 11.87, 'Surya': 7.83, 'Chandra': 4.49}
NET = {'Surya': 39.05, 'Shukra': 35.62, 'Guru': 22.20, 'Chandra': 20.05,
       'Budha': -11.41, 'Mangal': -19.21, 'Shani': -34.35}
HOUSE = ['self', 'wealth, family, speech', 'effort, courage, siblings',
         'home, mother, schooling', 'children, romance', 'adversity, health',
         'partnership', 'transformation', 'dharma, father, fortune',
         'career, standing', 'gains, networks', 'loss, foreign, moksha']
MD_A, MD_B = 2015.978, 2022.978

# =============================================================================
rule('1.  WHAT KIND OF INSTRUMENT MANGAL IS IN THIS CHART')
n = nak_of(POS['Mangal'])
print(f"""
  position        {fmt(POS['Mangal'])} — house {hs('Mangal')}
  nakshatra       {n[0]} pada {n[1]} — lord {n[2]}
  rules           houses {rules('Mangal')} — {HOUSE[rules('Mangal')[0]-1]} and {HOUSE[rules('Mangal')[1]-1]}
  aspects         houses {[(hs('Mangal')+a-2)%12+1 for a in (4, 7, 8)]}
  Shodhya Pinda   {SP['Mangal']} — HIGHEST in the chart
  Kashta          {KASHTA['Mangal']} — second worst
  net             {NET['Mangal']:+.2f}
  avastha         Vriddha (old)
  paid out by     {n[2]} — Kashta {KASHTA[n[2]]}, the cheapest effective channel
""")
deb = [v for v in [1, 2, 3, 4, 7, 9, 10, 12, 16, 20, 24, 27, 30, 40, 45, 60]
       if EXALT['Mangal'] == (varga(POS['Mangal'], v) + 6) % 12]
exa = [v for v in [1, 2, 3, 4, 7, 9, 10, 12, 16, 20, 24, 27, 30, 40, 45, 60]
       if EXALT['Mangal'] == varga(POS['Mangal'], v)]
print(f"  debilitated in  {['D'+str(v) for v in deb]}")
print(f"  exalted in      {['D'+str(v) for v in exa]}")
print(f"""
  READ THAT LIST.  Mangal is debilitated in the vargas of the PARENTS (D12),
  the MATERNAL LINE (D40), inherited wealth (D2 — the Moon's hora) and
  accumulated karma (D60).  It is exalted in exactly one: D27, the varga of
  VITALITY.

  So the seven years it governed were structurally aimed at the family and the
  inheritance, and structurally NOT aimed at the body.  That is an unusual and
  quite specific combination, and it is the first real answer to "what kind".
""")

sub('the shakti — what the tradition says this nakshatra DOES')
print(f"""
  Mangal stands in KRITTIKA, whose presiding deity is AGNI and whose shakti is
  DAHANA SHAKTI — the power to BURN AWAY.

  Krittika is the razor, the flame, the blade that separates.  Its classical
  function is not to destroy but to CUT AWAY WHAT IS NOT WANTED so that what
  remains is clean.  The chart's janma nakshatra is the same star.

  And Krittika's lord is SURYA, which is why the 8th lord's payout runs on the
  cheapest channel in the chart.  MANGAL BURNS; SURYA COLLECTS.
""")

# =============================================================================
rule('2.  EVERY ANTARDASHA, WITH DATES, AGES AND TRANSITS')


def jd_of(y):
    return swe.julday(int(y), 1, 1, 0) + (y % 1) * 365.25


def sgn(y, body):
    return sign_of(swe.calc_ut(jd_of(y), body, FLAG)[0][0] % 360)


def hfrom(s, base):
    return (s - base) % 12 + 1


i = [g for g, _ in VIM].index('Mangal')
tot = MD_B - MD_A
t = MD_A
ADS = []
for k in range(9):
    g, y = VIM[(i + k) % 9]
    d = tot * y / 120
    ADS.append((g, t, t + d))
    t += d

print(f"  {'antardasha':16s} {'from':>8s} {'to':>8s} {'ages':>13s}"
      f"  {'Shani':14s} {'Guru':12s}")
for g, a, b in ADS:
    m = (a + b) / 2
    ss, gs = sgn(m, swe.SATURN), sgn(m, swe.JUPITER)
    tag = ''
    if hfrom(ss, MOON) == 8:
        tag = ' << Ashtama Shani'
    print(f"  Mangal–{g:9s} {a:8.2f} {b:8.2f} {a-BIRTH_Y:5.1f} – {b-BIRTH_Y:5.1f}"
          f"  {SIGNS[ss]+' (h'+str(hfrom(ss,LAG))+')':14s} "
          f"{SIGNS[gs]+' (h'+str(hfrom(gs,LAG))+')':12s}{tag}")

sub('what each sub-lord contributes, in this chart specifically')
for g, a, b in ADS:
    r = rules(g)
    where = f"house {hs(g)}"
    extra = ''
    if g == 'Rahu':
        extra = ' — Marana Karaka Sthana, the Avayogi'
    if g == 'Shani':
        extra = ' — Amatyakaraka, worst Kashta in the chart'
    if g == 'Budha':
        extra = ' — lagna AND 10th lord, combust, the only failing graha'
    if g == 'Ketu':
        extra = ' — the Yogi planet, severest gandanta pada'
    if g == 'Shukra':
        extra = ' — ATMAKARAKA, highest Ishta Phala, in the 8th'
    if g == 'Surya':
        extra = ' — exalted, gandanta, 12th lord, in the 8th'
    if g == 'Chandra':
        extra = ' — exalted but Mrita, lowest delivery in the chart'
    print(f"  Mangal–{g:9s} {a-BIRTH_Y:4.1f}–{b-BIRTH_Y:4.1f}  {where:9s} "
          f"rules {str(r):10s}{extra}")

# =============================================================================
rule('3.  THE SIX THAT CARRY THE WEIGHT')
print("""
  Not all nine matter equally.  Six of these sub-periods are structurally
  loud in this chart, and they arrive in a legible order.
""")
AD = {g: (x, y) for g, x, y in ADS}
A = {g: (x - BIRTH_Y, y - BIRTH_Y) for g, x, y in ADS}

KEY = [
    ('Mangal–Rahu', 'Rahu', """
      The 8th lord's own period sub-ruled by the AVAYOGI from Marana Karaka
      Sthana in the 9th.  Rahu in the 9th disrupts INHERITED BELIEF and the
      father's authority specifically -- and Mangal is simultaneously the
      Pitrikaraka, the Jaimini father-significator.  Two father-markers active
      at once, one of them the chart's most destabilising body.
        THE TEXTURE: a break with something received rather than chosen.
        Not chosen by him either -- Rahu does not consult."""),
    ('Mangal–Guru', 'Guru', """
      Guru rules the 4TH (home, mother, schooling) and the 7TH, sits in the
      10th forming Amala, and carries the worst Drik Bala in the chart.
      ASHTAMA SHANI BEGINS INSIDE THIS PERIOD -- Saturn enters Dhanu, the 8th
      from the natal Moon.  And GURU ITSELF MATURES AT 16, inside this window.
        THE TEXTURE: the home and the schooling come under pressure at the
        exact moment the chart's one protective graha comes into its
        strength.  Both at once, which is why this reads as strained rather
        than simply bad."""),
    ('Mangal–Shani', 'Shani', """
      Saturn still in Dhanu -- Ashtama Shani from Chandra throughout.  Shani
      is the Amatyakaraka, holds the WORST Kashta in the chart (46.83), and
      rules the 5th (education, mind) and the 6th (health, adversity).
        THE TEXTURE: the heaviest and slowest stretch of the seven years.
        Where Rahu breaks, SHANI GRINDS.  The chart marks this for endurance
        rather than event -- education and health under the most expensive
        graha it owns, with transit Saturn on the 8th from the Moon."""),
    ('Mangal–Budha', 'Budha', """
      Budha is the LAGNA LORD and the 10TH LORD, combust, sitting in the 8th,
      and the only graha in the chart failing its Shadbala minimum.  Its Dig
      Bala is 4.28 of 60, the lowest of any body.  Ashtama Shani runs out
      partway through.
        THE TEXTURE: identity and direction, under the 8th lord, run by the
      one graha that cannot hold a position.  Ages 17-18 is exactly when a
      life is asked "who are you and what will you do" -- and the chart
      answers with its weakest instrument.  Expect the question to have been
      forced and the answer to have been unavailable."""),
    ('Mangal–Ketu', 'Ketu', """
      Five months under the YOGI planet in the severest gandanta pada -- and
      THE RAHU RETURN falls here, 20 November 2020, age 18.6.
        THE TEXTURE: emptying.  Short, and it clears the ground."""),
    ('Mangal–Shukra', 'Shukra', """
      Fourteen months under the ATMAKARAKA -- highest Ishta Phala in the
      chart, self-disposited, ruler of the 2nd and 9th, and the one
      Ashtakavarga column that supports the weak 8th.
        THE TEXTURE: THE TURN, and it arrives at the END of the mahadasha
      rather than the beginning.  This is the one genuinely favourable stretch
      of the seven years -- after the breaking and the grinding, not before."""),
]
for lbl, g, txt in KEY:
    lo, hi = A[g]
    print(f"\n  {lbl}   ages {lo:.1f} – {hi:.1f}   ({AD[g][0]:.0f}–{AD[g][1]:.0f})")
    print(txt)

sub('and the shape they make')
gp = [g for g, _, _ in ADS]
print(f"""
  Read in order, the seven years have a legible arc rather than being
  undifferentiated hardship:

      {A['Rahu'][0]:.1f} – {A['Rahu'][1]:.1f}   Rahu     a break with the inherited
      {A['Guru'][0]:.1f} – {A['Budha'][1]:.1f}   Guru, Shani, Budha
                     THE LONG MIDDLE — Ashtama Shani from the Moon runs
                     across all three, ages {A['Guru'][0]:.1f} to {A['Budha'][1]:.1f}
      {A['Ketu'][0]:.1f} – {A['Ketu'][1]:.1f}   Ketu     emptying, with the Rahu return in it
      {A['Shukra'][0]:.1f} – {A['Shukra'][1]:.1f}   Shukra   THE TURN, under the Atmakaraka
      {A['Surya'][0]:.1f} – {A['Chandra'][1]:.1f}   Surya, Chandra   the close

  THREE CONSECUTIVE YEARS OF ASHTAMA SHANI sit in the middle of it, ages
  {A['Guru'][0]:.1f} to {A['Budha'][1]:.1f}.  That is the spine of the period and the reading had
  never identified it.
""")

# =============================================================================
rule('4.  SO WHAT KIND OF TRANSFORMATION WAS IT?')
print("""
  Six independent markers, and they converge on one description.

  1. WHERE IT WAS AIMED.  Mangal aspects the 12th, 3rd and 4th and stands in
     the 9th.  That is LOSS, EFFORT/SCHOOLING, HOME and FATHER -- and it is
     debilitated in the vargas of the parents (D12) and the maternal line
     (D40).  The chart points this transformation at the FAMILY and at the
     conditions of his education, not at his career or his body.

  2. HOW MUCH IT DELIVERED.  Shodhya Pinda 212, the highest of any graha.
     This was not a thin period.  Whatever it did, it did a lot of.

  3. WHAT IT COST.  Kashta 38.87, second worst; net -19.21.  It charged
     heavily for what it delivered.

  4. HOW IT MOVED.  Mangal is fast, hot and sharp -- and it is in VRIDDHA
     avastha, the old state.  Not fresh vigour: force applied wearily.
     The classical reading is action that is necessary rather than eager.

  5. WHAT IT DID.  Krittika, deity Agni, shakti DAHANA -- the power to burn
     away.  Not destruction; SEPARATION.  Something was cut off rather than
     smashed.

  6. WHO COLLECTED.  The star lord is SURYA -- Kashta 7.83, the cheapest
     effective graha in the chart, ruler of the 12th, exalted in the 8th and
     forming Vimala.  The 8th lord's outcomes were paid out through the lord
     of RELEASE.

  PUT TOGETHER, AND THIS IS THE ANSWER:

      A SEPARATION, NOT A CATASTROPHE.  Aimed at home, family and the
      conditions of his schooling.  Heavy in volume, expensive, and carried
      out with a kind of tired force rather than violence.  Something was
      burned away -- and because the payout channel is the 12th lord, what it
      produced was RELEASE rather than wreckage.

  And the thing that makes it survivable rather than merely severe is the one
  varga where Mangal is EXALTED: D27, the chart of vitality.  The instrument
  that governed those seven years is at its strongest in precisely the chart
  that measures whether the body can take it.
""")

# =============================================================================
rule('5.  WHAT IT LEFT BEHIND')
print("""
  Two structural consequences that the rest of the reading depends on, and
  neither was traced back to this period before.

  1. THE 3RD HOUSE IS WHERE HE WORKS, AND MANGAL RULES IT.  The 3rd is the
     most-contacted house in the chart -- Ketu occupying, four grahas
     aspecting -- and its lord is the graha that ran his adolescence at
     maximum delivery.  The reading's repeated finding that EFFORT INTO SKILL
     PAYS FASTER THAN EFFORT INTO POSITION was installed here.  A boy whose
     8th-and-3rd lord governs ages 14 to 21 learns to work alone, under load,
     without external scaffolding, because that is the only thing available.

  2. IT RAN BEFORE MANGAL MATURED.  Mangal matures at 28, in 2030.  Its
     mahadasha ended in December 2022, more than seven years early.  So the
     8th lord governed those years WITHOUT ITS FULL STRENGTH -- which is the
     structural reason section 19 concludes the coming window is a different
     instrument rather than a repeat.

  A last note on proportion, because it matters.  This was seven years under
  the chart's most expensive effective graha, ending in a Rahu return.  It was
  also, by the life-anchored arithmetic in section 18, part of the stretch
  whose NET texture (+13.98 across ages 0-24.3) is the most favourable of his
  life.  BOTH ARE TRUE.  The Mangal years were the hard part of an otherwise
  cheap opening -- which is why they read as formative rather than as ruin.
""")
print('=' * 92)
