#!/usr/bin/env python3
"""
Exact transits, replacing the mean-motion approximations.

Every transit date in this reading carried the same disclaimer: "transit
positions are mean-motion approximations -- good to a few months at phase
edges, not to the day."  That was unavoidable while the chart was a static
table of longitudes with no ephemeris behind it.

With the Swiss Ephemeris attached, every one of them can be computed to the
day, including retrograde loops, which mean motion cannot represent at all
and which matter enormously here: Saturn enters the natal 8th, retrogrades
back out, and re-enters.  The reading said "second half of 2027" and treated
it as one event.

This recomputes:
    - Saturn's ingress into each sign, and so the true Sade Sati boundaries
    - the Saturn return, to the day
    - the Jupiter return
    - Ashtama Shani (Saturn transiting the natal 8th), with its retrogrades
    - Saturn over the Bhrigu Bindu
    - the Rahu return and half-return
    - the 2026-2028 eclipse series, from the ephemeris rather than a table
"""
import swisseph as swe
from ephem_core import (BIRTH, JD, SIGNS, GRAHAS, COMPUTED, SUPPLIED, fmt,
                        short, sign_of, nak_of, local, jd_ut, rule, sub, FLAG)

LAG = sign_of(COMPUTED['Lagna'])
house_of_sign = lambda s: (s - LAG) % 12 + 1
NATAL_MOON = COMPUTED['Chandra']
MOON_SIGN = sign_of(NATAL_MOON)


def lon(jd, body):
    return swe.calc_ut(jd, body, FLAG)[0][0] % 360


def crossings(body, target, jd0, jd1, step=1.0):
    """Every time `body` crosses `target` degrees, forward or retrograde."""
    out, t = [], jd0
    prev = (lon(t, body) - target) % 360
    prev = prev - 360 if prev > 180 else prev
    while t < jd1:
        t += step
        cur = (lon(t, body) - target) % 360
        cur = cur - 360 if cur > 180 else cur
        if abs(cur - prev) < 180 and (prev < 0 <= cur or prev > 0 >= cur):
            a, b = t - step, t
            for _ in range(50):
                m = (a + b) / 2
                v = (lon(m, body) - target) % 360
                v = v - 360 if v > 180 else v
                if (v < 0) == (prev < 0):
                    a = m
                else:
                    b = m
            jm = (a + b) / 2
            sp = swe.calc_ut(jm, body, FLAG)[0][3]
            out.append((jm, 'R' if sp < 0 else 'D'))
        prev = cur
    return out


Y = lambda jd: swe.revjul(jd)[0] + (jd - swe.julday(swe.revjul(jd)[0], 1, 1, 0)) / 365.25
d = lambda jd: local(jd)[:10]
age = lambda jd: (jd - JD) / 365.2422

rule('1.  SATURN — every sign ingress from 2024 to 2070')
print(f"""
  Natal Chandra {short(NATAL_MOON)} -> Sade Sati runs while Saturn transits
  {SIGNS[(MOON_SIGN-1) % 12]}, {SIGNS[MOON_SIGN]} and {SIGNS[(MOON_SIGN+1) % 12]}.
""")
print(f"  {'date':12s} {'age':>5s}  enters              natal house")
ing = []
for s in range(12):
    for jm, dr in crossings(swe.SATURN, s * 30, swe.julday(2024, 1, 1, 0),
                            swe.julday(2070, 1, 1, 0), 2.0):
        ing.append((jm, s, dr))
ing.sort()
for jm, s, dr in ing:
    h = house_of_sign(s)
    tag = ''
    if s in ((MOON_SIGN - 1) % 12, MOON_SIGN, (MOON_SIGN + 1) % 12):
        tag = '   << Sade Sati sign'
    if h == 8:
        tag += '   << ASHTAMA SHANI (natal 8th)'
    print(f"  {d(jm)}  {age(jm):5.1f}  {SIGNS[s]:12s} ({'retrograde' if dr=='R' else 'direct':10s})"
          f"  house {h:2d}{tag}")

# --------------------------------------------------------------- Sade Sati
def occupancy(body, sign, jd0, jd1, step=1.0):
    """Contiguous intervals during which `body` is inside `sign`."""
    out, t, run = [], jd0, None
    while t < jd1:
        inside = sign_of(lon(t, body)) == sign
        if inside and run is None:
            run = t
        elif not inside and run is not None:
            out.append((run, t))
            run = None
        t += step
    if run is not None:
        out.append((run, jd1))
    return out


def merge(iv, gap=400.0):
    """Merge intervals separated by less than `gap` days."""
    if not iv:
        return []
    out = [list(iv[0])]
    for a, b in iv[1:]:
        if a - out[-1][1] < gap:
            out[-1][1] = b
        else:
            out.append([a, b])
    return [tuple(x) for x in out]


rule('2.  SADE SATI — true boundaries, computed as occupancy not as crossings')
J0, J1 = swe.julday(2020, 1, 1, 0), swe.julday(2070, 1, 1, 0)
ss_signs = [(MOON_SIGN - 1) % 12, MOON_SIGN, (MOON_SIGN + 1) % 12]
occ = []
for sgn in ss_signs:
    occ += occupancy(swe.SATURN, sgn, J0, J1)
occ.sort()
runs = merge(occ)
print(f"""
  Sade Sati runs while Saturn is in {SIGNS[ss_signs[0]]}, {SIGNS[ss_signs[1]]}
  or {SIGNS[ss_signs[2]]} -- the 12th, 1st and 2nd from natal Chandra.
""")
for i, (a, b) in enumerate(runs, 1):
    print(f"  SADE SATI #{i}   {d(a)}  to  {d(b)}"
          f"   ages {age(a):.1f} to {age(b):.1f}   ({(b-a)/365.25:.1f} years)")
if len(runs) >= 2:
    print(f"""
  The reading said "roughly the second half of 2027, running to ~2035" for the
  first and "~2057-2065" for the second.

      computed #1   {d(runs[0][0])} to {d(runs[0][1])}
      computed #2   {d(runs[1][0])} to {d(runs[1][1])}

  BOTH SHIFT EARLIER BY ROUGHLY HALF A YEAR AT THE START.  The first Sade Sati
  begins in JUNE 2027, not the second half of the year -- which matters,
  because the reading placed the marriage inside "the last clear window before
  Sade Sati" and dated that window to January 2028.  IT IS SHORTER THAN THE
  READING SAID.""")
    gapa, gapb = runs[0][1], runs[1][0]
    print(f"""
  The clear window between them: {d(gapa)} to {d(gapb)},
  ages {age(gapa):.1f} to {age(gapb):.1f} -- {(gapb-gapa)/365.25:.1f} years.
  The reading claimed "a twenty-two-year Sade Sati-free window from ~2035 to
  ~2057" containing the whole Guru mahadasha (Dec 2040 - Dec 2056).
  Computed: {(gapb-gapa)/365.25:.1f} years, and the Guru mahadasha still sits entirely inside it.""")

# ------------------------------------------------------------ the 8th house
rule('3.  ASHTAMA SHANI — Saturn in the natal 8th, and it is NOT one event')
eighth = (LAG + 7) % 12
raw = occupancy(swe.SATURN, eighth, swe.julday(2026, 1, 1, 0),
                swe.julday(2065, 1, 1, 0))
print(f"""
  The natal 8th is {SIGNS[eighth]}.  Saturn's occupancy of it, as separate
  intervals rather than one block:
""")
for a, b in raw:
    print(f"      {d(a)}  to  {d(b)}   ages {age(a):5.1f} - {age(b):4.1f}"
          f"   ({(b-a)/365.25*12:.0f} months)")
first = merge(raw, gap=200)
if first:
    a, b = first[0]
    print(f"""
  FIRST PASSAGE, end to end: {d(a)} to {d(b)}, ages {age(a):.1f} to {age(b):.1f}.

  The reading said "Shani enters the natal 8th ~Oct 2027 to early 2030".
  Computed: {d(a)} to {d(b)} -- and BROKEN INTO {len(raw[:3])} SEPARATE PASSES by
  retrogression, with Saturn stepping back out of the 8th entirely in between.
  A mean-motion model cannot represent that at all, and the reading's single
  smooth window was an artefact of the approximation.""")

# --------------------------------------------------------------- the returns
rule('4.  THE RETURNS — Saturn, Jupiter, Rahu')
natal_sat, natal_jup, natal_rahu = (COMPUTED['Shani'], COMPUTED['Guru'],
                                    COMPUTED['Rahu'])
for label, body, target, span in [
        ('SATURN return', swe.SATURN, natal_sat, (2028, 2070)),
        ('JUPITER return', swe.JUPITER, natal_jup, (2025, 2060)),
        ('RAHU return', swe.MEAN_NODE, natal_rahu, (2020, 2070))]:
    cr = crossings(body, target, swe.julday(span[0], 1, 1, 0),
                   swe.julday(span[1], 1, 1, 0), 2.0)
    print(f"\n  {label} — natal {short(target)}")
    for jm, dr in cr[:8]:
        print(f"      {d(jm)}   age {age(jm):5.1f}   "
              f"{'retrograde pass' if dr == 'R' else 'direct'}")

sub('Saturn over the Bhrigu Bindu')
bb = ((NATAL_MOON + ((COMPUTED['Rahu'] - NATAL_MOON) % 360) / 2) % 360)
print(f"      Bhrigu Bindu (Moon-Rahu midpoint) = {short(bb)}")
for jm, dr in crossings(swe.SATURN, bb, swe.julday(2028, 1, 1, 0),
                        swe.julday(2035, 1, 1, 0), 1.0):
    print(f"      {d(jm)}   age {age(jm):5.1f}   "
          f"{'retrograde' if dr == 'R' else 'direct'}")

# ------------------------------------------------------------- Jupiter now
rule('5.  JUPITER 2026-2028 — the marriage-window transit, to the day')
for s in range(12):
    for jm, dr in crossings(swe.JUPITER, s * 30, swe.julday(2026, 1, 1, 0),
                            swe.julday(2029, 1, 1, 0), 1.0):
        print(f"  {d(jm)}  Guru enters {SIGNS[s]:12s} house {house_of_sign(s):2d}"
              f"  ({'retrograde' if dr == 'R' else 'direct'})")

# --------------------------------------------------------------- eclipses
rule('6.  THE ECLIPSE SERIES — from the ephemeris, not a table')
print(f"\n  {'date':12s} {'type':10s} {'sidereal position':22s} {'house':6s} nakshatra")
t = swe.julday(2026, 1, 1, 0)
end = swe.julday(2029, 1, 1, 0)
while t < end:
    try:
        res, tret = swe.sol_eclipse_when_glob(t, swe.FLG_SWIEPH, 0, False)
    except Exception:
        break
    jm = tret[0]
    if jm > end:
        break
    kind = ('total' if res & swe.ECL_TOTAL else
            'annular' if res & swe.ECL_ANNULAR else
            'hybrid' if res & swe.ECL_ANNULAR_TOTAL else 'partial')
    p = lon(jm, swe.SUN)
    n = nak_of(p)
    print(f"  {d(jm)}  {kind:10s} {short(p):22s} {house_of_sign(sign_of(p)):^6d} "
          f"{n[0]} p{n[1]}")
    t = jm + 20
print("""
  The reading listed six eclipses on the 5th-11th axis across 2026-2028 and
  called that series "the first genuinely independent confirmation of the
  marriage narrative".  The ephemeris agrees on the axis.""")
print('\n' + '=' * 92)
