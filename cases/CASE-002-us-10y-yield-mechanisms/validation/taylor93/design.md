# Taylor-93 first execution: frozen alignment addendum

Recorded 2026-10-05, after checking source coverage and before calculating comparison results. This supplements, and does not replace, the original daily-change CASE-002 protocol.

## Three distinct exercises

1. **Original Taylor replication**: historical paper's GDP-deflator inflation and real GDP relative to its 2.2% growth trend over 1984Q1–1992Q3. Not implemented by substituting staff potential output. Exact original data/trend intercept still required; no replication success claimed.
2. **Main real-time Taylor-93-style implementation**: YPDGDP quarterly vintages, Fed staff gap vintages, r*=2, target=2, coefficients 0.5/0.5. Formula in percentage points: `2 + pi + 0.5*(pi-2) + 0.5*gap`. No floor, inertia, estimated coefficients, or fit optimization.
3. **Modern sensitivity**: core PCE, modern neutral rate and gap. Separate future exercise, not used to replace missing main observations. Latest-revised/ex-post Taylor is also a separate sensitivity, not main.

## Calendar and information contract

- One signal per quarter, timestamped at quarter-end. Use that quarter's YPDGDP quarterly vintage, whose snapshot is in the middle month. Conservatively gate eligibility at the END of that middle month (February/May/August/November); this is an availability bound, not an invented exact BEA release date.
- Inflation = `100*(P[s,v]/P[s-4,v]-1)`. Both levels must be positive and in the SAME vintage. Use the latest observed quarter s strictly before the signal quarter. In normal coverage s=q-1. Do not backdate the inflation observation to the economic quarter as if known then.
- Select latest staff gap vintage with its documented staff publication date at or before quarter-end, and use its estimate for the SAME economic quarter s. This is a lagged-activity implementation; do not mix a current-quarter gap forecast with prior-quarter observed inflation. Do not select a later gap vintage because it fills a missing cell. Require the selected gap vintage to belong to signal quarter q; otherwise leave missing. This prevents carrying 2020's vintage into later years.
- Check gap column dates against the separate publication-date workbook. These dates mean staff circulation, NOT public release. Time-of-day not documented; no intraday claim.
- Main information set is **Fed-staff PIT**, reconstructed from archived records. It is NOT public-market PIT. The Tealbook five-year release rule does not establish exact public-release dates for individual output-gap files; leave those dates unknown. Do not merely add five years and call that an exact release date.
- Use all overlap allowed by these rules, with no choice of periods based on results. Observed files imply 2015Q2–2020Q4; audit actual row completeness.

## Comparisons fixed before results

### 2026-10-05 timing-alignment correction

The original first pass compared a quarter-end Taylor prescription with same-quarter average rates. After review, the main comparison is corrected to quarter-end versus quarter-end: exact calendar quarter-end DFF and the last available DGS2/DGS10 business-day observation on or before quarter-end. Preserve the original quarterly-average result unchanged as a robustness comparison. This is an alignment correction, not model optimization; the Taylor inputs, coefficients, sample and inclusion rules remain frozen. Report level correlation, consecutive-quarter change correlation, mean Taylor-minus-rate gap and sample size. Classify correlation changes versus the preserved average-rate result as stronger above +0.05, weaker below -0.05, and almost unchanged within ±0.05. This descriptive threshold was recorded before reading the corrected results.

Pre-result date-validation amendment: some 2017–2018 column dates differ from the publication workbook by 1–5 days. Match only if exactly one publication date lies within seven days; use the later date as a conservative bound and preserve both dates plus the inferred mapping flag. Ambiguous mappings fail. This is not an exact-day verification. The differences do not cross quarter-end in this sample. Intraday/event-study use remains disallowed pending individual-document verification.

- The first-pass comparison remains a robustness result: quarter-end Taylor versus same-quarter DFF calendar-day mean, then DGS2 and DGS10 available-business-day means. Its historical outputs are retained. Level distances to 2Y/10Y are NOT forecast errors: a spot policy prescription is not a maturity-matched yield model.
- Separately compare each quarter-end signal to FOLLOWING-quarter rate means. Outcome data are later realizations, never signal inputs. Include a descriptive no-change comparator using prior-quarter realized means, but do not call it fully publication-timed executable forecasting (last-day H.15 releases and later corrections are not vintage archived).
- No regression fitting, window search, regime selection, significance claims, or causal conclusion in this first small-sample pass. Pandemic observations retained. No winning H1–H4 declaration.
- Rates are current downloaded historical observations, possibly corrected; only Taylor's macro inputs are vintage selected. DFF uses seven-day calendar data; other yields exclude missing days without forward fill. Retain counts and complete-quarter checks.
- DGS30, DFII10, T10YIE and ACMTP10 are diagnostic outcomes. Current ACM download is a retrospective model estimate, NOT a PIT predictor. Use daily ACM sheet, then available-day quarterly mean. Do not add nominal term premium to real yield and breakeven as a three-part identity.

## Reproducibility

Preserve raw downloads, URLs, retrieval timestamps and SHA-256 hashes, each row's vintage/cell provenance, missing-coverage ledger, script and validation results. Changes remain within CASE-002 research/validation. No GCF production edits.
