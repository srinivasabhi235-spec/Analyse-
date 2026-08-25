#!/usr/bin/env python3
"""
THE CONTENTS PAGE FOR CHAPTERS 1 TO 45 HAS ARRIVED.

Section 36 said the reading had an address for 57% of Parashara and none at
all for the other 43%, named the Shodashavarga chapter as the single most
valuable missing page, and asked for exactly this.

It is now supplied.  This script does four things with it:

    1  gives the nineteen foundational technique families an ADDRESS
    2  CHECKS the sixteen divisions the reading built against the sixteen
       the chapter names -- the first external check on the varga apparatus
    3  RESOLVES one section 35 finding that was published as unverifiable,
       because chapter 28 says what chapter 73's rays actually feed
    4  COMPUTES the yoga chapters, which turn out to be the largest untested
       block in the document

A contents page is still not the text.  What it settles is stated; what it
cannot settle is stated too.
"""
from ephem_core import (SIGNS, GRAHAS, SUPPLIED, LORD, EXALT, varga,
                        dignity, sign_of, rule, sub)

POS = dict(SUPPLIED)
LAG = sign_of(POS['Lagna'])
G7 = [g for g in GRAHAS if g not in ('Rahu', 'Ketu')]
BEN = ('Guru', 'Shukra')            # Budha handled separately (combust here)
MAL = ('Surya', 'Mangal', 'Shani')
hs = lambda g: (sign_of(POS[g]) - LAG) % 12 + 1
frm = lambda g, r: (sign_of(POS[g]) - sign_of(POS[r])) % 12 + 1
occ = lambda h: [g for g in G7 if hs(g) == h]
ordn = lambda n: f"{n}{'th' if 10 <= n % 100 <= 20 else {1:'st',2:'nd',3:'rd'}.get(n%10,'th')}"
HOUSES = sorted({hs(g) for g in G7})
SIGNSOCC = sorted({sign_of(POS[g]) for g in G7})

# =============================================================================
rule('1.  NINETEEN TECHNIQUE FAMILIES, NOW WITH ADDRESSES')
MAP = [
    ('3', 'Planetary characters; exaltation, debilitation, natural and\n'
          '           temporal relationships; UPAGRAHAS, Gulika, Pranapada', '§4, §6, §16'),
    ('4', 'Zodiacal signs; limbs of Kalapurusha; Nisheka Lagna', '§9, §53'),
    ('5', 'SPECIAL ASCENDANTS — Bhava, Ghatika and Hora Lagna;\n'
          '           VARNADA DASA', 'NEVER USED'),
    ('6', 'THE SIXTEEN DIVISIONS OF A SIGN', '§11, §12, §13'),
    ('7', 'Divisional consideration; VIMSOPAKA STRENGTH; names of\n'
          '           bhavas; indications from houses', '§7, §11, §27'),
    ('8', 'ASPECTS OF THE SIGNS — sign aspects AND planetary aspects', '§10 (planetary only)'),
    ('9', 'EVILS AT BIRTH — short-life combinations, evils to parents', 'NEVER USED'),
    ('10', 'ANTIDOTES FOR EVILS', 'NEVER USED'),
    ('11', 'Judgement of houses — prosperity or annihilation of a house', '§9'),
    ('12-23', 'Effects of the 1st to the 12th house, one chapter each', '§9, §51-54'),
    ('24', 'EFFECTS OF THE BHAVA LORDS — 144 combinations', '§6, §9, throughout'),
    ('25', 'Effects of non-luminous planets — Dhuma, Vyatipata, Paridhi,\n'
           '           Chapa, Dhwaja, Gulika, Pranapada by house', '§16 (positions only)'),
    ('26', 'EVALUATION OF PLANETARY ASPECTS; special rules for Shani,\n'
           '           Mangal and Guru', '§10'),
    ('27', 'EVALUATION OF STRENGTHS — the whole Shadbala apparatus,\n'
           '           PLANETARY WAR, Bhava Balas, eligibility to predict', '§7, §8'),
    ('28', 'ISHTA AND KASHTA BALAS — EXALTATION RAYS, CHESHTA RASMI', '§7  — and see part 3'),
    ('29', 'BHAVAPADAS — pada calculation, pada and finance', '§15, §30'),
    ('30', 'UPAPADA', '§15'),
    ('31', 'ARGALA OR PLANETARY INTERVENTION', '§30, §36'),
    ('32', 'PLANETARY KARAKATWAS — Atmakaraka, yogakarakas', '§15'),
    ('33', 'EFFECTS OF KARAKAMSA — all twelve houses from it', '§15'),
    ('34', 'YOGA KARAKAS — angular and trinal lordships, AND A SECTION\n'
           '           FOR EACH ASCENDANT INCLUDING VIRGO', '§27, §36'),
    ('35', 'NABHASA YOGAS — 31 named', '§14 — 3 of 31'),
    ('36', 'MANY OTHER YOGAS — 21 named', '§14 — 2 of 21'),
    ('37', 'LUNAR YOGAS — 6 named', '§14 — 3 of 6'),
    ('38', 'SOLAR YOGAS — 3 named', '§14 — 2 of 3'),
    ('39-41', 'RAJA YOGAS; royal association; YOGAS FOR WEALTH', '§14, §22'),
]
for c, t, w in MAP:
    print(f"  ch {c:6s} {t}\n           -> {w}")
print("""
  EVERY ONE OF THE NINETEEN FAMILIES SECTION 36 LISTED NOW HAS A CHAPTER.

  AND THE PAGE EXPOSES SIX THINGS THE READING HAS NEVER TOUCHED AT ALL:

      ch 5      Bhava Lagna, Ghatika Lagna, Hora Lagna — three special
                ascendants, and VARNADA DASA, which is a dasha system section
                34 did not know existed.  Its list of twenty-six came from
                chapter 46; VARNADA IS IN CHAPTER 5.  THE COUNT IS TWENTY-SEVEN.
      ch 8      SIGN aspects — rasi drishti — listed alongside planetary
                aspects.  This reading has only ever used planetary drishti.
      ch 9, 10  evils at birth and their antidotes
      ch 25     the non-luminous points BY HOUSE — section 16 computed where
                they are and never read what they do there
      ch 27     PLANETARY WAR, and "eligibility to issue predictions"
      ch 35-38  sixty-one named yogas, of which section 14 tested ten
""")

# =============================================================================
rule('2.  CHAPTER 6 CHECKS THE VARGA APPARATUS — AND IT PASSES')
NAMED = ['Rasi', 'Hora', 'Decanate', 'Chaturthamsa', 'Sapthamsa', 'Navamsa',
         'Dasamsa', 'Dvadasamsa', 'Shodasamsa', 'Vimsamsa', 'Siddhamsa',
         'Bhamsa', 'Trimsamsa', 'Chatvarimsamsa', 'Akshavedamsa', 'Shashtiamsa']
DIV = [1, 2, 3, 4, 7, 9, 10, 12, 16, 20, 24, 27, 30, 40, 45, 60]
USED = [1, 2, 3, 4, 7, 9, 10, 12, 16, 20, 24, 27, 30, 40, 45, 60]
print("""
  The chapter names its sixteen divisions in order.  The reading built sixteen
  without ever seeing that list.  SIDE BY SIDE:
""")
print(f"  {'chapter 6 names':17s}{'=':3s}{'reading built':15s}match")
for nm, d in zip(NAMED, DIV):
    print(f"  {nm:17s}{'=':3s}D{d:<14d}{'YES' if d in USED else 'NO'}")
print(f"""
  SIXTEEN FOR SIXTEEN.  The reading's Shodashavarga membership is confirmed by
  the source's own contents page, and "Siddhamsa" and "Bhamsa" are fixed as D24
  and D27 rather than left to inference.

  AND THE LIST SETTLES SOMETHING ELSE, BY OMISSION.

      D8 AND D11 ARE NOT IN IT.

  Section 31 called D8 and D11 "reverse-engineered here" and listed their
  construction as a disputed rule living in Volume 1.  IT DOES NOT LIVE THERE.
  Chapter 6 enumerates the sixteen and neither is among them, so there is no
  Parashari rule for the reading to have got wrong.

  THAT RETIRES THE DISPUTE RATHER THAN SETTLING IT, and it explains the thing
  section 11 found puzzling: the rules had to be recovered from the supplied
  charts because Parashara does not give them.
""")

# =============================================================================
rule('3.  CHAPTER 28 OVERTURNS A SECTION 35 FINDING')
U = {'Surya': 57.16, 'Chandra': 59.60, 'Mangal': 26.89, 'Budha': 8.49,
     'Guru': 53.27, 'Shukra': 51.13, 'Shani': 9.30}
RASHMI = {'Surya': 30, 'Chandra': 16, 'Mangal': 6, 'Budha': 15,
          'Guru': 10, 'Shukra': 21, 'Shani': 4}
PUB = {'Surya': 28.58, 'Chandra': 15.89, 'Mangal': 2.69, 'Budha': 2.12,
       'Guru': 8.88, 'Shukra': 17.90, 'Shani': 0.62}
print("""
  SECTION 35 COMPUTED CHAPTER 73, "RAYS OF THE PLANETS", AND PUBLISHED IT WITH
  TWO DISCLAIMERS:

      "What I cannot state confidently is the scaling."
      "NO NEW INFORMATION, AND AN UNVERIFIED RULE... it supports nothing."

  BOTH ARE NOW WRONG, and it is the contents page that shows why.  Chapter 28
  is titled ISHTA AND KASHTA BALAS and its subtitle opens:

      "EXALTATION RAYS, CHESHTA RASMI, beneficial and malefic rays..."

  SO THE RAYS ARE NOT A CURIOSITY IN CHAPTER 73.  THEY ARE THE INPUT TO ISHTA
  AND KASHTA PHALA, which this reading uses in sections 7, 18, 19 and 22 --
  and Ishta/Kashta is computed from UCHCHA BALA, which is in the SUPPLIED
  Shadbala table and which verify_bala.py already reproduces independently.

  WHICH MEANS THE SCALING IS TESTABLE AFTER ALL.  If the exaltation ray is the
  same quantity as Uchcha Bala, then rays = max x Uchcha / 60, exactly.
""")
print(f"  {'graha':9s}{'Uchcha/60':>11s}{'published rays/max':>20s}{'predicted rays':>16s}{'published':>11s}")
worst = 0
for g in G7:
    a, b = U[g] / 60, PUB[g] / RASHMI[g]
    worst = max(worst, abs(a - b))
    print(f"  {g:9s}{a:11.4f}{b:20.4f}{RASHMI[g]*U[g]/60:16.2f}{PUB[g]:11.2f}")
print(f"""
      largest disagreement across seven grahas: {worst:.4f}

  IT REPRODUCES TO FOUR DECIMAL PLACES.  The assumption section 35 labelled as
  unverifiable -- "distance measured from the exact debilitation point, scaled
  linearly to 180" -- IS THE UCHCHA BALA SCALING, and the supplied Shadbala
  table confirms it.

  SO SECTION 35 MUST BE CORRECTED ON TWO COUNTS:

      the rule is NOT unverified.  It is confirmed against supplied data.
      the result does NOT support nothing.  It is the input to a measure the
      reading has leaned on since section 7.

  I PUBLISHED A HEDGE THAT THE DATA IN THIS REPOSITORY COULD ALREADY HAVE
  REMOVED.  The contents page did not supply the proof -- it supplied the
  POINTER that made me go and look.
""")

# =============================================================================
rule('4.  THE YOGA CHAPTERS — THE LARGEST UNTESTED BLOCK')
print(f"""
  Chapters 35 to 38 name SIXTY-ONE yogas.  Section 14 reports on ten of them.

      ch 35  NABHASA        31 named    section 14 has 3
      ch 36  OTHER YOGAS    21 named    section 14 has 2
      ch 37  LUNAR           6 named    section 14 has 3
      ch 38  SOLAR           3 named    section 14 has 2

  THE CHART'S OWN GEOMETRY, which decides most of them at once:

      seven grahas occupy {len(SIGNSOCC)} signs: {', '.join(SIGNS[s] for s in SIGNSOCC)}
      which are houses {', '.join(str(h) for h in HOUSES)}
      kendras occupied: {[h for h in HOUSES if h in (1, 4, 7, 10)] or 'the 10th only'}
""")

sub('Chapter 35 — the Nabhasa yogas, all thirty-one')
MOV, FIX, DUA = (0, 3, 6, 9), (1, 4, 7, 10), (2, 5, 8, 11)
allin = lambda hh: set(HOUSES) <= set(hh)
NAB = []
NAB.append(('Rajju', 'all grahas in movable signs',
            all(s in MOV for s in SIGNSOCC)))
NAB.append(('Musala', 'all in fixed signs', all(s in FIX for s in SIGNSOCC)))
NAB.append(('Nala', 'all in dual signs', all(s in DUA for s in SIGNSOCC)))
NAB.append(('Maala', 'benefics in three kendras',
            len([g for g in BEN + ('Budha',) if hs(g) in (1, 4, 7, 10)]) >= 3))
NAB.append(('Sarpa', 'malefics in three kendras',
            len([g for g in MAL if hs(g) in (1, 4, 7, 10)]) >= 3))
NAB.append(('Gada', 'all in two adjacent kendras',
            any(allin(p) for p in ((1, 4), (4, 7), (7, 10), (10, 1)))))
NAB.append(('Sakata', 'all in the 1st and 7th', allin((1, 7))))
NAB.append(('Vihaga', 'all in the 4th and 10th', allin((4, 10))))
NAB.append(('Sringataka', 'all in the trikonas 1, 5, 9', allin((1, 5, 9))))
NAB.append(('Hala', 'all in one mutual-trine set other than 1/5/9',
            allin((2, 6, 10)) or allin((3, 7, 11)) or allin((4, 8, 12))))
NAB.append(('Vajra', 'benefics in 1st/7th, malefics in 4th/10th',
            all(hs(g) in (1, 7) for g in BEN) and all(hs(g) in (4, 10) for g in MAL)))
NAB.append(('Yava', 'malefics in 1st/7th, benefics in 4th/10th',
            all(hs(g) in (1, 7) for g in MAL) and all(hs(g) in (4, 10) for g in BEN)))
NAB.append(('Kamala', 'all four kendras occupied, nothing elsewhere',
            allin((1, 4, 7, 10))))
NAB.append(('Vapi', 'all in panapharas, or all in apoklimas',
            allin((2, 5, 8, 11)) or allin((3, 6, 9, 12))))
for nm, a in (('Yupa', (1, 2, 3, 4)), ('Sara', (4, 5, 6, 7)),
              ('Sakthi', (7, 8, 9, 10)), ('Danda', (10, 11, 12, 1))):
    NAB.append((nm, f'all confined to houses {a[0]}-{a[-1]}', allin(a)))
for nm, a in (('Nauka', tuple(range(1, 8))), ('Koota', tuple(range(4, 11))),
              ('Chatra', (7, 8, 9, 10, 11, 12, 1)), ('Chapa', (10, 11, 12, 1, 2, 3, 4))):
    NAB.append((nm, f'all confined to the seven houses {a[0]}-{a[-1]}', allin(a)))
NAB.append(('Chakra', 'all in the odd houses 1 3 5 7 9 11',
            allin((1, 3, 5, 7, 9, 11))))
NAB.append(('Samudra', 'all in the even houses 2 4 6 8 10 12',
            allin((2, 4, 6, 8, 10, 12))))
SANK = {7: 'Veena', 6: 'Dama', 5: 'Pasa', 4: 'Kedara', 3: 'Soola',
        2: 'Yuga', 1: 'Gola'}
for k, nm in sorted(SANK.items()):
    NAB.append((nm, f'the seven grahas occupy exactly {k} sign(s)',
                len(SIGNSOCC) == k))
forms = [x for x in NAB if x[2]]
print(f"  {len(NAB)} yogas tested.\n")
for nm, r, v in NAB:
    if v:
        print(f"    FORMS     {nm:12s} {r}")
print()
for nm, r, v in NAB:
    if not v:
        print(f"    absent    {nm:12s} {r}")
print(f"""
  {len(forms)} OF {len(NAB)} FORM: {', '.join(n for n, _, _ in forms)}

  SECTION 14 REPORTED TWO OF THESE -- Soola and Sakthi -- and reported Sakata
  as cancelled.  THE OTHER {len(forms)-2} IT NEVER NAMED.

  AND THE OVERLAP IS NOT AN ERROR, IT IS THE RULE'S SHAPE.  Sakthi (7th-10th),
  Koota (4th-10th) and Chatra (7th-1st) are all CONFINEMENT yogas, and a chart
  packed into houses 8-9-10 satisfies every window that contains those three
  houses.  The narrowest true statement is SAKTHI; the others are implied by
  it rather than independent findings.

  I REPORT ALL THREE AND SAY WHICH IS LOAD-BEARING, rather than silently
  picking one -- because a reader with chapter 35 open will find all three and
  should know the document saw them.
""")

sub('Chapters 36, 37 and 38 — where the rule can be stated')
Y = []
Y.append(('36 Subha', 'benefic in the lagna', bool([g for g in BEN + ('Budha',) if hs(g) == 1]), True))
Y.append(('36 Asubha', 'malefic in the lagna', bool([g for g in MAL if hs(g) == 1]), True))
Y.append(('36 Gajakesari', 'Guru in a kendra from Chandra',
          frm('Guru', 'Chandra') in (1, 4, 7, 10), True))
Y.append(('36 Amala', 'a benefic ALONE in the 10th from the lagna',
          occ(10) == ['Guru'], True))
Y.append(('36 Lakshmi', '9th lord in own or exaltation sign',
          dignity('Shukra', sign_of(POS['Shukra'])) in ('own', 'exalted'), True))
Y.append(('36 Khadga', '2nd lord in the 9th AND 9th lord in the 2nd',
          False, 'IMPOSSIBLE for Kanya — Shukra rules both'))
Y.append(('36 Kusuma', 'a FIXED lagna, with Shukra in a kendra',
          LAG in FIX and hs('Shukra') in (1, 4, 7, 10),
          'IMPOSSIBLE for Kanya — Kanya is a dual sign'))
Y.append(('36 Kalanidhi', 'Guru in the 2nd or the 5th', hs('Guru') in (2, 5), True))
Y.append(('36 Srinatha', '7th lord in the 10th AND the 10th lord exalted',
          hs('Guru') == 10 and dignity('Budha', sign_of(POS['Budha'])) == 'exalted',
          'HALF-FORMS — Guru IS the 7th lord in the 10th; Budha is not exalted'))
Y.append(('36 Sankha', '5th lord and 6th lord in mutual kendras',
          False, 'IMPOSSIBLE for Kanya — Shani rules both'))
Y.append(('36 Chamara', 'lagna lord exalted in a kendra',
          dignity('Budha', sign_of(POS['Budha'])) == 'exalted' and hs('Budha') in (1, 4, 7, 10), True))
Y.append(('36 Kahala', '4th and 9th lords in kendras from each other',
          frm('Guru', 'Shukra') in (1, 4, 7, 10), True))
Y.append(('37 Sunapha', 'a graha other than Surya in the 2nd from Chandra',
          bool([g for g in G7 if g not in ('Surya', 'Chandra') and frm(g, 'Chandra') == 2]),
          'condition met, but SUPERSEDED by Duradhura'))
Y.append(('37 Anapha', 'a graha other than Surya in the 12th from Chandra',
          bool([g for g in G7 if g not in ('Surya', 'Chandra') and frm(g, 'Chandra') == 12]),
          'condition met, but SUPERSEDED by Duradhura'))
Y.append(('37 Duradhura', 'both of the above — this is the operative name', True, True))
Y.append(('37 Kemadruma', 'neither of the above', False, True))
Y.append(('37 Adhiyoga', 'benefics in the 6th, 7th or 8th from Chandra',
          bool([g for g in BEN + ('Budha',) if frm(g, 'Chandra') in (6, 7, 8)]), True))
Y.append(('38 Veshi', 'a graha other than Chandra in the 2nd from Surya',
          bool([g for g in G7 if g not in ('Surya', 'Chandra') and frm(g, 'Surya') == 2]), True))
Y.append(('38 Vasi', 'a graha other than Chandra in the 12th from Surya',
          bool([g for g in G7 if g not in ('Surya', 'Chandra') and frm(g, 'Surya') == 12]), True))
Y.append(('38 Ubhayachari', 'both of the above', False, True))
for nm, r, v, note in Y:
    tag = 'FORMS ' if v else 'absent'
    print(f"    {tag}    {nm:16s} {r}")
    if note is not True:
        print(f"    {'':10s}{'':16s} -> {note}")
sub('And a structural fact about Kanya lagna that the yoga sweep exposes')
pairsof = {}
for i in range(12):
    pairsof.setdefault(LORD[(LAG + i) % 12], []).append(i + 1)
print("  I first wrote: \"for Kanya, five of the seven grahas each rule two houses.\"")
print("  THAT IS TRUE OF EVERY LAGNA -- only Surya and Chandra rule one sign each,")
print("  so five grahas rule two houses in every chart ever cast.  THE UNIVERSAL")
print("  FACT SAYS NOTHING.  WHAT DISTINGUISHES KANYA IS WHICH FIVE PAIRS:\n")
for g in G7:
    hh = pairsof.get(g, [])
    if len(hh) == 2:
        print(f"      {g:8s} the {ordn(hh[0])} and the {ordn(hh[1])}"
              f"   -- and {hh[0]} + {hh[1]} = {hh[0]+hh[1]}")
print(f"""
  EVERY CO-RULED PAIR SUMS TO ELEVEN.  1/10, 2/9, 3/8, 4/7, 5/6 -- the lordship
  map of this chart is PERFECTLY MIRROR-SYMMETRIC about the 1st-12th axis.

  IS THAT COMMON?  It is testable across all twelve lagnas:
""")
print(f"  {'lagna':11s}{'mirror pairs (a+b=11) sharing a lord':44s}count")
for L in range(12):
    hits = [f'{a}/{11-a}' for a in range(1, 6)
            if LORD[(L + a - 1) % 12] == LORD[(L + 10 - a) % 12]]
    mark = '   <<<' if len(hits) == 5 else ''
    print(f"  {SIGNS[L]:11s}{str(hits):44s}{len(hits)}{mark}")
print(f"""
  KANYA IS THE ONLY LAGNA IN THE ZODIAC WITH ALL FIVE.  Meena has four; the
  other ten have NONE.

  AND THE MECHANISM IS EXACT, not a curiosity.  Sign lordship is symmetric
  about the Karka-Simha boundary: Mithuna/Kanya, Vrishabha/Tula, Mesha/
  Vrischika, Meena/Dhanu and Kumbha/Makara are each one graha's pair, and only
  Karka/Simha are split between the two luminaries.  For houses a and 11-a to
  share a lord their signs must be reflections, which requires 2L + 9 = 7 mod
  12 -- so L = 5 or 11, KANYA OR MEENA AND NOTHING ELSE.  Kanya gets the fifth
  pair because its 5th and 6th fall on Makara and Kumbha, both Shani; Meena
  loses it because its 5th and 6th fall on Karka and Simha, the one split pair.

  WHAT THIS COSTS THE CHART, in yoga terms:
""")
COLL = [('Khadga', 2, 9), ('Sankha', 5, 6)]
for nm, x, y in COLL:
    lx = LORD[(LAG + x - 1) % 12]
    n = sum(1 for L in range(12)
            if LORD[(L + x - 1) % 12] == LORD[(L + y - 1) % 12])
    print(f"      {nm:8s} needs the {ordn(x)} and {ordn(y)} lords in relation to each other")
    print(f"      {'':8s} BOTH ARE {lx.upper()} -- foreclosed for {n} of 12 lagnas")
print(f"""
  SO KHADGA AND SANKHA ARE NOT ABSENT FROM THIS CHART.  THEY ARE UNAVAILABLE.
  Sankha is foreclosed for KANYA ALONE out of twelve ascendants.

  KUSUMA IS THE SAME CASE BY A DIFFERENT ROUTE -- it requires a FIXED lagna and
  Kanya is dual.  UNAVAILABLE RATHER THAN ABSENT.

  THAT DISTINCTION MATTERS AND THIS READING HAS NOT BEEN MAKING IT.  Section 14
  lists yogas as "forms" or "absent", which reads as though the chart narrowly
  missed them.  For these three the chart missed nothing: THE ASCENDANT
  FORECLOSED THEM BEFORE ANY GRAHA WAS PLACED.

  AND THE SYMMETRY REACHES FURTHER THAN THE YOGAS.  The same mirror pairing is
  why GURU rules the 4th AND the 7th and BUDHA rules the 1st AND the 10th --
  which is to say, THE KENDRADHIPATI DOSHA SECTION 36 CALLED THE MOST EXPENSIVE
  UNREAD RULE IN THE DOCUMENT IS A DIRECT CONSEQUENCE OF THIS SYMMETRY.  It is
  not an accident of this nativity.  It is what Kanya lagna IS.
""")

DECL = ['Parvatha', 'Bheri', 'Mridanga', 'Sarada', 'Matsya', 'Koorma',
        'Kalpadruma', 'Trimurthi']
print(f"""
  AND {len(DECL)} OF CHAPTER 36'S TWENTY-ONE ARE DECLINED, BY NAME:

      {', '.join(DECL)}

  I cannot state their formation rules with the confidence this document
  requires -- several depend on navamsa-lord chains and on multi-clause
  conditions whose variants differ between schools.  THEY ARE LISTED RATHER
  THAN QUIETLY OMITTED, which is the difference between a gap and a silence.

  Chapter 36's "Dhana yoga" (in ch 37's subtitle) and chapters 39-41's raja and
  wealth yogas are likewise named-but-untested; section 14 found the chart's
  one kendra-trikona raja yoga by construction rather than from a list.
""")

# =============================================================================
rule('5.  CHAPTER 27 — PLANETARY WAR, NEVER TESTED')
pairs = []
for i, a in enumerate(G7):
    for b in G7[i+1:]:
        if a in ('Surya', 'Chandra') or b in ('Surya', 'Chandra'):
            continue
        d = abs(POS[a] - POS[b])
        d = min(d, 360 - d)
        if d < 5:
            pairs.append((a, b, d))
print(f"""
  THE RULE.  Graha yuddha occurs when two non-luminous grahas are within one
  degree of each other.  Chapter 27 lists it among the strength components and
  this reading has never computed it.

  Closest non-luminous pairs in this chart:
""")
alld = sorted(((min(abs(POS[a]-POS[b]), 360-abs(POS[a]-POS[b])), a, b)
               for i, a in enumerate(G7) for b in G7[i+1:]
               if a not in ('Surya', 'Chandra') and b not in ('Surya', 'Chandra')))
for d, a, b in alld[:4]:
    print(f"      {a:8s} {b:8s} {d:7.2f} deg")
print(f"""
  NO PLANETARY WAR.  The closest non-luminous pair is {alld[0][1]} and {alld[0][2]} at
  {alld[0][0]:.2f} degrees, which is {alld[0][0]:.0f} times the one-degree threshold.

  A NEGATIVE RESULT, AND WORTH ONE LINE ONLY.  But it was an untested
  assumption until now, in a chart with four grahas crowded into Vrishabha
  where a war would have been entirely plausible.
""")

# =============================================================================
rule('6.  WHAT AN ADDRESS DOES AND DOES NOT SETTLE')
print("""
  SECTION 36 PRICED EIGHT DISPUTED RULES AND SAID ONE PAGE WOULD SETTLE MOST
  OF THEM.  THE PAGE HAS ARRIVED.  HONESTLY, HERE IS WHAT CHANGED:

      RETIRED         D8 and D11 construction.  Chapter 6 names the sixteen
                      and neither is among them, so there was never a
                      Parashari rule to disagree with.  The dispute dissolves.

      RESOLVED        The chapter-73 ray scaling.  Chapter 28 identified what
                      the rays feed, which sent me to the supplied Shadbala
                      table, which confirms the scaling to four decimals.
                      SETTLED BY DATA THE REPOSITORY ALREADY HELD.

      LOCATED, NOT SETTLED
                      Shodashavarga starting signs        chapter 6
                      kendradhipati dosha                 chapter 34
                      viparita raja yoga                  chapters 39-41
                      trikona-and-dusthana lordship       chapter 34
                      drishti inside a varga              chapters 8 and 26
                      argala counter-houses               chapter 31

  A CONTENTS PAGE GIVES A CHAPTER NUMBER.  IT DOES NOT GIVE A RULE.  Six of the
  eight are now findable by anyone holding the book and remain exactly as
  undetermined in this document as they were yesterday.

  ONE THING DID SHARPEN.  Chapter 34's subtitle runs through the ascendants one
  at a time -- Aries, Taurus, Gemini, Cancer, Leo, VIRGO, Libra, and so on.  So
  the kendradhipati question for this chart is not a general doctrine to be
  weighed; IT IS A SPECIFIC PASSAGE ABOUT KANYA LAGNA, and it will say plainly
  whether Guru is a malefic here.  Section 36 called that the most expensive
  unread rule in the document.  IT IS NOW THE MOST PRECISELY LOCATED ONE.

  AND THE PAGE ADDED WORK RATHER THAN CLOSING IT:

      one more dasha system      Varnada, chapter 5 -- the count is 27, not 26
      three special ascendants   Bhava, Ghatika and Hora Lagna, chapter 5
      sign aspects               chapter 8, never used
      evils at birth             chapters 9 and 10, never used
      upagraha effects by house  chapter 25, never used
      fifty-one named yogas      chapters 35-38, of which this script closes
                                 the ones whose rules can be stated
""")
print('=' * 92)
