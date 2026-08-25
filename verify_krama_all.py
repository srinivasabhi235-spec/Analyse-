#!/usr/bin/env python3
"""
THE WHOLE READING REBUILT IN CLASSICAL ORDER — ALL TWELVE BHAVAS.

The instruction was to follow the Parashari bhava-judgment sequence and rewrite
the entire analysis by it:

    1  identify what the bhava represents
    2  judge the BHAVA -- sign, occupants, aspects
    3  judge the BHAVA LORD -- house, sign, dignity, conjunction, aspect,
       affliction, strength, favourable or unfavourable placement
    4  judge the natural KARAKA
    5  check the relevant VARGA
    6  planetary strength (Shadbala)
    7  bhava strength (Bhava Bala)
    8  benefic/malefic influence, affliction, yogas
    9  dasha -- WHEN, and only now
    10 Ashtakavarga and transit, last

This script produces the computed workup for every house in that order.  The
prose document is written from its output; nothing is asserted that does not
appear here.

ONE THING IS DONE DIFFERENTLY FROM THE EARLIER SECTIONS, DELIBERATELY.  The
verdict for each bhava is recorded at STEP 3 and then again at STEP 10, so the
document can state for every house whether the last seven steps changed the
judgment or merely qualified it.
"""
from ephem_core import (SIGNS, GRAHAS, SUPPLIED, LORD, varga, dignity,
                        sign_of, rule, sub)

POS = dict(SUPPLIED)
LAG = sign_of(POS['Lagna'])
G7 = [g for g in GRAHAS if g not in ('Rahu', 'Ketu')]
NAT_BEN = ('Guru', 'Shukra', 'Chandra')
NAT_MAL = ('Surya', 'Mangal', 'Shani', 'Rahu', 'Ketu')
hs = lambda g: (sign_of(POS[g]) - LAG) % 12 + 1
ordn = lambda n: f"{n}{'th' if 10 <= n % 100 <= 20 else {1:'st',2:'nd',3:'rd'}.get(n%10,'th')}"
ASPECTS = {'Surya': [7], 'Chandra': [7], 'Budha': [7], 'Shukra': [7],
           'Mangal': [4, 7, 8], 'Guru': [5, 7, 9], 'Shani': [3, 7, 10],
           'Rahu': [], 'Ketu': []}
RUPAS = {'Surya': 11.39, 'Chandra': 6.42, 'Mangal': 6.33, 'Budha': 6.46,
         'Guru': 8.21, 'Shukra': 6.68, 'Shani': 6.39}
MINREQ = {'Surya': 5.0, 'Chandra': 6.0, 'Mangal': 5.0, 'Budha': 7.0,
          'Guru': 6.5, 'Shukra': 5.5, 'Shani': 5.0}
SRANK = {'Surya': 1, 'Chandra': 6, 'Mangal': 3, 'Budha': 7,
         'Guru': 4, 'Shukra': 5, 'Shani': 2}
ISHTA = {'Surya': 46.88, 'Chandra': 24.54, 'Mangal': 19.66, 'Budha': 18.91,
         'Guru': 37.30, 'Shukra': 47.49, 'Shani': 12.48}
KASHTA = {'Surya': 7.83, 'Chandra': 4.49, 'Mangal': 38.87, 'Budha': 30.32,
          'Guru': 15.10, 'Shukra': 11.87, 'Shani': 46.83}
BRUP = [8.39, 9.18, 7.49, 9.28, 7.91, 7.21, 8.86, 7.00, 7.61, 7.39, 7.08, 12.59]
BRANK = [5, 3, 8, 2, 6, 10, 4, 12, 7, 9, 11, 1]
SAV = {'Mesha': 21, 'Vrishabha': 22, 'Mithuna': 29, 'Karka': 28, 'Simha': 24,
       'Kanya': 29, 'Tula': 24, 'Vrischika': 28, 'Dhanu': 29, 'Makara': 29,
       'Kumbha': 41, 'Meena': 33}
# Vimshottari periods that activate a graha (mahadasha / current-era antardasha)
DASHA = {'Surya': 'MD to Dec 2005 (lived); Rahu-Surya Jul 2037 - Jun 2038',
         'Chandra': 'MD 2005-2015 (lived); Rahu-Chandra Jun 2038 - Dec 2039',
         'Mangal': 'MD 2015-2022 (lived); Rahu-Mangal Dec 2039 - Dec 2040',
         'Rahu': 'MAHADASHA NOW, Dec 2022 - Dec 2040',
         'Guru': 'Rahu-Guru NOW to 31 Jan 2028; MD Dec 2040 - Dec 2056',
         'Shani': 'Rahu-Shani Jan 2028 - Dec 2030; MD Dec 2056 - Dec 2075',
         'Budha': 'Rahu-Budha Dec 2030 - Jun 2033; MD from Dec 2075',
         'Shukra': 'Rahu-Shukra Jul 2034 - Jul 2037',
         'Ketu': 'Rahu-Ketu Jun 2033 - Jul 2034'}

# subject, karakas, relevant varga -- varga assignment marked where it is
# standard and where this reading is choosing
BHAVA = {
    1:  ('body, self, constitution, the visible person',
         ['Surya'], (9, 'D9 — general strength of the self')),
    2:  ('wealth held, family, speech, food',
         ['Guru', 'Budha'], (2, 'D2 Hora — wealth. Standard')),
    3:  ('younger siblings, courage, effort, the hands',
         ['Mangal'], (3, 'D3 Drekkana — siblings. Standard')),
    4:  ('mother, home, land, vehicles, inner happiness',
         ['Chandra', 'Mangal'], (4, 'D4 Chaturthamsa — property. Standard')),
    5:  ('children, intelligence, purva punya, mantra',
         ['Guru'], (7, 'D7 Saptamsa — children. Standard')),
    6:  ('enemies, disease, debt, service, competition',
         ['Mangal', 'Shani'], (30, 'D30 Trimshamsa — misfortune. D6 is declined in this reading')),
    7:  ('spouse, partnership, the other',
         ['Shukra'], (9, 'D9 Navamsa — marriage. Standard')),
    8:  ('longevity, upheaval, the hidden, inheritance',
         ['Shani'], (30, 'D30 Trimshamsa. D8 is not among Parashara sixteen')),
    9:  ('fortune, father, dharma, the teacher',
         ['Surya', 'Guru'], (9, 'D9 — dharma; D12 for the father')),
    10: ('profession, authority, status, action in the world',
         ['Surya', 'Budha', 'Guru', 'Shani'], (10, 'D10 Dasamsa — career. Standard')),
    11: ('gains, income, elder siblings, networks',
         ['Guru'], (11, 'D11 — outside Parashara sixteen; reverse-engineered here')),
    12: ('loss, expenditure, foreign lands, the bed, moksha',
         ['Shani', 'Ketu'], (12, 'D12 — used here for the 12th by extension, not by rule')),
}
DUST, KEND, TRIK = (6, 8, 12), (1, 4, 7, 10), (1, 5, 9)


def aspects_onto(sign_idx):
    return [(g, a) for g in GRAHAS for a in ASPECTS[g]
            if (sign_of(POS[g]) + a - 1) % 12 == sign_idx]


def workup(h):
    s = (LAG + h - 1) % 12
    lord = LORD[s]
    occ = [g for g in GRAHAS if sign_of(POS[g]) == s]
    subject, karakas, (vn, vnote) = BHAVA[h]
    rule(f'BHAVA {h} — {SIGNS[s]}')

    sub('1  what the bhava represents')
    print(f"      {subject}")

    sub('2  the bhava itself')
    inc = aspects_onto(s)
    ben = [g for g, _ in inc if g in NAT_BEN] + [g for g in occ if g in NAT_BEN]
    mal = [g for g, _ in inc if g in NAT_MAL] + [g for g in occ if g in NAT_MAL]
    print(f"      sign          {SIGNS[s]}")
    print(f"      occupants     {', '.join(occ) or 'EMPTY'}")
    print(f"      aspects onto  {', '.join(f'{g}({ordn(a)})' for g, a in inc) or 'NONE'}")
    print(f"      benefic touch {', '.join(sorted(set(ben))) or 'none'}")
    print(f"      malefic touch {', '.join(sorted(set(mal))) or 'none'}")

    sub('3  the bhava lord')
    lh = hs(lord)
    ldig = dignity(lord, sign_of(POS[lord]))
    c = abs(POS[lord] - POS['Surya'])
    c = min(c, 360 - c)
    comb = 'COMBUST' if (lord != 'Surya' and c < 12) else '—'
    conj = [g for g in GRAHAS if g != lord and sign_of(POS[g]) == sign_of(POS[lord])]
    linc = aspects_onto(sign_of(POS[lord]))
    quality = ('DUSTHANA' if lh in DUST else
               'kendra' if lh in KEND else 'trikona' if lh in TRIK else 'neutral house')
    also = [i + 1 for i in range(12) if LORD[(LAG + i) % 12] == lord and i + 1 != h]
    print(f"      lord          {lord}")
    print(f"      placed in     the {ordn(lh)} — {SIGNS[sign_of(POS[lord])]} ({quality})")
    print(f"      dignity       {ldig}")
    print(f"      combustion    {c:.2f} deg from Surya   {comb}")
    print(f"      conjoined     {', '.join(conj) or 'none'}")
    print(f"      aspected by   {', '.join(f'{g}({a})' for g, a in linc) or 'NONE'}")
    print(f"      also rules    the {', '.join(ordn(x) for x in also) or '(nothing else)'}")

    sub('4  the natural karaka')
    for k in karakas:
        ph = (f" Ishta {ISHTA[k]:5.2f}  Kashta {KASHTA[k]:5.2f}" if k in ISHTA
              else "  (node — no Ishta/Kashta; Parashara gives phala to the seven)")
        print(f"      {k:8s} in the {ordn(hs(k)):5s} "
              f"{dignity(k, sign_of(POS[k])):12s}{ph}")

    sub(f'5  the relevant varga — {vnote}')
    vl = {g: varga(POS[g], vn) for g in list(GRAHAS) + ['Lagna']}
    vlag = vl['Lagna']
    vh = (vlag + h - 1) % 12
    vocc = [g for g in GRAHAS if vl[g] == vh]
    print(f"      varga lagna   {SIGNS[vlag]}")
    print(f"      its {ordn(h):5s}     {SIGNS[vh]} — occupants {', '.join(vocc) or 'empty'}")
    print(f"      lord {lord:8s} in {SIGNS[vl[lord]]:11s} "
          f"({ordn((vl[lord]-vlag) % 12 + 1)}), {dignity(lord, vl[lord])}")
    for k in karakas:
        print(f"      karaka {k:6s} in {SIGNS[vl[k]]:11s} "
              f"({ordn((vl[k]-vlag) % 12 + 1)}), {dignity(k, vl[k])}")

    sub('6  planetary strength')
    for g in dict.fromkeys([lord] + karakas):
        if g in RUPAS:
            r = RUPAS[g] / MINREQ[g]
            print(f"      {g:8s} {RUPAS[g]:5.2f} rupas / {MINREQ[g]:.2f} required"
                  f"  ratio {r:.2f}  rank {SRANK[g]}  "
                  f"{'FAILS' if r < 1 else 'passes'}")

    sub('7  bhava strength')
    print(f"      {BRUP[h-1]:.2f} rupas, rank {BRANK[h-1]} of 12")

    sub('8  benefic / malefic, affliction, yogas')
    flags = []
    if not inc and not occ:
        flags.append('bhava EMPTY and UNASPECTED — nothing reaches it at all')
    if not inc:
        flags.append('receives NO aspect from any graha')
    if comb == 'COMBUST':
        flags.append(f'lord COMBUST at {c:.2f} deg')
    if lh in DUST:
        flags.append(f'lord in a DUSTHANA (the {ordn(lh)})')
    if ldig in ('exalted', 'own'):
        flags.append(f'lord {ldig}')
    if ldig == 'debilitated':
        flags.append('lord DEBILITATED')
    if set(mal) and not set(ben):
        flags.append('malefic influence only')
    if set(ben) and not set(mal):
        flags.append('benefic influence only')
    for f in flags or ['nothing structural to flag']:
        print(f"      {f}")

    sub('9  dasha — when')
    for g in dict.fromkeys([lord] + karakas):
        print(f"      {g:8s} {DASHA[g]}")

    sub('10  ashtakavarga, last')
    print(f"      SAV of {SIGNS[s]:11s} {SAV[SIGNS[s]]:3d}")
    print(f"      SAV of the lord's sign ({SIGNS[sign_of(POS[lord])]}) {SAV[SIGNS[sign_of(POS[lord])]]}")
    print()


for h in range(1, 13):
    workup(h)

# =============================================================================
rule('THE CROSS-BHAVA PICTURE — what only appears when all twelve are done')
empty = [h for h in range(1, 13)
         if not [g for g in GRAHAS if sign_of(POS[g]) == (LAG + h - 1) % 12]]
unasp = [h for h in range(1, 13) if not aspects_onto((LAG + h - 1) % 12)]
dead = [h for h in empty if h in unasp]
lords_in = {}
for h in range(1, 13):
    lords_in.setdefault(hs(LORD[(LAG + h - 1) % 12]), []).append(h)
print(f"""
      houses with no occupant          {empty}
      houses receiving no aspect       {unasp}
      houses BOTH empty and unaspected {dead}

  EIGHT BHAVAS HAVE NO OCCUPANT.  SIX RECEIVE NO ASPECT.  THREE HAVE NEITHER --
  the 1st, the 5th and the 7th are untouched by any graha in either way.

  SO FOR EIGHT OF TWELVE HOUSES, STEP 2 RETURNS ALMOST NOTHING and the judgment
  falls entirely to step 3.  For three of them it returns literally nothing.

  THAT IS THE STRUCTURAL FACT THE HOUSE-BY-HOUSE PASS EXPOSES AND THE EARLIER
  SECTIONS NEVER STATED IN THESE TERMS.  The classical sequence puts the bhava
  before its lord for a reason -- but in a chart this concentrated, the bhava
  is usually SILENT, and the lord does the speaking.

  AND NOTE WHICH THREE ARE WHOLLY UNTOUCHED: the SELF, the CHILDREN, and the
  SPOUSE.  The three most personal houses in the chart are the three no graha
  occupies or aspects.
""")
print("      where each bhava's lord sits:")
for hh in sorted(lords_in):
    print(f"        the {ordn(hh):5s} holds the lords of houses {lords_in[hh]}")
print(f"""
  THE LORDS OF ALL TWELVE HOUSES SIT IN {len(lords_in)} HOUSES.

  Every bhava in this chart is administered from the 8th, the 9th or the 10th.
  Whatever the subject -- mother, children, spouse, wealth, enemies, loss --
  the graha responsible for it is standing in one of three adjacent houses,
  two of which are the stellium and one of which is sealed.
""")
print('=' * 92)
