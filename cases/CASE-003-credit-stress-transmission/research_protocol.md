# CASE-003 — Research Protocol V1

Status: DRAFT — NOT FROZEN
Date: 2026-10-21
Data license: PENDING
Empirical testing: NOT STARTED

## 1. Primary Research Question

Does the CCC & Below minus BB OAS differential provide
incremental early-warning information about broad equity
market stress beyond aggregate HY OAS?

The objective is predictive information, not causal proof.

## 2. Primary Indicators

Aggregate HY OAS:
BAMLH0A0HYM2

CCC–BB differential:
BAMLH0A3HYC - BAMLH0A1HYBB

Convert percentage-point spreads to basis points
by multiplying by 100.

Compare both levels and trailing 20-observation changes.

B-rated OAS is a secondary diagnostic, not a required
component of the primary differential.

## 3. Primary Outcome — Proposed

Forward 20-trading-day S&P 500 maximum drawdown
of at least 5%, measured from the decision-date close
against the lowest subsequent close.

This is a proposed definition, not yet frozen.

## 4. Secondary Outcomes

- Forward 10-trading-day equity stress
- Forward 20-trading-day VIX threshold exceedance
- Historical crisis episode diagnostics

Secondary outcomes must not replace the primary outcome
based on favorable results.

## 5. Baseline Comparison

Model A:
Aggregate HY OAS level and trailing 20-observation change.

Model B:
Model A plus CCC–BB differential level and trailing
20-observation change.

The incremental value of CCC–BB is measured by comparing
Model B against Model A on identical evaluation dates.

## 6. Evaluation

Primary comparison:
- Out-of-sample PR-AUC
- Brier score
- Recall at a fixed alert rate

Secondary diagnostics:
- 5/10/20-day lead-lag comparisons
- False-positive frequency
- Regime sensitivity
- Crisis and non-crisis performance

Avoid random train/test splits.

Use chronological walk-forward evaluation with an
explicit policy for overlapping forward outcomes.

## 7. Falsification

The incremental-warning hypothesis is weakened if:

- Model B does not consistently improve out-of-sample
  performance over Model A.
- Apparent improvement depends on one crisis episode.
- The differential produces materially more false alerts
  without meaningful improvement in stress detection.
- Performance disappears under reasonable alternative
  stress definitions or evaluation windows.

No improvement is a valid research result.

## 8. Data Integrity Requirements

Before empirical testing, verify:

- Source identity and observation dates
- Missing values and duplicate dates
- Common-date alignment
- Units and spread conversion
- Historical/current overlap consistency
- Availability timing and look-ahead risk
- Archive provenance and licensing conditions

No interpolation or backfilling without explicit,
predeclared justification.

## 9. Research Boundaries

- No trading performance claim
- No optimized GCF thresholds
- No production modifications
- No causal claim from predictive association alone
- No publication of restricted ICE raw data

ICE data use and data-derived publication remain
subject to license clarification.

## 10. Freeze Gate

This protocol is NOT FROZEN.

Before freezing, review:
- Primary outcome definition
- Model specification and regularization
- Walk-forward train/test windows
- Alert-rate definition
- Dependence and uncertainty estimation
- Historical episode selection rules
- Data access and licensing conditions

No empirical results may be used to choose the
primary specification before protocol freeze.
