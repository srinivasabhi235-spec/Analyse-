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
    'Surya': 'effort and transformation on the chart\'s cheapest channel',
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
      f'Kashta {KASHTA[ND[m]]:.2f} -- the CHEAPEST in the chart.')
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
