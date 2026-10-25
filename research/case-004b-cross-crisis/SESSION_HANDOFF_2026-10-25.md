# CASE-004B — Session Handoff
Date: 2026-10-25
Branch: research/case-003-credit-stress

## FINAL RESEARCH OBJECTIVE

Identify common financial-system vulnerabilities that
amplify different shocks into systemic financial crises.

Develop an original, falsifiable CONDITIONAL transmission
model using historical data, primary event evidence,
counterexamples and independent validation.

Do not assume all crises follow the same mechanism.
Do not claim causality from correlation or chronology.

## 1. PRIOR QUANTITATIVE FINDINGS

Dataset: JST Macrohistory R6, 18 countries.

Archived banking-crisis onset records:
88 country-year records, 1870-2008.

Modern 1981+ crisis records:
23, including 13 records in 2007-2008.

Credit/GDP expansion remains the strongest
leading-indicator candidate.

LTD and real house-price growth are accompanying
vulnerability candidates.

Triple-boom risk-set exploratory result:
- 504 eligible country-years
- All three positive: 40/206 (19.42%) with
  JST crisis markers in the next 3 years
- Other cases: 26/298 (8.72%)

These are overlapping historical observation windows,
NOT independent events or validated forecasts.

Five-year episode audit:
- 53 triple-boom descriptive episodes
- 11 linked to crisis within the fixed five-year window
- 40 without crisis in that window
- 2 right-censored

Bank capital ratio (lev) and noncore funding did
NOT consistently distinguish crisis/non-crisis episodes.

Within-country funding comparisons also produced
mixed signs. No causal mechanism was established.

## 2. RESEARCH STRATEGY CHANGE

Previous strategy:
Repeatedly add indicators and compare crisis/non-crisis
levels or changes.

New strategy:
1. Establish a defensible crisis universe.
2. Audit crisis definitions and global-wave clustering.
3. Reconstruct real shocks and transmission mechanisms.
4. Compare crisis and stress-without-crisis cases.
5. Form explicitly testable conditional hypotheses.
6. Test out of sample, avoiding shared-shock leakage.

The selected three historical cases are DISCOVERY PILOTS,
not evidence sufficient for generalization.

## 3. PRIMARY CASE PILOTS

USA 2007:
- New Century, Bear Stearns, BNP Paribas and
  Federal Reserve market-response anchors documented.
- Three funding-transmission hypotheses recorded.
- ABCP weekly download failed due to timeouts.
- Published-research evidence is not a replacement
  for institution-level causal transmission evidence.

Sweden 1991:
- Seven timeline events recorded.
- Four mechanism hypotheses created.
- Finance-company stress began in 1990.
- 1992 currency crisis cannot explain initial 1990
  banking/finance-company distress.

Japan 1997:
- Five timeline records.
- Four mechanism hypotheses created.
- Sanyo securities, call-market default,
  Hokkaido Takushoku, Yamaichi and policy response.
- Direct causal links still NOT IDENTIFIED.

All links are hypotheses, not proven causal chains.
Verify underlying source documents and original dates
before promoting individual claims to verified status.

## 4. CRISIS UNIVERSE WORK

JST:
- 88 crisis onset country-years.
- 63 before 1946.
- 23 in 1981+.
- 13 of modern records fall in 2007-2008.

Wave classifications are PROVISIONAL.
Same-year events are not automatically one common shock.
1991 Switzerland and UK were removed from the
incorrect Nordic-wave automatic classification.

IMF:
- Official Laeven-Valencia 2026 PDF downloaded locally.
- Original PDF: 001-article-A001-en.pdf
- SHA256: 89939196f0f0ccf19e76777396ec0728ed7c75dc13e405aa142bc4c69035a340
- PDF length: 43 pages.
- Appendix I, Table A1 begins on PDF page 23.
- Candidate table text extracted from PDF pages 23-34.
- IMF crisis event rows VERIFIED: 0.
- IMF-to-JST reconciliation: NOT STARTED.
- No global sampling split or model frozen.

The PDF and large verbatim raw extraction are retained
locally only and excluded from public Git history.

## 5. FIRST TASK NEXT SESSION

IMF Table A1 structured extraction and validation:

A. Inspect all table continuation pages and footnotes.
B. Verify columns for country, onset, end year,
   borderline flags, policy/cost measurements.
C. Parse country-event rows from the PDF with
   checks against printed source, including multiline
   country names and footnote markers.
D. Establish validated row count; do not assume 164
   parsed rows solely because a paper reports 164.
E. Preserve original country names, dates, categories,
   page numbers and parsing exceptions.
F. Normalize ISO IDs separately from source records.
G. Reconcile overlapping IMF/JST events, retaining
   definition and onset-year disagreements.

Only AFTER that:

- Select diverse discovery cases and controls.
- Reserve untouched validation cases.
- Audit stress, trigger and funding transmission
  across regions and eras.
- Construct and falsify conditional mechanism model.

## SAFETY AND STATUS

- Production and GCF remain unchanged.
- Existing canonical research results are preserved.
- No causal crisis mechanism proven yet.
- Do not silently turn source claims into OBSERVED
  when the underlying primary record was not read.
- Do not use same-year clustering as causal evidence.
- Do not optimize thresholds using validation data.
