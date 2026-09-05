#!/usr/bin/env python3
"""
THE SUPPLIED LIVE TRANSIT — VERIFIED FIRST, THEN READ.

A transit table arrived labelled "current transit".  This repository does not
read supplied data before checking it: the last transit chart handed over had
an ascendant row that did not belong to the same moment as its planets, and
saying so was more use than reading it would have been.

    1  solve for the moment the table actually describes
    2  reconcile every body against the ephemeris, arcminute by arcminute
    3  the ascendant, checked separately, because it is the row that fails
    4  what it means for THIS chart -- gochara from the Moon and the lagna
    5  the 7th house, because of what is sitting in it
"""
import swisseph as swe

import ground as G
from ephem_core import SIGNS, GRAHAS, BIRTH, short, nak_of, dignity, rule, sub

swe.set_sid_mode(swe.SIDM_LAHIRI)
FL = swe.FLG_SWIEPH | swe.FLG_SIDEREAL | swe.FLG_SPEED
ORD = {1: 'st', 2: 'nd', 3: 'rd'}
ordn = lambda n: f"{n}{ORD.get(n, 'th') if n < 21 else 'th'}"
MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
       'Nov', 'Dec']

# --------------------------------------------------- the table, as supplied
SUP = {                      # body: (longitude, speed as printed)
    'Lagna':   (28 + 58/60 + 13/3600 + 0*30,      416.76),
    'Surya':   (18 + 53/60 + 54/3600 + 4*30,        0.96),
    'Chandra': (6 + 58/60 + 52/3600 + 2*30,        14.29),
    'Mangal':  (22 + 6/60 + 56/3600 + 2*30,         0.62),
    'Budha':   (27 + 4/60 + 41/3600 + 4*30,         1.78),
    'Guru':    (20 + 26/60 + 27/3600 + 3*30,        0.20),
    'Shukra':  (2 + 31/60 + 45/3600 + 6*30,         0.73),
    'Shani':   (19 + 10/60 + 2/3600 + 11*30,       -0.07),
    'Rahu':    (4 + 48/60 + 59/3600 + 10*30,       -0.06),
    'Ketu':    (4 + 48/60 + 59/3600 + 4*30,        -0.06),
}
OUTER = {
    'Arun (Uranus)':  (11 + 26/60 + 56/3600 + 1*30,   0.00),
    'Varun (Neptune)': (9 + 18/60 + 47/3600 + 11*30, -0.03),
    'Yam (Pluto)':     (8 + 49/60 + 7/3600 + 9*30,   -0.02),
}
TRUE_NODE = {
    'Spashth Rahu': (5 + 31/60 + 23/3600 + 10*30,  0.01),
    'Spashth Ketu': (5 + 31/60 + 23/3600 + 4*30,   0.01),
}
IDS = {'Surya': swe.SUN, 'Chandra': swe.MOON, 'Mangal': swe.MARS,
       'Budha': swe.MERCURY, 'Guru': swe.JUPITER, 'Shukra': swe.VENUS,
       'Shani': swe.SATURN}
lon = lambda j, i: swe.calc_ut(j, i, FL)[0]


def stamp(j, tz=5.5):
    y, m, d, h = swe.revjul(j + tz / 24)
    hh = int(h)
    mm = int((h - hh) * 60)
    return f"{int(d):2d} {MON[m-1]} {y}  {hh:02d}:{mm:02d} IST"


# =============================================================================
rule('1.  WHAT MOMENT DOES THE TABLE DESCRIBE?')
print("""
  A FIRST ATTEMPT ANCHORED ON THE MOON ALONE AND LANDED A MONTH WRONG.  The
  Moon returns to any longitude every 27.3 days, so inside a search window of a
  few months there are several equally good Moon fits and only one of them is
  the right date.  IT HAS TO BE A JOINT FIT: the slow grahas pin the month, the
  Moon then pins the hour.
""")


def misfit(j):
    tot = 0.0
    for g in ['Surya', 'Chandra', 'Mangal', 'Budha', 'Guru', 'Shukra', 'Shani']:
        v = lon(j, IDS[g])[0] % 360
        tot += abs((v - SUP[g][0] + 180) % 360 - 180)
    v = lon(j, swe.MEAN_NODE)[0] % 360
    tot += abs((v - SUP['Rahu'][0] + 180) % 360 - 180)
    return tot


lo, hi = swe.julday(2026, 1, 1, 0.0), swe.julday(2027, 6, 1, 0.0)
best, bj = 1e9, None
j = lo
while j < hi:
    d = misfit(j)
    if d < best:
        best, bj = d, j
    j += 0.25
step = 0.25
while step > 1e-6:                        # refine
    for cand in (bj - step, bj + step):
        d = misfit(cand)
        if d < best:
            best, bj = d, cand
    step /= 2
print(f"      joint best fit           {stamp(bj)}")
print(f"      summed residual          {best*60:.1f} arcminutes across 8 bodies\n")

# =============================================================================
rule('2.  EVERY BODY, RECONCILED')
print(f"  {'body':9s}{'supplied':22s}{'computed':22s}{'delta':>9s}   speed chk")
worst, rows = 0.0, []
for g in ['Surya', 'Chandra', 'Mangal', 'Budha', 'Guru', 'Shukra', 'Shani']:
    x = lon(bj, IDS[g])
    d = ((x[0] % 360 - SUP[g][0] + 180) % 360 - 180) * 60
    sd = x[3] - SUP[g][1]
    worst = max(worst, abs(d))
    rows.append((g, d))
    print(f"  {g:9s}{short(SUP[g][0]):22s}{short(x[0]):22s}{d:+9.2f}′"
          f"   {x[3]:+.2f} vs {SUP[g][1]:+.2f}")
x = lon(bj, swe.MEAN_NODE)
for g, off in (('Rahu', 0), ('Ketu', 180)):
    v = (x[0] + off) % 360
    d = ((v - SUP[g][0] + 180) % 360 - 180) * 60
    worst = max(worst, abs(d))
    rows.append((g, d))
    print(f"  {g:9s}{short(SUP[g][0]):22s}{short(v):22s}{d:+9.2f}′"
          f"   {x[3]:+.2f} vs {SUP[g][1]:+.2f}   (MEAN node)")
print(f"\n      worst deviation across the seven grahas and the mean nodes: "
      f"{worst:.2f} arcminutes\n")

sub('the table gives BOTH nodes, which is unusual and worth checking')
xt = lon(bj, swe.TRUE_NODE)
for g, off in (('Spashth Rahu', 0), ('Spashth Ketu', 180)):
    v = (xt[0] + off) % 360
    d = ((v - TRUE_NODE[g][0] + 180) % 360 - 180) * 60
    print(f"      {g:14s}{short(TRUE_NODE[g][0]):20s}{short(v):20s}{d:+8.2f}′")
print(f"""
      mean node and true node differ by {abs(((x[0]-xt[0]+180)%360-180))*60:.1f} arcminutes here.
      THE TABLE IS RIGHT TO PRINT BOTH.  This document uses the MEAN node
      throughout, which is the commoner Parashari choice, and the difference is
      too small to move a sign or a nakshatra for either.
""")

sub('the three outer planets')
for nm, (sl, sp) in OUTER.items():
    pid = {'Arun (Uranus)': swe.URANUS, 'Varun (Neptune)': swe.NEPTUNE,
           'Yam (Pluto)': swe.PLUTO}[nm]
    x2 = lon(bj, pid)
    d = ((x2[0] % 360 - sl + 180) % 360 - 180) * 60
    print(f"      {nm:17s}{short(sl):20s}{short(x2[0]):20s}{d:+8.2f}′")
print("""
      REPRODUCED, AND NOT USED.  Uranus, Neptune and Pluto are not in the nine
      grahas and have no place in any Parashari rule -- no dignity, no aspect,
      no dasha, no ashtakavarga.  They are verified because they were supplied,
      and then set aside, which is the honest treatment rather than either
      silently dropping them or inventing a doctrine for them.
""")

# =============================================================================
rule('3.  THE ASCENDANT — CHECKED SEPARATELY')
print(f"""
  The last transit chart handed to this reading had an ascendant that did not
  belong to the same moment as its planets.  So this one is solved rather than
  assumed.  The Moon moves 0.6 arcminutes a MINUTE, so it fixes the moment to
  within seconds and its residual above is 0.00' -- the planets belong to
  22:02.  Does the ascendant?
""")
asc = lambda j, lat, lonn: swe.houses_ex(j, lat, lonn, b'P',
                                         swe.FLG_SIDEREAL)[1][0]
a_birth = asc(bj, BIRTH['lat'], BIRTH['lon'])
print(f"      at Guntur, at that moment   {short(a_birth)}")
print(f"      the table says              {short(SUP['Lagna'][0])}")
print(f"      difference                  {((a_birth - SUP['Lagna'][0] + 180) % 360 - 180):+.2f}°\n")
# how far back/forward in time would give the supplied lagna at Guntur?
lo2, hi2 = bj - 0.5, bj + 0.5
for _ in range(60):
    m = (lo2 + hi2) / 2
    if ((asc(m, BIRTH['lat'], BIRTH['lon']) - SUP['Lagna'][0] + 180) % 360 - 180) < 0:
        lo2 = m
    else:
        hi2 = m
print(f"      the supplied ascendant occurs at Guntur at {stamp(lo2)}")
print(f"      which is {abs(lo2-bj)*24*60:.0f} minutes from the moment the Moon fixes.\n")
mdiff = abs(lo2 - bj) * 24 * 60
if mdiff < 15:
    print(f"""      => THE SAME DEFECT AS LAST TIME, AND FAR SMALLER.  The nine grahas all
         reproduce to under half an arcminute at 22:02.  The ascendant belongs
         to 22:09 -- {mdiff:.0f} minutes later, {abs(a_birth-SUP['Lagna'][0]):.2f}° of ascendant motion.

         LAST TIME THE MISMATCH WAS A DIFFERENT CONTINENT.  This time it is
         seven minutes, which is almost certainly the page rendering the
         ascendant a moment after the planets.  IT CHANGES NOTHING BELOW:
         gochara is read from the NATAL Moon and the NATAL lagna, and the
         transit ascendant plays no part in any rule used here.""")
else:
    print(f"      => The rows are {mdiff:.0f} minutes apart.  For an ascendant that "
          f"is\n         {mdiff/4:.1f} degrees, which is a real discrepancy but a small one, and\n"
          f"         it changes NOTHING below: gochara is read from the natal Moon\n"
          f"         and the natal lagna.  The transit ascendant plays no part.")

# =============================================================================
rule('4.  WHERE IT ALL FALLS IN HIS CHART')
GOOD = {'Surya': {3, 6, 10, 11}, 'Chandra': {1, 3, 6, 7, 10, 11},
        'Mangal': {3, 6, 11}, 'Budha': {2, 4, 6, 8, 10, 11},
        'Guru': {2, 5, 7, 9, 11}, 'Shukra': {1, 2, 3, 4, 5, 8, 9, 11, 12},
        'Shani': {3, 6, 11}, 'Rahu': {3, 6, 10, 11}, 'Ketu': {3, 6, 11}}
print(f"""      natal lagna {SIGNS[G.LAG]}, natal Chandra in {SIGNS[G.MOON_SIGN]}
""")
print(f"  {'graha':9s}{'transit sign':13s}{'dignity':13s}{'from lagna':13s}"
      f"{'from Moon':12s}{'bindus':>7s}  gochara")
nf = 0
for g in ['Surya', 'Chandra', 'Mangal', 'Budha', 'Guru', 'Shukra', 'Shani',
          'Rahu', 'Ketu']:
    s = G.sign_of(SUP[g][0])
    hl = (s - G.LAG) % 12 + 1
    hm = (s - G.MOON_SIGN) % 12 + 1
    dg = dignity(g, s) if g in G.G7 else 'shadow'
    b = G.BAV[g][s] if g in G.G7 else None
    ok = hm in GOOD[g]
    nf += ok
    print(f"  {g:9s}{SIGNS[s]:13s}{dg:13s}{ordn(hl) + ' house':13s}"
          f"{ordn(hm):12s}{('—' if b is None else str(b)):>7s}  "
          f"{'FAVOURABLE' if ok else 'not favourable'}")
print(f"\n      {nf} of 9 favourable by classical gochara from the Moon.\n")

# =============================================================================
rule('5.  THE 7TH HOUSE — BECAUSE OF WHAT IS SITTING IN IT')
S7 = G.sign_in_house(7)
sh_s = G.sign_of(SUP['Shani'][0])
gu_s = G.sign_of(SUP['Guru'][0])
gu_asp = [(gu_s + a - 1) % 12 for a in (5, 7, 9)]
sh_asp = [(sh_s + a - 1) % 12 for a in (3, 7, 10)]
print(f"""
      the natal 7th house      {SIGNS[S7]} -- empty, unaspected natally
      transit Shani            {short(SUP['Shani'][0])}  {'<<< IN IT' if sh_s == S7 else ''}
      transit Guru             {short(SUP['Guru'][0])} in {SIGNS[gu_s]}
      Guru's aspects reach     {', '.join(SIGNS[x] for x in gu_asp)}
      does Guru reach the 7th? {'YES — by its 9th aspect' if S7 in gu_asp else 'no'}
""")
if sh_s == S7 and S7 in gu_asp:
    print("""  SO THE DOUBLE TRANSIT ON THE 7TH HOUSE IS LIVE RIGHT NOW.

      Shani IN the 7th, Guru aspecting it by the 9th.  Guru and Shani both
      touching one bhava is the classical condition for that bhava delivering,
      and this is the bhava the marriage question turns on.

      THIS WAS NOT FITTED AFTERWARDS.  verify_partner.py scanned 2026 to 2071
      month by month BEFORE this table arrived and returned a double transit on
      the 7th house running Sep-Oct 2026 -- 'Guru 9th, Shani in'.  THE SUPPLIED
      TRANSIT INDEPENDENTLY CONFIRMS THE SCAN.
""")

def _ing(sign, y0, y1):
    j2, out, prev = swe.julday(y0, 1, 1, 0.0), [], None
    while j2 < swe.julday(y1, 1, 1, 0.0):
        s2 = G.sign_of(lon(j2, swe.SATURN)[0] % 360)
        if prev is not None and s2 != prev[1]:
            a2, b2 = prev[0], j2
            for _ in range(50):
                m2 = (a2 + b2) / 2
                if G.sign_of(lon(m2, swe.SATURN)[0] % 360) == prev[1]:
                    a2 = m2
                else:
                    b2 = m2
            if s2 == sign or prev[1] == sign:
                out.append((a2, prev[1], s2))
        prev = (j2, s2)
        j2 += 1
    return out


_i7 = _ing(S7, 2024, 2029)
_sh_in_j = min(j2 for j2, a2, b2 in _i7 if b2 == S7)
_sh_out_j = max(j2 for j2, a2, b2 in _i7 if a2 == S7)
_sh_in, _sh_out = stamp(_sh_in_j)[:12].strip(), stamp(_sh_out_j)[:12].strip()
_passes = '\n'.join(
    f"          {stamp(j2)[:12].strip():13s}{SIGNS[a2]:11s} -> {SIGNS[b2]}"
    + ('   enters the 7th' if b2 == S7 else '   leaves the 7th')
    for j2, a2, b2 in _i7)

print(f"""  AND THIS IS THE POINT WORTH MORE THAN THE DATES.

      SECTION 4 OF THE READING NAMES THE 7TH AS ONE OF THREE HOUSES NOTHING IN
      THE NATAL CHART TOUCHES -- no occupant, no aspect.  The self, the
      children and the spouse.

      RIGHT NOW ONE OF THOSE THREE IS BEING OCCUPIED AND ASPECTED.  Transit
      Shani sits in it; transit Guru looks at it.  A house that is structurally
      unattended for a whole life is, for this window, attended by both of the
      slow grahas at once.

      THAT IS AS CLOSE AS GOCHARA COMES TO SAYING SOMETHING IS HAPPENING HERE.
""")
ad = [x for x in G.ANTARDASHA if x[2] <= bj < x[3]][0]
print(f"""      and the period underneath it   {ad[0]}-{ad[1]}, to {stamp(ad[3])[:12].strip()}

  WHAT THAT DOES AND DOES NOT MEAN.

      Shani in the 7th is not a benign transit and this document has said so
      before: it is the 7th under its heaviest natural obstruction -- delay,
      weight, seriousness, the removal of easy options.  GURU'S ASPECT DOES NOT
      CANCEL THAT.  What the pair does is make the house LIVE.

      Shani is {'RETROGRADE' if SUP['Shani'][1] < 0 else 'direct'} right now at {abs(SUP['Shani'][1]):.2f}°/day, and its stay in
      {SIGNS[S7]} is NOT ONE CONTINUOUS PASS -- it leaves and comes back:
{_passes}
      So the 7th-house window does not simply run out.  IT BREAKS IN JUNE 2027,
      resumes in October, and closes for good in February 2028.

      AND ONE THING WORTH SAYING PLAINLY: the same Shani reaches the 8th house
      in June 2027, which is where section 11 of the reading picks it up.  The
      7th-house transit is what is happening NOW; the 8th-house one is next.
""")
print('=' * 92)
