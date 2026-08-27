#!/usr/bin/env python3
"""
"WHAT IF HE IS IN THE USA?"

THIS IS A FAIR CHALLENGE TO SECTION 43 AND IT LANDS.

Section 43 dismissed the 28 August 2026 Chandra grahan on four grounds, and the
one it called decisive was VISIBILITY: the Moon is 54 degrees below the horizon
at Guntur, and a grahan is held to act where it is seen.

BUT VISIBILITY IS A PROPERTY OF WHERE HE IS NOW, NOT WHERE HE WAS BORN.
I computed it for the birthplace.  If he is in America the argument reverses.

SO THIS SCRIPT DOES TWO THINGS:

    1  settles what relocation DOES and DOES NOT change in Jyotisha, because
       the answer is stricter than most people assume
    2  recomputes section 43's entire eclipse table from American longitudes,
       and reports the inversion

The natal chart does not move.  One argument in section 43 does.
"""
import swisseph as swe
from ephem_core import (SIGNS, GRAHAS, SUPPLIED, LORD, jd_ut, varga, sign_of,
                        dignity, nak_of, rule, sub)

swe.set_sid_mode(swe.SIDM_LAHIRI)
F = swe.FLG_SWIEPH | swe.FLG_SIDEREAL
POS = dict(SUPPLIED)
LAG = sign_of(POS['Lagna'])
MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
       'Nov', 'Dec']
PLACES = [('Guntur', 80.44, 16.31, 5.5), ('New York', -74.01, 40.71, -4.0),
          ('Chicago', -87.63, 41.88, -5.0), ('Dallas', -96.80, 32.78, -5.0),
          ('San Francisco', -122.42, 37.77, -7.0), ('Seattle', -122.33, 47.61, -7.0)]
hsign = lambda si: (si - LAG) % 12 + 1
ordn = lambda n: f"{n}{'th' if 10 <= n % 100 <= 20 else {1:'st',2:'nd',3:'rd'}.get(n%10,'th')}"
BRANK = [5, 3, 8, 2, 6, 10, 4, 12, 7, 9, 11, 1]
BRUP = [8.39, 9.18, 7.49, 9.28, 7.91, 7.21, 8.86, 7.00, 7.61, 7.39, 7.08, 12.59]


def kind(f):
    if f & swe.ECL_TOTAL:
        return 'TOTAL'
    if f & swe.ECL_PARTIAL:
        return 'partial'
    if f & swe.ECL_PENUMBRAL:
        return 'penumbral'
    return '?'


def alt(tj, lon, lat):
    tr = swe.calc_ut(tj, swe.MOON, swe.FLG_SWIEPH)[0]
    return swe.azalt(tj, swe.ECL2HOR, (lon, lat, 0), 0, 0, (tr[0], tr[1], tr[2]))[1]


# =============================================================================
rule('1.  WHAT RELOCATION CHANGES — AND IT IS LESS THAN PEOPLE THINK')
print("""
  THE NATAL CHART DOES NOT MOVE.  It is fixed by the moment and place of birth
  and nothing later alters it.  If he is in Chicago the lagna is still 27 37'
  Kanya, Guru is still alone in the 10th, Budha is still combust in the 8th.

  THERE IS NO PARASHARI RELOCATION CHART.  Recasting a nativity for a new city
  -- the relocated chart, astrocartography, local space lines -- is a modern
  WESTERN technique.  It is coherent within its own system.  IT IS NOT IN
  PARASHARA, none of the fifty-five chapters this reading has enumerated
  contains it, and this document does not import it.

  WHAT DOES DEPEND ON WHERE HE IS NOW:

      ECLIPSE AND TRANSIT VISIBILITY  -- a grahan acts where it is seen
      the daily PANCHANGA             -- tithi, vara, sunrise, and therefore
                                         Gulika and the other upagrahas FOR
                                         CURRENT DAYS, not for the natal chart
      MUHURTA                         -- choosing a moment is always local

  THAT IS THE WHOLE LIST, AND THE FIRST ITEM IS THE ONE SECTION 43 LEANED ON.
""")

# =============================================================================
rule('2.  SECTION 43 RECOMPUTED FROM AMERICAN LONGITUDES')
print("""
  Section 43's four objections to the 28 August 2026 grahan, re-examined for a
  native standing in the United States:

      1  the STRICT D10 mapping fails            -- unchanged.  Geometry.
      2  transits are not run through vargas     -- unchanged.  Method.
      3  a Chandra grahan is the wrong graha     -- unchanged.  Doctrine.
      4  THE ECLIPSE IS NOT VISIBLE              -- THIS ONE MOVES.

  THREE OF THE FOUR ARE PROPERTIES OF THE CHART AND THE METHOD, AND THEY DO NOT
  CARE WHERE HE STANDS.  THE FOURTH IS ENTIRELY ABOUT WHERE HE STANDS.
""")
EV = [(2026, 8, 28), (2028, 1, 12), (2028, 12, 31), (2029, 12, 21)]
for y, m, d in EV:
    r = swe.lun_eclipse_when(jd_ut(y, m, d, 0, 0, 0, 5.5) - 4,
                             swe.FLG_SWIEPH, 0, False)
    tj = r[1][0]
    mo = swe.calc_ut(tj, swe.MOON, F)[0][0]
    yy, mm, dd, hh = swe.revjul(tj)
    h = hsign(sign_of(mo))
    sub(f"{kind(r[0])} in {SIGNS[sign_of(mo)]} {mo%30:.1f} — his {ordn(h)} house"
        f"   (max {int(dd)} {MON[mm-1]} {yy} {int(hh):02d}:{int(hh%1*60):02d} UT)")
    for nm, lon, lat, tz in PLACES:
        a = alt(tj, lon, lat)
        y2, m2, d2, h2 = swe.revjul(tj + tz / 24)
        print(f"      {nm:15s}{a:+7.1f}   {'VISIBLE' if a > 0 else 'below  '}"
              f"   local {int(d2)} {MON[m2-1]} {int(h2):02d}:{int(h2%1*60):02d}")

# =============================================================================
rule('3.  THE INVERSION, STATED PLAINLY')
print("""
  THE ECLIPSE HE ASKED ABOUT BECOMES VISIBLE.

      28 August 2026, partial, Kumbha -- the D10-lagna sign and his 6th house.
      INVISIBLE from Guntur at -54 degrees.
      VISIBLE FROM EVERY AMERICAN LONGITUDE TESTED, from +13 in Seattle to +39
      in New York, around midnight Eastern on the night of 27-28 August.

      SO IF HE IS IN THE UNITED STATES, SECTION 43'S DECISIVE OBJECTION FAILS.
      The other three still stand, and they are enough to sink the D10 claim on
      their own -- but the strongest and simplest of the four is gone.

  AND A CAREER ECLIPSE APPEARS THAT I HAD FILTERED OUT.

      12 January 2028, partial, MITHUNA 27.3 -- HIS TENTH HOUSE.
      Section 43 struck this one off the list: "below horizon -- does not
      apply."  That is true at Guntur, where it is -36 degrees.
      FROM NEW YORK IT IS +69 DEGREES.  Nearly overhead.

      A partial eclipse in the career house, high in an American sky, falling
      inside RAHU-SHANI -- the period sections 17 and 42 call the foundation.
      IT WAS INVISIBLE IN INDIA AND I DISMISSED IT ON THAT BASIS.

  AND THE ONE SECTION 43 CALLED THE IMPORTANT ONE DISAPPEARS.

      31 December 2028, TOTAL, Mithuna 16.3, the 10th house, 1.52 degrees from
      natal Guru.  Section 43 called it the eclipse that actually matters.
      VISIBLE FROM GUNTUR AT +63 DEGREES.
      BELOW THE HORIZON ACROSS THE ENTIRE UNITED STATES -- -6 in Seattle, -26
      in New York.  It peaks at lunchtime in America.

      IF HE IS IN THE USA THAT DECEMBER, THE STRONGEST ECLIPSE CONTACT IN HIS
      CHART DOES NOT REACH HIM.

  AND THE FOURTH IS GENUINELY SPLIT.

      21 December 2029, TOTAL, Mithuna 5.0, also the 10th house.
      Visible from Guntur (+32), from New York (+13) and marginally from
      Chicago (+4).  BELOW THE HORIZON at Dallas, San Francisco and Seattle.
      THIS ONE DEPENDS ON WHICH AMERICAN CITY.
""")

# =============================================================================
rule('4.  WHAT THE NATAL CHART ALREADY SAYS ABOUT HIM BEING ABROAD')
s12 = (LAG + 11) % 12
print(f"""
  NONE OF THE FOLLOWING NEEDS A RELOCATION TECHNIQUE.  It is in the birth chart
  and has been since 2002.

      THE 12TH HOUSE -- foreign residence, the place away
          {SIGNS[s12]}, empty, lord {LORD[s12]} EXALTED and undivided
          Bhava Bala {BRUP[11]:.2f} rupas -- RANK {BRANK[11]} OF 12, THE STRONGEST BHAVA
          and its lord is the strongest graha in the chart

      THE D24, the varga of learning
          Budha, RAHU AND KETU in its 12th house
          section 13 already reads that as "foreign study, unambiguously"

      SECTION 41 ranked the four senses of "his place" and put ELSEWHERE first
      by a margin of 3.31 rupas over a home, with a standing ninth of twelve.

  SO THE CHART DOES NOT NEED TO BE ASKED WHETHER HE SHOULD BE ABROAD.  IT
  ALREADY SAYS THAT BEING SOMEWHERE OTHER THAN WHERE HE STARTED IS THE THING IT
  IS BEST BUILT FOR.

  If he is in the USA, he is living in the strongest house he owns.  That is a
  natal statement, not a relocation one, and it was true before he went.
""")

# =============================================================================
rule('5.  THE ANSWER')
print("""
  THE CHART IS THE SAME CHART.  Nothing about the nativity changes with an
  address, and no classical technique recasts it for a new city.

  WHAT CHANGES IS WHICH SKY EVENTS HE IS UNDER, AND SECTION 43 HAS TO BE
  AMENDED ON EXACTLY ONE POINT:

      I applied the visibility filter at the BIRTHPLACE.  Visibility belongs to
      the CURRENT location.  For a native in America the 28 August 2026 grahan
      is plainly visible, and that objection -- the one I called decisive --
      does not apply to him.

      THE OTHER THREE OBJECTIONS SURVIVE INTACT, and they are sufficient:
      the strict D10 mapping still fails, this reading still does not run
      transits through vargas, and a Chandra grahan still governs the mind
      rather than the profession.

  THE PRACTICAL DIFFERENCE, IF HE IS IN THE UNITED STATES:

      GAINED   12 January 2028 -- a partial eclipse in his 10TH HOUSE, nearly
               overhead from the east coast, inside the foundation period.
               I had struck this one off for being invisible in India.

      LOST     31 December 2028 -- the total eclipse 1.5 degrees from natal
               Guru in the sealed 10th house.  Below the horizon everywhere in
               America.

      SPLIT    21 December 2029 -- visible from the east, not from the west.

  AND THE LARGER POINT THAT DOES NOT DEPEND ON ANY OF THIS: his 12th house is
  the best-built bhava in the chart with an exalted lord, his learning varga
  puts three grahas in ITS 12th, and section 41 already ranked "elsewhere"
  first among the four senses of place.

      THE CHART WAS ALWAYS POINTING AT SOMEWHERE ELSE.  Whether that somewhere
      is the USA is not something Jyotisha can name, and this document will not
      pretend otherwise.
""")
print('=' * 92)
