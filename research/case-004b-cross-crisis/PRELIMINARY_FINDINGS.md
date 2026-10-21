# CASE-004B — Cross-Crisis Financial Amplification

## Research Status

PRELIMINARY EVIDENCE CHECKPOINT

Not a validated forecasting model.
Not a causal identification result.
Not a final research conclusion.

## Primary Research Question

What common financial-system vulnerabilities amplify
different shocks into systemic financial crises?

## Dataset

Jorda-Schularick-Taylor Macrohistory Database R6

18 countries, 1870–2020.

The original external dataset is not bundled here.
See RESEARCH_QUESTION.md for its source.

## Data Feasibility

- 88 JST crisis-marked country-years.
- 72 with at least 3 of 5 prior years available
  for credit, funding and bank capital.
- Bank capital variable: lev, not capital_tr.
- Crisis events and globally correlated episodes
  must not be treated as fully independent.

## Preliminary Historical Results

Within-country-era comparison,
excluding 2007–2009:

Credit/GDP 3-year increase:
- Positive difference in 29/34 groups.
- Country-cluster bootstrap interval:
  +1.758 to +8.109 percentage points.

Loan/deposit ratio:
- Positive difference in 25/34 groups.
- Bootstrap interval:
  +2.445 to +24.097 ratio points.

Noncore funding:
- Bootstrap interval crosses zero.

Bank capital:
- Bootstrap interval crosses zero.

## Three-Year Historical Risk-Set Comparison

After excluding 2005–2009 index years:

Credit-growth quartile crisis frequencies:
Q1 4.52%, Q2 5.95%, Q3 8.59%, Q4 16.43%.

Loan/deposit quartile crisis frequencies:
Q1 2.62%, Q2 9.05%, Q3 10.50%, Q4 13.33%.

Joint high-credit/high-loan-deposit group:
16.56%.

Joint low-credit/low-loan-deposit group:
5.10%.

These are descriptive historical frequencies,
not real-time crisis probabilities.

## Interpretation

H1: Preliminary support for credit expansion
as a recurring pre-crisis vulnerability.

H2: Loan/deposit ratio is promising;
noncore funding evidence is less stable.

H3: Consistent evidence for lower bank capital
has not been established.

H4: Resilience and shock amplification
have not yet been directly tested.

## Open Limitations

- Historical vintages and release timing.
- Crisis onset definition and classification.
- Overlapping three-year outcome windows.
- Correlated multinational crisis episodes.
- Retrospective sample selection.
- Country and era dependence.
- Out-of-sample evaluation.
- Incremental value beyond credit alone.
- Incremental value beyond BIS benchmarks.
- Association does not establish amplification
  mechanisms or causality.

## Next Phase

Evaluate credit-only versus credit-plus-funding
models with temporally separated test periods.

Avoid threshold tuning against test outcomes.
Keep all findings, including negative results.

## Publication Status

Research checkpoint only.
Public GitHub publication and LinkedIn communication
require separate review after research validation.
