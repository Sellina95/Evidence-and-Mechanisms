# CASE-002 Event Identification V0 — Results

## Scope

This report applies the pre-frozen V0 classification rules to the clean daily event sample.

Daily classifications are event-day associations and must not be interpreted as strict causal identification.

## Sample

- Total event rows: 162
- Clean daily events: 113
- Excluded / duplicate / contaminated / unavailable rows: 49

## Overall Classification

- POLICY_PATH: 15 (13.3%)
- INFLATION_COMPENSATION: 22 (19.5%)
- TERM_PREMIUM_LONG_END: 19 (16.8%)
- MIXED: 45 (39.8%)
- INCONCLUSIVE: 12 (10.6%)

## Dominant Pattern by Event Type

- **CPI**: MIXED (19/43, 44.2%)
- **FOMC_STATEMENT**: POLICY_PATH (6/22, 27.3%)
- **PCE**: MIXED (18/41, 43.9%)
- **TREASURY_REFUNDING**: INCONCLUSIVE (3/7, 42.9%)

## Interpretation

The V0 result does not support a single universal mechanism for U.S. 10Y Treasury yield moves.

MIXED classifications are common, indicating that policy-path / real-rate and long-end / term-premium signals often move together.

POLICY_PATH, INFLATION_COMPENSATION, and TERM_PREMIUM_LONG_END also appear as distinct response structures in subsets of events.

Therefore the evidence is more consistent with a state-dependent multi-mechanism interpretation than with one mechanism explaining all long-term yield moves.

## Important Limits

- FOMC statement and press conference cannot be separated using daily data.
- Same-day major-event overlaps are excluded from clean daily attribution.
- DGS2 is policy-path-sensitive but not a direct Fed-expectations measure.
- T10YIE is inflation compensation, not pure expected inflation.
- ACM term premium is model-estimated and should be treated as secondary evidence.
- DGS30 is a long-end diagnostic, not a pure term-premium measure.
- Intraday proxy confirmation remains a separate follow-up validation step.

## Example Classified Events

### POLICY_PATH

- FOMC_STATEMENT_20230322 (2Y -21.0000000000bp, 10Y -11.0000000000bp, 30Y -5.0000000000bp, Real -16.0000000000bp, BE 5.0000000000bp, TP 3.7874407642bp)
- FOMC_STATEMENT_20231213 (2Y -27.0000000000bp, 10Y -16.0000000000bp, 30Y -11.0000000000bp, Real -16.0000000000bp, BE 0.0000000000bp, TP 1.4039208004bp)
- FOMC_STATEMENT_20240320 (2Y -9.0000000000bp, 10Y -3.0000000000bp, 30Y 1.0000000000bp, Real -4.0000000000bp, BE 1.0000000000bp, TP 2.4911719037bp)

### INFLATION_COMPENSATION

- FOMC_STATEMENT_20230726 (2Y -3.0000000000bp, 10Y -5.0000000000bp, 30Y -1.0000000000bp, Real -2.0000000000bp, BE -3.0000000000bp, TP 16.7368730227bp)
- FOMC_STATEMENT_20230920 (2Y 4.0000000000bp, 10Y -2.0000000000bp, 30Y -3.0000000000bp, Real 0.0000000000bp, BE -2.0000000000bp, TP -5.3642465663bp)
- FOMC_STATEMENT_20260128 (2Y 3.0000000000bp, 10Y 2.0000000000bp, 30Y 2.0000000000bp, Real 0.0000000000bp, BE 2.0000000000bp, TP 2.2537839572bp)

### TERM_PREMIUM_LONG_END

- FOMC_STATEMENT_20230614 (2Y 7.0000000000bp, 10Y -1.0000000000bp, 30Y -4.0000000000bp, Real -2.0000000000bp, BE 1.0000000000bp, TP -11.2444198389bp)
- FOMC_STATEMENT_20250507 (2Y 0.0000000000bp, 10Y -4.0000000000bp, 30Y -4.0000000000bp, Real -3.0000000000bp, BE -1.0000000000bp, TP -5.7042650566bp)
- FOMC_STATEMENT_20260318 (2Y 8.0000000000bp, 10Y 6.0000000000bp, 30Y 3.0000000000bp, Real 3.0000000000bp, BE 3.0000000000bp, TP 0.4144670891bp)

### MIXED

- FOMC_STATEMENT_20240918 (2Y 2.0000000000bp, 10Y 5.0000000000bp, 30Y 7.0000000000bp, Real 5.0000000000bp, BE 0.0000000000bp, TP 7.7552558580bp)
- FOMC_STATEMENT_20241107 (2Y -6.0000000000bp, 10Y -11.0000000000bp, 30Y -8.0000000000bp, Real -6.0000000000bp, BE -5.0000000000bp, TP -7.3012139703bp)
- FOMC_STATEMENT_20241218 (2Y 10.0000000000bp, 10Y 10.0000000000bp, 30Y 6.0000000000bp, Real 9.0000000000bp, BE 1.0000000000bp, TP 4.2236424986bp)

### INCONCLUSIVE

- FOMC_STATEMENT_20250129 (2Y 2.0000000000bp, 10Y 0.0000000000bp, 30Y 1.0000000000bp, Real 2.0000000000bp, BE -2.0000000000bp, TP -1.8842995471bp)
- FOMC_STATEMENT_20250618 (2Y 0.0000000000bp, 10Y -1.0000000000bp, 30Y 0.0000000000bp, Real -1.0000000000bp, BE 0.0000000000bp, TP 1.0225988852bp)
- FOMC_STATEMENT_20250917 (2Y 1.0000000000bp, 10Y 2.0000000000bp, 30Y 1.0000000000bp, Real 1.0000000000bp, BE 1.0000000000bp, TP -0.0783250478bp)

