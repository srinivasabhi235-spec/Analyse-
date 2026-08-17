#!/usr/bin/env python3
"""
The questions nobody asked.

Every reading is shaped by what it was asked.  This chart was interrogated
hard on marriage, career, transformation, the spouse, the in-laws, envy,
love and rarity -- and never once on the father, the mother, the siblings,
speech, property, the enemies house, foreign residence, spiritual practice,
remedy, or what the chart hides from the man himself.

Silence in the questioning is not silence in the chart.  This computes the
areas that were never put as questions, using the same apparatus as the rest
of the suite, so that Part III of the reading rests on measurement rather
than on the observation that nobody asked.

Nothing here is speculative extension: every figure is derived from the
verified D1 longitudes, the supplied strength tables, or the varga engine
already used by build_charts.py.
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
EXALT = {'Surya': 0, 'Chandra': 1, 'Mangal': 9, 'Budha': 5,
         'Guru': 3, 'Shukra': 11, 'Shani': 6}
SP = {'Mangal': 212, 'Shani': 184, 'Budha': 152, 'Surya': 138,
      'Shukra': 95, 'Guru': 81, 'Chandra': 33}
KASHTA = {'Shani': 46.83, 'Mangal': 38.87, 'Budha': 30.32, 'Guru': 15.10,
          'Shukra': 11.87, 'Surya': 7.83, 'Chandra': 4.49}
ISHTA = {'Shukra': 47.49, 'Surya': 46.88, 'Guru': 37.30, 'Chandra': 24.54,
         'Mangal': 19.66, 'Budha': 18.91, 'Shani': 12.48}
SAV = {'Mesha': 21, 'Vrishabha': 22, 'Mithuna': 29, 'Karka': 28,
       'Simha': 24, 'Kanya': 29, 'Tula': 24, 'Vrischika': 28,
       'Dhanu': 29, 'Makara': 29, 'Kumbha': 41, 'Meena': 33}
# Bhava Bala rank, houses 1..12
BRANK = [5, 3, 8, 2, 6, 10, 4, 12, 7, 9, 11, 1]
UPAGRAHA = {'Yama Ghantaka': ('Mithuna', 12, 42), 'Mrityu': ('Mesha', 26, 49),
            'Parivesha': ('Vrishabha', 15, 12), 'Ardha Prahara': ('Vrishabha', 20, 48),
            'Gulika': ('Karka', 25, 16), 'Mandi': ('Karka', 22, 22),
            'Kala': ('Kanya', 10, 9), 'Dhuma': ('Simha', 14, 48),
            'Vyatipata': ('Vrischika', 15, 12), 'Indra Chapa': ('Kumbha', 14, 48),
            'Upaketu': ('Meena', 1, 28)}


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
hs = lambda g: (sg(g) - LAG) % 12 + 1
house_sign = lambda n: SIGNS[(LAG + n - 1) % 12]
occupants = lambda n: [g for g in GRAHAS if hs(g) == n]
rule = lambda t: print('\n' + '=' * 92 + f'\n  {t}\n' + '=' * 92)
sub = lambda t: print(f'\n  --- {t} ' + '-' * max(0, 82 - len(t)))

ASPECT = {'Mangal': [4, 7, 8], 'Guru': [5, 7, 9], 'Shani': [3, 7, 10],
          'Rahu': [5, 7, 9], 'Ketu': [5, 7, 9]}


def aspects_house(n):
    """Which grahas cast a drishti onto house n."""
    out = []
    for g in GRAHAS:
        for a in ASPECT.get(g, [7]):
            if (hs(g) + a - 1 - 1) % 12 + 1 == n:
                out.append(g)
                break
    return out


def upagrahas_in(n):
    return [u for u, (s, d, m) in UPAGRAHA.items()
            if (SIGNS.index(s) - LAG) % 12 + 1 == n]


# ---------------------------------------------------------------- varga engine
def v(l, n):
    """Same engine as build_charts.py -- classical Parashari varga rules."""
    s, deg = int(l // 30), l % 30
    part = int(deg / (30.0 / n))
    if n == 1:
        return s
    if n == 2:
        return 4 if (s % 2 == 0) == (deg < 15) else 3
    if n == 3:
        return (s + part * 4) % 12
    if n == 4:
        return (s + part * 3) % 12
    if n == 7:
        return ((s if s % 2 == 0 else s + 6) + part) % 12
    if n == 9:
        return int(l / (30.0 / 9)) % 12
    if n == 10:
        return ((s if s % 2 == 0 else s + 8) + part) % 12
    if n == 12:
        return (s + part) % 12
    if n == 16:
        return ({0: 0, 1: 4, 2: 8}[s % 3] + part) % 12
    if n == 20:
        return ({0: 0, 1: 8, 2: 4}[s % 3] + part) % 12
    if n == 24:
        return ((4 if s % 2 == 0 else 3) + part) % 12
    if n == 27:
        return int(l / (30.0 / 27)) % 12
    if n == 30:
        lim = ([(5, 0), (10, 10), (18, 8), (25, 2), (30, 6)] if s % 2 == 0
               else [(5, 1), (12, 5), (20, 11), (25, 9), (30, 7)])
        for hi, sign in lim:
            if deg < hi:
                return sign
        return lim[-1][1]
    if n == 40:
        return ((0 if s % 2 == 0 else 6) + part) % 12
    if n == 45:
        return ({0: 0, 1: 4, 2: 8}[s % 3] + part) % 12
    if n == 60:
        return (s + int(deg * 2)) % 12
    raise ValueError(n)


def varga(n):
    return {g: v(D1[g], n) for g in D1}


def vh(chart, g):
    """House of g in a varga chart, from that chart's own lagna."""
    return (chart[g] - chart['Lagna']) % 12 + 1


def dignity(g, s):
    if g in ('Rahu', 'Ketu'):
        return ''
    if EXALT.get(g) == s:
        return 'EXALTED'
    if EXALT.get(g) == (s + 6) % 12:
        return 'debilitated'
    if LORD[s] == g:
        return 'own sign'
    return ''


def house_dossier(n, label):
    """The standard block: sign, lord, occupants, aspects, strength, delivery."""
    sign = house_sign(n)
    lord = LORD[SIGNS.index(sign)]
    lord_h = hs(lord)
    lnak = nak_of(D1[lord])
    occ = occupants(n)
    asp = aspects_house(n)
    ups = upagrahas_in(n)
    print(f'\n  {label}  --  house {n}, {sign}')
    print(f'    lord {lord}, standing in house {lord_h} ({SIGNS[sg(lord)]}), '
          f'{lnak[0]} p{lnak[1]}')
    print(f'    DELIVERED BY {lnak[2]}'
          + (f'   (Shodhya Pinda {SP[lnak[2]]}, Kashta {KASHTA[lnak[2]]})'
             if lnak[2] in SP else '   (a shadow -- no strength figures)'))
    print(f'    occupants : {", ".join(occ) if occ else "empty"}')
    print(f'    aspects   : {", ".join(asp) if asp else "NONE"}')
    print(f'    upagrahas : {", ".join(ups) if ups else "none"}')
    print(f'    SAV {SAV[sign]:2d} of 337   |   Bhava Bala rank {BRANK[n-1]:2d} of 12')
    return dict(sign=sign, lord=lord, deliverer=lnak[2], occ=occ,
                asp=asp, sav=SAV[sign], rank=BRANK[n - 1])


# =============================================================================
rule('THE QUESTIONS NEVER PUT TO THIS CHART')
print("""
  Asked, across the whole reading:  transformation and its timing, the solar
  eclipse, his own traits, the wife's traits, the mechanism of the 8th, the
  purpose of the transformations, the in-laws' wealth, career growth, whether
  he "gets all but with pain", the dispositor chains, whether life is "good
  but with friction", why people envy him, who loves him and when, marital
  satisfaction in both directions, the remaining vargas and gaps, the overall
  trajectory, and what is uncommon.

  NEVER asked, and each one is loud in this chart:
     1. the father          -- and the chart's rarest knot sits on him
     2. the mother          -- and she is better placed than anyone assumes
     3. the siblings        -- Ketu in the 3rd of BOTH D1 and D3
     4. speech              -- the 2nd house, with Rakshasa gana behind it
     5. enemies, debt, disease -- the 6th, the chart's HIGHEST bindu house
     6. property and vehicles  -- D4 and D16, never once computed for him
     7. foreign residence   -- everywhere in the reading, never a question
     8. spiritual practice  -- D20, led by the chart's strongest graha
     9. the 12th house      -- the STRONGEST bhava, and it was never read
    10. what he cannot see  -- the blind spots the chart itself creates
    11. remedy (upaya)      -- the one thing every classical reading ends on
    12. longevity           -- declined, and the reason must be stated
""")

# =============================================================================
rule('1.  THE FATHER')
f9 = house_dossier(9, 'The 9th -- father, dharma, fortune')
print()
print(f'    Surya (karaka of the father) : {fmt(D1["Surya"])}, house {hs("Surya")}')
print(f'    Pitrikaraka (Jaimini)        : Mangal, {fmt(D1["Mangal"])}, house {hs("Mangal")}')
sn = nak_of(D1['Surya'])
print(f'    Surya nakshatra              : {sn[0]} p{sn[1]}, lord {sn[2]}')
print(f'    Surya dignity                : EXALTED, vargottama, GANDANTA')
gand = D1['Surya'] % 30
print(f'    gandanta depth               : {gand:.2f}° into Mesha, at the Meena/Mesha junction')
for name, lim in [('full pada (3°20′) -- the standard definition', 10 / 3),
                  ('half pada (1°40′) -- the stricter reading', 5 / 3),
                  ('abhukta (0°48′) -- the severest sub-zone', 0.8)]:
    print(f'      {name:52s} {"INSIDE" if gand < lim else "outside"}')

d12 = varga(12)
print('\n    D12 (Dwadamsha -- the parents varga), lagna '
      f'{SIGNS[d12["Lagna"]]}:')
for g in ['Surya', 'Chandra', 'Mangal', 'Budha']:
    print(f'      {g:8s} {SIGNS[d12[g]]:11s} house {vh(d12, g):2d}  {dignity(g, d12[g])}')

d45 = varga(45)
print(f'\n    D45 (Akshavedamsha -- paternal legacy), lagna {SIGNS[d45["Lagna"]]}:')
for g in GRAHAS:
    dg = dignity(g, d45[g])
    if dg:
        print(f'      {g:8s} {SIGNS[d45[g]]:11s} house {vh(d45, g):2d}  {dg}')

print(f"""
  READING.  The father is the single best-supported relationship in this
  chart and the single most knotted.  Surya is exalted, vargottama, exalted
  again in D12 -- and sits in GANDANTA in the 8th house, delivered by Ketu.
  The 9th itself is rank {f9['rank']} of 12 with only {f9['sav']} bindus and four grahas
  crowded into it, one of them Rahu in Marana Karaka Sthana.

  So: a father who is genuinely strong, genuinely dignified, and whose
  significator is tied in the tightest karmic knot the chart contains.  The
  relationship is not weak.  It is UNFINISHED -- which is a different thing,
  and it is why authority in general is this chart's lifelong subject.
""")

# =============================================================================
rule('2.  THE MOTHER')
f4 = house_dossier(4, 'The 4th -- mother, home, roots, formal education')
print()
print(f'    Chandra (karaka of the mother) : {fmt(D1["Chandra"])}, house {hs("Chandra")}, EXALTED')
print('    Matrikaraka (Jaimini)          : Budha, house 8')
print(f'    Chandra avastha                : Mrita (dead) -- exalted and Mrita at once')
print(f'    Chandra Shodhya Pinda          : {SP["Chandra"]} -- the lowest in the chart')
print(f'    Chandra Kashta                 : {KASHTA["Chandra"]} -- the LOWEST cost in the chart')
print(f'\n    D12 Chandra: {SIGNS[d12["Chandra"]]}, house {vh(d12,"Chandra")}, {dignity("Chandra", d12["Chandra"])}')
d40 = varga(40)
print(f'    D40 (Khavedamsha -- maternal legacy), lagna {SIGNS[d40["Lagna"]]}:')
for g in GRAHAS:
    dg = dignity(g, d40[g])
    if dg:
        print(f'      {g:8s} {SIGNS[d40[g]]:11s} house {vh(d40, g):2d}  {dg}')

print(f"""
  READING.  The 4th is the SECOND-STRONGEST bhava in the chart (rank 2 of 12),
  aspected by Guru, its lord Guru forming Amala Yoga -- and it is empty, which
  in Parashari terms means undisturbed.  Chandra is exalted.  Both parents are
  exalted in D12.

  The mother is the most reliably benign figure in the entire chart, and she
  is the ONLY one whose house outranks everything except the 12th.  The one
  caution is not about her: Chandra's delivery capacity is 33, the lowest in
  the chart, so what she gives is unstinted and thin -- excellent in quality,
  limited in quantity.  Also note Chandra has the lowest Kashta of any graha:
  whatever comes through the mother costs him almost nothing.
""")

# =============================================================================
rule('3.  THE SIBLINGS')
f3 = house_dossier(3, 'The 3rd -- siblings, courage, self-effort, skill')
print()
print('    Bhratrikaraka (Jaimini) : Guru, house 10, enemy sign, worst Drik Bala (-8.58)')
kn = nak_of(D1['Ketu'])
print(f'    Ketu occupies it        : {fmt(D1["Ketu"])}, {kn[0]} p{kn[1]} -- '
      'the SEVEREST gandanta pada in the zodiac')
d3 = varga(3)
print(f'\n    D3 (Drekkana -- the siblings varga), lagna {SIGNS[d3["Lagna"]]}:')
for g in GRAHAS:
    print(f'      {g:8s} {SIGNS[d3[g]]:11s} house {vh(d3, g):2d}  {dignity(g, d3[g])}')
print(f'\n    Ketu is in house {vh(d3,"Ketu")} of D3 and house {hs("Ketu")} of D1 '
      '-- THE SAME HOUSE IN BOTH.')

print(f"""
  READING.  Ketu sits in the 3rd of D1 and the 3rd of D3, in the severest
  gandanta pada there is.  FOUR grahas aspect the house -- Chandra, Mangal,
  Shani and Rahu -- making it the most heavily-contacted house in the chart,
  and the Bhratrikaraka is the most aspectually besieged graha in it.

  Two conclusions, and they pull opposite ways:
    - SIBLINGS: separation, distance, or an absence where one is expected.
      Ketu in the 3rd in both charts is the classical signature of a sibling
      bond that does not function as company.  Not necessarily loss -- more
      often distance, or a sibling who is present and unavailable.
    - SELF-EFFORT: this is the chart's real working house.  Occupied by Ketu
      and aspected by four grahas, it is where effort converts fastest.
      The chart pays for SKILL and OUTPUT more reliably than for anything else
      it offers.
  The same placement produces both.  He does the work of the 3rd alone --
  which is exactly the condition under which the 3rd pays best.
""")

# =============================================================================
rule('4.  SPEECH -- the 2nd house')
f2 = house_dossier(2, 'The 2nd -- speech, family, accumulated wealth, the face')
print()
print('    2nd lord Shukra  : house 8, own nakshatra Bharani p4, Atmakaraka,')
print(f'                       highest Ishta Phala in the chart ({ISHTA["Shukra"]})')
print('    Speech karaka    : Budha -- COMBUST, below its Shadbala minimum,')
print('                       Dig Bala 4.28 of 60 (lowest in the chart)')
print('    Aspects on the 2nd: ' + ', '.join(aspects_house(2)))
print('    Gana of both personal points: Rakshasa (self-authorising, non-deferring)')

print("""
  READING.  Nobody asked how this man speaks, and the chart has an unusually
  specific answer.  The 2nd is rank 3 of 12 -- well built -- and receives
  aspects from Guru and from the entire 8th-house stellium (Surya, Budha,
  Shukra).  Its lord is the Atmakaraka with the chart's highest Ishta Phala.

  But the karaka of speech is combust and directionally the weakest graha in
  the chart, and both personal points are Rakshasa gana.

  The composite is exact: WHAT he says is unusually well-made -- precise,
  weighty, worth hearing, and the 8th-house aspect gives it depth other people
  do not have.  HOW it lands is the problem.  Combust Budha means it is not
  performed; Rakshasa gana means it does not defer; and Guru's aspect makes it
  sound more authoritative than he intends.  He is heard as blunter and more
  certain than he feels.  This is the same visibility-lags-ability finding,
  arriving through the mouth instead of the career.
""")

# =============================================================================
rule('5.  ENEMIES, DEBT AND DISEASE -- the 6th, the chart\'s strongest by bindus')
f6 = house_dossier(6, 'The 6th -- adversaries, litigation, debt, disease, service')
print()
print(f'    {f6["sign"]} carries {f6["sav"]} bindus -- the HIGHEST of the twelve signs')
print(f'    Bhava Bala rank {f6["rank"]} of 12 -- structurally light')
print(f'    Lord Shani: Shodhya Pinda {SP["Shani"]} (rank 2), Kashta {KASHTA["Shani"]} (worst)')
print('    Aspected by BOTH Guru and its own lord Shani')
print(f'    Delivered by {f6["deliverer"]} (Shodhya Pinda {SP[f6["deliverer"]]} -- lowest)')

print("""
  READING.  This is the loudest un-asked area in the chart.  41 bindus is the
  highest count of any sign, and it sits on the house of enemies, debt,
  disease and service -- aspected by Jupiter (protection) and by its own lord.

  What that combination actually means, stated carefully:
    - LITIGATION AND CONFLICT: he wins.  A 41-bindu 6th aspected by Guru is
      about as strong a "defeats adversaries" configuration as the technique
      produces.  He should not fear a fight he did not start.
    - DEBT: the same house governs it, and the same strength applies -- debt
      is survivable and clearable here.  But the 11th (gains) ranks 11 of 12
      with both harsh upagrahas, so BORROWING TO GAIN is the one financial
      move the chart argues against, twice over.
    - DISEASE: the 6th is strong, which classically favours recovery, and Guru
      aspects it.  Against that, the 6th DELIVERS through Chandra at Shodhya
      Pinda 33 -- the same thin channel as the 5th.  Illness here is
      low-grade and chronic in character rather than acute, and recovery is
      reliable but slow.
    - SERVICE: the 6th is also the house of service, and Kanya rises.  The
      strongest house in his chart by bindus is a service house.  That is not
      incidental to a life the D60 terminates in the 12th.
""")

# =============================================================================
rule('6.  PROPERTY, LAND AND VEHICLES')
d4 = varga(4)
d16 = varga(16)
print(f'\n    D4 (Chaturthamsha -- fixed assets), lagna {SIGNS[d4["Lagna"]]}:')
for g in GRAHAS:
    print(f'      {g:8s} {SIGNS[d4[g]]:11s} house {vh(d4, g):2d}  {dignity(g, d4[g])}')
print(f'\n    D16 (Shodashamsha -- vehicles, comforts, happiness), lagna {SIGNS[d16["Lagna"]]}:')
for g in GRAHAS:
    print(f'      {g:8s} {SIGNS[d16[g]]:11s} house {vh(d16, g):2d}  {dignity(g, d16[g])}')
ex16 = [g for g in GRAHAS if dignity(g, d16[g]) == 'EXALTED']
print(f'\n    D16 exaltations: {", ".join(ex16)}  ({len(ex16)} -- the highest of any varga)')
print(f'    D16 lagna is {SIGNS[d16["Lagna"]]} -- Kumbha again, the chart\'s recurring sign')
print(f'    4th house: rank {BRANK[3]} of 12, SAV {SAV[house_sign(4)]}, lord Guru forming Amala')

print("""
  READING.  Never asked, and the answer is better than the D1 suggests.  The
  4th is rank 2 of 12.  D16 -- comforts and vehicles -- carries THREE
  exaltations, the highest count of any of the sixteen vargas, on a Kumbha
  lagna.  D4 is ordinary rather than emphasised.

  So: material comfort and domestic quality are considerably better supported
  than this chart's austere reputation implies, and they arrive through the
  4th (home, mother, roots) rather than through the 2nd (accumulation) or the
  11th (gains).  Property is owned rather than accumulated -- one good home
  rather than a portfolio -- and the D16 evidence says it is comfortable.
  The austerity in this chart is in its EARNING, not in its LIVING.
""")

# =============================================================================
rule('7.  FOREIGN RESIDENCE -- assumed everywhere, asked nowhere')
f12 = house_dossier(12, 'The 12th -- loss, foreign lands, seclusion, moksha')
d24 = varga(24)
d60 = varga(60)
print()
print(f'    12th is Bhava Bala rank {BRANK[11]} of 12 -- THE STRONGEST BHAVA, and empty')
print(f'    12th lord Surya: exalted, vargottama, best net balance (+39.05), in the 8th')
print(f'    D24 12th holds: {[g for g in GRAHAS if vh(d24,g)==12]} -- foreign study')
print(f'    D60 Shukra: {SIGNS[d60["Shukra"]]}, house {vh(d60,"Shukra")}, {dignity("Shukra", d60["Shukra"])}')
print('    Rahu (foreign karaka) in the 9th; badhakesh Guru for a dual lagna')
print('    Jaimini: 10th from Karakamsa AND Rajya Pada both = Simha = the natal 12th')

print("""
  READING.  Six independent techniques point at foreign residence and NOT ONE
  of them was ever put as a question.  Collected:
    1. the 12th is the strongest bhava in the chart
    2. its lord is the best-dignified graha in the chart, exalted and vargottama
    3. Budha and Rahu occupy the 12th of D24 -- foreign education
    4. D60, the karmic arbiter, places its ONLY exaltation in its 12th
    5. both Jaimini authority indicators fall on the natal 12th
    6. the mahadasha lord Rahu -- the foreign significator -- sits in the 9th

  The 12th being EMPTY is the key nuance.  An empty house of this strength
  operates as a DESTINATION rather than as daily experience.  He does not live
  a 12th-house life early.  He arrives at one.  On the timeline that reads as
  foreign settlement becoming fact rather than intention across 2034-2038, and
  as the terminal condition of the whole arc.
""")

# =============================================================================
rule('8.  SPIRITUAL PRACTICE -- the D20, never computed for him')
d20 = varga(20)
print(f'\n    D20 (Vimshamsha -- upasana, devotion, practice), lagna {SIGNS[d20["Lagna"]]}:')
for g in GRAHAS:
    print(f'      {g:8s} {SIGNS[d20[g]]:11s} house {vh(d20, g):2d}  {dignity(g, d20[g])}')
print(f'\n    Moksha trikona (4, 8, 12) occupancy: '
      f'{[g for g in GRAHAS if hs(g) in (4,8,12)]}')
print('    Nakshatra dispositor chain terminates on: Ketu (moksha karaka)')
print('    Yogi planet: Ketu.   Karakamsa: Vrischika.   5th from Karakamsa: Mangal + Ketu')

print("""
  READING.  Surya -- the strongest graha in the chart -- is EXALTED in D20.
  The spiritual-practice varga is led by the best material the chart owns.

  What kind of practice, specifically, since the chart is unusually explicit:
    - Ketu terminates the nakshatra chain and is the Yogi planet, so the mode
      is INVESTIGATIVE and dissolving rather than devotional.
    - Mangal with Ketu in the 5th from Karakamsa is mantra-siddhi -- practice
      that is EARNED BY REPETITION AND EFFORT, not received by grace.
    - Surya exalted in D20 makes the object of practice solar: light,
      authority, the self, the father -- not a goddess-form, not bhakti.
    - Karakamsa Vrischika makes it private and hidden.  He will not join
      anything, and will not discuss it.
  A solitary, technical, repetition-based practice with a solar object,
  pursued privately.  That is about as specific as this apparatus gets.
""")

# =============================================================================
rule('9.  WHAT HE CANNOT SEE -- the blind spots the chart itself manufactures')
print("""
  Each of these is a place where the chart's own structure prevents accurate
  self-assessment.  They are derived, not invented -- each names its source.

  1.  HE UNDERRATES HIMSELF, STRUCTURALLY.
      Both luminaries exalted and both crippled by avastha (1 in 3,571).
      The material is first-rate and the deployment is not, so his own
      self-estimate tracks the OUTPUT rather than the EQUIPMENT.  He will
      correct for this too late, if at all.

  2.  HE READS OTHERS' REACTIONS AS BEING ABOUT HIM.
      Arudha Lagna in Vrischika with Ketu in it, lit by three malefics.  The
      image is harder than the person.  What comes back at him is a response
      to the arudha, and he has no instrument for seeing that.

  3.  HE WILL MISREAD HIS MARRIAGE.
      Ketu on the 7th from three directions guarantees a felt gap regardless
      of the partner.  The chart says explicitly that his dissatisfaction is
      not evidence about her -- and nothing in his equipment will make that
      obvious from the inside.

  4.  HE WILL TRY TO SOLVE POSITIONAL PROBLEMS WITH EFFORT.
      Budha's Dig Bala is 4.28 of 60 while its Chesta Bala is 42.15, second
      highest.  The deficit is WHERE HE STANDS.  A man built to work harder
      will reliably apply the wrong instrument.

  5.  HE WILL EXPECT THE PEER GROUP TO SUPPLY VALIDATION.
      The 11th is rank 11 of 12 with Gulika and Mandi in it, delivered by the
      chart's thinnest graha.  Four relational houses are strong; the one he
      is likeliest to test himself against is the one that fails.

  6.  HE WILL MISTAKE ABSENT HELP FOR ACTIVE HARM.
      Not one classical affliction is present -- no Kemadruma, no Kalasarpa,
      no debilitated lagna lord, nothing in the 6th or 12th.  What this chart
      has is MISSING SCAFFOLDING, and the two require opposite responses.
      Enduring a difficulty that is actually an absence wastes the decade.
""")

# =============================================================================
rule('10.  REMEDY -- derived from the chart rather than prescribed generically')
print("""
  Classical readings end on upaya.  This one never did, because it was never
  asked.  Deriving it from the chart's own measurements rather than from a
  standard table:

  STRENGTHEN WHAT IS WEAK AND LOAD-BEARING, not what is weak and peripheral.
    - BUDHA is the only graha below its Shadbala minimum and it rules the
      1st AND the 10th.  It is the single highest-value target in the chart.
      And its failure is POSITIONAL (Dig Bala 4.28), which means the remedy
      is literal: change where he stands.  Rooms, cities, institutions,
      visibility.  This is the rare case where the astrological remedy and
      the practical one are the same instruction.
    - CHANDRA delivers the 5th and 6th on a Shodhya Pinda of 33.  Children
      and health run on the chart's thinnest channel.  Rest, routine and
      regularity are not wellness advice here; they are the specific repair
      for the specific weakness.

  LEAN ON WHAT IS STRONG AND CHEAP.
    - SURYA: best net balance (+39.05), lowest cost among effective grahas,
      exalted in ten of sixteen vargas.  Anything solar -- father, authority,
      early rising, the 12th house, the disciplines of self-command -- pays
      disproportionately and charges almost nothing.
    - The 3rd HOUSE: occupied by Ketu and aspected by four grahas -- the
      most-contacted house in the chart.  Effort into SKILL pays
      faster than effort into position.

  DO NOT SPEND ON WHAT IS ALREADY WORKING.
    - The 4th and 12th are ranks 2 and 1 and both empty.  Home and release
      need no propitiation.
    - The 6th at 41 bindus does not need protecting from enemies.

  THE TWO GANDANTA KNOTS name their own deities, and this is the one place
  the tradition is specific:
    - Surya in Ashwini p1: the ASHWINI KUMARAS, the divine physicians;
      shakti = the power to heal quickly.  The knot is authority and the
      father.
    - Ketu in Jyeshtha p4: INDRA; shakti = arohana, the power to rise.  The
      knot is release.
  Both knots resolve through the same posture -- accepting authority he did
  not choose, and relinquishing what he did.
""")

# =============================================================================
rule('11.  LONGEVITY -- declined, and why that is the honest answer')
d27 = varga(27)
print(f'\n    D27 (Bhamsha -- vitality), lagna {SIGNS[d27["Lagna"]]}')
dush = [g for g in GRAHAS if vh(d27, g) in (6, 8, 12)]
print(f'    D27 dusthana occupancy (6th, 8th, 12th): '
      f'{dush if dush else "NONE -- zero"}')
print(f'    D1 8th house occupants: {occupants(8)}')
print(f'    D27 8th house occupants: {[g for g in GRAHAS if vh(d27,g)==8] or "empty"}')

print("""
  READING.  Ayurdaya is not computed here, and the reason is not squeamishness:
    - the birth time is known only to about ten minutes
    - the three classical methods (Pindayu, Nisargayu, Amsayu) disagree by
      decades on charts far better specified than this one
    - a number would be believed far more than it deserves

  What CAN be said is structural and is genuinely reassuring: the vitality
  varga carries ZERO dusthana occupancy, and its 8th house is empty while the
  D1 8th holds three grahas.  The chart's hardest house fires in five of six
  divisional levels and NOT in the one that measures whether the body can take
  it.  That is the strongest available statement that the transformations are
  severe and survivable, and it is offered instead of a number rather than
  alongside one.
""")

# =============================================================================
rule('SUMMARY -- what the un-asked questions change')
print("""
  Nothing in this section overturns the reading.  Every un-asked area resolves
  into the same structure the asked questions found.  But four of them add
  material the reading did not previously carry:

  1. THE 6TH AT 41 BINDUS IS THE CHART'S STRONGEST HOUSE BY THAT MEASURE, and
     it was only ever read as a career input.  Read directly, it says: he wins
     fights, clears debts, and recovers from illness -- slowly.

  2. THE 4TH AND D16 SAY HIS LIVING IS COMFORTABLE even though his earning is
     austere.  The reading had been uniformly severe about material life; that
     was an overcorrection.

  3. THE MOTHER IS THE MOST BENIGN FIGURE IN THE CHART and had never been read
     on her own -- rank 2 house, exalted karaka, lowest-cost graha.

  4. THE BLIND SPOTS ARE DERIVABLE.  Six of them, each traceable to a specific
     measurement.  That is the most practically useful thing in this file, and
     it exists only because nobody asked for it.
""")
print('=' * 92)
