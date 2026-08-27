#!/usr/bin/env python3
"""
CHANDRA GRAHAN AND THE D10 LAGNA.

The question: how would a lunar eclipse affect his D10 lagna?

THERE IS A LUNAR ECLIPSE IN KUMBHA ON 28 AUGUST 2026 -- three days after this
was asked -- AND KUMBHA IS HIS D10 LAGNA SIGN.  So the question has an obvious
occasion, and the obvious answer is wrong twice over.

THE SHAPE OF THE ANSWER, following the sequence section 38 fixed:

    1  the premise, computed -- which eclipse, where, when
    2  the STRICT test: mapped into the D10, does it touch the D10 lagna?
    3  the METHODOLOGICAL question, which section 33 already settled
    4  VISIBILITY -- and this is the one nobody raises
    5  what Kumbha actually carries in this chart
    6  the eclipse that DOES apply, and it is not this one
    7  what a Chandra grahan governs, and the natal hook that makes it matter
"""
import swisseph as swe
from ephem_core import (SIGNS, GRAHAS, SUPPLIED, LORD, jd_ut, nak_of, varga,
                        sign_of, dignity, rule, sub)

swe.set_sid_mode(swe.SIDM_LAHIRI)
F = swe.FLG_SWIEPH | swe.FLG_SIDEREAL
POS = dict(SUPPLIED)
LAG = sign_of(POS['Lagna'])
D10L = varga(POS['Lagna'], 10)
LON, LAT = 80.4400, 16.3067          # Guntur
MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
       'Nov', 'Dec']
# NOTE: ECL_TOTAL is 4 and ECL_PENUMBRAL is 64.  An earlier draft of this
# script had those two swapped and mislabelled half the eclipse list.
TYPES = [(swe.ECL_TOTAL, 'TOTAL'), (swe.ECL_PARTIAL, 'partial'),
         (swe.ECL_PENUMBRAL, 'penumbral')]
hsign = lambda si: (si - LAG) % 12 + 1
ordn = lambda n: f"{n}{'th' if 10 <= n % 100 <= 20 else {1:'st',2:'nd',3:'rd'}.get(n%10,'th')}"
occ = lambda si: [g for g in GRAHAS if sign_of(POS[g]) == si]
ASP = {'Surya': [7], 'Chandra': [7], 'Budha': [7], 'Shukra': [7],
       'Mangal': [4, 7, 8], 'Guru': [5, 7, 9], 'Shani': [3, 7, 10],
       'Rahu': [], 'Ketu': []}
SAV = {'Mesha': 21, 'Vrishabha': 22, 'Mithuna': 29, 'Karka': 28, 'Simha': 24,
       'Kanya': 29, 'Tula': 24, 'Vrischika': 28, 'Dhanu': 29, 'Makara': 29,
       'Kumbha': 41, 'Meena': 33}
BRANK = [5, 3, 8, 2, 6, 10, 4, 12, 7, 9, 11, 1]


def when(y, m, d):
    return swe.lun_eclipse_when(jd_ut(y, m, d, 0, 0, 0, 5.5) - 4,
                                swe.FLG_SWIEPH, 0, False)


def detail(y, m, d):
    r = when(y, m, d)
    tj = r[1][0]
    mo = swe.calc_ut(tj, swe.MOON, F)[0][0]
    tr = swe.calc_ut(tj, swe.MOON, swe.FLG_SWIEPH)[0]
    alt = swe.azalt(tj, swe.ECL2HOR, (LON, LAT, 0), 0, 0, (tr[0], tr[1], tr[2]))[1]
    yy, mm, dd, hh = swe.revjul(tj + 5.5 / 24)
    kind = next((v for k, v in TYPES if r[0] & k), '?')
    rah = swe.calc_ut(tj, swe.MEAN_NODE, F)[0][0]
    return dict(jd=tj, lon=mo, kind=kind, alt=alt, rahu=rah,
                when=f"{int(dd)} {MON[mm-1]} {yy}, {int(hh):02d}:{int(hh%1*60):02d} IST")


E1 = detail(2026, 8, 28)
E2 = detail(2027, 2, 21)
E3 = detail(2028, 12, 31)

# =============================================================================
rule('1.  THE PREMISE — AND ITS TIMING IS NOT A COINCIDENCE')
print(f"""
      THE NEXT CHANDRA GRAHAN      {E1['when']}
      type                         {E1['kind']}
      Moon at                      {SIGNS[sign_of(E1['lon'])]} {E1['lon']%30:.2f}, {nak_of(E1['lon'])[0]}
      that sign is his             {ordn(hsign(sign_of(E1['lon'])))} HOUSE
      and his D10 LAGNA sign is    {SIGNS[D10L]}

  THE ECLIPSE FALLS IN THE SIGN THAT IS HIS D10 ASCENDANT, AND IT IS THREE DAYS
  AWAY.  That is why the question was asked, and the premise is sound.

  Transit Rahu at the eclipse: {SIGNS[sign_of(E1['rahu'])]} {E1['rahu']%30:.2f} -- the node is IN Kumbha,
  which is what makes an eclipse there possible at all.
""")

# =============================================================================
rule('2.  THE STRICT TEST — DOES IT TOUCH THE D10 LAGNA?')
d10 = varga(E1['lon'], 10)
print(f"""
  "An eclipse on his D10 lagna" can mean two different things, exactly as the
  Dhanishtha claim in section 33 did:

      LOOSE    the eclipse is in Kumbha, and Kumbha is the SIGN the D10
               ascendant happens to fall in
      STRICT   the eclipse's longitude, MAPPED INTO THE D10, lands on the D10
               ascendant

  Only the strict version is a contact with the D10 lagna in any real sense.
  SO IT WAS COMPUTED:

      eclipse Moon            {E1['lon']:.3f} = {SIGNS[sign_of(E1['lon'])]} {E1['lon']%30:.2f}
      mapped into the D10     {SIGNS[d10]}
      the D10 lagna is        {SIGNS[D10L]}
      so it sits in D10 house {(d10 - D10L) % 12 + 1}, NOT the 1st

  THE STRICT CLAIM IS FALSE, and it fails the same way and for the same reason
  the Rahu-through-Dhanishtha claim failed in section 33.  A D10 sign is three
  degrees wide; anything crossing the zodiac sweeps through all twelve of them
  in one sign, so "being on the D10 lagna" is a matter of hours, not months,
  and it has nothing to do with which rashi the eclipse is in.
""")

# =============================================================================
rule('3.  AND THE DEEPER OBJECTION, WHICH SECTION 33 ALREADY SETTLED')
print("""
  Section 26 recorded that applying transit logic INSIDE a divisional chart is
  done by many and rejected by others, on the ground that a varga maps DIGNITY
  rather than a sky.  Section 33 then declined to run transits through a varga
  and said so.  Section 38 put transit at step 10, as a modifier on the natal
  promise rather than an actor in its own right.

  THAT POSITION HOLDS HERE AND IS NOT REOPENED FOR A MORE DRAMATIC TRANSIT.

  An eclipse is a spectacular event in the SKY.  The D10 is not a sky -- it is
  a tenfold subdivision used to grade the dignity of grahas for professional
  matters.  THERE IS NO POINT IN THE D10 FOR AN ECLIPSE TO HAPPEN AT.
""")

# =============================================================================
rule('4.  VISIBILITY — AND THIS IS THE FACT THAT DECIDES IT')
print(f"""
  THE CLASSICAL POSITION.  A grahan is held to act where it is SEEN.  An eclipse
  below the horizon at a place is traditionally taken not to apply to people
  there -- which is why panchangas print eclipse timings per city and why the
  ritual observances are dropped where the eclipse is invisible.

  SO THE ONLY QUESTION THAT MATTERS FIRST: is this eclipse visible from Guntur?

      eclipse maximum         {E1['when']}
      Moon's altitude at Guntur   {E1['alt']:+.1f} degrees

      THE MOON IS {abs(E1['alt']):.0f} DEGREES BELOW THE HORIZON.

  IT IS MID-MORNING IN INDIA WHEN THIS ECLIPSE PEAKS.  The Moon has set.  The
  entire event happens in his daytime sky, on the other side of the earth.

  BY THE STANDARD THE TRADITION ITSELF USES, THIS ECLIPSE DOES NOT APPLY TO HIM
  AT ALL -- and that is a stronger and simpler objection than anything about
  the D10.
""")

# =============================================================================
rule('5.  WHAT KUMBHA ACTUALLY CARRIES — BECAUSE THE INSTINCT IS SOUND')
ks = 10
print(f"""
  The reason people point at Kumbha for career questions is not silly.  Section
  33 found that KUMBHA CARRIES FIVE SEPARATE CAREER IDENTIFICATIONS, arrived at
  by five different techniques:

      1  the natal {ordn(hsign(ks))} house -- service, employment, competition
      2  the D10 ASCENDANT sign
      3  the ARUDHA OF THE 10TH, A10 -- how the career is perceived
      4  the 10TH FROM CHANDRA -- one of the three career references
      5  the HIGHEST SARVASHTAKAVARGA IN THE CHART -- {SAV['Kumbha']} bindus

      natal occupants of Kumbha   {', '.join(occ(ks)) or 'EMPTY'}
      natal aspects onto it       {', '.join(f'{g}({ordn(a)})' for g in GRAHAS for a in ASP[g] if (sign_of(POS[g])+a-1) % 12 == ks)}

  NO OTHER SIGN IN THIS CHART CARRIES MORE THAN TWO SUCH IDENTIFICATIONS.  So
  an event in Kumbha touches more career signification than an event anywhere
  else -- and the house is EMPTY, so nothing natal is being eclipsed.

  THE INSTINCT IS RIGHT AND THE MECHANISM OFFERED FOR IT IS WRONG.  It matters
  because Kumbha is the career sign, not because the D10 ascendant sits there.
""")

# =============================================================================
rule('6.  WHICH ECLIPSE ACTUALLY REACHES HIM — AND I HAD THIS WRONG TWICE')
print("""
  I DREW UP THIS LIST ONCE WITH THE ECLIPSE-TYPE CONSTANTS SWAPPED.  In Swiss
  Ephemeris ECL_TOTAL is 4 and ECL_PENUMBRAL is 64; I had them the other way
  round, which labelled half the eclipses in the next decade as TOTAL when they
  are penumbral and vice versa.  THE CORRECTED LIST IS BELOW AND IT CHANGES THE
  ANSWER.

  TWO FILTERS ARE APPLIED, AND BOTH ARE CLASSICAL:
      PENUMBRAL eclipses darken nothing visibly and are widely not observed as
      grahan at all.
      An eclipse BELOW THE HORIZON at a place does not apply to people there.
""")
j = jd_ut(2026, 8, 25, 0, 0, 0, 5.5)
print(f"  {'date':15s}{'type':11s}{'Moon':21s}{'house':6s}{'alt':>7s}   verdict")
best = None
for _ in range(12):
    r = swe.lun_eclipse_when(j, swe.FLG_SWIEPH, 0, False)
    tj = r[1][0]
    mo = swe.calc_ut(tj, swe.MOON, F)[0][0]
    tr = swe.calc_ut(tj, swe.MOON, swe.FLG_SWIEPH)[0]
    alt = swe.azalt(tj, swe.ECL2HOR, (LON, LAT, 0), 0, 0, (tr[0], tr[1], tr[2]))[1]
    yy, mm, dd, hh = swe.revjul(tj + 5.5 / 24)
    k = next((v for kk, v in TYPES if r[0] & kk), '?')
    h = hsign(sign_of(mo))
    real = k != 'penumbral' and alt > 0
    note = 'counts' if real else ('penumbral — not a grahan' if k == 'penumbral'
                                  else 'BELOW HORIZON — does not apply')
    if real and h == 10 and best is None:
        note = '<<< IN HIS 10TH HOUSE, AND IT COUNTS'
        best = tj
    print(f"  {int(dd):2d} {MON[mm-1]} {yy}   {k:11s}"
          f"{SIGNS[sign_of(mo)] + ' ' + format(mo % 30, '.1f'):21s}{h:<6d}{alt:>+7.1f}   {note}")
    j = tj + 30
orb = abs(E3['lon'] - POS['Guru'])
print(f"""
  SO THE ONE THE QUESTION ASKS ABOUT DOES NOT COUNT, THE NEXT ONE IS MERELY
  PENUMBRAL, AND THE CAREER ECLIPSE IS TWENTY-EIGHT MONTHS AWAY.

      {E3['when']}
      type                     {E3['kind']}
      Moon at                  {SIGNS[sign_of(E3['lon'])]} {E3['lon']%30:.2f}, {nak_of(E3['lon'])[0]} pada {nak_of(E3['lon'])[1]}
      his                      {ordn(hsign(sign_of(E3['lon'])))} HOUSE -- the career house itself
      altitude at Guntur       {E3['alt']:+.1f} degrees -- HIGH IN THE SKY, FULLY VISIBLE
      natal Guru at            {SIGNS[sign_of(POS['Guru'])]} {POS['Guru']%30:.2f}
      ORB FROM NATAL GURU      {orb:.2f} DEGREES

  A TOTAL LUNAR ECLIPSE, VISIBLE FROM HIS BIRTHPLACE, IN HIS TENTH HOUSE, ONE
  AND A HALF DEGREES FROM THE ONLY GRAHA THAT OCCUPIES IT.

  Section 38 established that the 10th is a SEALED house -- no natal graha
  aspects it at all.  This is an eclipse landing inside that sealed chamber, on
  its single occupant.  Nothing else in the next decade comes close.

  AND IT FALLS INSIDE RAHU-SHANI (Jan 2028 - Dec 2030), which section 42 calls
  the first period in which the vocation karaka runs -- the window this reading
  has named "the foundation" since section 17.

  There is a second one a year later: 21 Dec 2029, TOTAL, Mithuna 5.0, also the
  10th house, also visible.  TWO TOTAL ECLIPSES IN THE CAREER HOUSE INSIDE THE
  FOUNDATION PERIOD.
""")

rule('7.  WHAT A CHANDRA GRAHAN GOVERNS — AND THE NATAL HOOK')
print(f"""
  A lunar eclipse is Rahu or Ketu taking the MOON.  What that afflicts,
  classically, is what Chandra signifies: THE MIND, the mother, the public, the
  emotional body -- not the profession, which belongs to Surya, Budha, Guru and
  Shani.

  A CHANDRA GRAHAN IS NOT A CAREER EVENT IN THE FIRST PLACE.  Even if the D10
  objection and the visibility objection are both set aside, the graha being
  eclipsed does not govern the subject the question is about.

  BUT THERE IS A REAL NATAL HOOK, AND IT IS WORTH MORE THAN THE QUESTION ASKED
  FOR:

      natal Chandra   {POS['Chandra']:.2f} = Vrishabha {POS['Chandra']%30:.2f}, EXALTED, in the 9th
      avastha         MRITA -- 'dead' by the Baladi scheme
      Kashta          4.49, the lowest cost of any graha in the chart

  An exalted Moon in a dead avastha is the most distinctive single fact in this
  chart about his inner life.  ANY Chandra grahan speaks to that -- but it
  speaks to it as a recurring seasonal touch on an existing condition, not as a
  cause of it.

      NEITHER eclipse falls on the natal Moon's axis: the Moon is in Vrishabha,
      the eclipses are in Kumbha and Simha.  So even the mind-level contact is
      indirect.
""")

# =============================================================================
rule('8.  THE VERDICT')
print(f"""
  1  THE PREMISE IS CORRECT.  There is a Chandra grahan in Kumbha on 28 August
     2026, and Kumbha is the sign his D10 ascendant falls in.

  2  THE STRICT CLAIM IS FALSE.  Mapped into the D10, the eclipse degree lands
     in that chart's {(d10 - D10L) % 12 + 1}th house, not its 1st.

  3  THE METHOD DOES NOT ALLOW THE QUESTION ANYWAY.  This reading does not run
     transits through vargas -- section 33 settled that, section 38 put transit
     at step 10 as a modifier.  A varga is not a sky.

  4  AND THE ECLIPSE IS NOT VISIBLE FROM GUNTUR.  The Moon is {abs(E1['alt']):.0f} degrees below
     the horizon at maximum; it peaks at {E1['when'].split(', ')[1]} on an Indian morning.  By the
     tradition's own standard IT DOES NOT APPLY TO HIM, and that is the simplest
     objection of the four.

  5  IT IS ALSO THE WRONG GRAHA FOR THE SUBJECT.  A Chandra grahan afflicts the
     mind, the mother and the public.  Career belongs to Surya, Budha, Guru and
     Shani.

  6  THE ECLIPSE THAT ACTUALLY MATTERS FOR HIS CAREER IS {E3['when'].split(',')[0].upper()}:
     a TOTAL lunar eclipse, {E3['alt']:+.0f} degrees up and fully visible from Guntur, in his
     TENTH HOUSE, {abs(E3['lon']-POS['Guru']):.2f} DEGREES FROM NATAL GURU -- the only graha that
     occupies that house, in a house section 38 showed nothing natal can reach.
     A second total eclipse lands in the same house on 21 Dec 2029.

     BOTH FALL INSIDE RAHU-SHANI, the period sections 17 and 42 call the
     foundation.

  SO THE HONEST ANSWER INVERTS THE QUESTION.  The eclipse three days away is in
  the right sign and cannot touch him.  The eclipses that can touch him are two
  and four years out, in the right HOUSE, on the right GRAHA, inside the right
  PERIOD -- and nobody is talking about those.

  AND THE CAVEAT THIS DOCUMENT ALWAYS ATTACHES.  An eclipse marks a window in
  which part of a chart is under pressure.  It does not say what happens in it,
  and it does not create a promise the natal chart does not already hold.
""")
print('=' * 92)
