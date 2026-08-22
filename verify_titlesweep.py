#!/usr/bin/env python3
"""
THE WHOLE READING SWEPT AGAINST THE CHAPTER TITLES.

Sections 31 and 32 mapped the reading to Parashara's chapters and closed three
gaps.  This goes further: it takes the titles as a CHECKLIST and asks of each
one, what does this reading do with that subject?

The sweep turns up one omission larger than all three gaps combined, and it is
methodological rather than technical.

    CHAPTER 46 IS TITLED "DASAS (PERIODS) OF PLANETS" AND ITS SUBTITLE LISTS
    ROUGHLY TWENTY-SIX DASHA SYSTEMS BY NAME.

    THIS READING USES ONE.

Every date in fifty-eight sections comes from Vimshottari, and the document has
never once noted that Vimshottari is a CHOICE rather than the method.  So this
script computes a second system independently and asks whether the timeline
survives the change.
"""
import swisseph as swe
from ephem_core import SUPPLIED, jd_ut, nak_of, sign_of, rule, sub

M = SUPPLIED['Chandra']
SPAN = 360 / 27
NI = int(M // SPAN)
FRAC = (M - NI * SPAN) / SPAN
JD0 = jd_ut(2002, 4, 15, 18, 2, 45, 5.5)
MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
YOG = [('Mangala', 'Chandra', 1), ('Pingala', 'Surya', 2), ('Dhanya', 'Guru', 3),
       ('Bhramari', 'Mangal', 4), ('Bhadrika', 'Budha', 5), ('Ulka', 'Shani', 6),
       ('Siddha', 'Shukra', 7), ('Sankata', 'Rahu', 8)]


def show(jd):
    y, m, d, _ = swe.revjul(jd)
    return f"{int(d)} {MON[m-1]} {y}"


# =============================================================================
rule('1.  THE OMISSION THE TITLES EXPOSE')
print("""
  Chapter 46's subtitle names, in the supplied contents page:

      Vimsottari, Ashtottari, Shodasottari, Panchottari, Shashtihayani,
      Chaturshitisama, Dwisaptatisama, Shashtisama, Shatabdika, Kalachakra,
      Chara, Sthira, Kendra, Brahmagraha, Mandook, Yogardha, Shoola, Drig,
      Rasi, Panchaswara, YOGINI, Naisargika, Pinda, Shodhya, Ashtakavarga,
      Pachaka, and Tara Dasa.

  ROUGHLY TWENTY-SIX SYSTEMS.  THIS READING USES ONE.

  That is not wrong -- Vimshottari is the standard for a reason, and Parashara
  treats it first -- but the document has never SAID it is a choice.  Every
  date in fifty-eight sections rests on a single selection from a list of
  twenty-six, presented as though it were the calendar itself.

  SO THE HONEST TEST IS TO COMPUTE A SECOND SYSTEM AND SEE WHAT SURVIVES.
  YOGINI is chosen because its construction rule is simple enough to state and
  check, and because it is COMPLETELY UNRELATED to Vimshottari: a 36-year cycle
  of eight periods against a 120-year cycle of nine, keyed to the same Moon but
  by a different arithmetic.
""")

# =============================================================================
rule('2.  YOGINI DASHA, COMPUTED')
start = (NI + 1 + 3) % 8 or 8
idx = start - 1
bal = YOG[idx][2] * (1 - FRAC)
print(f"""
  THE RULE, stated before use.  Eight yoginis of 1 to 8 years, 36 in all.  The
  starting yogini is (janma nakshatra number + 3) mod 8, and the first period
  runs for the unexpired portion of it.

      Chandra          {M:.4f}
      nakshatra        #{NI+1} {nak_of(M)[0]}, {FRAC*100:.1f}% elapsed
      ({NI+1} + 3) mod 8 = {start}   ->   {YOG[idx][0]}, ruled by {YOG[idx][1]}, {YOG[idx][2]} years
      balance at birth {bal:.2f} years
""")
print(f"  {'yogini':10s}{'lord':9s}{'from':13s}{'to':13s}ages")
t, k = bal, idx
print(f"  {YOG[idx][0]:10s}{YOG[idx][1]:9s}{show(JD0):13s}"
      f"{show(JD0 + bal*365.2425):13s}0.0 – {bal:.1f}")
rows = []
for _ in range(9):
    k = (k + 1) % 8
    n, l, y = YOG[k]
    a, b = t, t + y
    rows.append((n, l, a, b))
    print(f"  {n:10s}{l:9s}{show(JD0 + a*365.2425):13s}"
          f"{show(JD0 + b*365.2425):13s}{a:.1f} – {b:.1f}")
    t = b

# =============================================================================
rule('3.  WHERE THE TWO SYSTEMS AGREE — AND ONE AGREEMENT IS REMARKABLE')
print("""
  Vimshottari and Yogini share nothing but the Moon.  Different cycle length,
  different number of periods, different lords, different arithmetic.  So any
  agreement between them is not built in.

  THREE AGREEMENTS, IN ASCENDING ORDER OF FORCE.
""")
sub('1. The adolescent window — both systems mark it')
print(f"""
      VIMSHOTTARI   Mangal mahadasha, ages 13.7 – 20.7
      YOGINI        SANKATA, ruled by RAHU, {show(JD0 + (bal+7)*365.2425)} – {show(JD0 + (bal+15)*365.2425)}
                    ages {bal+7:.1f} – {bal+15:.1f}

  Sankata is the eight-year yogini and its name means crisis or straits -- the
  harshest of the eight.  It covers ages 10.7 to 18.7, overlapping FIVE of the
  seven years sections 18 and 19 identify as the transformation already lived.

  AN INDEPENDENT SYSTEM MARKS THE SAME ADOLESCENCE AS HARD, and this reading
  never checked.
""")
sub('2. The present period — both hand it to Guru')
print(f"""
      VIMSHOTTARI   Rahu–GURU, Sep 2025 – 31 Jan 2028
      YOGINI        DHANYA, ruled by GURU, {show(JD0 + (bal+18)*365.2425)} – {show(JD0 + (bal+21)*365.2425)}

  Both systems are running a GURU period right now, arrived at by unrelated
  routes.  Yogini's ends {show(JD0 + (bal+21)*365.2425)}, about fourteen months before Vimshottari's.
""")
sub('3. December 2030 — and this one is close enough to be worth stating twice')
vd = "7 Dec 2030"
yd = show(JD0 + (bal + 7 + 8 + 1 + 2 + 3 + 4) * 365.2425)
print(f"""
      VIMSHOTTARI   Rahu–BUDHA opens          {vd}
      YOGINI        BHADRIKA, ruled by BUDHA  {yd}

  EIGHTEEN DAYS APART.

  Two dasha systems with no shared arithmetic, keyed to the same Moon by
  different rules, hand the SAME GRAHA the SAME MOMENT within three weeks.

  And that moment is the one this reading has called THE HINGE since section 17
  -- identity and career reassessment, run by the chart's weakest graha, under
  Saturn crossing the natal 10th on a single bindu (section 29).

  I DID NOT EXPECT THIS AND WENT LOOKING FOR DISAGREEMENT.  It is the strongest
  independent confirmation of any dated claim in the document, and it exists
  only because the chapter titles prompted the check.
""")

sub('And where they disagree')
print(f"""
      VIMSHOTTARI puts the material peak at Rahu–SHUKRA, Jul 2034 – Jul 2037.
      YOGINI runs BHADRIKA (Budha) to {show(JD0 + (bal+30)*365.2425)}, then
        ULKA (Shani) {show(JD0 + (bal+30)*365.2425)} – {show(JD0 + (bal+36)*365.2425)}.

      NEITHER OF THEM IS SHUKRA.

  SO THE TWO SYSTEMS AGREE ON THE HARD DATES AND DISAGREE ON THE GOOD ONE.
  That asymmetry is worth recording rather than smoothing: the confirmations
  cluster on the difficult windows and the divergence falls on the favourable
  one.
""")

# =============================================================================
rule('4.  THE REST OF THE SWEEP — WHAT THE TITLES SHOW UNUSED')
print("""
  Taking every remaining title as a checklist item:

  CHAPTER 44, MARAKA, lists TEN sub-topics in its subtitle:
      marakas by lordship · maraka dasa · star groups related to death ·
      Rahu-Ketu as marakas · the 3rd house and death · occupants of the 8th ·
      fate of the corpse · serpent decanates · prenatal abode · ascent after
      death

      SECTION 27 USED ONE OF THE TEN -- marakas by lordship -- and found both
      maraka houses empty.  Four of the others are computable and untouched;
      the rest belong to the longevity question section 56 declines.

  CHAPTERS 62 AND 63 -- Sookshma and Prana dasas.  THE READING STOPS AT
      PRATYANTARDASHA.  Parashara goes two levels finer.  Nothing in this
      document would change, but the stopping point was never declared.

  CHAPTER 73 -- rays of the planets.  NEVER TOUCHED.
  CHAPTER 76 -- the five elements.  NEVER TOUCHED.
  CHAPTER 77 -- the three gunas.  NEVER TOUCHED.
      All three are temperament layers, all three are computable, and the
      reading answered "what are his natural traits" (section 38) without them.

  CHAPTER 83 -- curses from a previous birth, with combinations for lack of a
      male issue.  NEVER TOUCHED, and the reading has a children section.
      This one is left alone deliberately: the doctrine attributes childlessness
      to curses from named relatives, and applying it to a living person on a
      chart alone is not something this reading is willing to do.

  CHAPTER 82 -- moles and marks.  NOT APPLICABLE without physical data.
""")

# =============================================================================
rule('5.  THE LEDGER')
print("""
  Against the two contents pages, chapters 42 to 96:

      APPLIED AND SOUND        the dasha tree (46, 51, 52-61), the whole
                               Ashtakavarga chain (66-72), Sudarshana Chakra
                               (74), Panchamahapurusha (75), badhaka (50),
                               avasthas (45, three of five schemes)

      APPLIED THIS SESSION     asceticism yogas (79), penury (42),
                               Lajjitadi and Deeptadi (45), YOGINI DASHA (46)

      DECLINED WITH REASON     longevity (43, 71), Sayanadi (45),
                               curses (83), moles (82)

      STOPPED SHORT            sookshma and prana dasas (62, 63)

      NEVER TOUCHED            rays (73), elements (76), gunas (77),
                               nine of ten maraka sub-topics (44),
                               twenty-four of twenty-six dasha systems (46)

  THE HONEST SUMMARY OF THE SWEEP:

      The reading's APPARATUS is broad and its SELECTION was never declared.
      It uses one dasha system out of twenty-six, one maraka rule out of ten,
      and three avastha schemes out of five -- and until this sweep it
      presented all of that as simply "the method".

      THE ONE PLACE THAT SELECTION WAS TESTED, IT HELD: an unrelated dasha
      system independently confirms the hinge at December 2030 to within
      eighteen days.
""")
print('=' * 92)
