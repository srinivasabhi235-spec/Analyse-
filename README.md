# Analyse-

A complete Parashari reading of a single Vedic natal chart, computed from the
birth moment with the Swiss Ephemeris and cross-checked against every supplied
table.

**Birth data:** 15 April 2002, 18:02:45 IST, Guntur, Andhra Pradesh, India.
The nine grahas reproduce the supplied chart to **under one arcminute**; the
whole Vimshottari timeline reproduces to the month; and three predictions the
reading had made *from the chart alone, before the data arrived* — the date,
the weekday and the tithi — all held.

## How the reading is organised

The document is in three parts, and the third is not an appendix.

| Part | Sections | What it is |
|---|---|---|
| **I — The chart** | 1–7 | Positions, dignity, houses and lords, drishti, strength, ashtakavarga, Jaimini — every table generated from `ground.py` |
| **II — The structure** | 8–9 | The one configuration everything else restates, and what kind of exchange it is |
| **III — Time** | 10–11 | Vimshottari, what has been spent, and what is coming |
| **IV — The questions** | 12–15 | Career, marriage and its timing, place, transformation |
| **V — Method** | 16–20 | Derived against supplied, every dispute priced, what checks the document, what is not known |

The previous hand-written version — 73 sections, 10,873 lines, grown by
appending over many sessions — is kept at
[`archive/reading-v1.md`](archive/reading-v1.md), with its bhava-krama companion
at [`archive/bhava-krama-v1.md`](archive/bhava-krama-v1.md). It carries
long-form answers and a chapter-provenance audit this version summarises rather
than reproduces. It is archived, not deleted, and it is no longer the
deliverable: it was written, and this one is generated.

## Contents

| File | What it is |
|---|---|
| [`bhava-krama.md`](bhava-krama.md) | **The reading rebuilt in classical order** — all twelve bhavas judged through the Parāśari ten-step sequence, no technique given a percentage weight and none allowed to speak before its turn |
| [`bhava-krama.html`](bhava-krama.html) | The same, as a formatted page |
| [`vedic-chart-analysis.md`](vedic-chart-analysis.md) | **The reading** — concepts, the questions asked, the questions not asked |
| [`chart-reading.html`](chart-reading.html) | The same reading as a formatted page, generated from the markdown |
| [`ephem_core.py`](ephem_core.py) | Shared Swiss Ephemeris engine — birth moment, positions, rise/set, and the varga rules for all 28 schemes |
| [`verify_birthdata.py`](verify_birthdata.py) | Tests the birth moment against the chart: graha-by-graha agreement, the ayanamsa variant, the ascendant residual measured across 27 vargas, the panchanga, and the dasha rebuilt from the exact Moon |
| [`verify_chalit.py`](verify_chalit.py) | **Bhava Chalit** — four house systems, which grahas move under each, and which yogas survive. Closes the gap audit's largest item |
| [`verify_upagraha.py`](verify_upagraha.py) | All eleven upagrahas recomputed from sunrise, with the source's own convention reverse-engineered from the data |
| [`verify_transits.py`](verify_transits.py) | Every transit to 2070 computed to the day, retrogrades included — Sade Sati, Ashtama Shani, the three returns, the Bhrigu Bindu, and the eclipse series |
| [`build_allvargas.py`](build_allvargas.py) | The twelve vargas outside the Shodashavarga, D8 and D11 rebuilt from recovered rules, and a dignity census across all 28 schemes |
| [`build_charts.py`](build_charts.py) | Computes and emits all sixteen Shodashavarga charts in full — master grid, dignity tally, and each varga with houses and classes |
| [`build_html.py`](build_html.py) | Regenerates the HTML page from the markdown, preserving the design system |
| [`verify_chart.py`](verify_chart.py) | Verifies positions, divisional charts, nakshatras, gandanta, dasha |
| [`verify_bala.py`](verify_bala.py) | Verifies Shadbala, Bhava Bala, Ashtakavarga, Reduced Ashtakavarga, Shodhya Pinda |
| [`verify_timeline.py`](verify_timeline.py) | Merges dasha and antardasha against Saturn and Jupiter transits into one life timeline, and scores every year 2026–2076 for transformation-window intensity |
| [`verify_shodasha.py`](verify_shodasha.py) | Computes all sixteen Shodashavarga charts, Vimshopaka Bala and the Vaiseshikamsha dignity census |
| [`verify_houseclass.py`](verify_houseclass.py) | Kendra/trikona/upachaya/dusthana census across all seven vargas |
| [`verify_pastfuture.py`](verify_pastfuture.py) | Past against future in detail — how the outputs differ across eight dimensions, including a weighting reversal the script reports rather than hides |
| [`verify_titlesweep.py`](verify_titlesweep.py) | The whole reading swept against Parashara's chapter titles as a checklist — and Yogini dasha computed as an independent second timeline, which confirms the December 2030 hinge to within eighteen days |
| [`verify_rahutransit.py`](verify_rahutransit.py) | Tests the claim that Rahu through Dhanishtha matters because it touches the D10 ascendant — computes the two windows and their real end dates, maps the transit into the D10 properly, and finds the reason the claim should have given |
| [`verify_loop.py`](verify_loop.py) | Tests whether a closed dispositor loop means adversity converts to good — classifies the chart's single parivartana by type for the first time (Dainya, not Maha), checks whether its one viparita yoga fires, and sets the measured delivery-cost correlation against the assumption |
| [`verify_d81.py`](verify_d81.py) | Computes the D81 nava-navamsa in full, measures its precision (one division = 93 seconds of birth time; the grahas are stable, the lagna is not), and audits section 2's undertaking to flag any claim resting on the D12, D24, D36 or D60 ascendant — reproducing section 2's eight movers and 19-of-27 exactly, and finding three published claims that were never flagged |
| [`verify_shani8.py`](verify_shani8.py) | Transit Saturn through the 8th house: every ingress, retrograde pass and exact crossing of the three natal grahas there; the Ashtakavarga rebuilt from the benefic-place tables (11 of 12 signs and 336 of 337 bindus reproduce the supplied sheet, the one discrepancy localised to Venus in Cancer) so that kakshya can be computed; vedha tested under both schools; and the Saturn antardasha and Jupiter double transit that run underneath it |
| [`verify_exchange.py`](verify_exchange.py) | Tests an externally supplied reading of the chart's 8th–9th parivartana against the chart: the two lords' mutual non-aspect (never checked in sixteen prior mentions), the Dainya typology against the trikona/dusthana reading, each of the six named significations, the Vimshottari arithmetic showing both lords' mahadashas are out of play, and the own-sign substitution measured rather than assumed |
| [`verify_partner.py`](verify_partner.py) | Times the 7th house: the carriers (7th lord, Upapada lord, Darakaraka, Shukra), every remaining period one of them rules, the double transit scanned month by month rather than by ingress, and the pratyantardasha resolution of the window now running |
| [`ground.py`](ground.py) | Derives every fact the reading rests on from the birth moment and tags the handful that cannot be derived as SUPPLIED — 206 facts, 159 derived, 47 supplied. Nothing downstream types a number twice |
| [`compose.py`](compose.py) | Generates `vedic-chart-analysis.md` from `ground.py`. Every figure is looked up at build time, so a value cannot drift between sections |
| [`react_loop.py`](react_loop.py) | Reads the generated document back and re-derives every claim it can parse — reason, act, observe, reflect, run to fixpoint. Returns PASS, FAIL or CONTINGENT, and declines to act where it cannot resolve the frame |
| [`verify_trigger.py`](verify_trigger.py) | Asks whether an eclipse triggers events for an individual at all — separates what classical method licenses from popular elaboration, computes the gochara position and tara bala of the eclipse (both favourable), and shows the dasha underneath is doing the work |
| [`verify_relocation.py`](verify_relocation.py) | Settles what relocation does and does not change in Jyotisha, then recomputes the whole eclipse table from American longitudes — the eclipse dismissed as invisible becomes visible, a career-house eclipse dismissed for India reappears nearly overhead from New York, and the strongest one drops below the horizon |
| [`verify_grahan.py`](verify_grahan.py) | Tests whether a lunar eclipse can affect the D10 ascendant — the strict varga mapping, the standing refusal to run transits through vargas, the eclipse's altitude at the birthplace, and a corrected decade-long eclipse table that finds the two total eclipses landing on the natal 10th |
| [`verify_field.py`](verify_field.py) | Separates finding a field from deepening it — computes the chara karakas and the Amatyakaraka for the first time, the 10th from Karakamsa, and the D24 varga of learning, then times the two eras independently |
| [`verify_place.py`](verify_place.py) | Computes the four houses that can mean "his place" — the 4th, 10th, 11th and 12th — side by side in the classical sequence, ranks them, and times each by its lord's and karaka's periods plus Jupiter's transits through them |
| [`verify_marriage_when.py`](verify_marriage_when.py) | Times the marriage question at step 9 — computes the Upapada (the 7th lord and the Upapada lord turn out to be the same graha), the pratyantardasha structure inside the current window, and every double transit on the 7th house between 2026 and 2040 |
| [`verify_ashlesha.py`](verify_ashlesha.py) | Tests the claim that Jupiter through Ashlesha stirs fears into dreams — computes the two-window passage with its retrograde re-entry, the gochara verdict from the Moon, the natal dream apparatus, and the three gandanta crossings into and out of the 12th house that the claim never mentions |
| [`verify_krama_all.py`](verify_krama_all.py) | Runs the classical ten-step bhava sequence on all twelve houses and produces the full computed workup `bhava-krama.md` is written from — plus the cross-bhava facts only a complete pass exposes: eight empty bhavas, three untouched entirely, and all twelve house lords standing in three adjacent houses |
| [`verify_bhavakrama.py`](verify_bhavakrama.py) | Runs the classical bhava-judgment sequence in strict order on the 10th house — subject, bhava, bhava lord, karaka, varga, planetary strength, bhava strength, yogas, dasha, Ashtakavarga — recording the running verdict after each step to test whether the reading's career conclusions depend on the order its evidence was gathered in |
| [`verify_vol1.py`](verify_vol1.py) | Works the BPHS chapters 1–45 contents page — maps all nineteen foundational technique families to chapters, checks the sixteen divisions the reading built against the sixteen chapter 6 names, shows chapter 28 makes the chapter-73 ray scaling testable against supplied data, sweeps all sixty-one yogas in chapters 35–38, and finds Kanya to be the only lagna of twelve with a fully mirror-symmetric lordship map |
| [`verify_foundation.py`](verify_foundation.py) | Prices the eight school-dependent rules that live in the forty-one BPHS chapters no contents page covers — finds that six Shodashavarga members carry the same disputed starting-sign defect section 12 declined six other vargas for, bounds Vimshopaka Bala exactly under every possible rule, and shows all six adjacencies in the strength order are reversible |
| [`verify_remaining.py`](verify_remaining.py) | Closes every BPHS chapter still closable — the five elements and three gunas (both of which turn out to restate the stellium), the rays with their scaling assumption labelled, sookshma and prana computed and then declared out of scope, four more maraka sub-topics, and the fifteen inauspicious-birth conditions of chapters 85–94 tested for the first time, all fifteen negative |
| [`verify_tocgaps.py`](verify_tocgaps.py) | Closes the three gaps the BPHS contents pages exposed — Lajjitadi and Deeptadi avasthas computed and Sayanadi declined, the classical sannyasa combinations tested for the first time, and the penury combinations tested for the first time |
| [`verify_career_d1d9.py`](verify_career_d1d9.py) | Career read from the rashi chart and the navamsa alone, with no D10 and no strength measures — the 10th from lagna, Chandra and Surya; argala on the career house; the arudha of the 10th; and the 10th lord's navamsa read as the fate of the profession |
| [`verify_jobloss.py`](verify_jobloss.py) | Job loss and career disruption — bhavat bhavam on the 10th, the aspect census that shows nothing can reach the career house, the single dated vulnerable window where Saturn crosses the 10th on one bindu, and whether loss arrives or is chosen |
| [`verify_gochara.py`](verify_gochara.py) | A supplied live transit table verified against Swiss Ephemeris to the arcminute — including one row that does not reconcile — then read as gochara from the natal Moon and lagna, weighted by each transiting graha's own bindus |
| [`verify_housenature.py`](verify_housenature.py) | All six house-classification schemes assembled and applied — angle, benefit, purushartha, maraka, badhaka and modality — plus the functional benefic/malefic table derived from lordship, and the kendra/apoklima census |
| [`verify_navamsa.py`](verify_navamsa.py) | The D9 read as a chart rather than a table row — its own lagna and house lords, dignity gained and lost between D1 and D9, vargottama, the yogas it does not carry, the D9 seventh, and the 64th navamsa from both the Moon and the lagna |
| [`verify_bhanga.py`](verify_bhanga.py) | Every classical cancellation doctrine tested against this chart — Kuja dosha and its bhangas (computed here for the first time), Kemadruma, neecha bhanga, papakartari, the combustion exemption, yoga bhanga, and the viparita yoga that may be cancelled by its own lord being too strong |
| [`verify_rank.py`](verify_rank.py) | A named achievement tier in a selling organisation — what Jyotisha can and cannot say about a corporate rank, the kama trikona and its single occupant, and when the gains apparatus is actually under period support |
| [`verify_placement.py`](verify_placement.py) | The same career and earning question with every strength figure discarded — house lords, aspects, dignity, combustion, exchange and placement-only yogas. Finds a second unaspected house the drishti section had missed, and overturns one of the score-based conclusions |
| [`verify_earning.py`](verify_earning.py) | Career and earning from a job held now — the four channels separated (standing, service, income, retention), the growth curve to 2040, the two maturities that set the timetable, and where transit and antardasha support coincide |
| [`verify_role.py`](verify_role.py) | Which role the coming window names and what kind of authority it carries — the past's assigned positions against three roles entered rather than inherited, and the finding that all three are the same structure |
| [`verify_marsdasha.py`](verify_marsdasha.py) | The Mangal mahadasha opened up — every antardasha with real transits, the three-year Ashtama Shani spine, and what kind of transformation it was |
| [`verify_relinquish.py`](verify_relinquish.py) | Why he sets down what he wanted most — the desire apparatus tested, Ketu's reach across the kama trikona, and whether the mechanism is loss, renunciation or dissolution |
| [`verify_pastwindow.py`](verify_pastwindow.py) | The 8th-house passage he has already lived, scored against the one ahead on the same markers — whether it discharges, repeats, or is a different instrument on the same target |
| [`verify_elapsed.py`](verify_elapsed.py) | What has already been lived — the three finished mahadashas, twenty-four years of falsifiable retrodiction, the maturity table half-fired, and the net balance recomputed over a livable span rather than the nominal 120-year cycle |
| [`verify_deepvarga.py`](verify_deepvarga.py) | The varga apparatus beyond the charts themselves — four Vimshopaka schemes, the sixty named shashtiamshas, the trimshamsha lords, vargottama across all 28, varga-level raja yogas, and Pushkara bhaga |
| [`verify_missed2.py`](verify_missed2.py) | The second pass of un-asked questions — marriage durability, fame, accident risk, escape, Kalapurusha illness mapping, employment mode, purva punya, and children |
| [`verify_unasked.py`](verify_unasked.py) | The areas nobody asked about — father, mother, siblings, speech, the 6th, property, foreign residence, spiritual practice, the blind spots, remedy, and why longevity is declined |
| [`verify_rarity.py`](verify_rarity.py) | Monte Carlo over 200,000 synthetic charts — measures how rare each feature of this nativity actually is, and retracts the ones that turned out ordinary |
| [`verify_gaps.py`](verify_gaps.py) | Gap audit — vargas not computed and why, per-varga birth-time sensitivity, whole techniques never applied, and data never supplied |
| [`verify_love.py`](verify_love.py) | The six registers of affection ranked, every Shukra period dated, and marital satisfaction read in both directions |
| [`verify_perception.py`](verify_perception.py) | How others see him: the Arudha Lagna and what touches it, arudha-relative houses, the 6th of rivals, the 11th of peers, and Drik Bala |
| [`verify_audit.py`](verify_audit.py) | **Master audit** — tests the good-but-with-friction claim, then re-derives and asserts all 53 headline figures the reading rests on |
| [`verify_dispositors.py`](verify_dispositors.py) | Both dispositor chains — rashi and nakshatra — with the house lords routed through their star lords to show who delivers each house |
| [`verify_cost.py`](verify_cost.py) | Tests whether delivery and cost correlate: Shodhya Pinda against Kashta Phala, plus gain/cost quadrants across the remaining timeline |
| [`verify_career.py`](verify_career.py) | Dashamsha audit, the three-fold tenth, the Jaimini career apparatus, and a scored growth curve across every antardasha to 2078 |
| [`verify_inlaws.py`](verify_inlaws.py) | The spouse's family by bhavat bhavam, measured against Bhava Bala ranks and bindu counts, with Upapada and arudha cross-checks |
| [`verify_purpose.py`](verify_purpose.py) | Purushartha trikona tally, the moksha trikona, Atmakaraka and Karakamsa, the gandanta knots, and Ketu's standing across the chart |
| [`verify_eighth.py`](verify_eighth.py) | Full 8th-house dossier: occupants, house-lord routing, ashtakavarga weakness, the parivartana engine, varga repetition, graha maturity |
| [`verify_spouse.py`](verify_spouse.py) | The spouse from five independent apparatuses: 7th house and lord, Shukra, Darakaraka and Darakaramsa, Upapada, and the 7th of D9 |
| [`verify_traits.py`](verify_traits.py) | The character apparatus: nakshatra kootas, avasthas, vargottama, arudha gap, dispositor chain, concentration, temperament yogas |
| [`verify_eclipse.py`](verify_eclipse.py) | Places the 2026–2028 solar eclipse series in the chart; calibrated against the supplied transit set to three arcminutes |
| [`verify_concepts.py`](verify_concepts.py) | Computes the full classical-concept sweep: nabhasa and lunar-solar yogas, avasthas, Jaimini karakas and arudhas, Yogi/Avayogi, KP star-lords, derived D3/D7/D12, sensitive points |

## Source data

D1 (Rashi), D9 (Navamsha), D10 (Dashamsha), D11 (Rudramsha), D8 (Ashtamsha),
D27 (Bhamsha), D30 (Trimshamsha); eleven upagrahas; the Vimshottari dasha tree;
Shadbala with all sub-components; Bhava Bala; Ashtakavarga and Reduced
Ashtakavarga; Shodhya Pinda; and a transit chart for August 2026.

## Verification

Nothing was taken at face value. Every script runs standalone, and
`verify_audit.py` re-derives and asserts all 53 headline figures the reading
rests on:

```
pip install -r requirements.txt   # pyswisseph, for the ephemeris scripts
python3 verify_audit.py           # 53/53 pass
for f in verify_*.py; do python3 "$f"; done
```

Every script runs clean. Sixty-nine scripts, no drift.

| Check | Result |
|---|---|
| D9 and D27 recomputed from D1 longitudes | All 20 positions match to a few arc-seconds |
| Nine Rahu antardashas rebuilt from Vimshottari proportions | Every boundary matches exactly |
| Shadbala sub-components → totals → rupas → rank | Reproduces exactly |
| Bhava Bala: Bhavadhipati + Disha + Drishti | Reproduces all twelve totals |
| Sarvashtakavarga total | **337** — the classical value |
| Reduced Ashtakavarga → Shodhya Pinda | Rebuilds all sixteen values via the standard Gunakara multipliers |

**A retraction.** An earlier pass flagged D8 and D30 as containing node
errors, reasoning that Rahu and Ketu are 180° apart and so must never share a
divisional sign. **That reasoning was wrong and the supplied data was right.**
A 180° separation is exactly six signs, which preserves sign parity and
modality and leaves the degree-in-sign identical — so any varga built as
"starting sign by parity/modality, plus an offset" *must* place both nodes in
the same divisional sign. Only linear-map vargas (D9, D27) separate them.
`build_charts.py` reproduces the supplied D8 and D30 placements exactly.

**Two columns excluded.** The Shadbala table's "Bhava (in %)" row and the Reduced
Ashtakavarga's "Sarv" column do not reconcile against any tested derivation, and
are identified and set aside rather than guessed at.

**Birth data — derived first, then supplied, then confirmed.** Before the data
was given, the reading determined it from the chart alone three ways: the
Vimshottari balance implied **15 April 2002**; Vara Bala of 45 to Chandra
required a **Monday**; Paksha Bala fixed the tithi at **Shukla Tritiya**. All
three were later confirmed against the ephemeris. That is the only genuinely
falsifiable prediction the reading ever made, and it held.

## Note

This is an interpretation within the framework of Jyotisha, presented on its own
terms.
