# Analyse-

A complete Parashari reading of a single Vedic natal chart, with every supplied
table independently recomputed before interpretation.

## Contents

| File | What it is |
|---|---|
| [`vedic-chart-analysis.md`](vedic-chart-analysis.md) | The reading — chart structure, yogas, strength analysis, life areas, timeline, transits |
| [`chart-reading.html`](chart-reading.html) | The same reading as a formatted page |
| [`build_charts.py`](build_charts.py) | Computes and emits all sixteen Shodashavarga charts in full — master grid, dignity tally, and each varga with houses and classes |
| [`build_html.py`](build_html.py) | Regenerates the HTML page from the markdown, preserving the design system |
| [`verify_chart.py`](verify_chart.py) | Verifies positions, divisional charts, nakshatras, gandanta, dasha |
| [`verify_bala.py`](verify_bala.py) | Verifies Shadbala, Bhava Bala, Ashtakavarga, Reduced Ashtakavarga, Shodhya Pinda |
| [`verify_timeline.py`](verify_timeline.py) | Merges dasha and antardasha against Saturn and Jupiter transits into one life timeline, and scores every year 2026–2076 for transformation-window intensity |
| [`verify_shodasha.py`](verify_shodasha.py) | Computes all sixteen Shodashavarga charts, Vimshopaka Bala and the Vaiseshikamsha dignity census |
| [`verify_houseclass.py`](verify_houseclass.py) | Kendra/trikona/upachaya/dusthana census across all seven vargas |
| [`verify_gaps.py`](verify_gaps.py) | Gap audit — vargas not computed and why, per-varga birth-time sensitivity, whole techniques never applied, and data never supplied |
| [`verify_love.py`](verify_love.py) | The six registers of affection ranked, every Shukra period dated, and marital satisfaction read in both directions |
| [`verify_perception.py`](verify_perception.py) | How others see him: the Arudha Lagna and what touches it, arudha-relative houses, the 6th of rivals, the 11th of peers, and Drik Bala |
| [`verify_audit.py`](verify_audit.py) | **Master audit** — tests the good-but-with-friction claim, then re-derives and asserts all 52 headline figures the reading rests on |
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
`verify_audit.py` re-derives and asserts all 52 headline figures the reading
rests on:

```
python3 verify_audit.py     # 52/52 pass
for f in verify_*.py; do python3 "$f"; done
```

Every script runs clean.

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

**Birth data derived.** Not supplied, but determined by the chart and confirmed
three ways: the Vimshottari balance implies **15 April 2002**; the Sun at 1°28′
sidereal Mesha matches mid-April; and Vara Bala of 45 to Chandra requires a
Monday — which 15 April 2002 was. Paksha Bala fixes the tithi at Shukla Tritiya.

## Note

This is an interpretation within the framework of Jyotisha, presented on its own
terms.
