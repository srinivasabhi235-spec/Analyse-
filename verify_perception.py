#!/usr/bin/env python3
"""
How others see him -- and why that produces envy rather than warmth.

Jyotisha separates what a person IS (the lagna) from what a person APPEARS TO
BE (the Arudha Lagna).  Envy is a reaction to the image, not to the substance,
so the apparatus for it is the arudha, the grahas that aspect it, the 6th house
of rivals, the 11th of the peer circle, and Drik Bala -- which measures exactly
how much benefic or malefic attention each graha receives.

All strength figures are the verified tables from verify_bala.py.
"""
SIGNS = ['Mesha', 'Vrishabha', 'Mithuna', 'Karka', 'Simha', 'Kanya',
         'Tula', 'Vrischika', 'Dhanu', 'Makara', 'Kumbha', 'Meena']
LORD = ['Mangal', 'Shukra', 'Budha', 'Chandra', 'Surya', 'Budha',
        'Shukra', 'Mangal', 'Guru', 'Shani', 'Shani', 'Guru']
BENEFIC = {'Guru', 'Shukra', 'Budha', 'Chandra'}
MALEFIC = {'Shani', 'Mangal', 'Surya', 'Rahu', 'Ketu'}
ASPECT = {'Mangal': [4, 7, 8], 'Guru': [5, 7, 9], 'Shani': [3, 7, 10],
          'Rahu': [5, 7, 9], 'Ketu': [5, 7, 9]}
DRIK = {'Surya': 1.67, 'Chandra': -0.04, 'Mangal': -0.73, 'Budha': 0.54,
        'Guru': -8.58, 'Shukra': 0.00, 'Shani': -2.99}
SAV = {'Mesha': 21, 'Vrishabha': 22, 'Mithuna': 29, 'Karka': 28, 'Simha': 24,
       'Kanya': 29, 'Tula': 24, 'Vrischika': 28, 'Dhanu': 29, 'Makara': 29,
       'Kumbha': 41, 'Meena': 33}
BHAVA_RANK = [5, 3, 8, 2, 6, 10, 4, 12, 7, 9, 11, 1]
UPAGRAHA = {'Mrityu': ('Mesha', 26.82), 'Yama Ghantaka': ('Mithuna', 12.70),
            'Gulika': ('Karka', 25.27), 'Mandi': ('Karka', 22.37),
            'Kala': ('Kanya', 10.15), 'Dhuma': ('Simha', 14.80),
            'Parivesha': ('Vrishabha', 15.20), 'Upaketu': ('Meena', 1.47),
            'Ardha Prahara': ('Vrishabha', 20.80),
            'Vyatipata': ('Vrischika', 15.20), 'Indra Chapa': ('Kumbha', 14.80)}


def dms(s, d, m, sec=0):
    return SIGNS.index(s) * 30 + d + m / 60 + sec / 3600


D1 = {'Lagna': dms('Kanya', 27, 37, 37), 'Surya': dms('Mesha', 1, 28, 3),
      'Chandra': dms('Vrishabha', 1, 47, 15), 'Mangal': dms('Vrishabha', 7, 19, 32),
      'Budha': dms('Mesha', 10, 27, 50), 'Guru': dms('Mithuna', 14, 47, 52),
      'Shukra': dms('Mesha', 23, 36, 49), 'Shani': dms('Vrishabha', 17, 54, 25),
      'Rahu': dms('Vrishabha', 26, 55, 52), 'Ketu': dms('Vrischika', 26, 55, 52)}
GRAHAS = [g for g in D1 if g != 'Lagna']
LAG = int(D1['Lagna'] // 30)
AL = 7                                   # Vrischika, from verify_concepts.py
sg = lambda g: int(D1[g] // 30)
h = lambda s: (s - LAG) % 12 + 1
occ = lambda s: [g for g in GRAHAS if sg(g) == s]
rule = lambda t: print('\n' + '=' * 92 + f'\n{t}\n' + '=' * 92)


def aspects_on(sign):
    out = []
    for g in GRAHAS:
        offs = ASPECT.get(g, [7])
        if any((sg(g) + o - 1) % 12 == sign for o in offs):
            out.append(g)
    return out


# --- 1 ----------------------------------------------------------------------
rule('1. THE IMAGE vs THE SUBSTANCE')
print(f'  Lagna        {SIGNS[LAG]:11} — analytical, corrective, service-framed')
print(f'  Arudha Lagna {SIGNS[AL]:11} — the sign the world actually sees')
print(f'  AL is the {h(AL)}rd house from the lagna, and it is NOT the lagna sign.')
print(f'\n  Occupant of the Arudha Lagna: {occ(AL) or "none"}')
on_al = aspects_on(AL)
ben = [g for g in on_al if g in BENEFIC]
mal = [g for g in on_al if g in MALEFIC]
print(f'  Aspects onto the Arudha Lagna: {", ".join(on_al)}')
print(f'    benefic: {", ".join(ben) or "NONE"}')
print(f'    malefic: {", ".join(mal) or "none"}')
print(f'  Upagrahas in the AL sign: '
      f'{[k for k, v in UPAGRAHA.items() if v[0] == SIGNS[AL]]}')
print('\n  THREE MALEFICS aspect the image against ONE benefic, KETU occupies')
print('  it, and the malefic upagraha VYATIPATA sits in the same sign.  The')
print('  lone softening influence is Chandra -- which is in Mrita avastha with')
print('  the lowest Shodhya Pinda in the chart, so it softens very little.')
print('\n  The picture the world gets: an intense, secretive sign, occupied by')
print('  the node of dissolution, lit almost entirely by hard planets.')
print('\n  Set that against a Kanya lagna whose actual business is diagnosis,')
print('  correction and service.  THE IMAGE IS HARDER AND STRANGER THAN THE')
print('  PERSON.  People do not react to who he is; they react to that.')

# --- 2 ----------------------------------------------------------------------
rule('2. THE ARUDHA-RELATIVE HOUSES — where rivalry to the image comes from')
for off, label in [(2, '2nd from AL — what the image sustains'),
                   (3, '3rd from AL — the image\'s own effort'),
                   (6, '6th from AL — RIVALS TO THE IMAGE'),
                   (11, '11th from AL — what the image gains'),
                   (12, '12th from AL — what the image loses')]:
    s = (AL + off - 1) % 12
    print(f'  {label:38} {SIGNS[s]:11} = natal house {h(s):<2} '
          f'{", ".join(occ(s)) or "empty"}')
print('\n  The 6th from the Arudha Lagna is MESHA -- his own 8th house, holding')
print('  Surya, Budha and Shukra.  Read plainly: THE RIVALS TO HIS IMAGE ARE')
print('  GENERATED BY HIS OWN DEPTH.  What he goes through is what makes')
print('  people compete with him.  He does not have to provoke anybody.')
print('\n  And the 11th from AL is KANYA -- the lagna itself.  What his image')
print('  gains from is his actual substance.  The image is fed by the real')
print('  thing, which is why the gap never closes by presentation alone.')

# --- 3 ----------------------------------------------------------------------
rule('3. RAHU ASPECTS THE LAGNA')
print(f'  Rahu sits in {SIGNS[sg("Rahu")]} (house {h(sg("Rahu"))}) and casts its')
print(f'  5th aspect onto {SIGNS[LAG]} — the ascendant itself.')
print('\n  Rahu on a lagna, by conjunction or aspect, inflates the APPARENT.')
print('  It makes a person look like they are getting more, faster, and from')
print('  somewhere unexplained.  Combined with a Ketu-occupied arudha, the')
print('  composite reads as: SEEMS TO BE RISING, WON\'T SAY HOW.')
print('\n  That specific combination — visible ascent plus withheld method —')
print('  is the most reliable envy generator in the classical vocabulary.')

# --- 4 ----------------------------------------------------------------------
rule('4. THE 6TH HOUSE — his capacity to defeat people')
s6 = (LAG + 5) % 12
print(f'  6th house {SIGNS[s6]}, lord {LORD[s6]} (the Amatyakaraka), '
      f'SAV {SAV[SIGNS[s6]]}')
print(f'  Rank by bindus: 1 of 12 — THE HIGHEST-SUPPORTED SIGN IN THE CHART')
print(f'  Bhava Bala rank {BHAVA_RANK[5]} of 12;  occupants: '
      f'{occ(s6) or "empty"};  aspects: {", ".join(aspects_on(s6))}')
print('\n  The 6th is the house of enemies, rivals and competition, and it is')
print('  the single best-supported house he owns — aspected by Guru AND by')
print('  its own lord Shani.  In gochara terms he wins contests; in social')
print('  terms, HE BEATS PEOPLE, and that is what manufactures rivals.')
print('\n  Note the asymmetry: the house of DEFEATING rivals is 41 bindus.')
print(f'  The house of ALLIES — the 11th — is {SAV["Karka"]} bindus and ranks')
print(f'  {BHAVA_RANK[10]} of 12 by Bhava Bala.  He is far better equipped to')
print('  overcome people than to be liked by them.')

# --- 5 ----------------------------------------------------------------------
rule('5. THE 11TH — the peer circle, and why it turns')
s11 = (LAG + 10) % 12
print(f'  11th house {SIGNS[s11]}, lord {LORD[s11]}, SAV {SAV[SIGNS[s11]]}, '
      f'Bhava rank {BHAVA_RANK[10]} of 12')
print(f'  Occupants: {occ(s11) or "empty"}')
print(f'  Upagrahas: {[k for k, v in UPAGRAHA.items() if v[0] == SIGNS[s11]]}')
print(f'  Delivered at nakshatra level by Chandra — Shodhya Pinda 33, the')
print('  lowest delivery capacity in the chart.')
print('\n  GULIKA AND MANDI, the two harshest shadow points, both sit in the')
print('  house of friends and peer groups — on the second-weakest bhava, paid')
print('  out by the weakest deliverer.  The peer circle is structurally')
print('  shadowed: it thins, it turns, and the concealed element in it is')
print('  what surfaces.  This is not bad luck with people; it is the')
print('  configuration of the house that holds them.')

# --- 6 ----------------------------------------------------------------------
rule('6. DRIK BALA — who is under attack')
print('  Drik Bala measures net aspectual pressure: positive means benefic')
print('  attention, negative means malefic.\n')
for g in sorted(DRIK, key=lambda x: DRIK[x]):
    bar = '-' * int(abs(min(DRIK[g], 0)) * 2) or '+' * int(max(DRIK[g], 0) * 2)
    flag = '  <== by far the worst in the chart' if DRIK[g] == min(DRIK.values()) else ''
    print(f'  {g:9} {DRIK[g]:+6.2f}  {bar}{flag}')
print('\n  GURU carries -8.58, nearly three times the next worst.  And Guru is:')
print('    - the ONLY graha in a kendra')
print('    - the giver of AMALA YOGA, the chart\'s reputation yoga')
print('    - the 4th and 7th lord, and the BADHAKESH')
print('    - carrying YAMA GHANTAKA 2 05 away')
print('\n  So the one graha responsible for his good name is also the most')
print('  aspectually besieged body in the chart.  HIS REPUTATION IS PERMANENTLY')
print('  UNDER PRESSURE — not because it is undeserved, but because the graha')
print('  that holds it is the one everything else is aimed at.')

# --- 7 ----------------------------------------------------------------------
rule('7. THE COMPOSITE — six mechanisms, none of them about arrogance')
for n, (title, why) in enumerate([
    ('He looks harder than he is',
     'Arudha Lagna in Vrischika with Ketu in it, zero benefic aspects and '
     'three malefic ones, against a Kanya lagna that is actually in the '
     'correction-and-service business.'),
    ('He appears to be rising without explanation',
     'Rahu aspects the ascendant from the 9th and inflates the apparent, '
     'while the Ketu-arudha withholds the method.  Visible ascent plus '
     'withheld method is the classical envy signature.'),
    ('He wins contests he did not pick',
     'The 6th, the house of rivals, is the chart\'s highest-bindu sign at 41 '
     'and is aspected by both Guru and its own lord.  Beating people reliably '
     'is what manufactures people who mind.'),
    ('He is visibly better than his output',
     'Both luminaries are exalted and both are crippled by avastha; the lagna '
     'and Surya are vargottama.  Others can sense substance that is not being '
     'cashed, and unspent potential reads as withholding rather than modesty.'),
    ('He does not defer',
     'Both personal points are Rakshasa gana.  Non-deference is experienced as '
     'arrogance by anyone who requires deference, regardless of how it is meant.'),
    ('His intelligence is not performed',
     'Budha is combust — absorbed into an exalted Sun rather than displayed. '
     'Ability that is simply present is far harder to compete with than '
     'ability that is shown off, because there is no performance to match.'),
], 1):
    print(f'  {n}. {title}')
    print(f'     {why}\n')

print('  What is NOT in the chart is equally worth saying: no yoga of')
print('  ostentation, no Panchamahapurusha, no exalted graha in a kendra, no')
print('  strong 11th, and an Amala yoga under the heaviest malefic pressure in')
print('  the chart.  He is not provoking this.  THE ENVY IS A RESPONSE TO A')
print('  GAP — between an image that reads formidable and unreadable, and a')
print('  person who is neither — and the gap is structural, so it does not')
print('  close by being nicer.')
