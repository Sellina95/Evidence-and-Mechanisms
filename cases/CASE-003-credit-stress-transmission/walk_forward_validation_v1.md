# CASE-003 — Walk-Forward Validation Protocol V1

Status: PROPOSED — NOT FROZEN
Purpose: Predefine an out-of-sample validation design.
No ICE data ingestion or empirical backtesting is authorized.

## 1. Research Question

Does the CCC-minus-BB OAS differential provide incremental
early-warning information beyond aggregate HY OAS?

Evaluate separately:

Track A: Future aggregate HY OAS widening.
Track B: Future BBB investment-grade OAS widening.

BB widening is a diagnostic outcome, not a substitute for
either primary track.

## 2. Prediction Horizon

Candidate horizon: 20 trading sessions.

For outcome series S:

FutureWidening(t) =
max[S(t+1), ..., S(t+20)] - S(t)

The label is only known after the full forward window
has matured.

Do not use future outcomes to construct predictors.

## 3. Information Availability

Observation date is not necessarily publication time.

Determine when each OAS observation became available.

If exact availability cannot be established, evaluate
a conservative one-trading-session signal delay.

The prediction origin, feature cutoff, and outcome start
must be aligned to prevent look-ahead bias.

## 4. Chronological Walk-Forward

Use expanding training windows and strictly later
out-of-sample test windows.

Candidate:
- Initial training history: sufficient pre-2015 observations.
- First test period: no earlier than 2015.
- Subsequent tests: chronological calendar-year blocks.

These dates are candidates, not finalized fold boundaries.

Never use random train/test splitting.

Do not choose fold boundaries based on observed performance.

## 5. Purging and Outcome Maturity

At every test boundary:

- Exclude training examples whose forward outcome window
  extends into the test period.
- Require the full 20-session outcome to have matured
  before a training example becomes eligible.
- Add an embargo where feature availability or overlapping
  information requires it.
- Record the exact eligible training and test dates.

A simple fixed 20-row gap is not automatically sufficient
when dates are missing or publication timing is uncertain.

## 6. Missing Data and Archive Boundaries

Construct an explicit common-date calendar.

Do not interpolate or forward-fill ICE OAS gaps.

Do not allow trailing-change or future-outcome windows
to jump across missing historical archive segments.

Record excluded dates and reasons.

Evaluate Track A and Track B on matched dates for
their respective Model A versus Model B comparisons.

Cross-track comparisons must disclose sample differences.

## 7. Model Comparison

Model A:
- Aggregate HY OAS level
- Aggregate HY OAS trailing 20-observation change

Model B:
- Model A features
- CCC-minus-BB OAS level
- CCC-minus-BB trailing 20-observation change

Use the same outcome, eligible dates, folds, and model
family within each A-versus-B comparison.

Candidate model: regularized logistic regression.

Standardization and hyperparameter selection must use
training information only.

Any internal tuning must itself be chronological.

## 8. Stress Threshold Policy

Candidate binary event:
Future widening above a training-derived threshold.

The previously proposed training-fold 90th percentile
is NOT YET APPROVED as the primary definition.

Reasons:
- Different folds may define different event severities.
- Crisis composition may change the threshold.
- Pooled cross-fold metrics may mix outcome definitions.

Before protocol freeze, select either:
- An anchored historical calibration threshold; or
- A fixed, economically interpretable basis-point threshold.

Training-fold percentiles may be retained as sensitivity
analysis if fully documented.

Threshold selection must not use test outcomes.

## 9. Evaluation Metrics

Primary candidate comparisons:
- PR-AUC
- Brier score
- Recall at a fixed alert rate

Report event prevalence and the number of positive
observations in every test fold.

Use an alert-rate budget chosen before testing.

Report calibration and false-alert burden.

A performance improvement must be assessed against
uncertainty, not only point estimates.

## 10. Overlapping Events

Daily forward 20-session labels overlap.

Do not treat all positive days as independent crises.

In addition to daily metrics, evaluate:
- Distinct stress episodes
- Whether alerts preceded episode onset
- Lead time to episode onset
- False-alert episodes

Define episode merging and alert matching rules
before empirical testing.

Use dependence-aware uncertainty methods, such as
block resampling, when statistically appropriate.

## 11. Interpretation Limits

Aggregate HY OAS contains lower-rated HY constituents.

CCC-minus-BB is mechanically related to aggregate HY
and shares a BB component with some diagnostics.

Track B reduces direct constituent overlap but cannot
establish causal transmission.

Compare CCC and BB components separately to diagnose
which leg drives the differential.

Predictive improvement is not proof of contagion.

## 12. Gates Before Protocol Freeze

OPEN:
1. ICE written licensing clarification.
2. Independent verification of all five data sources.
3. Common calendar and publication-lag policy.
4. Final fold boundaries and initial training minimum.
5. Primary stress threshold definition.
6. Alert budget and episode definition.
7. Dependence-aware uncertainty procedure.

No empirical result is claimed in this document.
