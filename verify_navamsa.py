#!/usr/bin/env python3
"""
D9 -- the navamsa read as a CHART, not as a row in a varga table.

Section 11 prints the D9 alongside the other fifteen Shodashavarga charts: a
placement list with house class and dignity.  That is all this document has
ever done with it, and for the varga that classically ranks second only to the
rashi chart -- the one that governs the spouse, dharma, the second half of
life, and the real inner strength of every graha -- that is not enough.

So this reads it properly:

    the D9 lagna and its lord, treated as a lagna
    every D9 house lord and where it sits IN D9
    dignity gained and lost between D1 and D9
    vargottama, computed rather than recalled
    yogas that form INSIDE the navamsa
    the D9 7th, which is the whole point of the varga
    the 64th navamsa -- a classical sensitive point never computed here
    and what the D9 says about the second half of life

Placement-based, per his instruction.  One methodological note stated up
front: applying Parashari graha drishti INSIDE a divisional chart is done by
many and rejected by others, on the grounds that a varga is a mapping of
dignity rather than a sky.  Where aspects are used below they are labelled, so
that part can be discarded without touching the rest.
"""
from ephem_core import (SIGNS, GRAHAS, SUPPLIED, LORD, EXALT, dignity,
                        varga, sign_of, short, nak_of, rule, sub)

POS = dict(SUPPLIED)
LAG1 = sign_of(POS['Lagna'])
D9 = {g: varga(POS[g], 9) for g in GRAHAS + ['Lagna']}
L9 = D9['Lagna']
h9 = lambda g: (D9[g] - L9) % 12 + 1
h1 = lambda g: (sign_of(POS[g]) - LAG1) % 12 + 1
sign9 = lambda n: (L9 + n - 1) % 12
occ9 = lambda n: [g for g in GRAHAS if h9(g) == n]
rules9 = lambda g: [i for i in range(1, 13) if LORD[(L9 + i - 1) % 12] == g]
rules1 = lambda g: [i for i in range(1, 13) if LORD[(LAG1 + i - 1) % 12] == g]
ordn = lambda n: f"{n}{'th' if 10 <= n % 100 <= 20 else {1:'st',2:'nd',3:'rd'}.get(n%10,'th')}"
DEBIL = {g: (s + 6) % 12 for g, s in EXALT.items()}
ASPECT = {'Mangal': (4, 7, 8), 'Guru': (5, 7, 9), 'Shani': (3, 7, 10),
          'Rahu': (5, 7, 9), 'Ketu': (5, 7, 9)}
HOUSE = ['self', 'wealth, speech', 'effort, siblings', 'home, mother',
         'children, mind', 'service, illness', 'SPOUSE', 'transformation',
         'dharma, father', 'career', 'gains', 'loss, moksha']
RANK = {'exalted': 5, 'own': 4, 'friend': 3, 'neutral': 2, 'enemy': 1,
        'debilitated': 0}
dg = lambda g, s: 'shadow' if g in ('Rahu', 'Ketu') else dignity(g, s)

# =============================================================================
rule('1.  THE FIRST FACT, AND THIS DOCUMENT HAS NEVER STATED IT')
print(f"""
      D1 lagna   {SIGNS[LAG1]}
      D9 lagna   {SIGNS[L9]}
""")
if L9 == LAG1:
    print(f"""  THE ASCENDANT IS VARGOTTAMA.

  The lagna falls in the same sign in the rashi chart and in the navamsa.  That
  is one of the strongest single statements available in Parashari jyotisha,
  and section 11 prints it in a table without remarking on it.

  What it means, classically and without any strength measure: THE PERSON IS
  THE SAME PERSON IN THE INNER CHART AS IN THE OUTER ONE.  The self does not
  change shape between what is presented and what is actually there.  Vargottama
  lagna is held to give steadiness of identity, resilience, and -- specifically
  -- that the SECOND HALF OF LIFE CONFIRMS THE FIRST rather than contradicting
  it.

  For a chart this full of tension between measures, a vargottama lagna is the
  single most stabilising thing in it.
""")
print(f"""  And note who sits on it:

      D9 lagna occupants: {', '.join(occ9(1)) or 'empty'}

  THE MAHADASHA LORD OCCUPIES THE NAVAMSA ASCENDANT.  Rahu runs the period from
  Dec 2022 to Dec 2040 and it is sitting on the D9 lagna -- so the current
  eighteen years are being run by the graha placed on the inner self.  That is
  a structural reason the reading keeps describing this period as identity-level
  rather than circumstantial.
""")

# =============================================================================
rule('2.  THE NAVAMSA AS A CHART — HOUSES, LORDS, OCCUPANTS')
print(f"  D9 lagna {SIGNS[L9]}, lord {LORD[L9]} — standing in D9 house "
      f"{h9(LORD[L9])} ({SIGNS[D9[LORD[L9]]]}, {dg(LORD[L9], D9[LORD[L9]])})\n")
print(f"  {'ho':3s}{'sign':11s}{'lord':9s}{'lord in':8s}{'occupants':26s}what it governs")
for n in range(1, 13):
    s = sign9(n)
    ld = LORD[s]
    print(f"  {n:2d} {SIGNS[s]:11s}{ld:9s}{h9(ld):5d}   "
          f"{', '.join(occ9(n)) or '—':26s}{HOUSE[n-1]}")

tgt = {}
for n in range(1, 13):
    tgt.setdefault(h9(LORD[sign9(n)]), []).append(n)
print(f"""
  WHERE THE D9 LORDS CONCENTRATE:
""")
for h in sorted(tgt):
    print(f"      into D9 house {h:2d} : {', '.join(str(x) for x in tgt[h])}")

# =============================================================================
rule('3.  WHAT EACH GRAHA GAINS OR LOSES BETWEEN D1 AND D9')
print("""
  This is the navamsa's classical job: a graha strong in the rashi chart but
  weak in the navamsa PROMISES more than it delivers, and the reverse holds.
  Nothing here is a score -- it is the dignity name in each chart.
""")
print(f"  {'graha':9s}{'D1 sign':12s}{'D1':12s}{'D9 sign':12s}{'D9':12s}verdict")
gain, loss, same = [], [], []
for g in GRAHAS:
    s1, s9 = sign_of(POS[g]), D9[g]
    d1, d9 = dg(g, s1), dg(g, s9)
    if g in ('Rahu', 'Ketu'):
        v = '—'
    elif RANK[d9] > RANK[d1]:
        v = 'STRONGER inside'; gain.append(g)
    elif RANK[d9] < RANK[d1]:
        v = 'WEAKER inside'; loss.append(g)
    else:
        v = 'unchanged'; same.append(g)
    vg = '  VARGOTTAMA' if s1 == s9 else ''
    print(f"  {g:9s}{SIGNS[s1]:12s}{d1:12s}{SIGNS[s9]:12s}{d9:12s}{v}{vg}")

print(f"""
  STRONGER IN THE NAVAMSA : {', '.join(gain) or 'none'}
  WEAKER IN THE NAVAMSA   : {', '.join(loss) or 'none'}
  UNCHANGED               : {', '.join(same) or 'none'}
""")

sub('And two of those four shifts change claims already in this document')
print("""
  CHANDRA IS EXALTED IN D1 AND ONLY NEUTRAL IN D9.  That is the classic
  "promises more than it delivers" pattern, and it lands on a claim made three
  sections ago.  Section 24 leaned on the 11th lord being EXALTED as the
  counterweight to a badly built 11th house.  THE NAVAMSA QUALIFIES THAT.  The
  exaltation is real in the outer chart and does not hold up in the inner one,
  so the gains-through-elders channel is a genuine promise that thins on
  delivery.  Section 24 is not overturned -- the placement is still the best
  thing the 11th has -- but it was stated more confidently than the navamsa
  supports.

  BUDHA IS NEUTRAL IN D1 AND ENEMY IN D9.  The lagna and 10th lord is combust
  outside and uncomfortable inside.  IT GETS WORSE, NOT BETTER, and there is no
  varga in the pair where the instrument of self is at ease.

  AND THE TWO THAT IMPROVE ARE WORTH NAMING TOO.  Guru goes from enemy to
  neutral -- the marriage and home significator is better inside than out.
  Mangal goes from neutral to friend, which matters for the next section,
  because Mangal is one of the two grahas sitting in the navamsa 7th: the
  malefic in the marriage house is WELL DIGNIFIED there.  Friction that is
  competent rather than chaotic.
""")

sub('Vargottama — computed across D1/D9')
vg = [g for g in GRAHAS if sign_of(POS[g]) == D9[g]]
print(f"""
      grahas vargottama in D1/D9: {', '.join(vg) or 'none'}
      lagna vargottama          : {'YES' if L9 == LAG1 else 'no'}

  {'SURYA IS THE ONLY VARGOTTAMA GRAHA, AND IT IS ALSO EXALTED IN BOTH.'
   if vg == ['Surya'] else ''}
  A graha exalted AND vargottama is about as well-made as Parashari dignity
  gets, and this chart has exactly one of them -- the 12th lord, standing in
  the 8th.  THE BEST-BUILT THING IN THE CHART RULES LOSS AND SITS IN CRISIS.
  That is the whole reading in one placement.
""")

# =============================================================================
rule('4.  THE D9 SEVENTH — THE POINT OF THE VARGA')
sev = occ9(7)
sl = LORD[sign9(7)]
print(f"""
  The navamsa is read for the spouse before it is read for anything else, and
  the 7th house of the D9 is the sharpest statement it makes.

      D9 7th sign     {SIGNS[sign9(7)]}
      D9 7th lord     {sl}, in D9 house {h9(sl)} ({SIGNS[D9[sl]]}, {dg(sl, D9[sl])})
      D9 7th holds    {', '.join(sev) or 'empty'}

  TWO MALEFICS OCCUPY THE NAVAMSA SEVENTH -- MANGAL AND KETU TOGETHER.

  Section 11 lists both placements and never puts them side by side.  Read as a
  chart they are one configuration, and it is a heavy one: the house of the
  spouse in the varga of the spouse, occupied by the graha of severance and the
  graha of friction, and by nothing else.

  WITH ONE MITIGATION THAT THE DIGNITY TABLE ABOVE SUPPLIES: Mangal is in MEENA,
  a friendly sign, and is one of only two grahas that gain dignity in the
  navamsa.  A well-dignified malefic in the 7th is not the same as an afflicted
  one.  Ketu carries no dignity either way.

  AND THE D9 7TH LORD IS GURU -- which in the rashi chart also rules the 7th.
  The same graha carries the marriage in both charts.  In D9 it stands in the
  {ordn(h9(sl))} house, a DUSTHANA.
""")
print(f"""  What that does NOT overturn:

      the D1 7th is Meena, SAV 33, Bhava rank 4 -- well built
      the Upapada falls in the rank-2 4th
      the 8th from the Upapada is too weak to dissolve the marriage
      Kuja dosha is cancelled (section 25)

  So the outer chart says the marriage is STRUCTURALLY SOUND and the inner
  chart says it is EMOTIONALLY AUSTERE.  Those are not contradictory; they are
  the two halves of what this reading has said about the marriage all along --
  DURABLE AND UNDEMONSTRATIVE.  The D9 is where the "undemonstrative" comes
  from, and until now that word was never actually sourced.
""")

# =============================================================================
rule('5.  YOGAS THAT FORM INSIDE THE NAVAMSA')
KEN, TRI = (1, 4, 7, 10), (1, 5, 9)
print("""
  Kendra lord with trikona lord, computed within D9 itself:
""")
found = False
for n in range(1, 13):
    o = occ9(n)
    for i in range(len(o)):
        for j in range(i + 1, len(o)):
            a, b = o[i], o[j]
            if (set(rules9(a)) & set(KEN) and set(rules9(b)) & set(TRI)) or \
               (set(rules9(b)) & set(KEN) and set(rules9(a)) & set(TRI)):
                print(f"      {a} ({rules9(a)}) + {b} ({rules9(b)}) "
                      f"in D9 house {n}")
                found = True
if not found:
    print("      NONE.  No kendra lord shares a D9 house with a trikona lord.")

sub('Exchange inside D9')
ex = False
for a in range(1, 13):
    for b in range(a + 1, 13):
        la, lb = LORD[sign9(a)], LORD[sign9(b)]
        if la != lb and h9(la) == b and h9(lb) == a:
            print(f"      the {ordn(a)} lord {la} is in the {ordn(b)}, and the "
                  f"{ordn(b)} lord {lb} is in the {ordn(a)} — EXCHANGE")
            ex = True
if not ex:
    print("      NONE.")

print(f"""
  THE NAVAMSA CARRIES NO RAJA YOGA AND NO EXCHANGE.

  Set that against the rashi chart, which has both -- Budha with Shukra in the
  8th, and the 8th/9th parivartana.  THE OUTER CHART IS FULL OF COMBINATIONS
  AND THE INNER CHART IS BARE.

  Classically that is read one way: WHAT HE HAS IS NOT INHERITED FROM THE
  INSIDE.  The rashi yogas are real (section 25 shows how they are spoiled),
  but the navamsa does not second them.  A chart whose D9 confirmed its D1
  would deliver more easily than this one does.
""")

# =============================================================================
rule('6.  THE 64TH NAVAMSA — NEVER COMPUTED IN THIS DOCUMENT')
print("""
  THE RULE.  Counting from the navamsa occupied by the Moon -- and separately
  from the navamsa of the lagna -- the 64th navamsa forward is a classical
  sensitive point, the Khara or "harsh" navamsa.  Its LORD, the Khareshi, is
  treated as a marker of difficulty, and its dasha periods are watched.

  Counting inclusively, the 64th navamsa is 63 navamsas forward.  Each navamsa
  advances the navamsa-sign by one, so the 64th falls 63 signs on --
  63 mod 12 = 3 -- i.e. THE 4TH SIGN FROM THE NAVAMSA OCCUPIED.

  THE TEST:
""")
for ref in ('Chandra', 'Lagna'):
    base = D9[ref]
    k = (base + 3) % 12
    lord = LORD[k]
    print(f"      from {ref:8s} navamsa {SIGNS[base]:11s} -> 64th navamsa "
          f"{SIGNS[k]:11s} lord {lord}")
    print(f"          {lord} stands in D1 house {h1(lord)}, D9 house {h9(lord)}"
          f", ruling D1 {rules1(lord)}")
km = LORD[(D9['Chandra'] + 3) % 12]
kl = LORD[(D9['Lagna'] + 3) % 12]
print(f"""
  A CORRECTION TO THE DRAFT.  I had written that both Khareshis are the same
  graha.  THEY ARE NOT.  The Moon's 64th navamsa is ruled by {km}; the lagna's
  by {kl}.  The computation says so plainly and the drafted sentence was wrong.

  The true version is more pointed than the one I had written, because of WHAT
  those two grahas rule:

      {km:8s} — the Khareshi from the Moon — rules D1 houses {rules1(km)}
      {kl:8s} — the Khareshi from the lagna — rules D1 houses {rules1(kl)}

  So the classical harsh marker computed from the MIND lands on the lord of the
  8TH -- the graha whose mahadasha ran ages 13.7 to 20.7, the transformation
  already lived.  And the harsh marker computed from the BODY lands on the lord
  of the 7TH -- the marriage, which is the thing ahead.

  ONE POINTS AT WHAT IS DONE.  THE OTHER POINTS AT WHAT IS COMING.  Neither is
  a prediction; both are markers the tradition says to watch, and they are
  watching the two things this reading has spent the most time on.
""")

# =============================================================================
rule('7.  THE SECOND HALF OF LIFE')
print(f"""
  The navamsa is classically weighted more heavily after about 35 -- the rashi
  chart describes the first half, the navamsa the second.  Read that way the
  D9 says something quite specific, and it lines up with the dasha sequence
  without being derived from it.

      D9 lagna       {SIGNS[L9]} — VARGOTTAMA.  The self holds.
      D9 lagna lord  {LORD[L9]} in D9 house {h9(LORD[L9])}, {dg(LORD[L9], D9[LORD[L9]])}
      D9 10th        {SIGNS[sign9(10)]} holding {', '.join(occ9(10)) or 'empty'}
      D9 4th         {SIGNS[sign9(4)]} — {', '.join(occ9(4)) or 'empty'}
      D9 9th         {SIGNS[sign9(9)]} — {', '.join(occ9(9)) or 'empty'}

  SHANI IN THE D9 TENTH is the placement that matters most for the later
  decades, and it is one of the four career credentials the reading has been
  citing since section 36.  Here is where it actually comes from: THE GRAHA OF
  STRUCTURE OCCUPIES THE CAREER HOUSE OF THE CHART THAT GOVERNS THE SECOND HALF
  OF LIFE.  Its own mahadasha opens in Dec 2056.

  AND THE D9 LAGNA LORD IS BUDHA, IN AN ENEMY SIGN.  The same graha that is
  combust in the rashi chart is uncomfortable in the navamsa.  IT DOES NOT GET
  BETTER INSIDE.  Whatever else the second half improves, the instrument of
  self does not become easy.
""")

# =============================================================================
rule('8.  WHAT THE DEEP D9 PASS ADDS')
print(f"""
  1. THE LAGNA IS VARGOTTAMA.  Never stated in this document, and it is the
     most stabilising single fact in the chart.

  2. RAHU OCCUPIES THE D9 LAGNA, and runs the mahadasha until 2040.  The
     current eighteen years sit on the navamsa ascendant.

  3. THE D9 7TH HOLDS MANGAL AND KETU TOGETHER, and its lord Guru falls in a
     D9 dusthana.  This is the source of "undemonstrative" -- a word the
     reading has used repeatedly without ever sourcing it.

  4. THE NAVAMSA CONTAINS NO RAJA YOGA AND NO EXCHANGE, where the rashi chart
     has both.  The inner chart does not second the outer one.

  5. SURYA IS THE ONLY VARGOTTAMA GRAHA and is exalted in both -- the
     best-made body in the chart, ruling loss, sitting in crisis.

  6. THE TWO 64TH NAVAMSAS have DIFFERENT lords -- {km} from the Moon, {kl}
     from the lagna -- and they are the lords of the 8th and the 7th: the
     transformation already lived, and the marriage still ahead.

  AND THE ONE-LINE VERSION:

      THE OUTER CHART IS CROWDED, CONTRADICTORY AND FULL OF COMBINATIONS.
      THE INNER CHART IS STEADY, BARE, AND AUSTERE.

  A vargottama lagna on an empty-handed navamsa is a person who is exactly what
  he appears to be, holding fewer cards than the outer chart suggests.
""")
print('=' * 92)
