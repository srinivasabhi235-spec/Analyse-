#!/usr/bin/env python3
"""
Purpose: what the chart says the transformations are FOR.

Jyotisha has a specific apparatus for this question and it is not vague.
The purushartha trikonas sort every graha into dharma, artha, kama or moksha.
The Atmakaraka and its Karakamsa are Jaimini's explicit soul-agenda technique.
The moksha trikona, the gandanta knots, and the nakshatra deities of the
personal points complete it.  This computes all of them.

Nothing here is added interpretation dressed as arithmetic -- every tally is
a straight count from the verified natal longitudes.
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
DEITY = {1: ('Ashwini Kumaras', 'shidhra-vyapani — the power to heal quickly'),
         2: ('YAMA — Dharmaraja, god of death and of dharmic judgment',
             'apabharani — the power to carry away'),
         3: ('Agni', 'dahana — the power to burn away'),
         6: ('Rudra', 'yatna — the power of effort'),
         14: ('Tvashtar / Vishwakarma, the divine artisan',
              'punya-chayani — the power to accumulate merit'),
         18: ('Indra', 'arohana — the power to rise')}
LORD = ['Mangal', 'Shukra', 'Budha', 'Chandra', 'Surya', 'Budha',
        'Shukra', 'Mangal', 'Guru', 'Shani', 'Shani', 'Guru']
TRIKONA = {'Dharma (meaning)': [1, 5, 9], 'Artha (resources)': [2, 6, 10],
           'Kama (desire)': [3, 7, 11], 'Moksha (release)': [4, 8, 12]}


def dms(s, d, m, sec=0):
    return SIGNS.index(s) * 30 + d + m / 60 + sec / 3600


def fmt(l):
    return f"{int(l % 30):02d}°{round((l % 1) * 60):02d}′ {SIGNS[int(l // 30)]}"


def nak_of(l):
    i = int(l // (360 / 27))
    return i + 1, NAK[i], int((l % (360 / 27)) // (360 / 108)) + 1, NAK_LORD[i]


def navamsha(l):
    sign, rem = int(l // 30), l % 30
    return ({0: sign, 1: (sign + 8) % 12, 2: (sign + 4) % 12}[sign % 3]
            + int(rem // (30 / 9))) % 12


D1 = {'Lagna': dms('Kanya', 27, 37, 37), 'Surya': dms('Mesha', 1, 28, 3),
      'Chandra': dms('Vrishabha', 1, 47, 15), 'Mangal': dms('Vrishabha', 7, 19, 32),
      'Budha': dms('Mesha', 10, 27, 50), 'Guru': dms('Mithuna', 14, 47, 52),
      'Shukra': dms('Mesha', 23, 36, 49), 'Shani': dms('Vrishabha', 17, 54, 25),
      'Rahu': dms('Vrishabha', 26, 55, 52), 'Ketu': dms('Vrischika', 26, 55, 52)}
GRAHAS = [g for g in D1 if g != 'Lagna']
LAG = int(D1['Lagna'] // 30)
h = lambda g: (int(D1[g] // 30) - LAG) % 12 + 1
D9 = {k: navamsha(v) for k, v in D1.items()}

rule = lambda t: print('\n' + '=' * 88 + f'\n{t}\n' + '=' * 88)

# --- 1 ---------------------------------------------------------------------
rule('1. THE PURUSHARTHA TRIKONAS — what this chart is actually built for')
tally = {}
for name, hs in TRIKONA.items():
    who = [g for g in GRAHAS if h(g) in hs]
    tally[name] = who
    bar = '#' * len(who)
    print(f'  {name:20} houses {str(hs):12} {len(who)}  {bar:9} '
          f'{", ".join(who) or "—"}')
print(f'\n  Lagna itself falls in {[k for k, v in TRIKONA.items() if 1 in v][0]}.')
d, m = len(tally['Dharma (meaning)']), len(tally['Moksha (release)'])
a, k = len(tally['Artha (resources)']), len(tally['Kama (desire)'])
print(f'\n  Dharma + Moksha = {d + m} of 9 grahas.   Artha + Kama = {a + k}.')
print('  And the single graha in the kama trikona is KETU -- the one body in')
print('  the zodiac whose entire function is to remove attachment to whatever')
print('  it touches.  Desire is represented in this chart by its own negation.')
print('\n  This is not a chart built for acquisition or enjoyment.  Structurally')
print('  it is built for meaning and for release, and the arithmetic is not')
print('  close: seven of nine grahas sit in the dharma and moksha trikonas.')

# --- 2 ---------------------------------------------------------------------
rule('2. THE MOKSHA TRIKONA — and why the 8th is inside it')
for hs in [4, 8, 12]:
    s = (LAG + hs - 1) % 12
    who = [g for g in GRAHAS if h(g) == hs]
    print(f'  house {hs:<2} {SIGNS[s]:11} lord {LORD[s]:8} '
          f'occupants: {", ".join(who) or "empty"}')
print('\n  All three moksha-house occupants are in the 8TH.  The house that the')
print('  reading has spent six sections calling the transformation engine is a')
print('  MOKSHA house -- one of the three doors of release.  The transformation')
print('  apparatus and the liberation apparatus are the same apparatus.')
print('\n  And the 12th lord Surya sits in the 8th, forming VIMALA YOGA.  The')
print('  lord of loss placed in the house of transformation: the technical')
print('  statement that loss is converted into release rather than wasted.')

# --- 3 ---------------------------------------------------------------------
rule('3. THE ATMAKARAKA — Jaimini\'s explicit soul-agenda technique')
ak = max((g for g in GRAHAS if g not in ('Rahu', 'Ketu')), key=lambda g: D1[g] % 30)
n, nm, p, nl = nak_of(D1[ak])
print(f'  Atmakaraka = {ak} at {fmt(D1[ak])}, house {h(ak)}')
print(f'  Nakshatra  {nm} pada {p}, lord {nl}')
if n in DEITY:
    print(f'  Deity      {DEITY[n][0]}')
    print(f'  Shakti     {DEITY[n][1]}')
print(f'  Karakamsa  {SIGNS[D9[ak]]} (the AK\'s navamsha sign)')
print('\n  Four independent mortality markers land on the soul-significator:')
print('    1. it sits in the 8TH HOUSE, the house of death and transformation')
print('    2. its nakshatra is BHARANI, whose deity is YAMA')
print('    3. it sits inside the 22nd (KHARA) DREKKANA')
print('    4. the MRITYU upagraha is 3°13′ away')
print('\n  In Jaimini the Atmakaraka\'s placement IS the soul\'s curriculum.')
print('  This one is enrolled in mortality and dharmic accounting -- and Yama')
print('  is not only the god of death.  He is DHARMARAJA: the one who weighs')
print('  what is owed.  The curriculum is judgment, not punishment.')

# --- 4 ---------------------------------------------------------------------
rule('4. THE KARAKAMSA — what the soul is equipped to do about it')
ka = D9[ak]
for off, label in [(4, '4th from KA — the seat of teaching'),
                   (5, '5th from KA — mantra, applied esoteric skill'),
                   (9, '9th from KA — transmission, the guru function'),
                   (12, '12th from KA — the moksha indicator')]:
    s = (ka + off - 1) % 12
    who = [g for g in GRAHAS if D9[g] == s]
    print(f'  {label:44} {SIGNS[s]:11} {", ".join(who) or "empty"}')
print('\n  Ketu with Mangal in the 5th from Karakamsa is the classical')
print('  mantra-siddhi placement: applied esoteric capacity, earned by effort.')
print('  Budha in the 9th from Karakamsa makes him a transmitter of what he')
print('  learns.  Guru in the 4th gives the teaching seat.  The soul is not')
print('  merely being processed -- it is being equipped to hand something on.')

# --- 5 ---------------------------------------------------------------------
rule('5. THE GANDANTA KNOTS — the technical marker of unfinished karma')
for g in GRAHAS:
    d = D1[g] % 30
    s = int(D1[g] // 30)
    water_end = s in (3, 7, 11) and d >= 26 + 40 / 60
    fire_start = s in (0, 4, 8) and d <= 3 + 20 / 60
    if water_end or fire_start:
        n, nm, p, nl = nak_of(D1[g])
        print(f'  {g:8} {fmt(D1[g]):18} {nm} pada {p}   GANDANTA')
        if n in DEITY:
            print(f'  {"":8} deity {DEITY[n][0]}, {DEITY[n][1]}')
print('\n  Two gandanta placements, and note WHICH two: SURYA, which signifies')
print('  the self, the father and one\'s own right to authority -- and KETU,')
print('  the karaka of moksha itself.  Gandanta marks a knot carried in rather')
print('  than made here.  The two knots in this chart are authority and release.')
print('  That is as precise a statement of the karmic brief as the system gives.')

# --- 6 ---------------------------------------------------------------------
rule('6. KETU IS CROWNED — the moksha karaka runs the chart')
for line in [
    'terminus of the nakshatra dispositor chain (nothing escapes the Ketu-Budha loop)',
    'the YOGI planet, by the Yogi-point computation',
    'the ONLY KP route by which houses 1 and 10 -- self and career -- deliver',
    'occupant of the ARUDHA LAGNA, so the public image is Ketu-coloured',
    'in the 3rd house of self-effort, in the severest gandanta pada',
    'in the 5th from Karakamsa, the mantra-siddhi placement',
    'aspecting the 7th, and occupying the 7th in four separate vargas',
]:
    print(f'  - {line}')
print('\n  In a chart this heavily Ketu-crowned, the transformations are not')
print('  incidental hardship.  Ketu\'s single function is to detach a person')
print('  from what they are holding, and it has been given every lever in the')
print('  chart with which to do it.')

# --- 7 ---------------------------------------------------------------------
rule('7. WHAT THE FRAMEWORK DOES AND DOES NOT CLAIM')
print('  Jyotisha describes a structure and a schedule.  It does not demonstrate')
print('  that suffering is deserved, that it is optimal, or that any of this is')
print('  true outside the framework.  What the computation above legitimately')
print('  supports is narrower and still substantial:')
print('    - the chart is weighted to dharma and moksha, not artha and kama')
print('    - its transformation house IS a moksha house')
print('    - the 12th lord in the 8th (Vimala) converts loss rather than wasting it')
print('    - the Atmakaraka is enrolled in mortality and judgment')
print('    - the Karakamsa equips him to transmit what he learns')
print('    - and Ketu, whose whole job is detachment, has been handed the chart')
print('\n  Read on its own terms, this is a chart in which the transformations')
print('  ARE the purpose rather than obstacles to it.  That is a claim about')
print('  structure, and it is the only kind of claim the technique can make.')
