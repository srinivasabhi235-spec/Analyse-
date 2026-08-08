# Analyse-

Analysis of a Vedic (Parashari) natal chart set.

## Contents

| File | What it is |
|---|---|
| [`vedic-chart-analysis.md`](vedic-chart-analysis.md) | The full written analysis — chart structure, yogas, life areas, and the Vimshottari timeline |
| [`verify_chart.py`](verify_chart.py) | Verification script. Every numeric claim in the analysis is derived from its output |

## Source data

D1 (Rashi), D9 (Navamsha), D10 (Dashamsha), D11 (Rudramsha), D8 (Ashtamsha),
D27 (Bhamsha), D30 (Trimshamsha), eleven upagrahas, and the Vimshottari dasha
tree — currently in Rahu mahadasha (25 Dec 2022 → 25 Dec 2040).

## Verification

Rather than reading the supplied tables at face value, D9 and D27 were
recomputed independently from the D1 longitudes and all nine Rahu antardashas
were rebuilt from the Vimshottari proportions.

```
python3 verify_chart.py
```

**Result:** the data is internally consistent — all twenty divisional positions
match to within a few arc-seconds, and every antardasha boundary matches the
source table exactly.

**Two bugs found.** Rahu and Ketu must be exactly 180° apart. In **D8** and
**D30** the source printed Ketu at Rahu's own longitude:

- D8 — Ketu should be **05°26′ Makara (11th)**, not Karka (5th)
- D30 — Ketu should be **27°56′ Vrishabha (7th)**, not Vrischika (1st)

The D30 correction is interpretively significant: it places Ketu 4° from
Chandra in the 7th, a conjunction the printed chart hides entirely. The
analysis uses the corrected values.

## Note

This is an interpretation within the framework of Jyotisha, presented on its
own terms.
