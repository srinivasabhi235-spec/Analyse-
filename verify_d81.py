#!/usr/bin/env python3
"""
THE D81 — NAVA-NAVAMSA — COMPUTED, AND WHAT COMPUTING IT EXPOSED.

Section 12 listed D81 as "never attempted -- needs a birth time finer than was
known", printed its positions in a table anyway, and declined to lean on it.
The request was to calculate it properly.

DOING SO TURNED UP SOMETHING LARGER THAN THE D81 -- not a missing test, but a
POLICY SECTION 2 STATED AND THREE LATER SECTIONS DID NOT HONOUR.

A FIRST DRAFT OF PART 4 CLAIMED SECTION 2 "NEVER ASKED WHICH VARGAS THE
RESIDUAL MOVES" AND THAT THE SHODASHAVARGA WAS UNTESTED.  BOTH ARE FALSE.
Section 2 tested all twenty-seven schemes and named eight movers, D12, D24 and
D60 among them.  Part 4 now checks the draft against section 2 and prints the
retraction rather than quietly deleting it.
"""
import swisseph as swe
from ephem_core import (SIGNS, GRAHAS, SUPPLIED, COMPUTED, BIRTH, LORD, varga,
                        dignity, sign_of, jd_ut, rule, sub)

swe.set_sid_mode(swe.SIDM_LAHIRI)
POS = dict(SUPPLIED)
LAG = sign_of(POS['Lagna'])
J0 = jd_ut(2002, 4, 15, 18, 2, 45, 5.5)
asc = lambda j: swe.houses_ex(j, BIRTH['lat'], BIRTH['lon'], b'P',
                              swe.FLG_SIDEREAL)[1][0]
ordn = lambda n: f"{n}{'th' if 10 <= n % 100 <= 20 else {1:'st',2:'nd',3:'rd'}.get(n%10,'th')}"

# =============================================================================
rule('1.  WHAT THE D81 IS, AND WHETHER IT IS PARASHARI')
print(f"""
  D81, the NAVA-NAVAMSA -- the navamsa of the navamsa.  Each sign divided into
  eighty-one parts of {30/81*60:.2f} ARCMINUTES each.

  IT IS NOT IN PARASHARA'S SIXTEEN.  Section 37 enumerated chapter 6's list --
  Rasi, Hora, Decanate, Chaturthamsa, Sapthamsa, Navamsa, Dasamsa, Dvadasamsa,
  Shodasamsa, Vimsamsa, Siddhamsa, Bhamsa, Trimsamsa, Chatvarimsamsa,
  Akshavedamsa, Shashtiamsa -- and D81 is not among them.  It belongs to the
  Nadi and Jaimini streams, where the nava-navamsa is used to refine the
  navamsa result.

  SO IT IS COMPUTED HERE AS AN EXTENSION, NOT AS PARASHARI DOCTRINE.  Its
  construction is not in dispute -- unlike the six vargas section 12 declined,
  D81 is a PURE LINEAR MAP with no starting-sign convention to disagree about.
  Whatever uncertainty it carries is arithmetic precision, not rule choice.
""")

# =============================================================================
rule('2.  THE D81 CHART, ON THE SUPPLIED LONGITUDES')
d81 = {g: varga(POS[g], 81) for g in list(GRAHAS) + ['Lagna']}
L = d81['Lagna']
print(f"      D81 LAGNA   {SIGNS[L]}      (natal lagna {SIGNS[LAG]})\n")
print(f"  {'body':9s}{'D1 longitude':>14s}{'div/81':>8s}   {'D81 sign':12s}{'house':>6s}  dignity")
print(f"  {'Lagna':9s}{POS['Lagna']:14.4f}{int((POS['Lagna']%30)/(30/81))+1:>8d}   "
      f"{SIGNS[L]:12s}{1:>6d}  —")
for g in GRAHAS:
    div = int((POS[g] % 30) / (30 / 81)) + 1
    h = (d81[g] - L) % 12 + 1
    dg = dignity(g, d81[g]) if g not in ('Rahu', 'Ketu') else '—'
    mark = '   <<<' if dg in ('exalted', 'own', 'debilitated') else ''
    print(f"  {g:9s}{POS[g]:14.4f}{div:>8d}   {SIGNS[d81[g]]:12s}{h:>6d}  {dg}{mark}")
print("\n      houses occupied:")
for h in range(1, 13):
    o = [g for g in GRAHAS if (d81[g] - L) % 12 + 1 == h]
    if o:
        print(f"        H{h:<3d}{SIGNS[(L+h-1) % 12]:12s}{', '.join(o)}")
print(f"""
  WHAT IT SHOWS, READ AT THE WEIGHT IT DESERVES:

      SHANI IN ITS OWN SIGN, Makara -- the only own-sign placement in the D81
      GURU DEBILITATED in Makara, sitting with it
      CHANDRA EXALTED in Vrishabha -- the only exaltation, and it repeats the
          D1, where Chandra is exalted in Vrishabha as well
      Guru, Shani and Rahu together in the {ordn((varga(POS['Guru'],81)-L)%12+1)} house
      Surya, Shukra and Ketu together in the {ordn((varga(POS['Surya'],81)-L)%12+1)}

  Shani own and Guru debilitated IN THE SAME SIGN is the sharpest thing in the
  chart -- the graha of depth at home, the graha of knowledge at its worst, in
  one place.  IT IS ALSO EXACTLY THE PAIR SECTION 42 GAVE THE DEEPENING ERA TO.

  THAT IS AS FAR AS THIS SHOULD BE PUSHED, AND PART 3 SAYS WHY.
""")

# =============================================================================
rule('3.  PRECISION — AND THE D81 LAGNA DOES NOT SURVIVE IT')
sp = asc(J0 + 30 / 86400) - asc(J0 - 30 / 86400)
w = 30 / 81
print(f"""      lagna speed at birth      {sp:.4f} deg/min = {sp*60:.2f} arcmin per minute
      one D81 division          {w*60:.2f} arcmin = {w/sp*60:.0f} SECONDS of clock time

  A D81 DIVISION IS NINETY-THREE SECONDS WIDE IN BIRTH TIME.  Section 2 records
  a residual of about a minute in the birth moment.  THE UNCERTAINTY IS TWO
  THIRDS OF A DIVISION.

  AND THE TWO LAGNA VALUES THE READING ALREADY HOLDS STRADDLE A D81 BOUNDARY --
  no perturbation needed:

      SUPPLIED  Kanya {SUPPLIED['Lagna']%30:.4f} = division {int((SUPPLIED['Lagna']%30)/w)+1}, {((SUPPLIED['Lagna']%30)%w)*60:5.2f}' into it  ->  {SIGNS[varga(SUPPLIED['Lagna'],81)]}
      COMPUTED  Kanya {COMPUTED['Lagna']%30:.4f} = division {int((COMPUTED['Lagna']%30)/w)+1}, {((COMPUTED['Lagna']%30)%w)*60:5.2f}' into it  ->  {SIGNS[varga(COMPUTED['Lagna'],81)]}

  THE CHART PRINTED IN PART 2 IS THE SUPPLIED ONE.  The stated birth moment
  gives a different D81 lagna.  The table below is anchored on the stated
  moment, so its middle column is the COMPUTED value, not the printed chart's.
""")
print(f"  {'body':9s}{'-60s':13s}{'stated':13s}{'+60s':13s}  ")
IDS = {'Surya': swe.SUN, 'Chandra': swe.MOON, 'Mangal': swe.MARS,
       'Budha': swe.MERCURY, 'Guru': swe.JUPITER, 'Shukra': swe.VENUS,
       'Shani': swe.SATURN, 'Rahu': swe.MEAN_NODE, 'Ketu': swe.MEAN_NODE}
F = swe.FLG_SWIEPH | swe.FLG_SIDEREAL
for g in ['Lagna'] + list(GRAHAS):
    row = []
    for dt in (-60, 0, 60):
        j = J0 + dt / 86400
        if g == 'Lagna':
            v = asc(j)
        else:
            v = swe.calc_ut(j, IDS[g], F)[0][0]
            if g == 'Ketu':
                v = (v + 180) % 360
        row.append(SIGNS[varga(v, 81)])
    tag = '  <<< MOVES' if len(set(row)) > 1 else '  stable'
    print(f"  {g:9s}{row[0]:13s}{row[1]:13s}{row[2]:13s}{tag}")
print("""
  THE NINE GRAHAS ARE ALL STABLE.  THE LAGNA IS NOT.

  That is the honest division of the result.  The D81 SIGN placements of the
  grahas are as solid as any varga in the document -- the grahas barely move in
  a minute.  The D81 HOUSES are not, because houses are counted from a lagna
  that changes division every ninety-three seconds.

  SO THE SHANI-GURU CONJUNCTION IN MAKARA IS REAL.  Its house number is not.
""")

# =============================================================================
rule('4.  AND COMPUTING IT EXPOSED SOMETHING LARGER')
s, c = SUPPLIED['Lagna'], COMPUTED['Lagna']
gap = (s - c) * 60
lo, hi = J0 - 300 / 86400, J0 + 300 / 86400
for _ in range(60):
    m = (lo + hi) / 2
    if asc(m) < s:
        lo = m
    else:
        hi = m
yy, mm, dd, hh = swe.revjul(lo + 5.5 / 24)
print(f"""
  The reading holds TWO lagna values and has always known it:

      SUPPLIED (from the source data)   {s:.4f} = Kanya {s%30:.4f}
      COMPUTED (from the birth moment)  {c:.4f} = Kanya {c%30:.4f}
      difference                        {gap:+.2f} arcmin = {gap/(sp*60)*60:+.0f} seconds of clock

      the clock time that reproduces the SUPPLIED lagna is
      {int(hh):02d}:{int(hh%1*60):02d}:{round((hh%1*60)%1*60):02d} IST, against a stated 18:02:45.

  A FIRST DRAFT OF THIS SECTION SAID SECTION 2 "NEVER ASKED WHICH VARGAS THAT
  MOVES", AND THAT THE SHODASHAVARGA HAD NEVER BEEN TESTED.  BOTH CLAIMS ARE
  CHECKED BELOW AGAINST WHAT SECTION 2 ACTUALLY PRINTS.
""")
SHOD = [1, 2, 3, 4, 7, 9, 10, 12, 16, 20, 24, 27, 30, 40, 45, 60]
FURTHER = [5, 6, 8, 11, 15, 18, 22, 36, 81, 108, 144, 150]
ALL27 = sorted(set(SHOD + FURTHER) - {1})   # D1 is the rashi itself, not a varga
diff = []
print(f"  {'varga':7s}{'on SUPPLIED':13s}{'on COMPUTED':13s}")
for n in SHOD:
    a, b = varga(s, n), varga(c, n)
    if a != b:
        diff.append(n)
    print(f"  D{n:<6d}{SIGNS[a]:13s}{SIGNS[b]:13s}{'  <<< DIFFERS' if a != b else ''}")
movers = [n for n in ALL27 if varga(s, n) != varga(c, n)]
S2 = [12, 24, 36, 60, 81, 108, 144, 150]      # the list section 2 prints
print(f"""
  {len(diff)} OF THE SIXTEEN SHODASHAVARGA LAGNAS DIFFER: {', '.join('D'+str(x) for x in diff)}.

  NOW THE CHECK.  Across all twenty-seven schemes the movers are:

      computed here          {', '.join('D'+str(x) for x in movers)}
      printed in section 2   {', '.join('D'+str(x) for x in S2)}
      identical?             {'YES — SECTION 2 HAD IT EXACTLY RIGHT' if movers == S2 else 'NO'}
      stable / total         {len(ALL27)-len(movers)} of {len(ALL27)}   (section 2 says "identical in 19 of 27")

  SO THE DRAFT WAS WRONG AND IS RETRACTED.  Section 2 tested the residual across
  twenty-seven schemes, named all eight movers, and D12, D24 and D60 are on its
  list.  Section 12's five-of-twelve was never meant to be the whole census --
  its scope is the TWELVE FURTHER VARGAS, and within that scope it is correct.
  THE APPARATUS HAD THIS RIGHT FROM THE BEGINNING.

  WHAT IS ACTUALLY WRONG IS NOT A MISSING TEST.  IT IS AN UNKEPT PROMISE.
  Section 2, having named the movers, wrote:

      "any claim resting specifically on the D12, D24, D36 or D60 ascendant now
       sits inside a one-minute ambiguity, AND THIS DOCUMENT FLAGS IT WHEREVER
       IT MAKES ONE"

  It then flagged exactly one -- the D60 destination finding in section 11.
  SECTIONS 13, 42 AND 44 EACH REST A PUBLISHED CLAIM ON THE D24 ASCENDANT AND
  NONE OF THEM FLAGGED IT.  Part 5 states those claims and what they become.

  AND THE MECHANISM IS THE ONE SECTION 12 ALREADY NAMED: sensitivity tracks
  WHERE A BOUNDARY FALLS, not division size.  A D24 division is {30/24*60:.0f} arcminutes
  wide and the gap is only {gap:.1f} -- but the lagna sits {abs(27.5-(s%30))*60:.1f} arcminutes from a
  D24 boundary, so a small shift crosses it.
""")

# =============================================================================
rule('5.  THE CONSEQUENCE FOR SECTION 42, STATED PLAINLY')
for lbl, lg in (('SUPPLIED', varga(s, 24)), ('COMPUTED', varga(c, 24))):
    h = lambda g: (varga(POS[g], 24) - lg) % 12 + 1
    print(f"      D24 lagna {SIGNS[lg]:11s} ({lbl:8s})  "
          f"Shukra H{h('Shukra')}, Budha H{h('Budha')}, "
          f"Rahu H{h('Rahu')}, Ketu H{h('Ketu')}, Guru H{h('Guru')}")
print("""
  SECTION 42 PUBLISHED TWO CLAIMS THAT DEPEND ON THE D24 LAGNA:

      "Shukra is the only occupant of the 10th in either varga, and it
       occupies both"                        -- Shukra H10 on supplied,
                                                H11 on computed
      "Budha, the career lord, is in the D24 TWELFTH, with both nodes"
                                             -- Budha H12 on supplied,
                                                H1 on computed

  BOTH ARE CONTINGENT ON WHICH LAGNA VALUE IS USED, AND SECTION 42 DID NOT SAY
  SO -- THOUGH SECTION 2 HAD ALREADY UNDERTAKEN TO SAY IT.  Section 13's "Budha,
  Rahu and Ketu in the 12th -- foreign study, unambiguously" has the same
  dependency, and section 44 leaned on it.  The word "unambiguously" is the
  worst of the three: it is the one place the reading claimed certainty about
  precisely the quantity section 2 had already marked ambiguous.

  WHAT SURVIVES REGARDLESS, BECAUSE IT DOES NOT USE THE D24 LAGNA AT ALL:

      GURU IS EXALTED IN THE D24.  Its sign is Karka either way.  That was
      section 42's strongest D24 finding and it is untouched.
      SHANI IS THE AMATYAKARAKA AND THE 5TH LORD.  Nothing to do with vargas.
      SHUKRA IS IN THE D10 TENTH.  The D10 lagna AGREES between the two values.

  SO SECTION 42'S CONCLUSION -- that depth is excellent and does not arrive
  through the career lord -- RESTS ON THE PART THAT SURVIVES.  The convergence
  it decorated the finding with does not.

  THE READING USES SUPPLIED THROUGHOUT, WHICH IS INTERNALLY CONSISTENT.  What
  was missing is not the knowledge -- section 2 has it -- but the flag at the
  three places where a claim was actually built on it.  Those three are now
  annotated in place.

  AND THE D81 ITSELF FALLS UNDER THE SAME RULE.  Its lagna is on section 2's
  mover list.  So this section prints the D81 GRAHA SIGNS, which are stable,
  and refuses to build anything on the D81 HOUSES, which are not.
""")
print('=' * 92)
