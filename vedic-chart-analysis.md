# A Kanya Lagna Chart — Complete Reading

A Parashari analysis of a single nativity, working from the rashi chart through
six divisional charts, the upagrahas, the six-fold strength calculations,
Ashtakavarga, the Vimshottari dasha, and the transits current at the time of
writing.

Read within the framework of Jyotisha, on its own terms and in its own
vocabulary.

Every numeric claim below was recomputed from the supplied longitudes rather
than taken on trust. The verification scripts are `verify_chart.py` (positions,
vargas, dasha) and `verify_bala.py` (Shadbala, Bhava Bala, Ashtakavarga,
Shodhya Pinda).

---

## 1. Provenance and verification

### What was supplied

D1 (Rashi), D9 (Navamsha), D10 (Dashamsha), D11 (Rudramsha), D8 (Ashtamsha),
D27 (Bhamsha), D30 (Trimshamsha); eleven upagrahas; the Vimshottari dasha tree;
Shadbala with all sub-components; Bhava Bala; Ashtakavarga and Reduced
Ashtakavarga; Shodhya Pinda; and a transit chart.

### What was verified

Rather than reading the tables at face value, each was reconstructed
independently:

| Check | Result |
|---|---|
| D9 and D27 recomputed from D1 longitudes | All 20 positions match to within a few arc-seconds |
| All nine Rahu antardashas rebuilt from Vimshottari proportions | Every boundary date matches exactly |
| Shadbala: five Sthana and nine Kala sub-components | Sum to their printed totals for all seven grahas |
| Shadbala: six balas → Total Pinda → Rupas → Rank | Reproduces exactly |
| Bhava Bala: Bhavadhipati + Disha + Drishti | Reproduces all twelve Total Pindas |
| Bhavadhipati figures vs. each house lord's Shadbala | Match under Kanya lagna lordships |
| Sarvashtakavarga total | **337** — the classical value |
| Reduced Ashtakavarga → Shodhya Pinda | Rebuilds all sixteen Rashi and Graha Pinda values exactly, using the standard Rashi and Graha Gunakara multipliers |

**This is an internally consistent, high-quality chart.** The convergence is
strong enough that the derived quantities below can be trusted.

### Two errors in the source

Rahu and Ketu must be exactly 180° apart. They are in D1, D9, D10, D11 and D27 —
but in **D8 and D30 the generator printed Ketu at Rahu's own longitude**:

| Varga | Printed | Correct | Consequence |
|---|---|---|---|
| **D8** | Ketu 05°26′ Karka (5th) | **05°26′ Makara — 11th** | Ketu joins exalted Mangal in the 11th, not Rahu in the 5th |
| **D30** | Ketu 27°56′ Vrischika (1st) | **27°56′ Vrishabha — 7th** | Ketu falls **4° from Chandra** in the 7th |

The D30 correction is interpretively significant: a tight Moon–Ketu conjunction
in the 7th of the Trimshamsha is a real signature, and the printed chart hides
it entirely. Corrected values are used throughout.

### Two rows left unused

- **"Bhava (in %)"** in the Shadbala table (Surya 74, Chandra 70, Mangal 33,
  Budha 14, Guru 19, Shukra 75, Shani 38) does not reconcile against any
  derivation tested: position within sign, nakshatra or pada; Ishta/Kashta
  proportion; Bhava Bala of the occupied house; or normalised Shadbala.
- **The "Sarv" column of the Reduced Ashtakavarga** is not the sum of the reduced
  graha columns (which do verify perfectly against Shodhya Pinda). It is
  presumably a separate reduction applied to the SAV totals.

Neither is used below. Nothing in this reading depends on them.

### Birth data, derived and triple-confirmed

The birth details were not supplied, but the chart determines them:

1. **Date.** The Moon at 1°47′ Vrishabha sits 38.41% through Krittika, leaving a
   Surya mahadasha balance of 3.6956 years. Adding Chandra (10) and Mangal (7)
   places the Rahu mahadasha 20.6956 years after birth. Against its given start
   of 25 Dec 2022, that implies **15 April 2002**.
2. **Confirmed by the Sun.** 1°28′ sidereal Mesha occurs every 15–16 April.
3. **Confirmed by Vara Bala.** The Kala Bala table awards 45 to Chandra, and
   Vara Bala goes to the lord of the weekday — requiring a **Monday**. 15 April
   2002 was a Monday.
4. **Lunar phase, from Paksha Bala.** Benefics score 10.11 and malefics 49.89,
   which back-solves to a Sun–Moon elongation of 30.32° — matching the D1
   longitudes exactly. That is **Shukla Tritiya, ~2.5 days after the new moon:
   a thin waxing crescent.** The Moon's doubled score of 20.21 confirms it.
5. **Time of day.** Hora Bala of 60 goes to Surya; on a Monday the Sun's hora is
   the 5th and 12th from sunrise. The ascendant sits 176° past the Sun, placing
   birth roughly eleven to twelve hours after sunrise. Both indicate **late
   afternoon or early evening**.

**The native is male and about 24 years old.** That matters: this is a chart at
the opening of its defining period, not one being assessed in retrospect.

---

## 2. The chart

**Lagna: 27°37′37″ Kanya (Virgo), Chitra pada 2.** Lagna lord Budha.

| Bhava | Sign | Lord | Occupants |
|---|---|---|---|
| 1 | Kanya | Budha | *(Lagna)* |
| 2 | Tula | Shukra | — |
| 3 | Vrischika | Mangal | **Ketu** *(gandanta)* |
| 4 | Dhanu | Guru | — |
| 5 | Makara | Shani | — |
| 6 | Kumbha | Shani | — |
| 7 | Meena | Guru | — |
| **8** | **Mesha** | **Mangal** | **Surya** *(exalted, gandanta)*, **Budha** *(combust)*, **Shukra** |
| **9** | **Vrishabha** | **Shukra** | **Chandra** *(exalted)*, **Mangal** *(Pushkara)*, **Shani**, **Rahu** |
| **10** | **Mithuna** | **Budha** | **Guru** |
| 11 | Karka | Chandra | — |
| 12 | Simha | Surya | — |

Lordships, which matter more here than usual:

| Graha | Rules | Sits in |
|---|---|---|
| Budha | **1 and 10** | 8th |
| Shukra | **2 and 9** | 8th |
| Mangal | 3 and 8 | 9th |
| Guru | 4 and 7 | 10th |
| Shani | 5 and 6 | 9th |
| Chandra | 11 | 9th |
| Surya | 12 | 8th |

**Eight of the nine grahas occupy three consecutive houses: 8, 9 and 10.**
Ketu in the 3rd is the sole exception. Houses 1, 2, 4, 5, 6, 7, 11 and 12 are
empty.

Because every house lord sits inside that block, the empty houses are not absent
from life — they are routed through it. Home and marriage (Guru) run through
career. Creativity and daily work (Shani) run through fortune and mentors.
Income (Chandra) runs through the same channel. Identity and career (Budha) are
one object, and both are buried in the 8th. **There is no separate compartment
for private life in this chart.**

---

## 3. The governing paradox

Three facts, each verified, that only make sense together:

**One.** Seven of the nine grahas sit in the 8th and 9th houses.

**Two.** Those same two houses carry **the two lowest Sarvashtakavarga totals in
the chart** — 21 and 22 against an average of 28.08 — and the 8th is dead last
in Bhava Bala at 7.00 rupas with **zero** aspectual support. Meanwhile the
**empty 6th house carries 41 bindus**, the highest by a margin of eight.

**Three.** The 8th house nonetheless holds **the lordships of houses 12, 1, 2, 9
and 10**, and with them the chart's entire raja-yoga apparatus: the
Dharma-Karmadhipati Yoga, a second kendra–trikona raja yoga, three dhana yogas,
and Vimala Yoga.

So: **the chart's greatest assets are buried in its poorest ground, and the
fertile ground is empty.**

That is not a contradiction to be resolved — it is the chart's actual structure,
and every other configuration restates it. The Mangal ⇄ Shukra parivartana welds
the best house to a dusthana. Vimala Yoga converts loss into gain. The exalted
Sun sits in the 8th and rules the 12th. The reading that follows is essentially
one proposition worked out in detail:

> **The difficulty and the fortune are the same object.**

Two practical consequences follow immediately, and they run through everything
below:

- **Effort concentrated where the grahas sit yields poorly.** Results come
  from the 6th house — competition, service, applied problem-solving — which is
  empty of grahas and rich in bindus.
- **The yogas are real but slow.** A raja yoga formed in the weakest bhava on
  the lowest-bindu ground delivers late, through obstruction, and in the domain
  of work rather than ease.

---

## 4. The self

### A lagna that repeats

Kanya rises at 27°37′, and **Kanya is also the lagna of D9 and of D11**.
Repetition of the ascendant across the rashi and navamsha is one of the more
reliable strength indicators available: the person he appears to be and the
person he is do not diverge much. Self-consistency rather than
self-contradiction.

Virgo supplies the working equipment — analysis, discrimination, diagnosis,
refinement, service, discomfort with the imprecise. Chitra pada 2 adds
craftsmanship; Chitra is the celestial artisan, and pada 2 falling in Virgo is
its most technically exacting quarter.

### A lagna lord that is under-resourced, and precisely how

Budha rules **both the 1st and the 10th** — an unusually tight fusion of
identity and vocation — and sits in the 8th, **combust**, 9°00′ from the Sun
against a 14° limit.

It is also **the only graha in the chart that falls below its Shadbala
minimum**: 6.46 rupas against 7.00 required, a ratio of 0.92, and net-malefic in
outcome (Ishta 18.91 against Kashta 30.32).

But the *shape* of that failure is the useful part:

| Component | Budha | Reading |
|---|---|---|
| Uchcha Bala | 8.49 | Only 25° from its debilitation point |
| **Dig Bala** | **4.28** | **The lowest of any graha, out of 60** |
| Sapta Vargaja | 90.00 | Joint-lowest |
| Nata-Unnata | **60.00** | Maximum |
| **Chesta Bala** | **42.15** | **Second-highest in the chart** |

Mercury earns directional strength in the 1st house and is sitting in the 8th,
so its Dig Bala is close to nothing — while its motional and temporal strength
are excellent.

**The failure is entirely positional, not intrinsic.** The chart's manager is
not badly made; he is badly placed. Faculties that depend on *where he stands* —
visibility, positioning, being in the right room — run at a deficit. Faculties
that depend on *how he thinks and moves* run at full strength. This distinction
recurs as the single most actionable finding in the whole reading.

Combustion adds its own note. Budha is burned not by an ordinary Sun but by one
in exaltation. The classical reading of a planet absorbed into a strong Sun is
assimilation rather than destruction: the intellect stops operating as a
separate performing faculty and fuses into the person's core authority.
Practically — someone whose thinking is inseparable from his sense of self, who
cannot do intellectual work he does not believe in, and whose ability surfaces
late and privately rather than early and publicly.

### The nakshatra chain closes on Ketu

Following each graha to the lord of the nakshatra it occupies:

```
Lagna → Chitra (Mangal) → Krittika (Surya) → Ashwini (Ketu)
      → Jyeshtha (Budha) → Ashwini (Ketu) ⟲ closed
```

The chain terminates in a **closed Ketu–Budha loop**. Nothing escapes it. At the
nakshatra level — which classical texts treat as more determinative than sign
placement — this chart is run by Ketu working through Mercury.

That is a precise signature: **detached, investigative, pattern-seeking
intelligence.** Ketu dissolves rather than accumulates; Budha analyses. Together
they describe someone who learns by taking things apart, is drawn to what is
hidden or discarded, works best alone, distrusts received explanations, and has
a pull toward the metaphysical that is forensic rather than sentimental. It also
describes someone not much interested in credentials for their own sake.

### Two gandanta placements

Gandanta is the knot at each water–fire junction — the last 3°20′ of a water
sign and the first 3°20′ of the fire sign following. Two bodies fall inside it:

- **Surya at 1°28′ Mesha.** Exalted *and* knotted on the same degree. Gandanta
  points at the significations of the planet it touches, and the Sun signifies
  father, authority, and one's own right to lead. Read plainly: **the
  relationship to authority — his father's and his own — is simultaneously his
  greatest source of strength and his deepest unresolved knot.** It tends to
  express as difficulty accepting authority above himself combined with
  reluctance to claim it openly, and it resolves through doing the depth work
  rather than through argument.
- **Ketu at 26°55′ Vrischika**, Jyeshtha pada 4 — the classical gandanta pada.
  Combined with the Ketu-terminated nakshatra chain, this makes the
  spiritual and investigative drive load-bearing rather than incidental, and
  gives it a knot of its own.

---

## 5. The grahas, by strength

Every figure below reconciles against the supplied Shadbala.

| Graha | Rupas | Req. | Ratio | Rank | Ishta | Kashta | **Net** | Shodhya |
|---|---|---|---|---|---|---|---|---|
| **Surya** | 11.39 | 5.00 | **2.28** | 1 | 46.88 | 7.83 | **+39.05** | 138 |
| Shani | 6.39 | 5.00 | 1.28 | 2 | 12.48 | 46.83 | **−34.35** | 184 |
| Mangal | 6.33 | 5.00 | 1.27 | 3 | 19.66 | 38.87 | −19.21 | **212** |
| Guru | 8.21 | 6.50 | 1.26 | 4 | 37.30 | 15.10 | +22.20 | 81 |
| Shukra | 6.68 | 5.50 | 1.21 | 5 | **47.49** | 11.87 | +35.62 | 95 |
| Chandra | 6.42 | 6.00 | 1.07 | 6 | 24.54 | 4.49 | +20.05 | **33** |
| **Budha** | 6.46 | 7.00 | **0.92** | 7 | 18.91 | 30.32 | −11.41 | 152 |

**Surya — the chart's engine.** At 2.28× requirement it is nearly twice as
strong relative to requirement as anything else, with a Sapta Vargaja Bala of
165 (the highest single component in the table, against 120 for the next) and
the best outcome balance of any graha. It holds dignity in six of the seven
vargas supplied. One honest caveat on that count: sitting at only 1°28′ of
Mesha, the Sun keeps mapping back into Aries in low-numbered divisions, so part
of it is arithmetic — but the classical system scores it at full value
regardless. **Both the strongest and the most benign influence in the chart.**

**Shukra — the pivot.** Highest Ishta Phala of all seven (47.49), net +35.62,
and — as §6 shows — the graha through which *both* of the chart's major yogas
run. After Surya, the most consequential graha here for outcomes. This is not
obvious from sign placement alone; it emerges only when the yogas and the
strength data are read together.

**Guru — strong but obstructed.** Rank 4 by ratio, second-highest rupas, good
outcome balance. But it carries **the worst Drik Bala in the chart at −8.58** —
by a wide margin the most aspect-afflicted graha — sits in an enemy's sign, and
has Yama Ghantaka 2°05′ away. Whatever Guru gives, it gives with interference
attached.

**Shani — strong and harsh at once.** Rank 2 in strength, **worst outcome
balance in the chart** (net −34.35). These measure different things: strength is
capacity to deliver, Ishta/Kashta is whether delivery is pleasant. Saturn will
absolutely produce results here, and producing them will hurt.

**Mangal — forceful.** A milder version of Saturn's shape (net −19.21), but with
**the highest Shodhya Pinda in the chart at 212**, meaning Mars periods deliver
substantially — forcefully rather than gently. Mitigated by falling in
**Pushkara navamsa** (7°19′ Vrishabha, inside the 6°40′–10°00′ span), with its
navamsha in Meena, Guru's sign. This is the one clean mitigator inside an
otherwise harsh 9th-house cluster, and it matters because Mangal is half the
central parivartana.

**Chandra — high quality, low quantity.** This requires care, because sign
dignity and actual strength point opposite ways. The Moon is exalted at 1°47′
Vrishabha, within 1°13′ of its deep exaltation point. But:

1. Shadbala ratio **1.07** — second-weakest in the chart.
2. Paksha Bala **20.21** of a possible 120, because birth falls 2.5 days after
   the new moon: dignified by sign, nearly empty of light.
3. **Two bindus** in its own sign in the Chandra Ashtakavarga.
4. **Shodhya Pinda of 33** — less than half the next-lowest — with a Graha Pinda
   of exactly **zero**.

Four independent measures agree. The exaltation is real, and the Kashta Phala of
4.49 is the lowest in the chart, so the Moon does very little harm. **But the
reserves are thin.** A mind fine in kind and limited in quantity. Its nakshatra
lord is Surya — exalted, in the 8th, gandanta — so the emotional life is pulled
toward depth and meaning and destabilises when the belief system does. There is
also a genuine **Chandra–Mangal yoga** (5°32′ separation): wealth through
enterprise, and emotional heat.

**Budha — the weak link.** Covered in §4. Only graha below minimum; failure is
positional.

---

## 6. The yogas

### Dharma-Karmadhipati Yoga — the chart's only raja yoga

The 9th house is Vrishabha, ruled by **Shukra**. The 10th is Mithuna, ruled by
**Budha**. Both sit in Mesha, **13°09′ apart in the same sign**. The lord of
dharma and the lord of karma directly conjunct:

> **Dharma-Karmadhipati Yoga, formed by conjunction, in the 8th house.**

Conjunction is the strongest of the three modes of formation, ahead of mutual
aspect and exchange. A systematic sweep of every kendra lord against every
trikona lord confirms something worth stating plainly: **this is the only
kendra–trikona raja yoga in the entire chart.** Budha–Shani, Guru–Shani and
Guru–Shukra all fail to connect by conjunction, aspect or exchange. Everything
in the raja-yoga class rests on this single conjunction.

**It carries more than the DKY.** Budha rules 1 and 10; Shukra rules 2 and 9. A
single conjunction fuses four lordships:

| Pairing | Yoga |
|---|---|
| 9 + 10 | **Dharma-Karmadhipati Yoga** |
| 1 + 9 | Kendra–trikona raja yoga |
| 2 + 9 | Dhana yoga — wealth through fortune |
| 2 + 10 | Dhana yoga — wealth through profession |
| 1 + 2 | Dhana yoga |

**But it is conditional**, and the conditions are stark:

| Supporting | Limiting |
|---|---|
| Formed by conjunction — the strongest mode | Formed **in the 8th**, a dusthana |
| Shukra holds the highest Ishta Phala in the chart | Budha is combust, fails Shadbala, has the lowest Dig Bala, and is net-malefic |
| Compounded with four further raja/dhana lordships | The 8th is **Bhava rank 12** with the **lowest SAV (21)** |
| **Echoed cleanly in D10** | **Absent in D9** — the 9th lord goes to the 3rd, the 10th lord to the 11th, unconnected |

The dharma half is strong and benign; the karma half is the chart's weakest
link; and the whole structure is built on its poorest ground. The missing
navamsha echo is the most serious limitation — a yoga that does not repeat in D9
delivers, but does not compound.

**The D10 echo is the good news.** In the dashamsha the lagna is Kumbha, making
Tula the 9th house — ruled by Shukra — and Shukra sits at 26°08′ Vrischika,
which is the **10th house of D10**, in a kendra. The source table states it
directly: Shukra "rules 4, 9 Bhava" and "is in 10 Bhava." So the 9th lord of the
career chart occupies the 10th house of the career chart.

Weak in the navamsha, strong in the dashamsha, which is precise: **this yoga
delivers in the domain of work and public role, not in inner life or marriage.**

### Mangal ⇄ Shukra parivartana — the spine

Mangal rules the 8th and sits in the 9th; Shukra rules the 9th and sits in the
8th. This is the chart's **only** parivartana, and it welds the best house to
the most difficult one. Read in both directions:

- **Fortune arrives through the 8th.** Not as smooth good weather, but as the
  crisis that turns out to be the opening, the obscure subject that becomes the
  career, the resource that comes through someone else's capital.
- **The 8th is dharmically protected.** Research, investigation, psychology,
  surgery, forensics, insurance, risk, security — depth work is the assigned
  path, and it carries the 9th house's protection.

Note that **Shukra is half of this exchange and half of the DKY**. Both of the
chart's major yogas run through the same graha — the one with the highest Ishta
Phala. That convergence is the strongest single positive signal available.

### Vimala Yoga

Surya rules the 12th and occupies the 8th — a 12th lord in a dusthana, forming
**Vimala Yoga**, one of the Vipreeta Raja Yogas. Adversity inverts into
advantage; expenses stay contained; independence comes naturally; the rise
follows the setback that would sink someone else. And the 12th is, by Bhava
Bala, **the strongest house in the chart** (§7).

### Amala Yoga

Guru, a benefic, in the 10th from lagna: clean reputation, fair dealing, a name
that holds up. Qualified three ways — enemy's sign, dispositor combust in the
8th, and Yama Ghantaka 2°05′ away — plus the worst Drik Bala in the chart.
Reputation here is earned rather than granted, and arrives with friction.

### In the vargas

- **D8: Mangal ⇄ Shani exchange** — exalted Mars in Makara trading with
  debilitated Saturn in Mesha, producing **neechabhanga** for Shani. Under
  adverse periods the worst case carries a built-in cancellation.
- **D11: Guru ⇄ Chandra exchange**, with Guru **exalted in the 11th** of the
  gains chart alongside Budha. The strongest single configuration in the entire
  varga set.

### Absent, and worth knowing

- **No Panchamahapurusha yoga.** No graha meets the own-or-exalted-in-kendra
  requirement. There is no overwhelming "great person" signature.
- **No Gaja Kesari.** Guru is 2nd from Chandra, not in a kendra from it.
- **Only one graha in a kendra at all** (Guru in the 10th). Kendras are the
  chart's structural pillars and here they are nearly vacant. This is the main
  structural weakness: enormous depth, very little scaffolding — and the fix is
  behavioural, not astrological.

---

## 7. The houses

### Bhava Bala and Ashtakavarga together

| House | Bhava rupas | Rank | SAV | Lord |
|---|---|---|---|---|
| **XII** | **12.59** | **1** | 24 | Surya |
| IV | 9.28 | 2 | 29 | Guru |
| II | 9.18 | 3 | 24 | Shukra |
| VII | 8.86 | 4 | **33** | Guru |
| I | 8.39 | 5 | 29 | Budha |
| V | 7.91 | 6 | 29 | Shani |
| IX | 7.61 | 7 | **22** | Shukra |
| III | 7.49 | 8 | 28 | Mangal |
| X | 7.39 | 9 | 29 | Budha |
| VI | 7.21 | 10 | **41** | Shani |
| XI | 7.08 | 11 | 28 | Chandra |
| **VIII** | **7.00** | **12** | **21** | Mangal |

The two metrics measure different things and should be read together: Bhava Bala
is largely inherited from the house lord's own strength, while SAV measures
benefic-point density — how productively that ground yields.

**The 12th is the strongest house**, outranking second place by 36%. Its
strength comes almost entirely from Surya's 683.48 contribution while its own
SAV is a modest 24 — so it is **powered by the Sun specifically rather than
broadly fertile**. Its strength flows through solar significations and through
the 12th's own domain: foreign lands, seclusion, retreat, release. Read
alongside Rahu in the 9th and the Ketu–Budha nakshatra loop, **the thread
running through foreign residence, withdrawal, and work done away from the
public eye is the chart's strongest single structure.**

**The 6th is the most productive territory.** 41 bindus, highest by eight, in a
house holding no grahas. The 6th governs service, competition, problem-solving,
disciplined labour, adversaries overcome. A 41-bindu 6th says about as loudly as
this system says anything: **he wins through the 6th house** — out-working,
out-lasting and out-analysing the opposition. Note also that **Kumbha is
simultaneously the D10 ascendant**: two independent techniques naming the same
sign.

**The 8th is weakest on both measures** — rank 12, lowest SAV, zero aspectual
support — while holding three grahas and all the raja yogas. This is §3's
paradox in its sharpest form.

**The 2nd is unusually well supported**: rank 3, and **the highest Drishti Bala
in the chart at +99.83**, because Surya, Budha and Shukra all aspect it from the
8th. Its lord holds the highest Ishta Phala.

**The 7th is well built**: rank 4, and 33 bindus — second-highest SAV. Its lord
Guru is the second-strongest graha. The difficulty in this area (§10) comes from
its *occupants and aspects*, not from the house itself. Its Drishti Bala of
+8.59 is second-lowest, so little aspectual help arrives.

**The 11th is rank 11** with Gulika and Mandi both in it — the weakest point in
the wealth picture.

### Aspects

| Graha | From | Aspects houses |
|---|---|---|
| Mangal | 9th | 3, 4, 12 |
| Guru | 10th | 2, 4, 6 |
| Shani | 9th | 3, 6, 11 |
| Rahu | 9th | 1, 3, 5 |
| Ketu | 3rd | 7, 9, 11 |
| Surya · Budha · Shukra | 8th | 2 |
| Chandra | 9th | 3 |

**The 3rd house takes almost everything** — Ketu occupies it while Mangal, Shani
and Chandra all aspect it. Courage, initiative, communication, self-generated
skill. This is the chart's real working house and its pressure valve: effort
put into *skill and output* pays disproportionately.

**Rahu aspects the lagna** from the 9th, and Rahu runs the current mahadasha —
identity is under active reconstruction across the whole 2022–2040 span.

**Guru aspects the 6th**, which is protective for health, debts and adversaries —
a genuine safety net in a chart carrying this much load.

---

## 8. The divisional charts

**D9 (Navamsha) — lagna Kanya, vargottama with D1.** Surya exalted again in the
8th. **Rahu conjoins the lagna** within 6°, while **Mangal and Ketu occupy the
7th** — a heavily loaded 1/7 axis. Guru, the 7th lord, falls in the 6th: friction
and service inside partnership. Shani sits in the **10th**, a strong career
placement. The DKY does not survive here.

**D10 (Dashamsha) — lagna Kumbha, lord Shani in the 5th.** Shukra in the 10th in
Vrischika, forming the DKY echo. Surya exalted in the 3rd. **Rahu in the 8th** —
unconventional, non-linear career turns, research and foreign involvement. Five
grahas sit at 26–29° of their signs, reading as **discontinuity**: a career
assembled from discrete moves rather than internal promotion.

**D11 (Rudramsha) — lagna Kanya again.** **Guru exalted in the 11th** with Budha
alongside, in **parivartana with Chandra**. Structurally the strongest varga in
the set for gains through knowledge, advisory and networks. Counterweight: **both
nodes debilitated**, in the 4th and 10th — instability in the *base* from which
gains are made.

**D8 (Ashtamsha) — lagna Meena.** Mangal exalted in the 11th (joined by Ketu
once corrected); Shani debilitated in the 2nd but **neechabhanga** via the
Mangal ⇄ Shani exchange. Shukra in own sign and mooltrikona in the 8th.

**D27 (Bhamsha) — lagna Karka.** Mangal, Budha, Shukra and Ketu all in the 7th,
with Rahu in the lagna — the 1/7 axis loading of D9 repeated. Mangal exalted.

**D30 (Trimshamsha) — lagna Vrischika.** Surya exalted in the 6th — good for
overcoming adversity and disease. Guru in own sign in the 2nd. **Chandra in
mooltrikona in the 7th, conjunct Ketu within 4°** once the source error is
corrected.

---

## 9. Upagrahas

| Upagraha | Position | House | Contact |
|---|---|---|---|
| **Yama Ghantaka** | 12°42′ Mithuna | 10 | **2°05′ from Guru** |
| Mrityu | 26°49′ Mesha | 8 | 3°13′ from Shukra |
| Parivesha | 15°12′ Vrishabha | 9 | 2°42′ from Shani |
| Ardha Prahara | 20°48′ Vrishabha | 9 | 2°53′ from Shani |
| Gulika · Mandi | 25°16′ · 22°22′ Karka | 11 | — |
| Kala | 10°09′ Kanya | 1 | — |
| Dhuma | 14°48′ Simha | 12 | — |
| Vyatipata | 15°12′ Vrischika | 3 | — |
| Indra Chapa | 14°48′ Kumbha | 6 | — |
| Upaketu | 01°28′ Meena | 7 | — |

The significant one is **Yama Ghantaka on Guru** — the chart's only kendra
graha, its Amala yoga giver, and its 4th and 7th lord, all one body carrying a
shadow point 2° away. This is the technical reason the reputation yoga does not
run clean, and it reinforces the partnership reading independently. **Gulika and
Mandi in the 11th** shadow the gains house, pairing with the debilitated nodes
in D11. **Upaketu in the 7th** adds to the detachment signature there.

---

## 10. Life areas

### Career

**Field.** Six indicators converge: Kanya lagna (analysis, diagnosis,
precision); D10 lagna Kumbha with Shani as lord (technology, large systems,
structure); the 6th house at 41 bindus (competition, troubleshooting, applied
problem-solving); Shukra in Vrischika on D10's 10th (finance, risk, insurance,
investigation, data); Rahu in D10's 8th (research, protected data, audit,
security, foreign work); and the Ketu–Budha nakshatra loop (forensic,
first-principles investigation).

**Technical and analytical work with an investigative edge** — the kind of role
where he is handed something broken, opaque or contested and made responsible
for resolving it. Aquarius–Scorpio territory, not a general management track.

**Mechanism.** The 10th house is unremarkable — Bhava rank 9, SAV 29 — with the
chart's only failing graha as its lord, and the kendras are nearly empty. There
is no inherited platform and no easy appointment mechanism. What there *is* is
the 41-bindu 6th and Amala Yoga: **advancement through demonstrated competence
and accumulated reputation, not position or patronage.** The Amala asset is a
*stock*, not a *flow* — it builds quietly for years before it pays.

**Shape.** Discontinuous. Discrete moves between roles and places, not one
ladder. And with Budha combust, **visibility lags ability**, persistently and by
design.

**Authority — what kind.** Surya, the karaka of authority and by far the
strongest graha here, sits in the 8th while ruling the 12th. There is no
Panchamahapurusha yoga. So: not administrative command over large numbers, but
**authority of the expert and the trusted advisor** — a technical or research
lead, a principal, the head of a function, someone whose judgement is decisive
within a domain. With a persistent behind-the-scenes quality: strongest house
the 12th, authority karaka in the 8th, Rahu in the 8th of D10.

### Wealth

Mixed, with an unusual mechanism, and better than the 8th-house placement alone
suggests.

The 2nd lord in the 8th is poor for linear accumulation from salary and good for
**inheritance, partner's resources, capital originating outside himself,
insurance**, with real windfall and loss volatility. But the **2nd house itself
is Bhava rank 3 with the highest Drishti Bala in the chart**, and its lord Shukra
holds the highest Ishta Phala — so the capacity is genuinely well supported. It
simply arrives through 8th-house channels. Three dhana yogas sit in the same
conjunction that forms the DKY.

The 11th lord Chandra is exalted in the 9th: gains via mentors, teaching,
publishing, foreign connections. **D11 is structurally strong** — Guru exalted
in the 11th, in parivartana with Chandra.

**The genuine caution is the gains house itself**: 11th at Bhava rank 11, with
Gulika and Mandi in it, and both nodes debilitated in D11. High gain capacity,
weak gains house. Income arrives through the specific channels D11 indicates —
knowledge, advisory, networks — rather than accumulating broadly. This argues
strongly against leverage and speculation.

### Partnership

The signal is consistent across five charts, and needs stating in both
directions.

**The difficulty.** In D1 the 7th is empty and its only aspect is **Ketu's**;
its lord Guru sits in the 10th in an enemy's sign, 2° from Yama Ghantaka, with
Upaketu in the 7th itself. In **D9**, Mangal and Ketu occupy the 7th while Rahu
conjoins the lagna. In **D27**, four bodies sit in the 7th, Rahu again in the
lagna. In **D30** (corrected), Chandra conjoins Ketu within 4° in the 7th. He is
**partially Manglik** — not from the lagna, but Mangal is 1st from Chandra and
2nd from Shukra. And in D9 the 7th lord falls in the 6th.

**Ketu touching the 7th in four separate vargas is a detachment signature** — a
tendency to be present without fully arriving, and to find the thing obtained is
not the thing wanted. This is structural, not situational.

**The support.** The 7th house is **Bhava rank 4** with **33 bindus, the
second-highest SAV in the chart**, and its lord is the second-strongest graha.
D30 gives Chandra its own mooltrikona there.

**The honest composite: a well-built house with a difficult tenant.**
Partnership is not structurally weak here — it is structurally sound and
karmically complicated, which is a materially different and more workable
proposition. It responds to deliberate choice rather than drift. Early or
conventionally-timed partnership is ill-advised; later and consciously chosen
does substantially better, because the detachment pattern needs to become
conscious before it can be worked with rather than merely acted out. The partner
indicated is met through work, public life or travel, and is someone who can
hold both intensity and independence.

### Health and constitution

Sound but not robust. The exalted Moon and Guru's aspect on the 6th are
protective; against them, a Virgo lagna with a **combust, Shadbala-failing lord
in the 8th**, and a Moon thin by four independent measures.

Virgo pathology is digestive and neurological and it is stress-mediated; Shani
ruling the 6th reads as chronic and low-grade rather than acute. The practical
form: **the system has limited reserves, runs hot on analysis, and has no
automatic off-switch.** Rest and routine are structural requirements here, not
lifestyle preferences — this is a primary finding, not a footnote.

---

## 11. The timeline

### Mahadasha sequence

| Mahadasha | Dates | Ages |
|---|---|---|
| **Rahu** | Dec 2022 – Dec 2040 | 20.7 – 38.7 |
| **Guru** | Dec 2040 – Dec 2056 | 38.7 – 54.7 |
| Shani | Dec 2056 – Dec 2075 | 54.7 – 73.7 |

**The Rahu mahadasha covers his entire career-forming span.** Rahu sits in the
9th, aspects the lagna, and keeps company with exalted Chandra, Mangal and
Shani — unorthodox mentors, foreign exposure, higher education approached at an
angle, and a relationship to tradition that is engaged but not obedient.

**The Guru mahadasha is the structural answer to the career question.** Guru is
the graha *occupying the 10th house* and giving Amala Yoga; its sixteen years
run across ages 39 to 55, precisely the decades when professional authority
matures. **This is a late-cresting chart** — and that is consistent with
everything else: a combust lagna lord means ability surfaces late; Vimala Yoga
means the rise follows adversity; the 8th–9th exchange means fortune arrives
through difficulty; and the DKY sits on the weakest ground so it delivers slowly.

The practical consequence matters more than the prediction. Measured at 28 or 32
against peers on conventional ladders, he will read as behind — and by those
metrics he will *be* behind. **That comparison is measuring the wrong window.**

### Graha maturity — an independent confirmation

Each graha has a **paripaka** or maturity age, before which it delivers its
significations rawly and after which it delivers them integrated. Laid against
this chart's dasha sequence, the standard ages produce a striking result.

| Graha | Matures at | Date |
|---|---|---|
| Guru | 16 | Apr 2018 |
| Surya | 22 | Apr 2024 |
| **Chandra** | **24** | **Apr 2026** |
| **Shukra** | **25** | **Apr 2027** |
| Mangal | 28 | Apr 2030 |
| Budha | 32 | Apr 2034 |
| Shani | 36 | Apr 2038 |
| Rahu | 42 | Apr 2044 |
| Ketu | 48 | Apr 2050 |

Now check each mahadasha lord against its own period:

| Mahadasha | Ages | Lord matures at | Status during its own period |
|---|---|---|---|
| **Rahu** | 20.7–38.7 | **42** | **Never matures — it ripens 3.3 years *after* its own mahadasha ends** |
| **Guru** | 38.7–54.7 | 16 | Mature **22.7 years** before the period begins |
| **Shani** | 54.7–73.7 | 36 | Mature **18.7 years** before the period begins |

**The entire Rahu mahadasha — the whole construction phase, ages 20.7 to 38.7 —
is governed by a graha that never matures within it.** Rahu ripens at 42, in
2044, by which time the Guru mahadasha is already four years old.

This is an independent mechanism for something the strength data showed but did
not explain: why a period packed with activity yields so little visible return.
It is not only that the 8th and 9th are low-bindu ground. It is that the dasha
lord itself is operating raw for its entire tenure — amplified desire without
integration, which is precisely the classical description of unripened Rahu.

And the sequence then improves monotonically: **immature → long-mature →
long-mature.** By the time the Shani mahadasha opens, Saturn has been mature for
nearly nineteen years, and has already had a substantial matured run as
Guru–Shani (Feb 2043 – Aug 2045). The Shani mahadasha does not have to ripen its
own lord; it inherits one already integrated.

**This materially strengthens the upward reading of the Shani period.** Saturn's
low Uchcha and Chesta Bala make it coarse, but a matured Saturn expresses as
endurance, structure, authority through service and accumulated competence —
which is exactly what its 5th/6th/9th rulership from the 9th house describes.

Two smaller observations from the same table:

- **Rahu–Budha (ages 28.6–31.2) runs entirely before Budha matures at 32.** The
  chart's only Shadbala-failing graha runs its own antardasha while still
  unripened. That compounds every other reason 2030–2033 is the vulnerable
  stretch.
- **Chandra matured in April 2026 and Shukra matures in April 2027** — both
  inside the current Rahu–Guru antardasha. The Moon is the chart's thin point by
  four independent measures, and it ripens now. Shukra is the pivot of both
  major yogas and the natural karaka of marriage, and it ripens in the middle of
  the marriage window identified in §12.

*(Paripaka is a genuine classical technique but a secondary one — it modulates
dasha and bala rather than overriding them, and the exact ages vary slightly
between traditions. It is used here as corroboration, not as a primary
argument.)*

### Rahu antardashas

| Period | Dates | Ages | Reading |
|---|---|---|---|
| Rahu–Rahu | Dec 2022 – Sep 2025 | 20.7–23.4 | The disoriented launch — ambition without direction, false starts. Past. |
| **Rahu–Guru** | **Sep 2025 – Jan 2028** | **23.4–25.8** | **Current.** Guru rules the 4th and 7th (Bhava ranks 2 and 4) from the 10th. First real professional standing; mentor, credential, reputation; marriage and home. Doubly activated — Guru sits in Rahu's nakshatra while Rahu's sub-lord is Guru. Caveat: worst Drik Bala in the chart, and Guru falls in D9's 6th. **Rewards narrowing, not adding.** |
| **Rahu–Shani** | Jan 2028 – Dec 2030 | 25.8–28.6 | **The foundation.** Shani is D10's lagna lord, sits in D9's 10th, and rules the 41-bindu 6th — three career credentials, all Saturn's. Rank 2 in strength, worst outcome balance in the chart. It will deliver, and it will cost. |
| **Rahu–Budha** | Dec 2030 – Jun 2033 | 28.6–31.2 | **The vulnerable stretch, and the strategic hinge.** The only failing graha, net-malefic, lowest Dig Bala, running its own 2.5 years over self and career. Saturn return lands here. Also the DKY's *karma* half — construction, not payoff. |
| Rahu–Ketu | Jun 2033 – Jul 2034 | 31.2–32.2 | Short and destabilising, Ketu gandanta in the 3rd. Consolidate and withdraw; poor for launching. |
| **Rahu–Shukra** | Jul 2034 – Jul 2037 | 32.2–35.2 | **Material peak of the mahadasha.** Highest Ishta Phala, rules the 2nd (rank 3) and 9th, and is the DKY's *dharma* half. |
| Rahu–Surya | Jul 2037 – Jun 2038 | 35.2–36.1 | Short but excellent — strongest and most benign graha ruling the strongest house. Recognition through foreign or behind-the-scenes channels. |
| Rahu–Chandra | Jun 2038 – Dec 2039 | 36.1–37.6 | Gentle, low harm, but low yield (Shodhya Pinda 33). |
| Rahu–Mangal | Dec 2039 – Dec 2040 | 37.6–38.7 | Forceful. Highest Shodhya Pinda with a heavily negative outcome balance — a disruptive transition right at the dasha junction. |

### Guru mahadasha — where the chart pays out

| Period | Dates | Age |
|---|---|---|
| Guru–Guru | Dec 2040 – Feb 2043 | 38.7 |
| Guru–Shani | Feb 2043 – Aug 2045 | 40.8 |
| **Guru–Budha** | Aug 2045 – Dec 2047 | 43.4 |
| Guru–Ketu | Dec 2047 – Nov 2048 | 45.6 |
| **Guru–Shukra** | **Nov 2048 – Jul 2051** | **46.6** |

**Guru–Budha and Guru–Shukra are the DKY's two halves running inside the
mahadasha of the graha that occupies the 10th house.** Guru–Shukra (2048–2051)
is likely the fullest expression of the yoga in the whole life. The DKY does not
deliver its best inside the Rahu period at all — it waits.

### Shani mahadasha — Dec 2056 to Dec 2075, ages 54.7 to 73.7

Nineteen years, and the natal Shani that governs them is the chart's clearest
example of **strong and harsh being different measurements**.

| Measure | Shani | Standing |
|---|---|---|
| Shadbala ratio | 1.28 | **Rank 2 of 7** |
| Sapta Vargaja Bala | 120.00 | **2nd highest** |
| Shodhya Pinda | 184 | **2nd highest** |
| Dig Bala | 43.24 | **2nd best** |
| **Ishta / Kashta** | 12.48 / 46.83 | **Net −34.35 — worst in the chart** |
| Uchcha Bala | 9.30 | Low — ~28° from its debilitation point |
| Ayana Bala | 3.98 | Very low |
| Own bindus in Vrishabha | 2 | Low |

It is also unusually well credentialed for delivering results:

- It **rules the 6th house — the chart's 41-bindu high point**, the most fertile
  ground available.
- It **aspects that same 6th house** by its 10th aspect from the 9th, so the
  strongest house in the chart is both ruled and aspected by the dasha lord.
- In **D9 it occupies the 10th**; in **D10 it is the lagna lord**.
- It also aspects the 3rd (effort and skill) and the 11th (gains).

So the capacity is real and the credentials are genuine.

#### What the Kashta figure actually measures — and what it does not

This matters enough to state precisely, because it is easy to over-read.
Ishta and Kashta Phala are derived from **only two** of the six balas:

```
Ishta  = √(Uchcha × Chesta)
Kashta = √((60 − Uchcha) × (60 − Chesta))
```

Verified against all seven grahas in the supplied table — it reproduces every
figure exactly. So Shani's worst-in-chart Kashta of 46.83 comes entirely from
its **Uchcha Bala of 9.30** (it sits ~28° from its debilitation point) and its
**Chesta Bala of 16.75** (slow motion). Neither quantity measures capacity to
produce outcomes in the world. Shani's *positional* (174.30), *directional*
(43.24), *temporal* (143.65) and *varga* (120.00) strengths are all solid.

**The Kashta figure describes how the period feels, not what it produces.**
Coarse, effortful, slow, unglamorous — but not unproductive.

And on production specifically, the comparison with the preceding mahadasha is
striking:

| | Shodhya Pinda |
|---|---|
| **Shani** | **184** — 2nd highest in the chart |
| **Guru** | **81** — 2nd lowest |

**Shani carries 2.3× Guru's delivery capacity.** So the Guru mahadasha is where
*recognition and quality* arrive; the Shani mahadasha is where the largest
*volume* of concrete results is delivered. They are peaks in different
currencies, not a peak followed by a decline.

#### What the period is about

Shani rules the **5th and 6th** and sits in the **9th**. Read together at ages
55 to 74, that is a recognisable configuration: children and students (5th),
service, obligation and health (6th), expressed through dharma, teaching and
mentorship (9th).

**This is the teaching and legacy period** — carrying and passing on what the
Guru mahadasha built. Saturn in the 9th is the elder's placement. And because
Shani is D9's tenth-house occupant and D10's lagna lord, **professional identity
stays central right through to 74.** This mahadasha is not a wind-down.

The sequence across the three mahadashas is coherent:

> **Rahu (21–39) builds it. Guru (39–55) is paid for it. Shani (55–74) carries
> it and hands it on.**

#### Two Saturn cycles land on top of it

| Cycle | Timing | Falls in |
|---|---|---|
| **Sade Sati #2** | ~2057 – ~2065 | The **first seven years** of the mahadasha |
| **Second Saturn return** | ~2060 | Shani–Budha |

The mahadasha opens almost exactly as the second Sade Sati begins. Ages **55 to
63 therefore stack three Saturn signatures at once** — Shani mahadasha, Sade
Sati, and the Saturn return.

Note the symmetry with the first half of life: Sade Sati #1 (2027–2035)
overlapped the Rahu–Shani antardasha, and Sade Sati #2 overlaps
Shani–Shani and Shani–Budha. **Both of this chart's Saturn-heavy periods
coincide with a Sade Sati.** That doubling is a genuine structural feature, and
it is why Saturn reads so much heavier here than its rank-2 strength alone
suggests.

#### Antardashas

| Period | Dates | Ages | Reading |
|---|---|---|---|
| **Shani–Shani** | Dec 2056 – Dec 2059 | 54.7–57.7 | **The hardest single stretch in the timeline.** Saturn's own sub-period, worst Kashta in the chart, opening into Sade Sati. |
| **Shani–Budha** | Dec 2059 – Sep 2062 | 57.7–60.4 | The failing graha ruling self and career, plus the **second Saturn return**. Identity, career and health pressure together. |
| Shani–Ketu | Sep 2062 – Oct 2063 | 60.4–61.5 | Detachment and withdrawal; Sade Sati releasing. Poor for new commitments. |
| **Shani–Shukra** | Oct 2063 – Dec 2066 | 61.5–64.7 | **The best stretch of the mahadasha.** Highest Ishta Phala in the chart, the DKY's dharma half, ruling the 2nd and 9th — and it arrives just as Sade Sati ends. |
| Shani–Surya | Dec 2066 – Nov 2067 | 64.7–65.6 | Short and strong. Best outcome balance in the chart, ruling the strongest bhava. |
| Shani–Chandra | Nov 2067 – Jun 2069 | 65.6–67.2 | Gentle and low-harm, but low-yield. |
| Shani–Mangal | Jun 2069 – Aug 2070 | 67.2–68.3 | Forceful and difficult — highest Shodhya Pinda with a negative outcome balance. |
| **Shani–Rahu** | Aug 2070 – Jun 2073 | 68.3–71.2 | Activates the natal **Shani–Rahu conjunction in the 9th**. The mirror of Rahu–Shani in 2028–2030, forty-two years later — the same conjunction, opposite order. The first built the career foundation; this one likely marks its final transformation or handing over. |
| Shani–Guru | Jun 2073 – Dec 2075 | 71.2–73.7 | Guru in the 10th, Amala Yoga. A dignified close to the period. |

#### Health during this mahadasha

This needs stating plainly and then qualifying, because both halves are true.

Shani rules the 6th, carries the chart's highest Kashta Phala, and its mahadasha
opens onto Sade Sati and a Saturn return. Against a Virgo lagna with a
Shadbala-failing lord and a thin Moon, **ages 55 to 63 are the period this chart
most requires health attention** — chronic and low-grade in character rather
than acute, consistent with Saturn.

**The qualifier matters as much.** The 6th house is the house of disease *and*
of triumph over it, and here its lord is the second-strongest graha ruling the
chart's highest-bindu house and aspecting it as well. A strong 6th lord means
difficulties are fought successfully rather than avoided. **Load is high;
resilience is also high.** The reading is demanding, not ominous.

*(After Shani, the Budha mahadasha opens in Dec 2075 at age 73.7 — the lagna
lord's own period, and the chart's weakest graha.)*

### Sade Sati

Saturn currently transits Meena, the **11th from the natal Moon** — one of the
most favourable positions in gochara. **He is not in Sade Sati.** It begins when
Saturn enters Mesha, in roughly the **second half of 2027**, and runs to ~2035.

Its severity is measurable. Saturn's own bindus across the three Sade Sati
signs:

| Sign | Natal house | Shani's bindus |
|---|---|---|
| Mesha | 8th | 3 |
| Vrishabha | 9th | 2 |
| **Mithuna** | **10th** | **1** |

**The final phase crosses the natal 10th house, where Saturn holds a single
bindu — the weakest planet-sign cell in the entire Ashtakavarga.** That falls
around 2032–2035, and it is the mechanism behind the late-cresting career:
career visibility is structurally suppressed during exactly the years he would
conventionally expect to climb.

**The hardest convergence in the first half of life is ~2030–2032**: Sade Sati's
peak phase over the natal Moon, *plus* the Rahu–Budha antardasha of the failing
lagna lord, *plus* the Saturn return.

The second Sade Sati (~2057–2065) repeats the pattern against the Shani
mahadasha — see above. Both of this chart's Saturn-heavy stretches carry a Sade
Sati on top of them.

---

## 12. Current transits

> **Dated snapshot: 8 August 2026.** Unlike everything above, this section reads
> a moment. The Sun at 21°35′ sidereal Karka dates the transit chart to 6–8
> August 2026.

| Transit | Sign | From lagna | From Moon | Own bindus | Sign SAV |
|---|---|---|---|---|---|
| Surya | Karka | 11th | 3rd | 3 | 28 |
| Chandra | Vrishabha | 9th | 1st | 2 | 22 |
| Mangal | Mithuna | **10th** | 2nd | 4 | 29 |
| Budha | Karka | 11th | 3rd | 2 | 28 |
| **Guru** *(combust)* | Karka | 11th | 3rd | **5** | 28 |
| Shukra | Kanya | **1st** | 5th | **5** | 29 |
| **Shani** | Meena | **7th** | **11th** | **5** | **33** |
| **Rahu** | Kumbha | **6th** | 10th | — | **41** |
| Ketu | Simha | 12th | 4th | — | 24 |

Three slow transits — Guru, Shukra and Shani — each carry **5 bindus**, above the
classical 4-bindu threshold at which a transit is held to deliver. These are
supported transits, not merely present ones.

### Marriage — the window is open now

Three independent activators of the 7th house are running simultaneously, which
is the classical signature for marriage timing:

1. **The antardasha lord is the 7th lord.** Guru rules the 7th, and Rahu–Guru
   runs to **31 January 2028**.
2. **Transit Shani sits in the natal 7th** — Meena — with 5 bindus, in the
   chart's second-highest-bindu house. It leaves in the second half of 2027.
3. **Transit Guru, exalted in Karka, aspects the natal 7th** by its 9th aspect.
   Jupiter remains in Karka until roughly mid-2027.

Supporting these: **transit Shukra — the natural karaka of marriage, and the
graha with the highest Ishta Phala in this chart — is in the natal lagna**, and
Sade Sati has not begun.

One timing detail: transit Guru is **currently combust**, 7°24′ from the Sun
against an 11° limit. The Sun pulls away at 0.73°/day, so Jupiter **clears
combustion around 13 August 2026** and its capacity improves markedly from
mid-month.

**This is the clearest marriage window the chart offers in the visible
timeline** — effectively late August 2026 through mid-2027, outer bound January
2028. Guru also rules the 4th, so marriage and settling a home read as one
movement rather than two.

The counterweights from §10 do not disappear because the timing is good. Ketu
touches the 7th in four vargas; he is partially Manglik; and **Saturn in the 7th
means slow and serious rather than swept-up** — formalising something
considered, often with an older or more sober partner. Saturn delays and then
confirms; it rarely does sudden.

**If this window passes**, the next comparable one is **Rahu–Shukra, 2034–2037**
— Shukra being the natural karaka of marriage, ruling the 2nd house of family,
and holding the chart's highest Ishta Phala. Nothing between 2028 and 2034
activates the 7th with similar force.

### Authority — yes, of a particular kind, on a particular schedule

**Rahu, the mahadasha lord, is transiting the natal 6th** — simultaneously
Rahu's own most favourable house, the chart's **41-bindu high point**, and the
**D10 ascendant sign**. Three independent reasons that placement is strong, at
once. With transit Mangal crossing the natal 10th and exalted Guru in the 11th,
the coming months genuinely favour advancement: winning a competitive situation,
being handed ownership, a step up in responsibility.

What they do not support is a large positional title — and that is structural,
per §10, not transitory.

| Window | What happens |
|---|---|
| **Now → Jan 2028** | Unobstructed. Responsibility and recognition, a step up in ownership. **The last clear run for years.** |
| ~H2 2027 → ~2035 | **Sade Sati.** |
| 2028–2030 | Rahu–Shani. Authority *earned* — heavy load, slow recognition. |
| ~2030–2032 | Hardest convergence: Sade Sati peak + failing lagna lord's dasha + Saturn return. |
| ~2032–2035 | Saturn over the natal 10th at 1 bindu. Visibility suppressed even as material conditions improve. |
| **From Dec 2040** | **Guru mahadasha.** Authority consolidates. |

**Recognition now → authority earned 2028–2030 → visibility suppressed
2032–2035 → authority held from 2040.**

---

## 13. Synthesis

A **Kanya lagna repeating across three vargas**, with a **combust lagna lord
that also rules the 10th** and is the chart's only graha failing its strength
minimum, sitting in the 8th beneath an **exalted, gandanta Sun** — and a
nakshatra chain closing in a **Ketu–Budha loop**. Eight of nine grahas packed
into houses 8, 9 and 10. A **Dharma-Karmadhipati Yoga** and a **Mangal ⇄ Shukra
parivartana** as the two load-bearing structures, both running through Shukra,
reinforced by **Vimala Yoga**.

The balance sheet:

- **Greatest asset: Surya** — 2.28× requirement, best outcome balance in the
  chart, ruling the strongest house.
- **Second: Shukra** — highest Ishta Phala, and the pivot of both major yogas.
- **Greatest liability: Budha** — only graha below minimum, ruling both self and
  career, and failing on *position* rather than capacity.
- **Most misread placement: Chandra** — exalted by sign, thin by four
  independent measures.
- **Sharpest structural fact:** the two houses holding seven of nine grahas
  carry the chart's two lowest bindu counts, while the empty 6th carries the
  highest. **All the activity is concentrated where results come hardest, and
  the fertile ground is somewhere else.**

### The overall trajectory

**Upward — decisively, but late, and along two curves that separate.**

Four structural facts carry the upward reading:

1. **Each successive mahadasha lord is better positioned for standing than the
   last.** Rahu holds no Parashari rulership and acts through its dispositor.
   Guru **occupies the 10th**, gives Amala Yoga, rules the 4th and 7th (Bhava
   ranks 2 and 4), and is the second-strongest graha. Shani ranks 2 in strength,
   **rules the 41-bindu 6th**, occupies **D9's 10th**, and is the **D10 lagna
   lord**. The sequence improves.
2. **The chart's only raja yoga fires late.** The DKY's fullest run is
   Guru–Shukra, 2048–2051, at ages 46–49.
3. **Vimala Yoga** is structurally a rise-after-adversity signature, and the
   12th it rules is the strongest bhava in the chart.
4. **There is a twenty-two-year Sade Sati-free window from ~2035 to ~2057** —
   between the two Sade Satis — and **the entire Guru mahadasha sits inside it.**
   The chart's best dasha runs through its clearest sky, across ages 33 to 55.

The shape is not a smooth ramp:

| Ages | Period | Shape |
|---|---|---|
| 21–33 | Rahu MD, Sade Sati #1 from ~2027 | **Flat to frustrating.** Construction on barren ground; visibility lags ability. |
| 33–39 | Rahu–Shukra, Rahu–Surya; Sade Sati over | **First real lift.** |
| **39–55** | **Guru MD, no Sade Sati, DKY fires** | **The steep rise.** |
| 55–61 | Shani–Shani and Shani–Budha, under Sade Sati #2 and the Saturn return | **The deepest trough of the life.** |
| **61–74** | **Shani–Shukra onward, Sade Sati over** | **Sustained recovery and rise**, in a different currency — see below. |

The Shani mahadasha is itself a **V, not a plateau**: it falls hard for its
first six years and rises for its last thirteen, ending higher than it began.
And because Shani carries 2.3× Guru's Shodhya Pinda, that second half is the
largest-delivering stretch of the life in sheer volume. What changes is the
**axis** of the rise — Guru ascends on the 10th-house status axis; Shani ascends
on the 5th/6th/9th axis of students, service, mentorship and dharma. Influence
and legacy rather than further positional climb.

**And here is the part that matters most.** Two curves run in opposite
directions:

- **Standing, competence and achievement rise** — late and steeply through the
  Guru mahadasha, then, after a hard six-year trough at 55–61, rise again
  through the second half of the Shani mahadasha on a different axis.
- **Ease does not rise with them.** Shani's outcome balance is **−34.35, the
  worst in the chart**, and it governs nineteen years with a second Sade Sati on
  top. But note the qualification in §10: that figure derives only from Uchcha
  and Chesta Bala, so it describes the *texture* of the period rather than its
  productivity.

**Outcomes improve while the experience gets heavier.** That is not a
contradiction in this chart; it is its thesis restated one final time. The 8th–9th
exchange, Vimala Yoga, and a raja yoga buried in the weakest bhava all say the
same thing about how good things arrive here.

**What could bend the curve down.** The upward reading is conditional, because
the chart supplies potential and almost no scaffolding:

- The **10th is rank 9 with a failing lord**. If he waits to be given position
  rather than building demonstrable competence, the rise does not happen —
  nothing in this chart confers status automatically.
- The **11th is rank 11** with both nodes debilitated in D11. Gains do not
  accumulate passively, and leverage is genuinely dangerous.
- **Empty kendras** mean that without self-imposed structure, the depth never
  converts into output.
- **Health** in 2030–2033 and again in 2056–2063.

The trajectory bends up if he specialises and builds structure. It flattens if
he waits for recognition. That choice is the actual variable — and it is the one
the chart leaves open.

**The strategy this implies:**

1. **Go deep, not wide.** No talent for breadth, enormous talent for depth.
   Every configuration rewards specialising into something difficult and
   unfashionable.
2. **Compete and serve rather than position and wait.** The 41-bindu 6th, the
   Aquarius D10 lagna and the rank-9 tenth house all say results come from
   out-working and out-analysing the problem, never from appointment or title.
3. **Change position, don't just push harder.** Budha's Dig Bala is 4.28 of 60
   while its Chesta Bala is near the top of the chart. What is under-resourced
   is *where he stands*, not what he can do. Environment, role and location are
   the high-leverage variables — most acutely in 2030–2033.
4. **Build structure deliberately, because the chart does not supply it.** Empty
   kendras mean routine, deadlines and external commitments have to be installed
   by hand. Rahu–Shani will impose this anyway from 2028; adopting it early
   converts an ordeal into an advantage.
5. **Use the window to January 2028 to commit, not to expand.** It activates the
   2nd- and 4th-strongest houses and is the last unobstructed run before Sade
   Sati. One direction, one mentor, one decision on the partnership question.
6. **Treat partnership as a conscious project** — with better odds than the
   affliction alone suggests. A rank-4 house with 33 bindus and the
   second-strongest graha as its lord is a sound foundation with a difficult
   tenant.
7. **Protect the nervous system.** A failing lagna lord and a Moon thin by four
   measures describe a system with limited reserves. This is primary, not
   peripheral.
8. **Expect the payoff late, and plan for it rather than against it.** The Guru
   mahadasha from 2040, and Guru–Shukra in 2048–2051, are where the chart's
   central yoga finally delivers. The first fifteen working years are the
   investment, not the return.
9. **The contemplative pull is native equipment.** A nakshatra chain terminating
   in Ketu, both Ketu and the Sun in gandanta, and the 12th standing as the
   strongest bhava — the same instruction given three times over.

The chart's own summary of itself is the 8th–9th exchange, Vimala Yoga, and a
raja yoga buried in the weakest house, all saying one thing:

> **The difficulty and the fortune are the same object.**

---

*Prepared from supplied D1, D9, D10, D11, D8, D27, D30, upagraha, Vimshottari,
Shadbala, Bhava Bala, Ashtakavarga, Reduced Ashtakavarga, Shodhya Pinda and
transit data. All divisional charts, dasha boundaries and strength tables were
independently recomputed and verified; see `verify_chart.py` and
`verify_bala.py`. Two source errors (D8 and D30 Ketu) are corrected throughout;
two unreconcilable columns are identified in §1 and excluded. An interpretation
within the framework of Jyotisha, presented on its own terms.*
