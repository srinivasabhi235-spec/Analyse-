# Vedic Chart Analysis — D1, D9, D10, D11, D8, D27, D30 + Upagrahas + Vimshottari

Analysis of the supplied Parashari chart set. Read within the interpretive
framework of Jyotisha, on its own terms and vocabulary.

Every numeric claim below was recomputed from the D1 longitudes rather than
taken on trust. The verification script is in `verify_chart.py`.

---

## 0. Data integrity — read this first

**The data is good.** I recomputed D9 and D27 independently from the D1
longitudes; all twenty positions matched the supplied tables to within a few
arc-seconds. I also rebuilt all nine Rahu antardashas from the Vimshottari
proportions, and every boundary date matched the supplied dasha table exactly
(07 Sep 2025, 31 Jan 2028, 07 Dec 2030, 26 Jun 2033, 14 Jul 2034, 14 Jul 2037,
08 Jun 2038, 07 Dec 2039, 25 Dec 2040). This is an internally consistent chart.

**Two rendering bugs.** Rahu and Ketu must always be exactly 180° apart. They
are in D1, D9, D10, D11 and D27 — but in **D8 and D30 the tool printed Ketu at
Rahu's own longitude**:

| Varga | Printed | Correct Ketu | Consequence |
|---|---|---|---|
| **D8** | Ketu 05°26′ Karka (5th) | **05°26′ Makara — 11th bhava** | Ketu joins exalted Mangal in the 11th, not Rahu in the 5th |
| **D30** | Ketu 27°56′ Vrischika (1st) | **27°56′ Vrishabha — 7th bhava** | Ketu falls **4° from Chandra** in the 7th — a tight Moon–Ketu conjunction |

The D30 correction matters. A Moon–Ketu conjunction in the 7th of the
Trimshamsha is a real signature (detachment and recurrent dissatisfaction in
partnership as a *character* tendency), and the printed chart hides it
completely. The corrected readings are used throughout below.

**Derived context.** The Moon at 1°47′ Vrishabha sits 38.4% through Krittika,
leaving a Surya mahadasha balance of 3.70 years at birth. Adding Chandra (10)
and Mangal (7) places the Rahu mahadasha start 20.70 years after birth — which,
against the given start of 25 Dec 2022, implies a birth around **15 April
2002**. This is independently corroborated: the Sun at 1°28′ sidereal Mesha
occurs ~15–16 April every year. So the native is **about 24**, and the chart was
cast around April 2026 (14y 8m remaining of an 18-year dasha).

That matters for the reading. This is not a mid-life chart being assessed in
retrospect — it is a chart at the opening of its defining period.

**Two further confirmations, from the Shadbala.** The Kala Bala components
independently pin down the birth circumstances:

- **Vara Bala of 45 goes to Chandra**, and Vara Bala is awarded to the lord of
  the weekday. That requires a **Monday** birth. **15 April 2002 was a Monday.**
  A third independent confirmation of the derived date, from data supplied
  separately.
- **Paksha Bala** resolves the lunar phase exactly. Benefics score 10.11 and
  malefics 49.89, which back-solves to a Sun–Moon elongation of 30.32° — matching
  the D1 longitudes precisely. That is **Shukla Tritiya, roughly 2.5 days after
  the new moon: a thin waxing crescent.** The Moon's own doubled score of 20.21
  confirms it. This turns out to matter a great deal — see §10.
- **Hora Bala of 60 goes to Surya.** On a Monday the Sun's hora is the 5th and
  12th from sunrise; the ascendant sits 176° past the Sun, which places birth
  roughly eleven to twelve hours after sunrise. Both point to **late afternoon
  or early evening**.

**Glyph key** (inferred from the data, and each one verified): `(Q)` = in a
kendra, `(T)` = in a trikona, `↺` = retrograde, `💱` = parivartana (sign
exchange), `🔥` = combust, `🌸` = Pushkara navamsa. Nothing below depends on
reading these correctly — each was confirmed by computation.

---

## 1. The one fact that organises everything

**Eight of the nine grahas occupy three consecutive houses: 8, 9 and 10.**

| House | Sign | Occupants |
|---|---|---|
| 8th | Mesha | **Surya** (exalted, gandanta), **Budha** (lagna lord, combust), **Shukra** |
| 9th | Vrishabha | **Chandra** (exalted), **Mangal**, **Shani**, **Rahu** |
| 10th | Mithuna | **Guru** |
| 3rd | Vrischika | **Ketu** (gandanta) |

Nothing else is tenanted. Houses 1, 2, 4, 5, 6, 7, 11 and 12 are all empty.

This is an extreme concentration, and it is the chart's governing fact. Lives
with this shape are not spread evenly across many arenas — they are *narrow and
deep*. One theme dominates and everything else gets pulled into its orbit. The
theme here is the 8th–9th–10th complex: **depth/crisis/hidden knowledge (8th),
meaning/mentors/fortune/higher learning (9th), and public work (10th)** — with
the 3rd (Ketu: effort, communication, self-generated skill) as the lone
counterweight.

The empty houses are not absent from life; they are *routed through the
cluster*, because their lords all sit inside it:

- 4th and 7th lord **Guru** → 10th. Home and marriage are entangled with career and public standing.
- 5th and 6th lord **Shani** → 9th. Creativity and daily work are entangled with belief and mentors.
- 11th lord **Chandra** → 9th. Income arrives through the same channel.
- 12th lord **Surya** → 8th. (A yoga in its own right — see §3.)
- 1st **and** 10th lord **Budha** → 8th. Identity and career are the same object, and both are buried in the 8th.

There is no separate compartment for private life here. Everything is the
same conversation.

---

## 2. The self: a Virgo lagna that repeats

The lagna is 27°37′ Kanya, Chitra pada 2 — and **Virgo recurs as the lagna in
D9 (08°38′) and D11 (03°53′)**. A vargottama-style repetition of the ascendant
across the rashi and navamsha is one of the more reliable strength indicators in
the system: the person you appear to be and the person you actually are do not
diverge much. Self-consistency, not self-contradiction.

Virgo gives the working equipment: analysis, discrimination, refinement,
diagnosis, service, discomfort with the imprecise. Chitra pada 2 (ruled by
Mangal, sub-lord Guru) adds craftsmanship — Chitra is the celestial artisan,
and pada 2 in Virgo is the most technically exacting quarter of it.

**But the lagna lord is compromised in an interesting way.** Budha rules both
the 1st and the 10th — an unusually tight fusion of identity and vocation — and
sits in the **8th house, combust**, 9°00′ from an exalted Sun (within the 14°
limit; confirmed by computation).

Combustion of the lagna lord is usually read as diminishment, and partly it is:
capability that is not visible from outside, an early career in which the person
is consistently underestimated, and a self-assessment harsher than the evidence
warrants. But the *specific* configuration matters. Budha is not burned by an
ordinary Sun — it is burned by a Sun in **exaltation**, in the 8th. The
classical reading of a planet absorbed into a strong Sun is not destruction but
**assimilation**: the intellect stops operating as a separate performing faculty
and fuses into the person's core authority. Practically, this describes someone
whose thinking is inseparable from their sense of self, who cannot do
intellectual work they don't believe in, and whose real ability surfaces late
and privately rather than early and publicly.

### The nakshatra chain closes on Ketu

Following each graha to the lord of the nakshatra it occupies produces the
chart's deepest dispositor:

```
Lagna → Chitra (Mangal) → Mangal in Krittika (Surya) → Surya in Ashwini (Ketu)
      → Ketu in Jyeshtha (Budha) → Budha in Ashwini (Ketu) → ⟲ closed loop
```

The chain terminates in a **closed Ketu–Budha loop**. Nothing escapes it. At the
nakshatra level — the level classical texts treat as more granular and more
determinative than sign placement — this chart is run by Ketu working through
Mercury.

That is a precise signature: **detached, investigative, pattern-seeking
intelligence.** Ketu dissolves rather than accumulates; Budha analyses. Together
they describe someone who learns by taking things apart, is drawn to what is
hidden or discarded, works best alone, distrusts received explanations, and has
a native pull toward the metaphysical that is not sentimental but *forensic*.
It also describes a person who is not very interested in credentials for their
own sake, which will matter in §7.

---

## 3. The structural spine: an 8th–9th exchange, and a Vipreeta Raja Yoga

Two configurations do most of the interpretive work.

### Mangal ⇄ Shukra parivartana (8th ⇄ 9th lords)

Mangal rules the 8th and sits in the 9th. Shukra rules the 9th and sits in the
8th. Computation confirms this is the chart's **only** parivartana — a clean
mutual exchange, and it links the chart's best house to its most difficult one.

An exchange means the two houses stop being separate. Fortune, mentorship,
belief, father, higher learning and long-distance movement (9th) become
*inseparable from* crisis, research, hidden systems, other people's resources,
inheritance, healing and transformation (8th). Read in both directions:

- **Fortune arrives through the 8th.** Luck in this chart does not show up as
  smooth good weather. It shows up as: the crisis that turns out to be the
  opening, the obscure subject that becomes the career, the resource that comes
  through someone else's estate or capital rather than through salary.
- **The 8th is dharmically protected.** Depth work — research, investigation,
  the occult, psychology, surgery, forensics, insurance, risk, taxation,
  security — is not a detour here. It is the assigned path, and it carries the
  9th house's protection.

This is the classic chart-shape of people who earn their living from what
others avoid.

### Vimala Yoga

Surya rules the 12th and occupies the 8th — the 12th lord in a dusthana, which
forms **Vimala Yoga**, one of the Vipreeta Raja Yogas. Its meaning is specific:
adversity inverts into advantage. Expenses stay contained, independence comes
naturally, and the person tends to *rise out of* the setback that would sink
someone else. Stacked on top of the 8th–9th exchange, the chart says the same
thing twice: **this life is built out of its own difficulties, not in spite of
them.**

---

## 4. Real strengths

**Surya — the strongest graha in the chart.** Exalted in D1, and also in Aries
in D9, D10, D11, D8 and D30 — six of the seven vargas shown. Worth being honest
about the mechanism: because the Sun sits at only 1°28′ of Aries, low-numbered
divisions keep mapping it back into Aries, so part of this is arithmetic rather
than independent confirmation. But classical scoring counts vargas as they fall,
and by that standard this is exceptional solar strength: integrity, spine, an
unwillingness to be directed by others, and genuine natural authority.

**Surya is also in gandanta** (1°28′ Mesha, within the 3°20′ Pisces–Aries knot;
verified). This is the chart's most interesting single placement — maximum
exaltation *and* a karmic knot on the same degree. Gandanta on the Sun points at
the significations of the Sun: father, authority, one's own right to lead. Read
plainly: the relationship to authority — both the father's and the native's own
— is simultaneously the greatest source of strength and the deepest unresolved
knot. It tends to express as difficulty accepting authority above oneself
combined with reluctance to claim it openly, and it typically resolves through
the 8th-house route of actually doing the depth work rather than through
argument.

**Chandra — near-peak exaltation.** At 1°47′ Vrishabha against a deep
exaltation point of 3°00′, this Moon is within 1°13′ of maximum. Emotional
capacity, stability and mental resilience are structurally high — an underrated
asset in a chart this heavy.

Two qualifications. First, the Moon sits in a crowded 9th with Mangal (5°32′
away — a genuine **Chandra–Mangal yoga**, the classical wealth-through-enterprise
combination, but also emotional heat and impatience), Shani, and Rahu. High
capacity operating under permanent load. Second, the Moon is in **Krittika,
ruled by Surya** — so the mind reports to the Sun, and the Sun is exalted in the
8th and in gandanta. The emotional life is therefore pulled toward depth,
secrecy and meaning, and it destabilises specifically when the belief system
destabilises. This Moon needs a philosophy to stay well. That is not a
metaphor — it is the mechanical reading of a Krittika Moon in the 9th under a
gandanta Sun.

**Mangal in Pushkara navamsa** (7°19′ Vrishabha, inside the 6°40′–10°00′
Pushkara span; verified — hence the `🌸`). Pushkara degrees are held to be
nourishing and protective. Mangal's navamsha falls in Meena, Guru's sign, which
softens it further. This is the one clean mitigating factor inside the otherwise
harsh 9th-house cluster, and it is worth noting because Mangal is half of the
chart's central exchange.

**Ketu in gandanta too** (26°55′ Vrischika, Jyeshtha pada 4 — the classical
gandanta pada; verified). Combined with the Ketu-terminated nakshatra chain,
this doubles down on §2: the spiritual/investigative drive is not incidental
here, it is load-bearing, and it carries a knot of its own.

---

## 5. Yogas — present and absent

Being straight about what is *not* there is as useful as listing what is.

**Present:**
- **Dharma-Karmadhipati Yoga** — 9th lord Shukra conjunct 10th lord Budha. The
  premier raja yoga of the classical hierarchy, and **the chart's only
  kendra–trikona raja yoga**. Treated in full below; it was missing from an
  earlier version of this list, which was an error.
- **Mangal ⇄ Shukra parivartana** (8th/9th) — the spine.
- **Vimala Yoga** (12th lord in 8th) — adversity inverts.
- **Chandra–Mangal Yoga** (5°32′) — wealth through enterprise; emotional heat.
- **Amala Yoga** — Guru, a benefic, in the 10th from lagna. Clean reputation,
  fair dealing, a name that holds up. **But qualified three ways:** Guru is in
  Mithuna, an enemy's sign; its dispositor Budha is combust in the 8th; and the
  upagraha **Yama Ghantaka sits 2°05′ from Guru** (verified). The yoga is real
  but it does not operate cleanly — reputation is earned rather than granted,
  and tends to arrive with friction attached.
- **1st + 10th lordship in one graha** (Budha) — raja-yoga-capable fusion of
  self and career, though delivered from the 8th and combust.
- **D8: Mangal ⇄ Shani parivartana** — exalted Mars in Capricorn exchanging with
  debilitated Saturn in Aries, which produces **neechabhanga** for Shani. Under
  adverse periods, the worst-case scenario has a built-in cancellation.
- **D11: Guru ⇄ Chandra parivartana**, with Guru **exalted** in the 11th of the
  gains-chart. This is the strongest single configuration in the entire varga
  set.

**Absent — and worth knowing:**
- **No Panchamahapurusha yoga.** No graha meets the own/exalted-sign-in-kendra
  requirement. There is no single overwhelming "great person" signature.
- **No Gaja Kesari.** Guru is 2nd from Chandra, not in a kendra from it.
- **Only one graha in a kendra at all** (Guru in the 10th). Kendras are the
  chart's structural pillars, and here they are almost entirely vacant. This is
  the chart's main structural weakness: it has enormous depth (trikona and
  dusthana loading) and very little scaffolding. Depth without structure is the
  problem to solve — and note that the fix is behavioural, not astrological:
  routine, containers, deadlines, external commitments.

### Dharma-Karmadhipati Yoga — the chart's only raja yoga

**This belonged at the top of the list above and I omitted it. It is the single
most important yoga in the chart.**

From Kanya lagna the 9th house is Vrishabha, ruled by **Shukra**, and the 10th
is Mithuna, ruled by **Budha**. Both sit together in Mesha, **13°09′ apart in
the same sign** — a conjunction. The lord of dharma and the lord of karma joined
directly:

> **Dharma-Karmadhipati Yoga, formed by conjunction in the 8th house.**

Conjunction is the strongest of the three ways this yoga can form (ahead of
mutual aspect and exchange). And a systematic sweep of every kendra lord against
every trikona lord confirms something worth stating plainly: **this is the only
kendra–trikona raja yoga in the entire chart.** Budha–Shani, Guru–Shani and
Guru–Shukra all fail to connect by conjunction, aspect or exchange. Everything
this chart has in the raja yoga class rests on this one conjunction.

**It is also carrying more than the DKY.** Budha rules the 1st and 10th; Shukra
rules the 2nd and 9th. So a single conjunction fuses the lordships of houses
**1, 2, 9 and 10**:

| Pairing | Yoga |
|---|---|
| 9th + 10th | **Dharma-Karmadhipati Yoga** |
| 1st + 9th | Kendra–trikona raja yoga |
| 2nd + 9th | Dhana yoga — wealth through fortune |
| 2nd + 10th | Dhana yoga — wealth through profession |
| 1st + 2nd | Dhana yoga |

Add Surya in the same sign, ruling the 12th, and the 8th house holds the
lordships of the 12th, 1st, 2nd, 9th and 10th. This materially revises §01: I
read the 8th-house stellium primarily as a burial. **It is also where the
chart's raja yogas live.** Both readings are true, and the tension between them
is the point.

#### But it is a conditional yoga, and the conditions matter

| Supporting it | Limiting it |
|---|---|
| Formed by **conjunction**, the strongest mode | Formed **in the 8th house** — a dusthana |
| Shukra has the chart's **highest Ishta Phala** (47.49), ratio 1.21, net +35.62 | Budha is **combust**, **fails its Shadbala minimum** (0.92), has the **lowest Dig Bala** (4.28), and is net-malefic (−11.41) |
| Compounded with four additional raja/dhana lordships | The 8th is **Bhava rank 12** with the **lowest SAV in the chart (21 bindus)** |
| **Echoed cleanly in D10** — see below | **Absent in D9** — in the navamsha the 9th lord goes to the 3rd and the 10th lord to the 11th, with no conjunction and no mutual aspect |

The shape is unusually legible: **the dharma half is strong and benign; the
karma half is the chart's weakest link; and the whole thing is built on its
poorest ground.**

The missing navamsha echo is the most serious limitation. A yoga that does not
repeat in D9 is classically held to lack durability — it delivers, but it does
not compound the way a navamsha-confirmed yoga does.

#### The D10 echo, which is the good news

In the dashamsha the lagna is Kumbha, making Tula the 9th house — ruled by
**Shukra**. And Shukra sits at 26°08′ Vrischika, which is the **10th house of
D10**, in a kendra. The source table states this directly: Shukra "rules 4, 9
Bhava" and "is in 10 Bhava."

So the **9th lord of the career chart occupies the 10th house of the career
chart** — a Dharma-Karmadhipati placement, cleanly formed, in exactly the varga
that governs profession. The yoga is weak in the navamsha and strong in the
dashamsha, which says something precise: **it delivers in the domain of work and
public role rather than in the domain of inner life and marriage.**

#### Shukra is the pivot of the whole chart

Note what Shukra is now doing. It is:

1. the **9th lord** in the Dharma-Karmadhipati Yoga,
2. half of the **Mangal ⇄ Shukra parivartana** — the spine identified in §03,
3. the **2nd lord**, ruling a house that is Bhava rank 3 with the highest
   Drishti Bala in the chart,
4. the graha with the **highest Ishta Phala** of all seven.

**Both of the chart's two major yogas run through Shukra.** After Surya, it is
the most consequential graha here for outcomes — which was not obvious from the
sign-level reading and only emerges once the yogas and the strength data are put
side by side.

#### When it fires

Yogas fructify in the dashas of their participants. The two halves fire in
back-to-back antardashas of opposite character:

| Period | Participant | Character |
|---|---|---|
| **Rahu–Budha** · Dec 2030 – Jun 2033 | Karma half | The chart's weakest graha, running under Sade Sati's peak and the Saturn return. **Construction, not payoff.** |
| **Rahu–Shukra** · Jul 2034 – Jul 2037 | Dharma half | Highest Ishta Phala in the chart. **The payoff.** |
| **Guru–Budha** · Aug 2045 – Dec 2047 | Karma half | Inside the Guru mahadasha, with Guru in the 10th. |
| **Guru–Shukra** · Nov 2048 – Jul 2051 | Dharma half | **Likely the fullest expression of the yoga in the whole life.** |

That two-stage structure — a hard, low-visibility Budha phase followed by a
Shukra payoff — restates the chart's governing theme once more. And the
strongest run comes in the **Guru mahadasha (2045–2051, ages 43–49)**, when the
dasha lord is the graha occupying the 10th house. The DKY does not deliver its
best inside the Rahu period at all. It waits.

This is now the fourth independent line of evidence for the late-cresting career
in §12, and it is the most specific of them.

---

## 6. Aspects — where the pressure actually lands

Computed graha drishti onto houses:

| Graha | From | Aspects houses |
|---|---|---|
| Mangal | 9th | 3, 4, 12 |
| Guru | 10th | 2, 4, 6 |
| Shani | 9th | 3, 6, 11 |
| Rahu | 9th | 1, 3, 5 |
| Ketu | 3rd | 7, 9, 11 |
| Surya / Budha / Shukra | 8th | 2 |
| Chandra | 9th | 3 |

Three things fall out of this:

1. **The 3rd house takes almost everything** — Ketu occupies it, and Mangal,
   Shani and Chandra all aspect it. Courage, initiative, communication,
   self-generated skill, siblings. This is the chart's real working house and
   its pressure valve. Effort put into *skill and output* pays disproportionately
   here; waiting to be given opportunities does not.
2. **Rahu aspects the lagna** from the 9th — and Rahu is the current mahadasha
   lord. Identity is under active reconstruction for the whole 2022–2040 period.
3. **Guru aspects the 6th** — protective for health, debts and adversaries. A
   genuine safety net in a chart that otherwise carries a lot of load.

---

## 7. Life areas

### Career (10th, D10)

10th lord Budha is combust in the 8th; Guru occupies the 10th (Amala, qualified).
In **D10** the lagna is Kumbha and its lord **Shani sits in the 5th**; **Shukra
occupies the 10th of D10 in Vrischika**; Surya is exalted in the 3rd; **Rahu is
in the 8th of D10**.

Synthesised, this points consistently in one direction: **analytical, systematic,
research- or investigation-shaped work** — Aquarius/Saturn for systems,
technology and structure; Scorpio on the D10 tenth for depth, finance, risk,
insurance, security, data or psychology; Rahu in the D10 eighth for
unconventional, non-linear career turns and possible foreign involvement;
exalted Sun in the D10 third for communication and self-driven output.

What it does *not* describe is a conventional linear ladder inside a stable
institution. Several D10 grahas sit at 27–29° of their signs (Shani 29°04′,
Rahu 29°18′, Ketu 29°18′, Guru 27°58′) — end-of-sign positions, which read as
transition and discontinuity in the career varga. Expect the path to be built
out of discrete moves rather than steady internal promotion. Given the Ketu–Budha
nakshatra loop, this is a fit, not a misfortune: credential-driven institutional
progression was never the natural route.

### Wealth (2nd, 11th, D11)

Mixed, but net positive, with an unusual mechanism.

2nd lord Shukra is in the 8th — poor for steady linear accumulation from salary,
good for **inheritance, partner's resources, capital that originates outside
oneself, insurance, and windfall/loss volatility**. 11th lord Chandra is exalted
in the 9th — strong gains via mentors, teaching, publishing, foreign connections.
Chandra–Mangal yoga supports enterprise income.

**D11 is the strong chart in this set.** Guru is **exalted in the 11th of D11**,
with Budha alongside, and Guru is in a **parivartana with Chandra**. Gains
through knowledge, advisory, teaching and networks are structurally well
supported. Counterweight: **Rahu and Ketu are both debilitated** in D11 (4th and
10th), which reads as instability in the *base* from which gains are made — home
and career footing — and argues strongly against leverage and speculation. The
money is real; the platform under it wobbles.

### Partnership (7th, D9, D27, D30)

This is the area that needs the most honesty, and the signal is consistent
across five charts.

- **D1:** the 7th (Meena) is empty. Its only aspect is **Ketu's** (from the 3rd).
  7th lord Guru is in the 10th, in an enemy's sign, 2° from Yama Ghantaka. The
  upagraha **Upaketu** also falls in the 7th.
- **D9:** **Mangal and Ketu occupy the 7th**, while **Rahu conjoins the D9 lagna**
  within 6°. A loaded Rahu–Ketu 1/7 axis in the navamsha.
- **D27:** the 7th holds **Mangal, Budha, Shukra and Ketu** — four bodies — with
  Rahu again in the lagna. The 1/7 axis repeats.
- **D30 (corrected):** **Chandra conjunct Ketu within 4°** in the 7th.
- **Manglik status:** not Manglik from the lagna (Mangal is in the 9th), but
  Mangal is 1st from Chandra and 2nd from Shukra — **partially Manglik** from
  both the Moon and Venus.

Every chart says the same thing, so it should be said plainly rather than softened:
**partnership is a karmically loaded, effortful arena for this native, not an
easy one.** Ketu touching the 7th in four separate vargas is a detachment
signature — a tendency to be present but not fully arrived, and to discover that
the thing obtained is not the thing wanted.

This is not a prediction of failure, and it should not be read as one. It is a
description of difficulty and of what the difficulty responds to. The
constructive reading: early or conventionally-arranged partnership is
ill-advised here; **later and deliberately chosen does substantially better**,
because the detachment pattern needs to be conscious before it can be worked
with rather than merely acted out. The partner indicated is someone met through
work, public life or travel (7th lord in the 10th), and someone who can hold
both intensity and independence. The soft spot in the picture is D30's Chandra
in its own mooltrikona in the 7th — real emotional depth is available; it is
Ketu sitting next to it that keeps it from settling.

### Health and constitution

Virgo lagna with a combust lagna lord in the 8th, and an exalted Moon under
Saturn/Mars/Rahu pressure in the 9th. The constitution is fundamentally sound —
the exalted Moon and Guru's aspect on the 6th are both protective — but the
system is nervous rather than robust. Virgo/Mercury pathology is digestive and
neurological, and it is stress-mediated. Shani rules the 6th and sits with the
Moon's sign lord in the 9th, which reads as *chronic and low-grade rather than
acute*.

The practical form this takes: rest is not optional and cannot be caught up
retroactively. The chart runs hot on analysis and has no natural off-switch, so
the switch has to be installed manually.

---

## 8. Upagrahas

Verified contacts within 5°:

| Upagraha | Position | House | Contact |
|---|---|---|---|
| **Yama Ghantaka** | 12°42′ Mithuna | 10th | **2°05′ from Guru** |
| Mrityu | 26°49′ Mesha | 8th | 3°13′ from Shukra |
| Parivesha | 15°12′ Vrishabha | 9th | 2°42′ from Shani |
| Ardha Prahara | 20°47′ Vrishabha | 9th | 2°53′ from Shani |
| Gulika / Mandi | 25°16′ / 22°22′ Karka | 11th | — |
| Kala | 10°08′ Kanya | 1st | — |
| Upaketu | 01°28′ Meena | 7th | — |

The significant one is **Yama Ghantaka on Guru** — the chart's only kendra graha,
its Amala yoga giver, and its 4th and 7th lord, all in one body, carrying a
shadow-point 2° away. This is the technical reason the reputation yoga does not
run clean, and it reinforces the 7th-house reading independently.

**Gulika and Mandi in the 11th** put a shadow on the gains house, which pairs
with the debilitated nodes in D11: income arrives, but not without complication.
**Kala in the lagna** and **Mrityu near Shukra in the 8th** both echo the
chart's existing 8th-house emphasis rather than adding anything new.

---

## 9. Timing — the Vimshottari picture

Rahu mahadasha, **25 Dec 2022 → 25 Dec 2040**, covering roughly **ages 20.7
to 38.7**. The entire career-forming span of this life falls under Rahu.

Rahu sits in the **9th**, in Vrishabha (Shukra, a friend), in Mrigashira
(Mangal), with exalted Chandra, Mangal and Shani, and it **aspects the lagna**.
Rahu in the 9th is the signature of someone who reworks inherited belief rather
than transmitting it: unorthodox mentors, foreign exposure, higher education
approached at an angle, and a relationship to tradition that is engaged but not
obedient.

### The current period: Rahu–Guru, 07 Sep 2025 → 31 Jan 2028 (ages ~23.4–25.8)

**This is one of the most activated antardashas of the whole eighteen years**,
for a technical reason worth stating: **Guru sits in Ardra, which is Rahu's
nakshatra, while Rahu's own sub-lord is Guru.** The two are mutually wired
together at the nakshatra level. Whatever this pairing is capable of, it is
delivering at full strength.

Guru rules the **4th and 7th** and occupies the **10th**. So the live themes are:
home, property and relocation; **marriage and partnership decisions**; formal
education and credentialing; and first real public and professional standing.
Rahu's own 9th-house position adds foreign travel, higher study, publishing,
law and ethics. The age-24 Jupiter return also falls inside this window, which
compounds the same significations.

**What this window is for: choosing a direction and committing to it.** Guru in
a kendra forming Amala yoga is a genuine opening.

**What to watch:** Guru is in an enemy's sign, 2° from Yama Ghantaka, and lands
in the **6th house of D9** — a weak navamsha placement. The realistic reading is
that this period's promise is real but delivers *through service, effort and
friction* rather than smoothly. Concretely: over-commitment, advisers who
overpromise, believing one's own momentum, and a tendency toward expansive plans
that outrun execution. Guru here rewards *narrowing*, not adding.

### Rahu–Shani, 31 Jan 2028 → 07 Dec 2030 (ages ~25.8–28.6)

**Probably the career-defining stretch of the entire mahadasha.** Rahu and Shani
are conjoined in the 9th in D1 (9°02′ apart). Independently, Shani is in the
**10th of D9** and is the **D10 lagna lord** — the strongest career credentials
of any graha in this chart, and both are Saturn's.

Expect: heavy sustained work, authority earned slowly rather than granted,
plausible relocation, and one long project that ends up defining the record.
Shani also rules the 6th, so discipline, routine and health maintenance stop
being optional in this window. This is the period that builds the structure the
chart otherwise lacks — which is precisely why it will feel like grinding rather
than like luck.

### Rahu–Budha, 07 Dec 2030 → 26 Jun 2033 (ages ~28.6–31.2)

The lagna lord's sub-period: identity reset, research output, writing,
communication, technology. But Budha is combust, in the 8th, and rules the 1st —
so this is also the period to take the nervous system and health seriously
rather than treat them as an afterthought. The Saturn return (~age 29.5, around
late 2031) falls inside this window, which sharpens the same theme.

### Rahu–Ketu, 26 Jun 2033 → 14 Jul 2034 (age ~31.2–32.2)

The fragile one. Rahu–Ketu is inherently destabilising, and Ketu here is
gandanta in the 3rd. Read it as a retreat-and-consolidate year: good for
research, withdrawal, spiritual practice and letting things go — poor for
launching, borrowing or making irreversible commitments.

### Rahu–Shukra, 14 Jul 2034 → 14 Jul 2037 (ages ~32.2–35.2)

Three years, and likely **the material peak of the mahadasha.** Shukra rules the
2nd and 9th and sits in the 8th in exchange with the 9th lord — i.e. it is one
half of the chart's central spine. Wealth through partner's resources,
inheritance, capital, and dharmic or foreign channels. This is where the
8th–9th exchange is most likely to pay out.

The tail (Surya 2037–38, Chandra 2038–39, Mangal 2039–40) winds the period down,
with Rahu–Mangal at the end being the one to handle carefully — Mangal rules the
8th and the dasha closes on it.

---

## 10. Shadbala — the strength audit

Every figure in the supplied Shadbala table reconciles. All five Sthana Bala
sub-components sum to the printed Sthana totals; all nine Kala Bala
sub-components sum to the printed Kala totals; the six balas sum to Total Pinda;
Pinda ÷ 60 gives the printed Rupas; and the Relative Rank column reproduces
exactly if you sort by strength ratio. See `verify_bala.py`.

| Graha | Rupas | Required | Ratio | Rank | Ishta | Kashta | **Net** |
|---|---|---|---|---|---|---|---|
| **Surya** | 11.39 | 5.00 | **2.28** | 1 | 46.88 | 7.83 | **+39.05** |
| Shani | 6.39 | 5.00 | 1.28 | 2 | 12.48 | 46.83 | **−34.35** |
| Mangal | 6.33 | 5.00 | 1.27 | 3 | 19.66 | 38.87 | −19.21 |
| Guru | 8.21 | 6.50 | 1.26 | 4 | 37.30 | 15.10 | +22.20 |
| Shukra | 6.68 | 5.50 | 1.21 | 5 | **47.49** | 11.87 | +35.62 |
| Chandra | 6.42 | 6.00 | 1.07 | 6 | 24.54 | 4.49 | +20.05 |
| **Budha** | 6.46 | 7.00 | **0.92** | 7 | 18.91 | 30.32 | −11.41 |

Four things fall out of this, and one of them revises the earlier reading.

### Surya is confirmed, quantitatively

At **2.28× its requirement and 11.39 rupas**, the Sun is not merely the
strongest graha — it is nearly twice as strong relative to requirement as
anything else in the chart. Its Sapta Vargaja Bala of **165** is the highest
single component score in the table, against 120 for the next best.

That figure is worth pausing on. In §04 I noted the Sun holds dignity across six
of seven vargas, with the honest caveat that some of this is arithmetic — an
early-degree planet keeps mapping back to the same sign. The Shadbala shows the
classical system **scores it at full value regardless**. So the caveat stands as
a matter of mechanism, and the strength stands as a matter of the system's own
accounting. Both were true.

Add the highest Ishta Phala-to-Kashta ratio in the chart (46.88 against 7.83,
net **+39.05** — the best of any graha) and the picture is unambiguous: the Sun
is both the strongest *and* the most benign influence here.

### Budha fails — and it rules the 1st and the 10th

**Budha is the only graha in the chart that falls below its minimum
requirement** — 6.46 rupas against 7.00 needed, a ratio of 0.92. It is also
net-malefic in outcome (Ishta 18.91 against Kashta 30.32).

This is the single most consequential number in the table, because Budha rules
**both the lagna and the 10th house** — the self and the career.

But look at *where* the deficit comes from:

| Component | Budha | Comment |
|---|---|---|
| Uchcha Bala | **8.49** | Only 25° from its debilitation point (verified exactly) |
| **Dig Bala** | **4.28** | The lowest of any graha, by a wide margin — out of 60 |
| Sapta Vargaja | 90.00 | Joint-lowest |
| Nata-Unnata | **60.00** | Maximum |
| Chesta Bala | **42.15** | Second-highest in the chart |

The failure is entirely **positional and directional**. Mercury's dig bala is
earned in the 1st house; sitting in the 8th, it scores 4.28 out of 60 — close to
nothing. Its motional and temporal strength, by contrast, are excellent.

That distinction is worth stating plainly, because it is actionable: **the
chart's manager is not badly made, it is badly placed.** The equipment is sound;
the vantage point is wrong. Faculties that depend on *where you are* — visibility,
positioning, being in the right room — run at a deficit. Faculties that depend on
*how you think and move* run at full strength. The remedy this points at is
changing context, environment and role, not trying harder in place.

### Shani is strong and harsh at the same time

Shani ranks **2nd in strength** (ratio 1.28) but carries the **worst outcome
balance in the chart** — Ishta 12.48 against Kashta 46.83, net −34.35.

These are not in conflict; they measure different things. Strength is capacity
to deliver. Ishta/Kashta is whether delivery is pleasant. Saturn here will
absolutely produce results, and producing them will hurt. This sharpens §09's
call on Rahu–Shani (2028–2030) from an intuition into a measurement: that period
is simultaneously **the most productive and the most punishing** of the
mahadasha.

Mangal shows a milder version of the same shape (net −19.21) — and Mangal is the
other half of the central 8th–9th exchange, opposite a Shukra with the chart's
**highest Ishta Phala (47.49)**. The exchange pairs the most benefic graha with a
net-malefic one. The chart states its central theme yet again, now in numbers:
fortune and difficulty are welded together.

### Correction: the Moon is weaker than I said

In §04 I called the near-peak exalted Moon one of the chart's real assets, on the
strength of its dignity. **The strength data does not support that emphasis, and
I was overweighting sign dignity.** Four independent measures agree:

1. **Shadbala ratio 1.07** — second-weakest in the chart, barely clearing its
   requirement.
2. **Paksha Bala 20.21** out of a possible 120 for the Moon. The birth falls
   ~2.5 days after the new moon, so the Moon is a thin crescent — dignified by
   sign, but nearly empty by light.
3. **Two bindus** in its own sign in the Chandra Ashtakavarga — very low.
4. **Shodhya Pinda of 33**, less than half the next-lowest graha, with a Graha
   Pinda of exactly **0**.

The accurate formulation is that the Moon is **high in quality and low in
quantity**. The exaltation is real: note the Kashta Phala of 4.49, the lowest in
the chart, meaning the Moon does very little harm. But the reserves are thin.

This does not reverse the practical advice from §07 — it promotes it from a
footnote to a central finding. A mind that is fine in kind but limited in
reserve is exactly the configuration for which rest, routine and a stable
philosophy are structural necessities rather than lifestyle preferences.

### One row I cannot account for

The table's final row, **"Bhava (in %)"** — Surya 74, Chandra 70, Mangal 33,
Budha 14, Guru 19, Shukra 75, Shani 38 — does not reconcile against any
derivation I tested: position within sign, nakshatra or pada; Ishta/Kashta
proportion; Bhava Bala of the occupied house; or normalised Shadbala. Rather
than invent a meaning, I have left it out of the reading. Nothing above depends
on it.

---

## 11. Bhava Bala and Ashtakavarga — where results actually land

Shadbala measures the *grahas*. Bhava Bala and Ashtakavarga measure the
*houses* — and they tell a story the graha concentration does not.

Both tables reconcile completely: every Bhavadhipati figure matches the
Shadbala Total Pinda of that house's lord under Virgo lagna lordships,
Bhavadhipati + Disha + Drishti reproduces every Total Pinda, and the
Sarvashtakavarga sums to **337**, the classical total.

| House | Bhava rupas | Rank | SAV bindus | Lord |
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

### The crowded houses are the low-yield houses

This is the finding that most complicates §01, and it is genuinely
counterintuitive.

**The 8th and 9th houses hold seven of the nine grahas — and score the two
lowest Sarvashtakavarga totals in the chart**, 21 and 22 against an average of
28.08. The 8th is also dead last in Bhava Bala at 7.00 rupas, and receives
**zero** aspectual support.

So the chart's centre of gravity sits in its least fertile ground. All the
activity is concentrated where results come hardest. That is a demanding
configuration, and it explains something the sign-level reading could not: why a
chart this loaded with exaltations and yogas would nonetheless feel like
persistent uphill work. The effort is real and the terrain is poor.

It also refines the parivartana reading from §03. An 8th–9th exchange across two
low-bindu houses means the 8th is **worked through, not enjoyed**. Fortune
transits this ground; it does not rest here.

### The 6th house is the chart's most productive territory

**Kumbha, the 6th house, carries 41 bindus** — the highest in the chart by a
margin of eight, in a house that holds no grahas at all.

The 6th governs service, competition, problem-solving, disciplined daily labour,
adversaries overcome, and health. A 41-bindu 6th says, about as loudly as this
system says anything: **the native wins through the 6th house.** Out-working,
out-lasting, and out-analysing the opposition. Sustained applied effort against
concrete problems.

And there is a convergence worth noting: **Kumbha is also the D10 lagna**. The
career chart's ascendant is the same sign as the natal chart's most fertile
house. Both point at the same territory — Aquarius/Saturn: systems, technology,
analysis, service, structural problem-solving. Add that Shani rules this house
and runs the 2028–2030 antardasha, and the career reading from §07 is now
supported three independent ways.

Against this, the **10th house itself is only rank 9** with a failing lord. The
message is consistent: **career here is built, not conferred.** It comes through
6th-house means — competence, service and endurance — rather than through
10th-house means of position and appointment.

### The 12th house is the strongest in the chart

At **12.59 rupas the 12th outranks the second-place house by 36%** — an
extraordinary margin. Its lord is Surya: exalted, the chart's strongest graha,
forming Vimala Yoga.

This is a decisive confirmation of §03. But note the nuance the two metrics
together provide: the 12th's Bhava Bala comes almost entirely from its lord's
enormous 683.48 contribution, while its own SAV is a modest 24. So the 12th is
**powered by the Sun specifically rather than broadly fertile**. Its strength
flows through solar significations — authority, soul, self-realisation — and
through the 12th's own domain of foreign lands, seclusion, retreat and release.

Read alongside Rahu in the 9th and the Ketu–Budha nakshatra loop, the thread
running through foreign residence, withdrawal and work done away from the public
eye is not incidental to this chart. It is the chart's strongest single
structure.

### Correction: partnership and wealth are better founded than I said

Two of §07's readings need revising **upward**, and the new tables are what
changed them.

**Partnership.** I read the 7th as a consistently difficult area, on the strength
of Ketu touching it in four vargas. That evidence stands. But the 7th house is
**4th strongest in Bhava Bala** and carries **33 bindus, the second-highest SAV
in the chart** — and its lord Guru is the second-strongest graha. The accurate
reading is therefore: **the house is well built; the occupants are difficult.**
Partnership is not structurally weak here. It is structurally sound and karmically
complicated, which is a materially different proposition, and a more hopeful one.
The practical advice from §07 is unchanged — deliberate, later, consciously
chosen — but the expected outcome of following it is better than I implied. The
one number that supports caution is the 7th's Drishti Bala of just **+8.59**,
second-lowest: little aspectual help arrives, so the work has to be done rather
than hoped for.

**Wealth.** I called the 2nd lord in the 8th "poor for linear accumulation." That
is still true of the *mechanism*, but I understated the *capacity*. The 2nd house
is **3rd strongest in Bhava Bala**, carries **the highest Drishti Bala in the
chart at +99.83** — three grahas aspect it from the 8th, exactly as the §06
aspect table showed — and its lord Shukra has the chart's **highest Ishta Phala**.
Wealth is well supported. It simply arrives through 8th-house channels rather
than by accumulation.

The genuine caution sits elsewhere: the **11th house is rank 11** with a
Shodhya Pinda-starved lord, and Gulika and Mandi both sit there. Set against the
strong D11 from §07, the honest synthesis is that **gain capacity is high but
the gains house is weak** — income arrives through the specific channels D11
indicates (knowledge, advisory, networks) rather than accumulating broadly. This
strengthens rather than weakens the earlier caution against leverage.

### Shodhya Pinda

| Graha | Rashi | Graha | **Shodhya** |
|---|---|---|---|
| Mangal | 164 | 48 | **212** |
| Shani | 133 | 51 | **184** |
| Lagna | 95 | 70 | 165 |
| Budha | 94 | 58 | 152 |
| Surya | 120 | 18 | 138 |
| Shukra | 78 | 17 | 95 |
| Guru | 61 | 20 | 81 |
| **Chandra** | 33 | **0** | **33** |

Read comparatively — the safe use of this measure — two entries stand out.
**Mangal is highest at 212** despite ranking only 3rd in Shadbala, which means
Mars periods deliver substantially; combined with its net −19.21 outcome
balance, they deliver **forcefully rather than gently**. That confirms the
caution in §09 about Rahu–Mangal closing the mahadasha in 2039–40.

And **Chandra at 33, with a Graha Pinda of exactly zero**, is the fourth
independent indicator of the weak Moon discussed in §10.

### What this does to the timeline

Applying the outcome balances to §09's antardasha sequence sharpens three calls
and changes one:

| Period | Lord's net | Rules | Revised read |
|---|---|---|---|
| **Rahu–Guru** (to Jan 2028) | +22.20 | 4th (rank 2), 7th (rank 4) | **Confirmed strong.** Activates the 2nd- and 4th-strongest houses. Caveat: Guru has the chart's worst Drik Bala (−8.58), the most aspect-afflicted graha — the good arrives with interference and criticism attached. |
| **Rahu–Shani** (2028–30) | −34.35 | 5th, **6th (41 bindus)** | **Confirmed, and sharpened.** Strongest-but-harshest graha, ruling the chart's most fertile house. Most productive and most punishing at once. |
| **Rahu–Budha** (2030–33) | −11.41 | 1st, 10th | **Upgraded to the chief concern.** The only graha failing its minimum, net-malefic, with the chart's lowest Dig Bala, running its own 2.5-year period over self and career. More structurally vulnerable than the shorter Rahu–Ketu that follows. |
| **Rahu–Shukra** (2034–37) | +35.62 | 2nd (rank 3), 9th | **Confirmed as the material peak.** Highest Ishta Phala in the chart, ruling the 3rd-strongest house. |
| **Rahu–Surya** (2037–38) | **+39.05** | **12th (rank 1)** | **Revised upward.** I called this a wind-down. It is the chart's strongest and most benign graha ruling its strongest house — short at 0.9 years, but likely a genuine high point. |

---

## 12. The career arc

Pulling every career indicator in the chart into one sequence.

### What the work is

Six independent indicators converge on the same territory:

| Indicator | Points at |
|---|---|
| Kanya lagna, Budha as lagna lord | Analysis, diagnosis, precision, systems, service |
| **D10 lagna Kumbha**, lord Shani | Technology, large systems, networks, structure, research |
| **6th house Kumbha at 41 bindus** | Competition, troubleshooting, service, applied problem-solving |
| Shukra in **Vrischika** on D10's 10th | Depth work — finance, risk, insurance, investigation, psychology, data |
| **Rahu in D10's 8th** | Research, hidden or protected data, audit, security, foreign involvement |
| Ketu–Budha nakshatra loop | Forensic, self-taught, first-principles investigation |

Note the convergence flagged in §11: **Kumbha is both the D10 ascendant and the
natal chart's 41-bindu house.** Two different techniques, one answer. The work is
**technical and analytical with an investigative edge** — the kind of role where
you are handed something broken, opaque or contested and made responsible for
resolving it.

### Why it is built rather than conferred

The 10th house itself is unremarkable: **Bhava Bala rank 9**, SAV 29, exactly
average. Its lord Budha is **the only graha in the chart failing its Shadbala
minimum**, and the kendras are nearly empty — so there is no inherited platform,
no structural head start, and no easy appointment mechanism.

What there *is*, is the 6th house at 41 bindus and **Amala Yoga** — Guru, the
second-strongest graha, sitting in the 10th. That combination has a specific
meaning: **advancement comes through demonstrated competence and accumulated
reputation, not through position or patronage.** Slow to start, compounding
once started. The Amala reputation asset is real but it is a *stock*, not a
*flow* — it builds quietly for years before it pays.

Two structural cautions sit alongside it. Five D10 grahas sit at 26–29° of their
signs, which reads as **discontinuity** — a career assembled from discrete moves
rather than internal promotion. And Budha's combustion means **visibility lags
ability**, persistently and by design.

### The arc is back-loaded — this is the headline

The dasha table supplied ends at Dec 2040. The most important career fact lies
just past it.

| Mahadasha | Dates | Ages | Career meaning |
|---|---|---|---|
| **Rahu** | Dec 2022 – Dec 2040 | 20.7 – 38.7 | **Construction.** Unconventional, non-linear, foreign-inflected. Builds the material. |
| **Guru** | **Dec 2040 – Dec 2056** | **38.7 – 54.7** | **The payoff.** Guru is the graha *sitting in the 10th house* — Amala Yoga giver, 2nd-strongest graha, net Ishta +22.20. |
| Shani | Dec 2056 – Dec 2075 | 54.7 – 73.7 | Consolidation, institutional weight — strong but harsh (worst Kashta in the chart). |

**The sixteen-year mahadasha of the planet occupying the 10th house runs across
ages 39 to 55** — precisely the decades in which professional authority normally
matures. That is the chart's answer to the career question, and it is
unambiguous: **this is a late-cresting career.**

It is also internally consistent with everything else. A combust lagna lord
means ability surfaces late. Vimala Yoga means the rise follows adversity. The
8th–9th exchange means fortune arrives through difficulty. All four say the same
thing: the first fifteen working years are the investment, not the return.

The practical consequence matters more than the prediction. Comparing himself at
28 or 32 against peers on conventional ladders will read as falling behind, and
by conventional metrics it will *be* behind. The chart says that comparison is
measuring the wrong window.

### Phase by phase

**Ages 20.7 – 23.4 · Rahu–Rahu · Dec 2022 – Sep 2025 — past.** The disoriented
launch. Rahu's own sub-period inside its mahadasha is classically the least
legible stretch of the whole eighteen years: ambition without direction, false
starts, possibly a change of field or place.

**Ages 23.4 – 25.8 · Rahu–Guru · to Jan 2028 — now.** Guru rules the 4th and
7th (Bhava ranks 2 and 4) from the 10th. The window for **first real
professional standing** — a mentor, a credential, an advisory or teaching
component, visible reputation. Rahu in the 9th adds foreign study, travel,
publishing. The age-24 Jupiter return falls here.
*Caveat:* Guru carries the chart's worst Drik Bala (−8.58), sits in an enemy's
sign, and has Yama Ghantaka 2° away. Expect interference, politics, criticism,
and advice that overpromises. **This period rewards narrowing to one direction,
not adding options.**

**Ages 25.8 – 28.6 · Rahu–Shani · Jan 2028 – Dec 2030 — the foundation.** The
single most career-defining stretch of the mahadasha. Shani is the D10 lagna
lord, sits in D9's 10th, and rules the 41-bindu 6th house — three independent
career credentials, all Saturn's. Expect a long, heavy, grinding project that
ends up defining the résumé; real responsibility; authority earned slowly.
Shadbala rank 2 but the **worst outcome balance in the chart**: it will deliver,
and it will cost. Health and routine stop being optional.

**Ages 28.6 – 31.2 · Rahu–Budha · Dec 2030 – Jun 2033 — the vulnerable stretch,
and the strategic hinge.** The lagna-and-10th lord runs its own 2.5-year period
while being the chart's only failing graha, net-malefic, with the lowest Dig
Bala. The Saturn return lands here (~late 2031). Expect a genuine reassessment
of direction, output-heavy but recognition-light, and the highest health and
nervous-system exposure of the mahadasha.
*But note the shape of the weakness.* Budha's Chesta Bala is 42.15 — near the
top of the chart — while its Dig Bala is 4.28. **Motion is strong; position is
weak.** The correct response is not to work harder in place but to **change
position** — role, employer, city, country. This is the period where relocating
or repositioning is likely to be worth more than any amount of additional
effort.

**Ages 31.2 – 32.2 · Rahu–Ketu · Jun 2033 – Jul 2034 — hold.** Short and
destabilising, with Ketu gandanta in the 3rd. Consolidate, research, withdraw.
Poor for launching ventures or making irreversible commitments.

**Ages 32.2 – 35.2 · Rahu–Shukra · Jul 2034 – Jul 2037 — the material peak of
the Rahu dasha.** Shukra holds the chart's highest Ishta Phala (47.49) and rules
the 2nd (rank 3) and 9th. Resources, capital, and standing all improve.
*One caution:* Saturn transits Mithuna — the 10th house — around 2033–2035, and
**Shani has only 1 bindu there, the weakest planet-sign cell in the entire
Ashtakavarga.** So the money and the visible position may diverge in that
window: materially good, positionally frustrating.

**Ages 35.2 – 36.1 · Rahu–Surya · 2037 – 2038 — short and excellent.** The
chart's strongest and most benign graha ruling its strongest house. Recognition
and authority; the 12th-house flavour suggests it arrives through foreign,
behind-the-scenes or research channels rather than public position. The age-36
Jupiter return falls here.

**Ages 36.1 – 38.7 · Rahu–Chandra, then Rahu–Mangal · 2038 – Dec 2040.** Gentle,
then forceful. Mangal closes the mahadasha carrying the highest Shodhya Pinda in
the chart (212) alongside a heavily negative outcome balance — expect a
disruptive transition right at the dasha junction, immediately before the Guru
period opens.

**Age 38.7 onward · Guru Mahadasha · from Dec 2040 — the second act.** Guru-Guru
opens it (Dec 2040 – Feb 2043), followed by Guru–Shani (to Aug 2045) and
Guru–Budha (to Dec 2047). The graha in the 10th running its own sixteen years,
with Amala Yoga finally cashing the reputation it has been accumulating since
the twenties.

### Summary of the career reading

- **Field:** technical, analytical, investigative — systems, data, research,
  risk, security, diagnostics. Aquarius–Scorpio territory, not a general
  management track.
- **Mechanism:** competence and reputation, not position or patronage. Won
  through the 6th house — out-working and out-analysing the problem.
- **Shape:** discontinuous. Discrete moves between roles and places, not one
  ladder.
- **Timing:** foundation 2028–2030, hinge 2030–2033, material gains 2034–2037,
  **authority from 2040**.
- **The single highest-leverage variable is position, not effort** — the one
  place the chart is explicit about what to change.

---

## 13. Current transits — authority and marriage

> **Dated snapshot: 8 August 2026.** Unlike the rest of this document, which is
> structural and permanent, this section reads a moment. The Sun at 21°35′
> sidereal Karka dates the transit chart to 6–8 August 2026; the fast-moving
> bodies below are valid for weeks, the slow ones for years.

### Where the transits fall

| Transit | Sign | From lagna | From Moon | Own bindus | Sign SAV |
|---|---|---|---|---|---|
| Surya | Karka | 11th | 3rd | 3 | 28 |
| Chandra | Vrishabha | 9th | 1st | 2 | 22 |
| Mangal | Mithuna | **10th** | 2nd | 4 | 29 |
| Budha | Karka | 11th | 3rd | 2 | 28 |
| **Guru** (combust) | Karka | 11th | 3rd | **5** | 28 |
| Shukra | Kanya | **1st** | 5th | **5** | 29 |
| **Shani** | Meena | **7th** | **11th** | **5** | **33** |
| **Rahu** | Kumbha | **6th** | 10th | — | **41** |
| Ketu | Simha | 12th | 4th | — | 24 |

Two structural facts frame everything else.

**He is not in Sade Sati.** Saturn in Meena is the **11th from the natal Moon** —
one of the most favourable Saturn positions in gochara, giving gains and relief.
Sade Sati only begins when Saturn enters Mesha, the 12th from the natal Moon,
in roughly the **second half of 2027**. The present window is therefore
comparatively unobstructed, and that will not be true again for a long time.

**Three slow transits carry 5 bindus each** — Guru, Shukra and Shani — all above
the classical 4-bindu threshold at which a transit is held to deliver. Saturn in
particular transits **Meena, a 33-bindu house**, the second-highest in the chart.
These are supported transits, not merely present ones.

### Marriage — the window is open now

Three independent activators of the 7th house are running simultaneously, which
is the classical signature for marriage timing:

1. **The antardasha lord is the 7th lord.** Guru rules the 7th from Kanya lagna,
   and Rahu–Guru runs to **31 January 2028**.
2. **Transit Shani is sitting in the natal 7th house** — Meena — with 5 bindus,
   in the chart's second-highest-bindu house. Saturn has been there since
   ~March 2025 and leaves in the second half of 2027.
3. **Transit Guru, exalted in Karka, aspects the natal 7th** by its 9th aspect
   (Karka to Meena is the 9th sign). Jupiter stays in Karka until roughly
   mid-2027.

Add two supports: **transit Shukra — the natural karaka of marriage, and the
graha with the highest Ishta Phala in this chart — is in the natal lagna** right
now; and Sade Sati has not begun.

One timing detail worth having. **Transit Guru is currently combust**, 7°24′ from
the Sun against an 11° limit. The Sun pulls away at 0.73°/day, so Jupiter
**clears combustion around 13 August 2026**. The 7th lord's transit capacity is
muted this fortnight and improves markedly from mid-August.

**Reading:** this is the clearest marriage window the chart offers in the visible
timeline — effectively **late August 2026 through mid-2027**, with an outer bound
of January 2028 when the Guru antardasha ends. It is also the window in which
Guru rules the 4th, so marriage and settling a home read as one movement rather
than two.

The counterweights from §07 do not disappear because the timing is good:

- Ketu touches the 7th in **four separate vargas**; the karmic complication is
  structural, not situational.
- Partial Manglik from both Chandra and Shukra.
- **Saturn in the 7th means slow and serious rather than swept-up** — formalising
  something considered, often with an older or more sober partner. Saturn
  delays and then confirms; it rarely does sudden.
- In D9 the 7th lord sits in the 6th — friction and service inside partnership.

Set against a 7th house that is **Bhava rank 4 with 33 bindus**, the honest
composite is: a well-built house, a difficult tenant, and a genuinely open door
for about eighteen months. This chart's 7th responds to deliberate choice, not
to drift.

**If this window passes**, the next comparable one is **Rahu–Shukra, 2034–2037** —
Shukra being the natural karaka of marriage, ruling the 2nd house of family, and
holding the chart's highest Ishta Phala. Nothing between 2028 and 2034 activates
the 7th with similar force.

### Authority — yes, but of a particular kind, on a particular schedule

**What the present transits support.** **Rahu, the mahadasha lord, is transiting
the natal 6th house** — which is simultaneously Rahu's own most favourable house,
the chart's **41-bindu high point**, and the **D10 ascendant sign**. Three
independent reasons that placement is strong, all at once. Add transit Mangal
crossing the natal 10th and exalted Guru in the 11th, and the next several months
genuinely favour advancement: winning a competitive situation, being handed
ownership of something, a step up in responsibility.

**What they do not support** is a large positional title, and the reason is
structural rather than transitory. The natal 10th is **Bhava rank 9** with a lord
that is the only graha failing its Shadbala minimum; there is no
Panchamahapurusha yoga; and Surya — the karaka of authority, and by far the
strongest graha here — sits in the **8th** while ruling the **12th**.

That combination is specific about *what kind* of authority this is. Not
administrative command over large numbers of people. **Authority of the expert
and the trusted advisor**: a technical or research lead, a principal, the head of
a function, someone whose judgement is decisive within a domain. And with a
persistent behind-the-scenes quality — the strongest house is the 12th, the
authority karaka is in the 8th, and Rahu occupies the 8th of the D10.

**The schedule is the real answer**, and Sade Sati is what shapes it:

| Window | What happens |
|---|---|
| **Now → Jan 2028** | Unobstructed. Responsibility and recognition, a step up in ownership — real, but not the title. **Use it; it is the last clear run for years.** |
| **~H2 2027 → ~2035** | **Sade Sati.** Saturn crosses Mesha (3 bindus), Vrishabha (2), Mithuna (1). |
| **2028–2030** | Rahu–Shani. Authority *earned* — heavy load, slow recognition. Sade Sati's first phase overlaps exactly. |
| **~2030–2032** | The hardest convergence in the chart: Sade Sati's peak phase over the natal Moon, **plus** the Rahu–Budha antardasha of the failing lagna lord, **plus** the Saturn return. |
| **~2032–2035** | Saturn crosses **Mithuna, the natal 10th, where it holds 1 bindu — the weakest planet-sign cell in the entire Ashtakavarga.** Career visibility at its most suppressed even as material conditions improve under Rahu–Shukra. |
| **From Dec 2040** | **Guru mahadasha.** The graha in the 10th, Amala Yoga giver, runs sixteen years across ages 39–55. This is where authority consolidates. |

So the answer on authority is **yes — but the climb runs straight through Sade
Sati, and that is precisely why §12 reads this as a late-cresting career.** The
sequence is: recognition now, authority earned 2028–2030, visibility suppressed
2032–2035, authority held from 2040.

---

## 14. Summary

A **Virgo lagna repeating across three vargas**, with a **combust lagna lord
that also rules the 10th**, sitting in the 8th under an **exalted, gandanta
Sun** — and a nakshatra chain that closes in a **Ketu–Budha loop**. Eight of
nine grahas are packed into houses 8, 9 and 10, and the chart's spine is a
**Mangal–Shukra exchange between the 8th and 9th**, reinforced by **Vimala
Yoga**.

Read as one statement: this is a narrow, deep, investigative chart whose fortune
is routed through exactly the material most people avoid.

The strength data reshapes the balance sheet. The **real asset is the Sun** —
2.28× its requirement, the best outcome balance in the chart, ruling the
strongest house. The **real liability is Budha**, the only graha failing its
minimum, ruling both the self and the career, and failing specifically on
*position* rather than on capacity. And two things I first read as assets or
deficits turned out to be neither: the exalted **Moon is thin, not strong**, and
the **7th house is well built** even though its occupants are difficult.

The sharpest structural fact is that the two houses holding seven of nine grahas
carry the chart's two **lowest** Sarvashtakavarga scores, while the empty 6th
carries the highest at 41. **All the activity is concentrated where results come
hardest, and the fertile ground is somewhere else.**

The strategic reading:

1. **Go deep, not wide.** The chart has no talent for breadth and enormous
   talent for depth. Every configuration rewards specialising into something
   difficult and unfashionable.
2. **Compete and serve rather than position and wait.** The 41-bindu 6th, the
   Aquarius D10 lagna and the rank-9 tenth house all say results come from
   out-working and out-analysing the problem, not from appointment or title.
3. **Change position, don't just push harder.** Budha's deficit is entirely
   directional — dig bala 4.28 out of 60 — while its motional strength is near
   the top of the chart. What is under-resourced is *where you stand*, not what
   you can do. Environment, role and location are the high-leverage variables.
4. **Build structure deliberately, because the chart doesn't supply it.** Empty
   kendras mean routine, deadlines and external commitments have to be
   installed by hand. Rahu–Shani (2028–2030) will impose this anyway; adopting
   it early converts an ordeal into an advantage.
5. **Use the current window (to Jan 2028) to commit, not to expand.** It
   activates the 2nd- and 4th-strongest houses, but Guru is the chart's most
   aspect-afflicted graha — expect the good to arrive with interference. Narrow:
   one direction, one mentor, one decision on the partnership question.
6. **Treat partnership as a conscious project — with better odds than the
   affliction alone suggests.** Ketu across four vargas is real, but so is a
   rank-4 house with 33 bindus and the chart's second-strongest graha as its
   lord. Deliberate and later, and the foundation is genuinely sound.
7. **Protect the nervous system — this is now a primary finding, not a
   footnote.** A failing lagna lord and a Moon that is thin by four independent
   measures describe a system with limited reserves. Rest and routine are
   structural requirements. Rahu–Budha (2030–2033) is the window that most
   demands this.
8. **The contemplative pull is native equipment.** A nakshatra chain terminating
   in Ketu, both Ketu and the Sun in gandanta, and the 12th house standing as
   the single strongest bhava in the chart — that is the same instruction given
   three times over.

The chart's own summary of itself is the 8th–9th exchange plus Vimala Yoga
stated twice over: **the difficulty and the fortune are the same object.**

---

*Prepared from the supplied D1, D9, D10, D11, D8, D27, D30, upagraha,
Vimshottari, Shadbala, Bhava Bala, Ashtakavarga and Shodhya Pinda data.
Divisional charts and dasha boundaries independently recomputed and verified
(`verify_chart.py`); all strength tables independently reconciled
(`verify_bala.py`). Two data errors in the source (D8 and D30 Ketu) are
corrected above. Sections 10 and 11 revise three conclusions from the earlier
sections — the Moon downward, partnership and wealth upward — and those
revisions are marked where they occur.*
