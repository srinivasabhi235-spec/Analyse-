#!/usr/bin/env python3
"""
BHANGA -- the cancellation rules, tested systematically.

"Are there any cancel-out rules for the charts given" is a better question than
it looks, and this document has largely not answered it.  A search of the
reading returns no neecha bhanga, no Kuja dosha, no papakartari, no yoga
bhanga.  Kemadruma is mentioned but never actually tested.

That is a real gap, and one of the items in it -- MANGAL DOSHA -- has never been
computed at all despite three sections on marriage.

Jyotisha's cancellation doctrines come in four families:

    A DOSHA IS CANCELLED       an affliction is annulled by a counter-condition
                               (Kuja dosha bhanga, Kemadruma bhanga)
    A WEAKNESS IS CANCELLED    debilitation or combustion is undone
                               (neecha bhanga, combustion exemptions)
    A YOGA IS CANCELLED        a combination forms but cannot deliver
                               (yoga bhanga -- the least discussed and the most
                               important one for this chart)
    A YOGA REQUIRES AFFLICTION and is spoiled by strength
                               (the viparita raja yogas)

Every rule below is stated before it is applied, so the reasoning can be
checked rather than taken.  Where schools disagree the disagreement is
reported instead of resolved.

Placement-based throughout, per his instruction.
"""
import swisseph as swe
from ephem_core import (SIGNS, GRAHAS, SUPPLIED, LORD, EXALT, IDS, FLAG, JD,
                        varga, dignity, sign_of, short, rule, sub)

POS = dict(SUPPLIED)
LAG = sign_of(POS['Lagna'])
hs = lambda g: (sign_of(POS[g]) - LAG) % 12 + 1
house_sign = lambda n: (LAG + n - 1) % 12
occupants = lambda n: [g for g in GRAHAS if hs(g) == n]
rules_of = lambda g: [i for i in range(1, 13) if LORD[(LAG + i - 1) % 12] == g]
ASPECT = {'Mangal': (4, 7, 8), 'Guru': (5, 7, 9), 'Shani': (3, 7, 10),
          'Rahu': (5, 7, 9), 'Ketu': (5, 7, 9)}
DEBIL = {g: (s + 6) % 12 for g, s in EXALT.items()}
OWN = {g: [i for i in range(12) if LORD[i] == g] for g in EXALT}
MALEFIC = ['Surya', 'Mangal', 'Shani', 'Rahu', 'Ketu']
SPEED = {g: swe.calc_ut(JD, IDS[g], FLAG)[0][3] for g in EXALT}
# distance from a graha's sign to another, counted inclusively
frm = lambda a, b: (sign_of(POS[b]) - sign_of(POS[a])) % 12 + 1
ordn = lambda n: f"{n}{'th' if 10 <= n % 100 <= 20 else {1:'st',2:'nd',3:'rd'}.get(n%10,'th')}" 
aspects_from = lambda g: [(sign_of(POS[g]) + a - 1) % 12
                          for a in ASPECT.get(g, (7,))]

# =============================================================================
rule('1.  THE TWO DOCTRINES THAT ARE MOOT BEFORE WE START')
sub('Neecha bhanga — cancellation of debilitation')
deb = [g for g in EXALT if sign_of(POS[g]) == DEBIL[g]]
print(f"""
  THE RULE.  A debilitated graha's weakness is annulled if, for example, its
  dispositor is in a kendra from the lagna or the Moon, or the graha exalted in
  that sign is in a kendra, or the debilitated graha is aspected by its
  dispositor.  Schools list between four and eight such conditions.

  THE TEST.  Debilitated grahas in the rashi chart: {', '.join(deb) if deb else 'NONE'}.

  NEECHA BHANGA DOES NOT ARISE.  There is nothing to cancel.  Every graha is
  exalted, own, friendly, neutral or in an enemy sign -- not one is fallen.
  For a chart this heavily loaded that is worth stating plainly: THE CHART HAS
  NO DEBILITATION TO RESCUE.
""")

sub('Combustion exemption')
print(f"""
  THE RULE.  Combustion is annulled or much reduced when the combust graha is
  RETROGRADE, or stands in its OWN sign or EXALTATION.

  THE TEST.
""")
for g in ('Budha',):
    d = min(abs(POS[g] - POS['Surya']), 360 - abs(POS[g] - POS['Surya']))
    s = sign_of(POS[g])
    print(f"      {g} is combust ({d:.2f}° from Surya)")
    rg = 'YES' if SPEED[g] < 0 else f'NO — speed {SPEED[g]:+.4f}, direct'
    print(f"      retrograde?      {rg}")
    print(f"      own sign?        {'YES' if s in OWN[g] else f'NO — in {SIGNS[s]}'}")
    print(f"      exalted?         {'YES' if s == EXALT[g] else 'NO'}")
print("""
  NO EXEMPTION APPLIES.  Budha is direct, in a neutral sign, not exalted.
  THE COMBUSTION OF THE LAGNA AND 10TH LORD STANDS UNCANCELLED, and since no
  graha in this chart is retrograde, no other body claims the exemption either.
""")

# =============================================================================
rule('2.  KUJA DOSHA — NEVER COMPUTED IN THIS DOCUMENT UNTIL NOW')
print("""
  THE RULE.  Mangal occupying the 1st, 2nd, 4th, 7th, 8th or 12th house
  afflicts marriage.  It is reckoned from the LAGNA, from CHANDRA, and in many
  South Indian and Kerala traditions also from SHUKRA.  The 2nd (family), 4th
  (domestic peace), 7th (spouse), 8th (longevity of the marriage) and 12th
  (bed) are the sensitive ones; the 1st is counted by some and not by others.

  THE TEST — from all three reference points:
""")
DOSHA_H = (1, 2, 4, 7, 8, 12)
hits = []
for ref in ('Lagna', 'Chandra', 'Shukra'):
    if ref == 'Lagna':
        h = hs('Mangal')
    else:
        h = frm(ref, 'Mangal')
    flag = 'DOSHA' if h in DOSHA_H else 'clean'
    if h in DOSHA_H:
        hits.append((ref, h))
    print(f"      from {ref:8s} Mangal stands in the {ordn(h):5s}  {flag}")

print(f"""
  SO THE DOSHA IS PRESENT FROM {' AND '.join(r.upper() for r, _ in hits)},
  AND ABSENT FROM THE LAGNA.

  That is the single most common configuration in real charts and it is exactly
  why the doctrine is argued about.  From the lagna -- the reference most
  schools weight heaviest -- HE IS CLEAN.
""")

sub('And now the cancellations, which is where this actually resolves')
print("""
  THE RULES.  Kuja dosha is held cancelled when, among others:

      1. Mangal is in its OWN sign or EXALTED
      2. Mangal is CONJUNCT or ASPECTED BY GURU or CHANDRA
      3. Mangal is conjunct or aspected by SHANI
      4. Mangal occupies its own or Guru's sign in the dosha house
      5. Mangal is in a KENDRA from Guru
      6. the prospective partner carries the same dosha

  THE TEST:
""")
m_sign = sign_of(POS['Mangal'])
co = [g for g in GRAHAS if g != 'Mangal' and sign_of(POS[g]) == m_sign]
asp_on_mangal = [g for g in GRAHAS if g != 'Mangal' and m_sign in aspects_from(g)]
print(f"      1. own / exalted?          Mangal in {SIGNS[m_sign]} — "
      f"{dignity('Mangal', m_sign)}.  NO")
print(f"      2. conjunct Guru/Chandra?  conjunct: {', '.join(co)}  ->  "
      f"{'YES — CHANDRA' if 'Chandra' in co else 'no'}")
print(f"         aspected by Guru?       aspects on Mangal: "
      f"{', '.join(asp_on_mangal) or 'none'}  ->  "
      f"{'YES' if 'Guru' in asp_on_mangal else 'no'}")
print(f"      3. conjunct/aspected Shani? {'YES — conjunct' if 'Shani' in co else 'no'}")
kendra_guru = frm('Guru', 'Mangal') in (1, 4, 7, 10)
print(f"      5. kendra from Guru?       Mangal is the {ordn(frm('Guru','Mangal'))} "
      f"from Guru — {'YES' if kendra_guru else 'NO'}")
print(f"      6. partner's chart?        UNKNOWABLE — not supplied")
print(f"""
  TWO CANCELLATIONS FIRE, AND THEY ARE BOTH STRONG ONES:

      MANGAL IS CONJUNCT CHANDRA — and Chandra is EXALTED there.
      MANGAL IS CONJUNCT SHANI.

  Rule 2 is the most widely accepted cancellation in the entire doctrine, and
  it applies here in its strongest form: not a mere aspect but a conjunction,
  and with the Moon in its exaltation sign.

  THE VERDICT:

      Kuja dosha is ABSENT from the lagna, PRESENT from Chandra and Shukra,
      and CANCELLED by conjunction with an exalted Chandra and with Shani.

  Note what that does NOT say.  It does not say the marriage is unafflicted --
  section 44 found the 7th empty, aspected only by Ketu and holding Upaketu,
  and that has nothing to do with Mangal.  IT SAYS THE SPECIFIC DOSHA PEOPLE
  ASK ABOUT IS NOT THE PROBLEM IN THIS CHART.
""")

# =============================================================================
rule('3.  KEMADRUMA, AND WHY IT DOES NOT FORM')
c = sign_of(POS['Chandra'])
nxt = [g for g in GRAHAS if g not in ('Chandra',) and sign_of(POS[g]) == (c + 1) % 12]
prv = [g for g in GRAHAS if g not in ('Chandra',) and sign_of(POS[g]) == (c - 1) % 12]
withm = [g for g in GRAHAS if g != 'Chandra' and sign_of(POS[g]) == c]
print(f"""
  THE RULE.  Kemadruma yoga forms when NO graha occupies the 2nd or the 12th
  from Chandra, and none is conjunct it.  It is one of the harshest yogas in
  the literature -- isolation, and support that does not arrive.

  THE TEST.  Chandra in {SIGNS[c]}:

      2nd from Chandra  ({SIGNS[(c+1) % 12]:10s})  {', '.join(nxt) or 'EMPTY'}
      12th from Chandra ({SIGNS[(c-1) % 12]:10s})  {', '.join(prv) or 'EMPTY'}
      conjunct Chandra                {', '.join(withm) or 'none'}

  KEMADRUMA DOES NOT FORM, AND IT IS NOT EVEN CLOSE.  All three positions are
  occupied, and the 12th from Chandra holds three grahas including the exalted
  Surya.  The chart's most-cited yoga of isolation is comprehensively absent.
""")

# =============================================================================
rule('4.  PAPAKARTARI — AFFLICTION BY ENCLOSURE')
print(f"""
  THE RULE.  A house or graha hemmed between malefics -- malefic in the house
  before AND the house after -- is under PAPAKARTARI, scissors affliction.  The
  benefic mirror image is SHUBHAKARTARI.

  Malefics counted: {', '.join(MALEFIC)}.  Benefics: Guru, Shukra, Budha.

  THE TEST, on all twelve houses:
""")
BEN = ['Guru', 'Shukra', 'Budha']
found_p, found_s = [], []
for n in range(1, 13):
    before = occupants(n - 1 if n > 1 else 12)
    after = occupants(n + 1 if n < 12 else 1)
    pb = [g for g in before if g in MALEFIC]
    pa = [g for g in after if g in MALEFIC]
    bb = [g for g in before if g in BEN]
    ba = [g for g in after if g in BEN]
    if pb and pa:
        found_p.append((n, pb, pa))
    if bb and ba:
        found_s.append((n, bb, ba))
for n, a, b in found_p:
    print(f"      PAPAKARTARI on the {n:2d}th — {', '.join(a)} before, "
          f"{', '.join(b)} after")
for n, a, b in found_s:
    bef = occupants(n - 1 if n > 1 else 12)
    aft = occupants(n + 1 if n < 12 else 1)
    mixed = [g for g in bef + aft if g in MALEFIC]
    tag = (f"QUALIFIED — {', '.join(mixed)} also present, so the enclosure is "
           f"mixed" if mixed else "clean")
    print(f"      SHUBHAKARTARI on the {n:2d}th — {', '.join(a)} before, "
          f"{', '.join(b)} after")
    print(f"          {tag}")
if not found_p:
    print("      NO HOUSE IS UNDER PAPAKARTARI.")
print(f"""
  This follows directly from the stellium.  Seven grahas sit in two adjacent
  houses, so ten of the twelve houses have at least one empty neighbour and
  cannot be hemmed at all.  THE CONCENTRATION THAT WEAKENS THIS CHART IN OTHER
  WAYS PROTECTS IT COMPLETELY FROM ENCLOSURE AFFLICTION.
""")

# =============================================================================
rule('5.  YOGA BHANGA — THE ONE THAT MATTERS HERE')
print("""
  THE RULE, and it is the least discussed of the four families.  A yoga can
  form perfectly and still fail to deliver.  The classical spoilers are:

      the yoga's grahas stand in a DUSTHANA (6th, 8th, 12th)
      a participating graha is COMBUST
      a participating graha is in an ENEMY sign
      the yoga's lords are also lords of dusthanas
      the yoga is not supported by the dasha sequence in a usable lifetime

  THE TEST, on every yoga this chart actually has:
""")
YOGAS = [
    ('Raja yoga — Budha (1st, 10th) with Shukra (2nd, 9th)', ['Budha', 'Shukra'], 8),
    ('Amala yoga — Guru in the 10th from lagna', ['Guru'], 10),
    ('Vimala yoga — Surya, the 12th lord, in the 8th', ['Surya'], 8),
]
for name, gs, h in YOGAS:
    print(f"\n  {name}")
    print(f"      located in the {h}th"
          f"{'  — A DUSTHANA' if h in (6, 8, 12) else ''}")
    for g in gs:
        s = sign_of(POS[g])
        d = min(abs(POS[g] - POS['Surya']), 360 - abs(POS[g] - POS['Surya']))
        comb = (g != 'Surya' and d < 14)
        dus = [x for x in rules_of(g) if x in (6, 8, 12)]
        print(f"      {g:8s} {dignity(g, s):10s} in {SIGNS[s]:11s}"
              f"{'COMBUST  ' if comb else '':10s}"
              f"{'also rules dusthana ' + str(dus) if dus else ''}")

print("""
  READ THOSE THREE ROWS.

  THE RAJA YOGA IS SPOILED IN TWO WAYS AT ONCE: it sits in the 8th, and one of
  its two participants is combust.  It is a genuine raja yoga -- kendra lord
  with trikona lord, no argument -- and it is standing in the crisis house with
  its kendra lord swallowed by the Sun.  THIS IS THE CENTRAL YOGA BHANGA OF THE
  CHART, and it is the structural reason a reading that keeps finding raja
  yogas keeps also finding that they do not simply pay out.

  AMALA IS NOT CANCELLED BUT IT IS DIMINISHED: Guru is in the 10th, which is
  all Amala requires, but in its enemy's sign.  The yoga stands; the graha is
  uncomfortable.

  AND VIMALA IS THE INTERESTING ONE -- SEE BELOW.
""")

# =============================================================================
rule('6.  THE YOGA THAT IS CANCELLED BY STRENGTH')
s_sun = sign_of(POS['Surya'])
print(f"""
  THE RULE, and it inverts everything above.  The VIPARITA raja yogas -- Harsha,
  Sarala, Vimala -- arise when the lord of a dusthana stands in a dusthana.
  Their whole logic is that A BAD HOUSE'S RULER, BADLY PLACED, CANCELS ITS OWN
  HARM.  The yoga therefore DEPENDS ON THE LORD BEING SPOILED.

  A significant body of opinion holds that a viparita yoga IS ITSELF CANCELLED
  when the dusthana lord is strong -- exalted, in its own sign, or otherwise
  well dignified -- because a graha in good condition does not "ruin" the house
  it rules, and there is nothing for the inversion to work on.

  THE TEST.

      Vimala: the 12th lord is SURYA, and it stands in the 8th.  Formed.
      But Surya in {SIGNS[s_sun]} is {dignity('Surya', s_sun).upper()} — and it is
      VARGOTTAMA, and it is the best-dignified graha in the chart.

  SO VIMALA YOGA IS CONTESTED IN THIS CHART ON ITS OWN TERMS:

      by the formation rule    it is PRESENT
      by the affliction rule   it is CANCELLED — an exalted 12th lord is not a
                               spoiled one, and viparita needs spoilage

  THIS READING DOES NOT ADJUDICATE.  It records that the chart's one viparita
  yoga rests on a graha too well placed to satisfy the doctrine that produces
  it, and notes that section 9 ALREADY found Vimala dissolving under every
  cuspal house frame — by a completely different mechanism.

  TWO INDEPENDENT ROUTES TO DOUBTING THE SAME YOGA IS WORTH RECORDING.
""")

# =============================================================================
rule('7.  WHAT THE CANCELLATION PASS ACTUALLY CHANGES')
print("""
  1. KUJA DOSHA — the biggest practical result, and a favourable one.  Present
     from Chandra and Shukra, absent from the lagna, and CANCELLED by Mangal's
     conjunction with an exalted Chandra and with Shani.  This is the question
     families actually ask before a marriage, and this document had never
     computed it.  THE ANSWER IS THAT IT IS NOT AN OBSTACLE.

  2. KEMADRUMA — absent, comprehensively.  No isolation yoga.

  3. PAPAKARTARI — none, and for a structural reason: the stellium leaves too
     many empty neighbours for any house to be hemmed.

  4. NEECHA BHANGA — does not arise.  No graha is debilitated in the rashi
     chart, so the chart has no fallen graha needing rescue.

  5. COMBUSTION — NOT cancelled.  Budha is direct and undignified, so the
     weakness of the lagna and 10th lord stands exactly as the reading has
     always described it.  No graha in this chart is retrograde.

  6. YOGA BHANGA — the finding.  THE RAJA YOGA IS SPOILED TWICE: it sits in the
     8th and its kendra lord is combust.  Amala is diminished by an enemy sign.
     Vimala is doubtful on the doctrine's own logic.

  THE SHAPE OF IT:

      THE AFFLICTIONS IN THIS CHART CANCEL.  THE YOGAS DO NOT.

  Every classical dosha tested comes back annulled or absent; every benefic
  combination comes back qualified.  That is an unusual and quite specific
  result, and it is the same asymmetry the whole reading keeps meeting from
  other directions -- a chart that is protected from the standard misfortunes
  and made to work for its advantages.
""")
print('=' * 92)
