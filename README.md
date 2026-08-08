# Analyse-

A complete Parashari reading of a single Vedic natal chart, with every supplied
table independently recomputed before interpretation.

## Contents

| File | What it is |
|---|---|
| [`vedic-chart-analysis.md`](vedic-chart-analysis.md) | The reading — chart structure, yogas, strength analysis, life areas, timeline, transits |
| [`chart-reading.html`](chart-reading.html) | The same reading as a formatted page |
| [`verify_chart.py`](verify_chart.py) | Verifies positions, divisional charts, nakshatras, gandanta, dasha |
| [`verify_bala.py`](verify_bala.py) | Verifies Shadbala, Bhava Bala, Ashtakavarga, Reduced Ashtakavarga, Shodhya Pinda |

## Source data

D1 (Rashi), D9 (Navamsha), D10 (Dashamsha), D11 (Rudramsha), D8 (Ashtamsha),
D27 (Bhamsha), D30 (Trimshamsha); eleven upagrahas; the Vimshottari dasha tree;
Shadbala with all sub-components; Bhava Bala; Ashtakavarga and Reduced
Ashtakavarga; Shodhya Pinda; and a transit chart for August 2026.

## Verification

Nothing was taken at face value. Both scripts run standalone:

```
python3 verify_chart.py
python3 verify_bala.py
```

| Check | Result |
|---|---|
| D9 and D27 recomputed from D1 longitudes | All 20 positions match to a few arc-seconds |
| Nine Rahu antardashas rebuilt from Vimshottari proportions | Every boundary matches exactly |
| Shadbala sub-components → totals → rupas → rank | Reproduces exactly |
| Bhava Bala: Bhavadhipati + Disha + Drishti | Reproduces all twelve totals |
| Sarvashtakavarga total | **337** — the classical value |
| Reduced Ashtakavarga → Shodhya Pinda | Rebuilds all sixteen values via the standard Gunakara multipliers |

**Two source errors found.** Rahu and Ketu must be exactly 180° apart. In **D8**
and **D30** the generator printed Ketu at Rahu's own longitude:

- D8 — Ketu should be **05°26′ Makara (11th)**, not Karka (5th)
- D30 — Ketu should be **27°56′ Vrishabha (7th)**, not Vrischika (1st)

The D30 correction is interpretively significant: it places Ketu 4° from Chandra
in the 7th, a conjunction the printed chart hides entirely. The reading uses
corrected values.

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
