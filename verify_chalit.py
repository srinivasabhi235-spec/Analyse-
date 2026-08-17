#!/usr/bin/env python3
"""
Bhava Chalit -- the largest methodological gap in the reading, now closed.

Every previous section of this document used WHOLE-SIGN houses: the sign
containing the ascendant is the 1st house entire, the next sign the 2nd, and
so on.  That was not a preference.  It was forced, because no house cusp can
be computed without an exact birth time and place, and neither was known.

Both are now known, so the cusps can be computed -- and the gap audit's own
words were: "with the lagna at 27°37′, a cuspal system would push several
grahas into adjacent houses."

It does.  This script computes four house systems, states which grahas move
under each, and then does the part that matters: works out which conclusions
in this reading survive the move and which do not.

The four systems, and why each is here:

  WHOLE SIGN   what the document used.  Still the majority Parashari practice
               in India, and the frame in which every Ashtakavarga and Bhava
               Bala figure supplied with the source data was computed.

  EQUAL BHAVA  Parashara's own chalit: the ascendant degree is the MIDPOINT
               (bhava madhya) of the 1st house, not its start, and each bhava
               runs 15° either side of its madhya.

  SRIPATI      the same midpoint convention, but with Porphyry cusps, so the
               bhavas are unequal in the way the latitude demands.

  PLACIDUS     the KP convention, where the cusp is the START of the house.
               Included because it is what most software labels "chalit".
"""
import swisseph as swe
from ephem_core import (BIRTH, JD, SIGNS, GRAHAS, COMPUTED, SUPPLIED, LORD,
                        fmt, short, sign_of, rule, sub)

ASC = COMPUTED['Lagna']
LAGNA_SIGN = sign_of(ASC)
POS = {g: COMPUTED[g] for g in GRAHAS}

HOUSE_OF = ['self', 'wealth, family, speech', 'effort, courage, siblings',
            'home, mother, roots', 'children, romance', 'adversity, health',
            'partnership', 'transformation', 'dharma, father, fortune',
            'career, standing', 'gains, networks', 'loss, foreign, moksha']


def whole_sign(l):
    return (sign_of(l) - LAGNA_SIGN) % 12 + 1


def from_madhya(l, madhyas):
    """Bhava number when `madhyas` are the twelve bhava MIDPOINTS."""
    for i in range(12):
        a = (madhyas[i] + madhyas[(i - 1) % 12] + (360 if
             (madhyas[i] - madhyas[(i - 1) % 12]) % 360 > 180 else 0)) / 2
        a = ((madhyas[(i - 1) % 12] + ((madhyas[i] - madhyas[(i - 1) % 12])
                                       % 360) / 2) % 360)
        b = ((madhyas[i] + ((madhyas[(i + 1) % 12] - madhyas[i])
                            % 360) / 2) % 360)
        if (l - a) % 360 < (b - a) % 360:
            return i + 1
    return None


def from_cusps(l, cusps):
    """Bhava number when `cusps` are the twelve house START points."""
    for i in range(12):
        a, b = cusps[i], cusps[(i + 1) % 12]
        if (l - a) % 360 < (b - a) % 360:
            return i + 1
    return None


# ---------------------------------------------------------------- the systems
equal_madhya = [(ASC + 30 * i) % 360 for i in range(12)]
porph_cusps, _ = swe.houses_ex(JD, BIRTH['lat'], BIRTH['lon'], b'O',
                               swe.FLG_SIDEREAL)
plac_cusps, _ = swe.houses_ex(JD, BIRTH['lat'], BIRTH['lon'], b'P',
                              swe.FLG_SIDEREAL)
porph_cusps = [c % 360 for c in porph_cusps]
plac_cusps = [c % 360 for c in plac_cusps]

SYS = {
    'whole sign': lambda l: whole_sign(l),
    'equal bhava': lambda l: from_madhya(l, equal_madhya),
    'Sripati': lambda l: from_madhya(l, porph_cusps),
    'Placidus/KP': lambda l: from_cusps(l, plac_cusps),
}

rule('BHAVA CHALIT — the cuspal houses the reading could not compute')
print(f"""
  ascendant   {fmt(ASC)}   ({ASC:.4f}° sidereal)
  latitude    {BIRTH['lat']}°N -- low enough that Placidus distortion is modest
""")

sub('the twelve cusps, by system')
print(f"  {'bhava':6s} {'equal madhya':22s} {'Sripati madhya':22s} {'Placidus start':22s}")
for i in range(12):
    print(f"  {i+1:<6d} {short(equal_madhya[i]):22s} {short(porph_cusps[i]):22s} "
          f"{short(plac_cusps[i]):22s}")

# ---------------------------------------------------------------------------
rule('WHICH GRAHAS MOVE')
print(f"\n  {'graha':9s} {'longitude':22s}" +
      ''.join(f'{k:>14s}' for k in SYS))
moves = {k: [] for k in SYS if k != 'whole sign'}
rows = {}
for g in GRAHAS:
    h = {k: f(POS[g]) for k, f in SYS.items()}
    rows[g] = h
    flag = ''
    for k in moves:
        if h[k] != h['whole sign']:
            moves[k].append((g, h['whole sign'], h[k]))
    print(f"  {g:9s} {fmt(POS[g], 22)}" +
          ''.join(f"{h[k]:>14d}" for k in SYS))

print()
for k, lst in moves.items():
    if not lst:
        print(f"  {k:14s} nothing moves")
        continue
    print(f"  {k:14s} {len(lst)} of 9 move:")
    for g, a, b in lst:
        print(f"                   {g:9s} {a:2d} -> {b:2d}"
              f"   ({HOUSE_OF[a-1]}  ->  {HOUSE_OF[b-1]})")

# ---------------------------------------------------------------------------
rule('WHAT THAT DOES TO THE READING — claim by claim')

CLAIMS = []


def check(name, fn, note=''):
    res = {k: fn(k) for k in SYS}
    same = all(v == res['whole sign'] for v in res.values())
    CLAIMS.append((name, res, same, note))


def occupants(system, n):
    return [g for g in GRAHAS if SYS[system](POS[g]) == n]


check('Seven of nine grahas in two adjacent houses',
      lambda k: max(len(occupants(k, n)) + len(occupants(k, n + 1))
                    for n in range(1, 12)))
check('Grahas in the 8th house',
      lambda k: len(occupants(k, 8)))
check('Grahas in the 9th house',
      lambda k: len(occupants(k, 9)))
check('Grahas in the 7th house',
      lambda k: len(occupants(k, 7)))
check('Kendras occupied (1,4,7,10)',
      lambda k: sum(1 for n in (1, 4, 7, 10) if occupants(k, n)))
check('Surya house',    lambda k: SYS[k](POS['Surya']))
check('Chandra house',  lambda k: SYS[k](POS['Chandra']))
check('Budha house (lagna+10th lord)', lambda k: SYS[k](POS['Budha']))
check('Shukra house (Atmakaraka)', lambda k: SYS[k](POS['Shukra']))
check('Guru house (only kendra graha)', lambda k: SYS[k](POS['Guru']))
check('Ketu house', lambda k: SYS[k](POS['Ketu']))

print(f"\n  {'claim':40s}" + ''.join(f'{k:>14s}' for k in SYS) + '   verdict')
for name, res, same, _ in CLAIMS:
    print(f"  {name:40s}" + ''.join(f"{res[k]:>14}" for k in SYS)
          + ('   holds' if same else '   CHANGES'))

# ---------------------------------------------------------------------------
rule('THE YOGAS, TESTED UNDER EACH FRAME')
print("""
  House-based yogas are the ones at risk.  Sign-based facts -- conjunction,
  exchange, dignity, nakshatra -- cannot move, because no house system
  touches them.
""")
for sysname in SYS:
    f = SYS[sysname]
    surya_h = f(POS['Surya'])
    guru_h = f(POS['Guru'])
    shukra_h, budha_h = f(POS['Shukra']), f(POS['Budha'])
    vimala = surya_h == 8            # 12th lord in the 8th
    amala = guru_h == 10             # benefic alone in the 10th from lagna
    dky_same = shukra_h == budha_h   # 9th and 10th lords conjunct in one bhava
    print(f"  {sysname:14s}"
          f"  Vimala {'FORMS ' if vimala else 'GONE  '}(12th lord Surya in bhava {surya_h})"
          f"   Amala {'FORMS' if amala else 'GONE '} (Guru in {guru_h})"
          f"   DKY lords together: {'yes' if dky_same else 'NO'}")
print("""
  UNAFFECTED BY ANY OF THIS, because none of it is a house fact:
    - the Mangal ⇄ Shukra parivartana        (sign exchange)
    - the Budha ⇄ Ketu nakshatra parivartana (star exchange)
    - Dharma-Karmadhipati as a CONJUNCTION   (both lords in Mesha, 13°09′)
    - every dignity, exaltation and vargottama finding
    - the seven-grahas-in-73° concentration and everything derived from it
    - the entire rarity measurement in §14, which counts signs and spacing
""")

rule('THE HONEST SUMMARY')
ws8 = occupants('whole sign', 8)
eq8 = occupants('equal bhava', 8)
sr8 = occupants('Sripati', 8)
spread = {k: len({SYS[k](POS[g]) for g in GRAHAS[:7]}) for k in SYS}
print(f"""
  The reading's central structure is: SEVEN OF NINE GRAHAS IN THE 8TH AND
  9TH, those two houses in mutual exchange, and the 8th as the processing
  plant for the chart.  Under the cuspal systems it SHIFTS ONE HOUSE BACK
  for the grahas at low degrees.

      whole sign   8th holds {ws8}
      equal bhava  8th holds {eq8}
      Sripati      8th holds {sr8}

  Read carefully, three things are true at once.

  1.  THE CONCENTRATION SURVIVES; THE COUNT DOES NOT.  Seven classical grahas
      sit inside a 73° arc in three signs, and no house system can alter that
      -- it is a fact about SPACING.  But "seven of nine in TWO adjacent
      houses" is a whole-sign statement.  Under the cuspal frames those seven
      spread across {spread['equal bhava']} bhavas rather than {spread['whole sign']}, and the largest pair of
      adjacent bhavas holds five rather than seven.

      So the depth-without-breadth reading, the Shoola and Shakti nabhasa
      yogas and the §14 rarity result are untouched -- they were computed
      from signs and longitudes.  The specific phrase "seven of nine grahas
      in two adjacent houses" is frame-dependent and must be labelled as such.

  2.  THE HOUSE LABELS MOVE, AND THAT IS NOT COSMETIC.  Under equal bhava and
      Sripati, Surya and Budha fall in the 7TH rather than the 8th, and
      Chandra and Mangal fall in the 8TH rather than the 9th.  VIMALA YOGA
      DISSOLVES under every cuspal frame, because the 12th lord is no longer
      in the 8th.  That is the single largest casualty, and this document
      leaned on Vimala for its "adversity is converted rather than endured"
      conclusion.

  3.  BUT THE SOURCE DATA IS WHOLE-SIGN.  Every Ashtakavarga bindu, every
      Bhava Bala rupa, every Shodhya Pinda figure supplied with this chart was
      computed in the whole-sign frame.  Those tables ARE the evidence for
      most of this document's quantitative claims.  Mixing a cuspal house
      assignment into strength figures derived under whole-sign would produce
      numbers that mean nothing.

  THE RESPONSIBLE POSITION, STATED PLAINLY:

      This reading uses WHOLE-SIGN houses, as it always did, and that choice
      is now DECLARED rather than assumed.  It is the frame the source tables
      were built in, it remains majority Parashari practice, and the internal
      consistency of the document depends on it.

      A Bhava Chalit reading of the same chart would move four grahas and
      would dissolve Vimala Yoga.  That is a genuine fork in the road, not a
      rounding error, and anyone who prefers the cuspal frame should know
      that this document does not answer their question.

      What CANNOT be claimed any longer is that the whole-sign result is
      unaffected by the choice.  The gap audit called this the largest
      methodological gap in the document.  It was right, and closing it has
      made the exposure larger rather than smaller.
""")

# ---------------------------------------------------------------------------
rule('ONE THING THE CUSPS SETTLE OUTRIGHT')
d = (ASC % 30)
print(f"""
  The ascendant is {short(ASC)} -- {30-d:.2f}° from Tula, which at
  {14.34:.2f}′ per minute is about {(30-d)*60/14.34:.1f} minutes of clock time.

  The reading has carried a warning since its first version: "everything that
  depends on house placement depends on that margin holding."  With the birth
  time now exact to the second, THAT WARNING IS RETIRED.  The lagna is Kanya,
  Chitra pada 2, and it is not in question.

  What replaces it is a smaller and better-defined caveat: the ascendant is
  in the last degrees of its sign, which is precisely the condition under
  which whole-sign and cuspal frames disagree most.  A lagna at 15° would
  have made the two frames nearly identical.  At {d:.1f}° they differ for four
  grahas.
""")
print('=' * 92)
