#!/usr/bin/env python3
"""
The two dispositor levels, laid out together.

Jyotisha has two independent chains of authority.  The RASHI level asks who
owns the sign a graha stands in; the NAKSHATRA level asks who owns the lunar
mansion.  Classical practice treats the rashi level as the FIELD a graha
works in and the nakshatra level as the AGENT that actually delivers the
result -- so when they disagree, the nakshatra generally wins for outcomes.

This computes both chains in full, finds every terminus, and then maps the
twelve house lords through their nakshatra lords, which reveals who is really
paying out each area of life.
"""
SIGNS = ['Mesha', 'Vrishabha', 'Mithuna', 'Karka', 'Simha', 'Kanya',
         'Tula', 'Vrischika', 'Dhanu', 'Makara', 'Kumbha', 'Meena']
NAK = ['Ashwini', 'Bharani', 'Krittika', 'Rohini', 'Mrigashira', 'Ardra',
       'Punarvasu', 'Pushya', 'Ashlesha', 'Magha', 'P.Phalguni', 'U.Phalguni',
       'Hasta', 'Chitra', 'Swati', 'Vishakha', 'Anuradha', 'Jyeshtha',
       'Mula', 'P.Ashadha', 'U.Ashadha', 'Shravana', 'Dhanishtha',
       'Shatabhisha', 'P.Bhadrapada', 'U.Bhadrapada', 'Revati']
NAK_LORD = ['Ketu', 'Shukra', 'Surya', 'Chandra', 'Mangal',
            'Rahu', 'Guru', 'Shani', 'Budha'] * 3
LORD = ['Mangal', 'Shukra', 'Budha', 'Chandra', 'Surya', 'Budha',
        'Shukra', 'Mangal', 'Guru', 'Shani', 'Shani', 'Guru']
SP = {'Mangal': 212, 'Shani': 184, 'Budha': 152, 'Surya': 138,
      'Shukra': 95, 'Guru': 81, 'Chandra': 33}
KASHTA = {'Shani': 46.83, 'Mangal': 38.87, 'Budha': 30.32, 'Guru': 15.10,
          'Shukra': 11.87, 'Surya': 7.83, 'Chandra': 4.49}
ISHTA = {'Shukra': 47.49, 'Surya': 46.88, 'Guru': 37.30, 'Chandra': 24.54,
         'Mangal': 19.66, 'Budha': 18.91, 'Shani': 12.48}
HOUSE_NAME = ['self', 'wealth, family, speech', 'effort, courage, siblings',
              'home, mother, roots', 'children, romance, intellect',
              'adversity, health, service', 'partnership', 'transformation',
              'dharma, father, fortune', 'career, standing',
              'gains, networks', 'loss, foreign, moksha']


def dms(s, d, m, sec=0):
    return SIGNS.index(s) * 30 + d + m / 60 + sec / 3600


def fmt(l):
    return f"{int(l % 30):02d}°{round((l % 1) * 60):02d}′ {SIGNS[int(l // 30)]}"


def nak_of(l):
    i = int(l // (360 / 27))
    return NAK[i], int((l % (360 / 27)) // (360 / 108)) + 1, NAK_LORD[i]


D1 = {'Lagna': dms('Kanya', 27, 37, 37), 'Surya': dms('Mesha', 1, 28, 3),
      'Chandra': dms('Vrishabha', 1, 47, 15), 'Mangal': dms('Vrishabha', 7, 19, 32),
      'Budha': dms('Mesha', 10, 27, 50), 'Guru': dms('Mithuna', 14, 47, 52),
      'Shukra': dms('Mesha', 23, 36, 49), 'Shani': dms('Vrishabha', 17, 54, 25),
      'Rahu': dms('Vrishabha', 26, 55, 52), 'Ketu': dms('Vrischika', 26, 55, 52)}
GRAHAS = [g for g in D1 if g != 'Lagna']
LAG = int(D1['Lagna'] // 30)
sg = lambda g: int(D1[g] // 30)
h = lambda g: (sg(g) - LAG) % 12 + 1
RD = {g: LORD[sg(g)] for g in GRAHAS}            # rashi dispositor
ND = {g: nak_of(D1[g])[2] for g in GRAHAS}       # nakshatra dispositor
rule = lambda t: print('\n' + '=' * 92 + f'\n{t}\n' + '=' * 92)


def chain(start, table):
    seen, out = [], start
    while out not in seen:
        seen.append(out)
        out = table.get(out, out)
        if out == seen[-1]:
            return seen + [out + ' ⟲ (self)']
    return seen + [f'{out} ⟲']


# --- 1 ----------------------------------------------------------------------
rule('1. THE TWO DISPOSITORS OF EVERY GRAHA')
print(f'  {"graha":9}{"position":19}{"sign lord":11}{"nakshatra":15}'
      f'{"star lord":11} agree?')
for g in GRAHAS:
    n, p, nl = nak_of(D1[g])
    same = 'SAME' if RD[g] == nl else ''
    self_ = '  <== in its OWN nakshatra' if nl == g else ''
    print(f'  {g:9}{fmt(D1[g]):19}{RD[g]:11}{n + " p" + str(p):15}{nl:11} '
          f'{same}{self_}')

# --- 2 ----------------------------------------------------------------------
rule('2. THE RASHI CHAIN — where the FIELD authority ends')
for g in GRAHAS:
    if g in ('Rahu', 'Ketu'):
        continue
    print('  ' + ' → '.join(chain(g, RD)))
print('\n  Every rashi chain terminates in MANGAL ⇄ SHUKRA — the 8th lord and')
print('  the 9th lord in mutual exchange.  That is the chart\'s field-level')
print('  attractor: transformation answering to dharma and back.')

# --- 3 ----------------------------------------------------------------------
rule('3. THE NAKSHATRA CHAIN — where the DELIVERY authority ends')
for g in GRAHAS:
    print('  ' + ' → '.join(chain(g, ND)))
term = {}
for g in GRAHAS:
    c = chain(g, ND)
    last = c[-1].split(' ')[0]
    # Budha and Ketu are the two nodes of one 2-cycle; group them as one
    key = 'Budha ⇄ Ketu cycle' if last in ('Budha', 'Ketu') else f'{last} (self-loop)'
    term.setdefault(key, []).append(g)
print('\n  Termini:')
for t, who in sorted(term.items(), key=lambda x: -len(x[1])):
    print(f'    {t:22} {len(who)} of 9   ({", ".join(who)})')
print('\n  EIGHT of nine grahas terminate in the BUDHA ⇄ KETU exchange.')
print('  Budha stands in Ashwini (Ketu\'s star) and Ketu stands in Jyeshtha')
print('  (Budha\'s star): a true NAKSHATRA PARIVARTANA, the star-level twin of')
print('  the Mangal ⇄ Shukra exchange at sign level.')
print('\n  The ninth is SHUKRA, which stands in its own nakshatra Bharani and')
print('  therefore disposits itself -- a fixed point answering to nothing.')
print('  And Shukra is the ATMAKARAKA.  At the level the tradition says')
print('  actually delivers results, the soul-significator is sovereign.')

# --- 4 ----------------------------------------------------------------------
rule('4. THE HOUSE LORDS, ROUTED THROUGH THEIR NAKSHATRA LORDS')
print(f'  {"house":6}{"significations":28}{"sign lord":10}{"in":13}'
      f'{"star lord":11} = who actually pays')
routed = {}
for i in range(12):
    s = (LAG + i) % 12
    l = LORD[s]
    nl = ND[l]
    routed.setdefault(nl, []).append(i + 1)
    print(f'  {i + 1:<6}{HOUSE_NAME[i]:28}{l:10}{nak_of(D1[l])[0]:13}{nl:11}')

# --- 5 ----------------------------------------------------------------------
rule('5. THE DELIVERY MAP — five grahas pay out all twelve houses')
print(f'  {"deliverer":10}{"houses":14}{"Shodhya":>9}{"Kashta":>8}{"net":>9}   '
      f'what it means')
NOTE = {
    'Ketu': 'self and career handed to the graha of dissolution',
    'Surya': 'effort and transformation on the best net-balance channel',
    'Shukra': 'wealth and dharma paid by the self-disposited Atmakaraka',
    'Rahu': 'home and marriage carry the foreign, unconventional signature',
    'Chandra': 'children and health on the LOWEST delivery capacity in the chart',
}
for nl in sorted(routed, key=lambda x: -len(routed[x])):
    hs = ', '.join(str(x) for x in routed[nl])
    sp = SP.get(nl, 0); ka = KASHTA.get(nl, 0); ish = ISHTA.get(nl, 0)
    spf = f'{sp:>9}' if sp else f'{"—":>9}'
    kaf = f'{ka:>8.2f}' if ka else f'{"—":>8}'
    nef = f'{ish - ka:>+9.2f}' if sp else f'{"—":>9}'
    print(f'  {nl:10}{hs:14}{spf}{kaf}{nef}   {NOTE.get(nl, "")}')
print('\n  FOUR of the seven classical grahas rule houses but deliver NONE.')
missing = [g for g in SP if g not in routed]
print(f'  {", ".join(missing)} are conduits, not sources: they hold the')
print('  lordships and hand every one of them to somebody else.')

# --- 6 ----------------------------------------------------------------------
rule('6. THE REFINEMENT THIS FORCES ON THE 8TH-HOUSE READING')
m = LORD[(LAG + 7) % 12]
print(f'  The 8th is ruled by {m}: Shodhya Pinda {SP[m]} (rank 1), '
      f'Kashta {KASHTA[m]:.2f} (rank 2).')
print(f'  {m} stands in {nak_of(D1[m])[0]}, whose lord is {ND[m]}: '
      f'Kashta {KASHTA[ND[m]]:.2f}.')
print(f'  Only Chandra is cheaper ({KASHTA["Chandra"]:.2f}), and Chandra\'s')
print(f'  Shodhya Pinda is {SP["Chandra"]} -- it barely delivers anything.  Among')
print('  grahas with real delivery capacity, Surya is the cheapest there is,')
print('  and it holds the best net balance in the chart.')
print(f'\n  So the transformation house is OWNED by the second-most-expensive')
print('  graha and ROUTED THROUGH the least expensive one.  At the level that')
print('  determines outcomes, the 8th pays out through Surya.')
print('\n  And Surya rules the 12th.  The house of upheaval delivers through')
print('  the lord of the house of release -- which is the same conclusion the')
print('  cost analysis reached from correlations, arrived at here through')
print('  nakshatra lordship alone.  Two unrelated techniques, one answer:')
print('  WHAT HE LETS GO OF IS THE CHANNEL EVERYTHING ELSE ARRIVES THROUGH.')

# --- 7 ----------------------------------------------------------------------
rule('7. WHERE THE TWO LEVELS DISAGREE — and what that means')
for g in GRAHAS:
    if RD[g] != ND[g]:
        print(f'  {g:9} field = {RD[g]:9} but delivery = {ND[g]:9}'
              f'   (house {h(g)})')
print('\n  Not one graha in this chart has the same rashi and nakshatra lord.')
print('  Nine for nine.  Every single placement is worked in one graha\'s')
print('  field and paid out by a different graha entirely.')
print('\n  That is the technical root of the chart\'s most persistent complaint:')
print('  the visible situation and the actual result never have the same')
print('  owner.  He is always doing the work in one place and being paid')
print('  from another -- which is exactly what "visibility lags ability" is,')
print('  stated at the level of dispositorship rather than of Dig Bala.')

# ===========================================================================
# ADDED LATER: THE D1 CHAIN'S STRUCTURE, MEASURED RATHER THAN ASSERTED.
#
# The section above establishes that every graha in the rashi chart funnels
# into the Mangal-Shukra exchange.  It never asked HOW UNUSUAL THAT IS, and
# section 6 learned the hard way -- with the 9-of-9 nakshatra mismatch -- that
# a striking-looking structural fact can turn out to be the default condition.
#
# So the same null model section 46 uses is applied here.
# ===========================================================================
import random
from ephem_core import SIGNS as _S, SUPPLIED as _P, LORD as _L, sign_of as _sg

_G7 = ['Surya', 'Chandra', 'Mangal', 'Budha', 'Guru', 'Shukra', 'Shani']


def _analyse(pos):
    """pos: graha -> sign index.  Returns (set of attractor cycles, max depth)."""
    disp = {g: _L[pos[g]] for g in _G7}
    loops, depth = set(), 0
    for g in _G7:
        path, cur = [], g
        while cur not in path:
            path.append(cur)
            cur = disp[cur]
        loops.add(frozenset(path[path.index(cur):]))
        depth = max(depth, path.index(cur))
    return loops, depth


print('\n' + '=' * 74)
print('  THE D1 DISPOSITOR STRUCTURE, MEASURED')
print('=' * 74)
_pos = {g: _sg(_P[g]) for g in _G7}
_loops, _depth = _analyse(_pos)
_own = sum(1 for g in _G7 if _L[_pos[g]] == g)
print(f"""
  THIS CHART
      attractors            {len(_loops)}  -- {sorted(next(iter(_loops)))}
      its size              {len(next(iter(_loops)))}-cycle, i.e. a PARIVARTANA
      grahas in own sign    {_own}
      max depth to the loop {_depth}   (Guru -> Budha -> Mangal <-> Shukra)
""")
random.seed(20260812)
N = 200_000
one, own0, one2, dep = 0, 0, 0, {}
for _ in range(N):
    su = random.uniform(0, 360)
    p = {'Surya': su, 'Budha': (su + random.uniform(-28, 28)) % 360,
         'Shukra': (su + random.uniform(-47, 47)) % 360,
         'Chandra': random.uniform(0, 360), 'Mangal': random.uniform(0, 360),
         'Guru': random.uniform(0, 360), 'Shani': random.uniform(0, 360)}
    pp = {g: int(p[g] // 30) for g in _G7}
    l, d = _analyse(pp)
    dep[d] = dep.get(d, 0) + 1
    if len(l) == 1:
        one += 1
        if len(next(iter(l))) == 2:
            one2 += 1
    if not any(_L[pp[g]] == g for g in _G7):
        own0 += 1
print(f"""  OVER {N:,} RANDOM CHARTS, SAME NULL MODEL AS SECTION 46

      a SINGLE attractor                    {one/N*100:5.2f}%
      NO graha in its own sign              {own0/N*100:5.2f}%
      a single attractor that is a 2-CYCLE  {one2/N*100:5.2f}%
      max depth exactly {_depth}                   {dep[_depth]/N*100:5.2f}%   (the commonest depth)

  AND THE VERDICT IS THE SAME LESSON SECTION 6 ALREADY LEARNED ONCE.

  NOTHING ABOUT THIS CHAIN'S SHAPE IS RARE.  Half of all charts funnel into a
  single attractor.  A third have no graha in its own sign.  Even the sharpest
  version -- a lone attractor that is a mutual exchange -- is one chart in six,
  and the depth is the single commonest value.

  IF THE DISPOSITOR CHAIN WERE PRESENTED AS A SIGNATURE OF THIS NATIVITY, THAT
  WOULD BE THE SAME OVERSELL THE 9-OF-9 MISMATCH TURNED OUT TO BE.

  WHAT SURVIVES IS WHAT SECTION 6 ALREADY SAID, AND IT SURVIVES INTACT: the
  distinguishing fact is not THAT there is one attractor but WHICH GRAHAS IT
  RUNS THROUGH.
""")
_h = lambda g: [i + 1 for i in range(12) if _L[(_sg(_P['Lagna']) + i) % 12] == g]
print(f"""      Mangal rules houses {_h('Mangal')}
      Shukra rules houses {_h('Shukra')}
      and seven of nine grahas stand in the 8TH AND THE 9TH

  SO THE SOLE ATTRACTOR OF THE ENTIRE RASHI CHART IS THE 8TH LORD IN MUTUAL
  EXCHANGE WITH THE 9TH LORD -- and those are precisely the two houses holding
  the stellium.

  EVERY GRAHA HE OWNS ULTIMATELY ANSWERS TO THE PAIR THAT OWNS THE CROWD.  That
  is structural rather than statistical, it does not depend on being rare, and
  it is the technical statement of why the 8th/9th axis governs this reading
  from end to end.
""")
print('=' * 74)
