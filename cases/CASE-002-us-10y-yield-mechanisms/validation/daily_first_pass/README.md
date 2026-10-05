# CASE-002 — Daily Competing-Mechanisms First Pass

**Status: COMPLETE UNDER FROZEN SPECIFICATION**

**Calculation date: 2026-10-05 (Asia/Seoul)**

**Specification:** [frozen daily specification](../../daily_competing_mechanisms_spec.md), unchanged SHA-256 `c332089e04af3e30418b72b21242c45e866d857a546a0aed51ba0c9369c8a9de`

## A. Common sample

- Frozen calendar boundary: 2006-02-09 through 2026-09-25.
- The user explicitly confirmed retaining 2026-09-25 after the latest-common-date wording was reconciled with the frozen specification. Later raw observations are excluded.
- Common non-missing level observations: 5,162.
- First change observation: 2006-02-10.
- Last change observation: 2026-09-25.
- Identical change sample for H1–H5: **N = 5,161**.
- Maximum interval between consecutive common dates: four calendar days.
- No interpolation, forward-fill, missing-value replacement, pairwise sample, lag, rolling window, or regime split was used.

## B. Frozen first-pass results

Each row estimates `d_DGS10_bp = intercept + coefficient × regressor + error` on the same observations. Values are shown in the fixed H1–H5 order, not sorted by fit.

| Hypothesis | Same-interval regressor | Pearson correlation | Univariate OLS R² | Coefficient | Positive sign matched? | N |
|---|---|---:|---:|---:|---|---:|
| H1 | ΔDGS2 | 0.735647 | 0.541177 | 0.808639 | Yes | 5,161 |
| H2 | ΔDFII10 | 0.807654 | 0.652305 | 0.883730 | Yes | 5,161 |
| H3 | ΔT10YIE | 0.437071 | 0.191031 | 0.729480 | Yes | 5,161 |
| H4 | ΔACMTP10 — **MODEL ESTIMATE** | 0.720843 | 0.519614 | 0.733688 | Yes | 5,161 |
| H5 | ΔDGS30 | 0.928766 | 0.862607 | 0.979895 | Yes | 5,161 |

All five coefficients have the pre-specified positive sign. These are same-interval associations, not causal rankings.

## C. Evidence categories

### Mechanical decomposition channels

H2 and H3 are components of the matched identity `DGS10 = DFII10 + T10YIE`. The maximum absolute change-identity residual was `1.11e-13 bp` in the primary calculation and `0.0 bp` after the exported values were rounded to ten decimals. Their fit describes how nominal-yield movement divides between the real-yield and inflation-compensation legs. It is not evidence that an independent causal model won.

### Non-identity diagnostics, with limits

- H1 uses DGS2 as a policy-path-sensitive proxy. It is not a direct measure of Federal Reserve expectations.
- H4 uses the current-vintage ACM 10-year term premium. It is a model-estimated, ex-post decomposition diagnostic whose historical estimates can be revised or depend on later estimation data.
- H5 uses DGS30 as a long-end curve diagnostic. It is another point on the Treasury curve and is not a pure term-premium measure.

The large H5 association can reflect shared Treasury-curve movements and cannot establish an independent long-end cause. ACM is also estimated from Treasury yield-curve inputs and is not statistically independent of observed Treasury yields.

## D. What this adds beyond the Taylor baseline

The frozen Taylor-93 staff-PIT baseline used 23 quarterly signals from 2015Q2–2020Q4 to compare a policy prescription with actual EFFR, 2Y and 10Y rates. Its level relationship was stronger than its quarterly-change relationship, and it was not designed to identify daily market shocks.

This first pass adds a different fact: over 5,161 matched daily intervals, nominal 10Y changes moved positively on the same interval with every pre-specified proxy. It also locates the accounting split: the real-yield leg has a larger univariate association with Δ10Y than the inflation-compensation leg in this fixed sample. The ACM estimate and both observed curve points co-move materially with Δ10Y. None of these observations identifies which news caused the move, and their R² values are not directly comparable as causal evidence because their construction and independence differ.

## E. Next-step candidate — not executed

The next defensible step is to freeze a separate design for independently timed news or event evidence that can discriminate policy-path, inflation, real-rate and duration-risk causes. Any onset window, regime split, lag, multivariate model, or robustness analysis requires a new pre-results specification. No such analysis was started here.

## Sources and raw provenance

The calculation reuses the immutable raw snapshot preserved by the Taylor audit rather than silently downloading a new vintage.

| Raw file | Series | Exact source URL | SHA-256 |
|---|---|---|---|
| `../taylor93/raw/rates.csv` | DGS2, DGS10, DGS30, DFII10, T10YIE | `https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF,DGS2,DGS10,DGS30,DFII10,T10YIE` | `8695904f2a34795a986e80f9739173ea25d491be6cecd2684cb77f1ae2fb9567` |
| `../taylor93/raw/ACMTermPremium.xls` | ACMTP10 | `https://www.newyorkfed.org/medialibrary/media/research/data_indicators/ACMTermPremium.xls` | `9c328d05615f7e7adcbf847d7eb2d3780de1b50609112b2dcb48588cae839e6e` |

Source landing pages: [DGS2](https://fred.stlouisfed.org/series/DGS2), [DGS10](https://fred.stlouisfed.org/series/DGS10), [DGS30](https://fred.stlouisfed.org/series/DGS30), [DFII10](https://fred.stlouisfed.org/series/DFII10), [T10YIE](https://fred.stlouisfed.org/series/T10YIE), and [NY Fed ACM](https://www.newyorkfed.org/research/data_indicators/term-premia-tabs).

## Transformation and validation provenance

1. Read the five FRED series from the preserved raw ZIP member `daily.csv` and ACMTP10 from the `ACM Daily` worksheet.
2. Restrict levels to the frozen boundary.
3. Keep only dates where all six levels are present.
4. Sort dates and calculate every change as 100 times the difference from the immediately preceding common level row.
5. Drop the first common level row and run five intercept-included univariate OLS regressions.

Artifacts:

- `common_sample_changes.csv` — level values, prior common date, interval length and all bp changes.
- `first_pass_metrics.csv` — frozen H1–H5 metrics.
- `source_manifest.json` — URLs, hashes, file sizes and snapshot metadata.
- `validation.json` — sample, identity and transformation audit.
- `independent_validation.json` — independent standard-library correlation and OLS recomputation.
- `build.py` and `check_independent.py` — executable provenance.

The independent implementation rebuilt the common-date intersection and all level-to-change transformations from the raw files using `csv` and `openpyxl`, then used standard-library arithmetic for the metrics. It reproduced every reported correlation, R², coefficient and intercept within `1e-9`, confirmed N = 5,161 for all five rows, and rechecked the decomposition identity. Both implementations share LibreOffice XLS conversion, so this is independent transformation and arithmetic validation, not an independent XLS decoder. The frozen specification hash was identical before and after calculation.

Reproduction: run `python build.py` followed by `python check_independent.py` in this directory, using Python with NumPy, pandas and openpyxl and the LibreOffice path recorded in the scripts. No network access is required. The original download timestamps and their limitations remain in `../taylor93/manifest.json`; no new download is claimed. Source publication timestamps were not independently certified, and this analysis is current-vintage descriptive evidence rather than a market-PIT reconstruction.
