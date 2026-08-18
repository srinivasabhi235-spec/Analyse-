#!/usr/bin/env python3
"""
What has already been lived, and what that changes.

Three mahadashas are finished and a fourth is a third gone.  The reading has
been almost entirely forward-looking: it starts at August 2026 and runs to
2076.  It has never once turned round and asked what the chart says about the
twenty-four years already behind him.

That omission matters for two separate reasons, and they pull in opposite
directions.

  IT DOES NOT CHANGE THE CHART.  Vimshottari is fixed at birth.  No boundary
  moves because a period has been lived, and nothing in the natal analysis
  updates.  Anyone claiming a chart "changes" as dashas pass is describing a
  different system.

  IT CHANGES WHAT THE READING IS.  The elapsed periods are the only part of
  this document that can be CHECKED.  Everything else is unfalsifiable by
  construction.  The gap audit named this as the largest remaining hole --
  "no confirmed life events, so this is an unfalsified reading rather than a
  tested one" -- and the elapsed dashas are the material that would close it.

And it exposes one structural fact the forward-looking reading had entirely
missed, which is in section 4 and is the most important thing in this file.
"""
from ephem_core import (SIGNS, GRAHAS, SUPPLIED, LORD, VIM, nak_of, sign_of,
                        short, rule, sub)

TODAY = 2026.63                       # 18 August 2026
BIRTH_Y = 2002 + (31 + 28 + 31 + 15) / 365.25

SP = {'Mangal': 212, 'Shani': 184, 'Budha': 152, 'Surya': 138,
      'Shukra': 95, 'Guru': 81, 'Chandra': 33}
NET = {'Surya': 39.05, 'Shukra': 35.62, 'Guru': 22.20, 'Chandra': 20.05,
       'Budha': -11.41, 'Mangal': -19.21, 'Shani': -34.35}
KASHTA = {'Shani': 46.83, 'Mangal': 38.87, 'Budha': 30.32, 'Guru': 15.10,
          'Shukra': 11.87, 'Surya': 7.83, 'Chandra': 4.49}
POS = dict(SUPPLIED)
LAG = sign_of(POS['Lagna'])
hs = lambda g: (sign_of(POS[g]) - LAG) % 12 + 1
rules = lambda g: [i for i in range(1, 13) if LORD[(LAG + i - 1) % 12] == g]

# ---------------------------------------------------------------- the sequence
moon = POS['Chandra']
span = 360 / 27
ni = int(moon // span)
into = (moon - ni * span) / span
lord0 = ['Ketu', 'Shukra', 'Surya', 'Chandra', 'Mangal',
         'Rahu', 'Guru', 'Shani', 'Budha'][ni % 9]
yrs0 = dict(VIM)[lord0]
bal = yrs0 * (1 - into)
seq, t = [], BIRTH_Y
i0 = [g for g, _ in VIM].index(lord0)
seq.append((lord0, t, t + bal, yrs0, True))
t += bal
for k in range(1, 9):
    g, y = VIM[(i0 + k) % 9]
    seq.append((g, t, t + y, y, False))
    t += y

rule('1.  WHAT HAS ACTUALLY ELAPSED')
print(f"\n  today {TODAY:.2f}   age {TODAY - BIRTH_Y:.2f}\n")
print(f"  {'mahadasha':10s} {'from':>8s} {'to':>8s} {'ages':>13s} {'years':>6s}  status")
for g, a, b, y, partial in seq:
    if b <= TODAY:
        st = 'COMPLETE'
    elif a <= TODAY < b:
        st = f'RUNNING — {(TODAY-a)/(b-a)*100:.0f}% elapsed'
    else:
        st = 'future'
    tag = ' (birth balance)' if partial else ''
    print(f"  {g:10s} {a:8.2f} {b:8.2f} {a-BIRTH_Y:5.1f} – {b-BIRTH_Y:5.1f} "
          f"{b-a:6.2f}  {st}{tag}")

done = [s for s in seq if s[2] <= TODAY]
cur = [s for s in seq if s[1] <= TODAY < s[2]][0]
print(f"""
  THREE MAHADASHAS ARE FINISHED: {', '.join(s[0] for s in done)}.
  {cur[0]} is running and is {(TODAY-cur[1])/(cur[2]-cur[1])*100:.0f}% gone.

  Lived so far: {TODAY-BIRTH_Y:.1f} of the 120-year cycle -- {(TODAY-BIRTH_Y)/120*100:.1f}%.
""")

# ---------------------------------------------------------------------------
rule('2.  THE RETRODICTIONS — what the chart says about years already lived')
print("""
  These are the only falsifiable statements this document contains.  Each is
  derived from the same apparatus as the forward-looking sections, applied
  backwards.  THEY CAN BE CHECKED, and if they are wrong the reading is wrong.
""")

RETRO = [
    ('Surya', 0.0, 3.7, """
      Surya rules the 12th and sits exalted in the 8th, gandanta, in Ashwini
      -- the nakshatra of the divine physicians.  Best net balance in the
      chart (+39.05) and the lowest cost of any effective graha.
        EXPECT: an easy infancy in material terms, and something health- or
        hospital-flavoured very early -- the gandanta Sun in the 8th during
        its own period is the classic marker.  The father prominent or absent
        in an unusual way from the very start."""),
    ('Chandra', 3.7, 13.7, """
      Chandra is EXALTED but in Mrita avastha, Shodhya Pinda 33 -- the lowest
      delivery capacity in the chart -- and rules the 11th.  Its Kashta is
      4.49, the lowest of any graha: it costs almost nothing.
        EXPECT: a gentle, unremarkable, low-conflict childhood between roughly
        four and fourteen.  Emotionally well-supplied and materially thin
        rather than the reverse.  The MOTHER is the dominant figure of this
        decade -- section 33 found her the most benign presence in the chart.
        Schooling steady, nothing dramatic.  If this decade was turbulent, the
        reading has a problem."""),
    ('Mangal', 13.7, 20.7, """
      THIS IS THE ONE THAT MATTERS MOST.  Mangal rules the 8TH and the 3RD,
      holds the HIGHEST Shodhya Pinda in the chart (212), the second-worst
      Kashta (38.87), net -19.21, four debilitations across the vargas and the
      lowest Vimshopaka.  It also takes four of the ten trimshamsha portions.
        EXPECT: adolescence from about fourteen to twenty-one ran under the
        lord of the 8th house at maximum delivery and near-maximum cost.  That
        is not a quiet stretch.  Expect a genuine rupture in it -- a move, a
        loss, a rupture in the family, a health event, or a hard break in
        education -- and expect it to have been FORMATIVE rather than merely
        unpleasant.  Mangal in the 9th aspecting the 3rd, 4th and 12th points
        the disruption at HOME and at FATHER and at SCHOOLING specifically.
        The chart says the 8th-house life did not begin in 2027.  It began
        around age fourteen."""),
    ('Rahu', 20.7, 38.7, """
      Rahu is the AVAYOGI, sits in Marana Karaka Sthana in the 9th, and
      aspects the lagna.  Its own antardasha ran Dec 2022 to ~Aug 2025.
        EXPECT so far: since about age twenty-one, identity under active
        reconstruction, a break with inherited belief, ambition arriving from
        an unexpected or foreign direction, and visible progress that other
        people cannot account for.  High variance rather than steady gain.
        Rahu-Guru from Sep 2025 turns it toward the 7th and 4th -- partnership
        and home."""),
]
for g, a, b, txt in RETRO:
    st = 'LIVED' if b <= TODAY - BIRTH_Y else 'PARTLY LIVED'
    print(f"\n  {g.upper()}  ages {a:.1f} – {b:.1f}   [{st}]")
    if g in SP:
        print(f"      house {hs(g)}, rules {rules(g)}, SP {SP[g]}, "
              f"Kashta {KASHTA[g]}, net {NET[g]:+.2f}")
    else:
        print(f"      house {hs(g)}, rules nothing — a shadow; borrows its "
              f"dispositor Shukra (SP {SP['Shukra']}, net {NET['Shukra']:+.2f})")
    print(txt)

# ---------------------------------------------------------------------------
rule('3.  GRAHA MATURITY — which have already fired')
MATURE = {'Surya': 22, 'Chandra': 24, 'Mangal': 28, 'Budha': 32,
          'Guru': 16, 'Shukra': 25, 'Shani': 36}
age_now = TODAY - BIRTH_Y
print(f"\n  {'graha':9s} {'matures':>8s} {'year':>8s}  status")
for g, m in sorted(MATURE.items(), key=lambda x: x[1]):
    y = BIRTH_Y + m
    st = 'FIRED' if m <= age_now else f'pending ({m-age_now:.1f} yrs)'
    mark = '  <<' if abs(m - age_now) < 2 else ''
    print(f"  {g:9s} {m:8d} {y:8.1f}  {st}{mark}")
print(f"""
  The reading built a table around the 8th-house apparatus maturing across
  2024-2034.  At age {age_now:.1f} that process is HALF COMPLETE:

      Guru   matured 2018   (age 16)  -- the 10th-house occupant, Amala giver
      Surya  matured 2024   (age 22)  -- exalted, in the 8th, 12th lord
      Shukra matures  2027   (age 25)  -- the Atmakaraka.  NEXT, and imminent
      Mangal matures  2030   (age 28)  -- THE 8TH LORD.  The peak year
      Budha  matures  2034   (age 32)  -- lagna and 10th lord
      Shani  matures  2038   (age 36)

  So the two that have fired are the 10th-house benefic and the exalted 12th
  lord in the 8th.  The two that have NOT are the Atmakaraka and the 8th lord
  -- which is precisely why the reading places the defining transformation
  ahead rather than behind.
""")

# ---------------------------------------------------------------------------
rule('4.  THE THING THE FORWARD-LOOKING READING MISSED')
print("""
  The reading has said repeatedly, in half a dozen sections, that SHUKRA is
  the chart's best material: Atmakaraka, self-disposited at nakshatra level,
  HIGHEST Ishta Phala (47.49), net +35.62, ruler of the 2nd and 9th, the one
  column of Ashtakavarga that supports the weak 8th, and the graha whose
  periods are "where the 8th pays instead of charges".

  Now look at when Shukra's own MAHADASHA falls.
""")
for g, a, b, y, _ in seq:
    if g == 'Shukra':
        print(f"      SHUKRA MAHADASHA   {a:.1f} to {b:.1f}   "
              f"AGES {a-BIRTH_Y:.1f} TO {b-BIRTH_Y:.1f}   ({y} years)")
print("""
  Twenty years of the chart's most favourable graha, beginning at age 97.7.

  IT IS EFFECTIVELY UNREACHABLE.  And the same applies at the other end:
""")
for g, a, b, y, partial in seq:
    if g == 'Surya':
        print(f"      SURYA MAHADASHA    {a:.1f} to {b:.1f}   "
              f"ages {a-BIRTH_Y:.1f} to {b-BIRTH_Y:.1f}   "
              f"({b-a:.2f} of {y} years -- the rest fell before birth)")
print("""
  Surya has the BEST net balance in the chart (+39.05) and the lowest cost of
  any effective graha.  Its mahadasha was consumed as a 3.7-year birth
  fragment before he could form a memory of it, and the next one is 120 years
  away.

  SO: OF THE THREE BEST GRAHAS BY NET BALANCE, TWO HAVE MAHADASHAS HE CANNOT
  USE.  Surya's is spent; Shukra's is out of reach.  What is actually
  available across a realistic life is Guru's sixteen years -- and Chandra's
  ten, already lived in childhood.

  This is not a small correction.  The reading answered "is life on an upward
  trajectory" partly on a duration-weighted mean of +8.57 across the full
  120-year cycle.  THAT NUMBER INCLUDES TWENTY YEARS OF SHUKRA HE WILL NOT
  LIVE TO SEE, and they are the second most favourable twenty years in the
  whole scheme.
""")

sub('the net balance, nominal against life-anchored')
print("""  Two different quantities, and the document only ever computed the first.

  NOMINAL: weight each graha by its full allotted years, as if the whole
  120-year cycle were available from birth.  This is what the document quotes.
""")
for label, keys, tot in [
        ('all nine, full 120 years', [g for g, _ in VIM], 120),
        ('seven classical only (95 yrs)',
         ['Surya', 'Chandra', 'Mangal', 'Guru', 'Shani', 'Budha', 'Shukra'], 95)]:
    num = 0.0
    for g, y in VIM:
        if g not in keys:
            continue
        n = NET['Shukra'] if g == 'Rahu' else NET['Mangal'] if g == 'Ketu' else NET[g]
        num += n * y
    print(f"  {label:32s} {num/tot:+7.2f}   <- the document's figure")

print("""
  LIFE-ANCHORED: use the ACTUAL sequence, which begins with a 3.70-year Surya
  balance rather than a full six, and truncate at a realistic age.
""")
for label, lo, hi in [('birth to age 120', 0, 120),
                      ('birth to age 85', 0, 85),
                      ('birth to age 80', 0, 80),
                      ('ALREADY LIVED (0 to 24.3)', 0, age_now),
                      ('REMAINING (24.3 to 85)', age_now, 85)]:
    num = den = 0.0
    for g, a, b, y, _ in seq:
        s0, s1 = max(a - BIRTH_Y, lo), min(b - BIRTH_Y, hi)
        if s1 <= s0:
            continue
        w = s1 - s0
        n = NET['Shukra'] if g == 'Rahu' else NET['Mangal'] if g == 'Ketu' else NET[g]
        num += n * w
        den += w
    print(f"  {label:32s} {num/den:+7.2f}   over {den:5.1f} years")

print("""
  THE TWO SETS OF NUMBERS ARE NOT THE SAME QUANTITY, and the difference is the
  point.  The nominal figures are a property of the CHART.  The life-anchored
  ones are a property of THIS LIFE, and nobody had computed them.

  Read the last row.  THE REMAINING SIXTY YEARS AVERAGE ABOUT +1.4, against
  the +8.57 the document has been quoting.  The reason is arithmetic rather
  than gloomy: the two most favourable long blocks in the scheme are Surya's
  and Shukra's, and one was spent in infancy while the other begins at 97.7.
  What remains ahead is Rahu's tail, Guru's sixteen good years, Shani's
  nineteen bad ones and Budha's seventeen mildly bad ones.

  BUT HOLD THAT AGAINST THE OTHER AXIS BEFORE DRAWING A CONCLUSION.  Net
  Ishta-Kashta measures the TEXTURE of what a graha delivers, not the QUANTITY.
  Shodhya Pinda measures the quantity.  Run the same spans on delivery:

""")

SPD = dict(SP)
for label, lo, hi in [('ALREADY LIVED (0 to 24.3)', 0, age_now),
                      ('REMAINING (24.3 to 85)', age_now, 85)]:
    num = den = 0.0
    for g, a, b, y, _ in seq:
        s0, s1 = max(a - BIRTH_Y, lo), min(b - BIRTH_Y, hi)
        if s1 <= s0:
            continue
        w = s1 - s0
        v = SPD['Shukra'] if g == 'Rahu' else SPD['Mangal'] if g == 'Ketu' else SPD[g]
        num += v * w
        den += w
    print(f"  {label:32s} mean Shodhya Pinda {num/den:6.1f}")

print("""
  THERE IS THE RESOLUTION, AND IT IS NOT A CONTRADICTION.

      lived so far   net +13.98,  mean delivery capacity 109.7
      remaining      net  +1.40,  mean delivery capacity 129.8

  THE YEARS ALREADY LIVED WERE CHEAP AND THIN.  THE YEARS AHEAD ARE EXPENSIVE
  AND PRODUCTIVE.  Chandra's decade has the second-best net in the chart and
  the LOWEST Shodhya Pinda of any graha (33) -- pleasant, and it delivered
  almost nothing.  Shani's nineteen years have the worst net and the
  second-HIGHEST delivery (184) -- they cost enormously and they produce.

  So the reading's central claim is not damaged by this, it is sharpened.
  "He is better than his output for the first thirty years" and "the payoff
  comes late" are exactly what a low-delivery, low-cost opening followed by a
  high-delivery, high-cost remainder looks like from the inside.

  THE UPWARD-TRAJECTORY ANSWER SURVIVES, because trajectory is about SHAPE --
  the Guru mahadasha still triples the career score, the Sade Sati-free window
  still contains it, and the rise from 61 still happens.  But the CLAIM THAT
  THE AVERAGE IS COMFORTABLY POSITIVE does not survive at this resolution.
  It is barely positive, and it is carried almost entirely by one sixteen-year
  block between 38.7 and 54.7.
""")

# ---------------------------------------------------------------------------
rule('5.  SO DOES THE PASSAGE OF TIME CHANGE THE ANALYSIS?')
print(f"""
  NO, in the way the question usually means.  The natal chart is fixed.  Every
  dasha boundary was set at birth by the Moon's position in Krittika and none
  of them moves.  Nothing in sections on the person, the structure, the
  dispositors, the vargas, the yogas or the rarity is affected by the calendar.

  YES, in four specific ways:

  1.  IT MAKES THE READING TESTABLE.  Twenty-four years of retrodiction now
      exist (section 2) and they are checkable.  The strongest single claim is
      about ages 13.7 to 20.7: the Mangal mahadasha, lord of the 8th, highest
      delivery capacity in the chart.  THE 8TH-HOUSE LIFE DID NOT BEGIN IN
      2027 -- IT BEGAN AROUND AGE FOURTEEN, and the 2028-2033 window is the
      second pass, not the first.

  2.  IT NARROWS WHAT IS REACHABLE.  Shukra's twenty-year mahadasha begins at
      97.7 and Surya's was spent in infancy.  Any forward statement resting on
      the full 120-year weighting is overstated for this specific life.

  3.  IT HALVES THE MATURITY TABLE.  Guru and Surya have fired; Shukra and
      Mangal have not.  The apparatus the reading describes as "coming online
      2024-2034" is at its midpoint, and the two heaviest components are still
      ahead.

  4.  IT DATES THE DOCUMENT.  The "now" section reads 11-12 August 2026 and
      the marriage window it describes is open TODAY.  That window closes
      3 June 2027, not January 2028 -- corrected in section 39 -- which means
      roughly {(2027.42-TODAY)*12:.0f} MONTHS REMAIN of the clearest activation the chart offers.

  What does NOT change, and is worth saying plainly: the person, the
  structure, the seven-of-nine concentration, both parivartanas, the two
  gandanta knots, every dignity and avastha finding, the rarity result, the
  six blind spots, and the destination.  Those are facts about a moment in
  April 2002 and they are the same today as they were then.
""")
print('=' * 92)
