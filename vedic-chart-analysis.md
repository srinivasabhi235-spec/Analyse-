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

## 10. Summary

A **Virgo lagna repeating across three vargas**, with a **combust lagna lord
that also rules the 10th**, sitting in the 8th under an **exalted, gandanta
Sun** — and a nakshatra chain that closes in a **Ketu–Budha loop**. Eight of
nine grahas are packed into houses 8, 9 and 10, and the chart's spine is a
**Mangal–Shukra exchange between the 8th and 9th**, reinforced by **Vimala
Yoga**.

Read as one statement: this is a narrow, deep, investigative chart whose fortune
is routed through exactly the material most people avoid. Its real assets are an
exceptionally strong Sun and a near-peak exalted Moon; its real deficits are an
almost empty set of kendras (structure) and a 7th house touched by Ketu in four
separate vargas (partnership).

The strategic reading is unusually clear:

1. **Go deep, not wide.** The chart has no talent for breadth and enormous
   talent for depth. Every configuration rewards specialising into something
   difficult and unfashionable.
2. **Build structure deliberately, because the chart doesn't supply it.** Empty
   kendras mean routine, deadlines and external commitments have to be
   installed by hand. Rahu–Shani (2028–2030) will impose this anyway; adopting
   it early converts it from an ordeal into an advantage.
3. **Use the current window (to Jan 2028) to commit, not to expand.** Guru in an
   enemy's sign and in D9's 6th rewards narrowing. One direction, one mentor,
   one decision on the partnership question.
4. **Treat partnership as a conscious project.** The signal is consistent
   enough across D1, D9, D27 and D30 to warrant deliberateness and patience
   rather than default timing.
5. **Protect the nervous system.** A combust Mercury ruling a Virgo lagna from
   the 8th, with the Moon under Saturn–Mars–Rahu pressure, describes a system
   that runs hot and has no automatic off-switch.
6. **The contemplative pull is native equipment, not a distraction.** A chart
   whose nakshatra chain terminates in Ketu, with Ketu in gandanta and the Sun
   in gandanta, is telling the same thing twice. Practice is load-bearing here.

The chart's own summary of itself is the 8th–9th exchange plus Vimala Yoga
stated twice over: **the difficulty and the fortune are the same object.**

---

*Prepared from the supplied D1, D9, D10, D11, D8, D27, D30, upagraha and
Vimshottari data. Divisional charts and dasha boundaries independently
recomputed and verified; see `verify_chart.py`. Two data errors in the source
(D8 and D30 Ketu) are corrected above.*
