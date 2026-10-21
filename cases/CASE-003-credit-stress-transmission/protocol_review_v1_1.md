# CASE-003 — Protocol Review V1.1

Status: PROPOSED — NOT FROZEN
Date: 2026-10-21
Empirical results consulted: NONE
ICE licensing: PENDING

## 1. Research Target

Primary target:
Incremental prediction of future broad equity-market stress.

Secondary target:
Credit stress propagation and rating-tier deterioration.

These are distinct outcomes and must not be conflated.

## 2. Primary Outcome

Candidate definition:

At decision date t, define Y(t) = 1 if the S&P 500
has at least one closing price during trading days
t+1 through t+20 that is 5% or more below its
closing price at t.

Otherwise Y(t) = 0.

This is a forward decline from the decision-date
close, not a conventional peak-to-trough drawdown.

The threshold and horizon remain subject to
pre-empirical review.

## 3. Information Available at Decision Time

Use only observations demonstrably available
by the forecast timestamp.

The decision timestamp and same-day publication
availability must be specified before testing.

If release timing cannot be established, use
a conservative one-trading-day information lag
and test sensitivity to additional lags.

Do not assume same-date observations were
available simultaneously.

## 4. Predictors

Model A:
- Aggregate HY OAS level
- Trailing 20-observation change in HY OAS

Model B:
- All Model A predictors
- CCC minus BB OAS level
- Trailing 20-observation change in CCC minus BB

Apply identical sample dates and identical
training/evaluation procedures to both models.

No outcome-dependent feature selection.

## 5. Model Specification

Candidate:
Regularized logistic regression.

Use training-only scaling and preprocessing.

Regularization selection, if any, must occur
inside chronological training folds.

No random train/test splitting.

## 6. Walk-Forward Validation

Chronological out-of-sample evaluation.

Proposed structure:
- Initial training history ending before 2015
- Subsequent expanding-window evaluations
- Crisis and non-crisis subgroup reporting

Exact fold dates remain UNRESOLVED.

Overlapping forward 20-day labels require
explicit treatment of training/evaluation
boundary leakage and serial dependence.

No random cross-validation.

## 7. Evaluation Metrics

Primary:
- Out-of-sample PR-AUC
- Out-of-sample Brier score

Operational:
- Recall at equal alert frequency
- False-alert frequency
- Warning lead time

Compare against Model A on identical dates.

Specify an alert threshold using training
data only.

A positive result on one metric does not
automatically establish overall superiority.

## 8. Secondary Credit-Stress Outcome

Candidate:
Future broad HY OAS widening.

Unresolved:
- Horizon
- Magnitude threshold
- Whether the outcome is independent enough
  from the predictors to support interpretation
- How to distinguish mechanical overlap from
  genuine incremental predictive information

Do not designate this a confirmed secondary
outcome until these issues are resolved.

## 9. Historical Episode Diagnostics

Candidate episodes:
- 2007–2009
- 2015–2016
- 2020
- 2022

Episode analysis is explanatory and diagnostic,
not a substitute for full-sample evaluation.

Do not choose episodes based on model success.

## 10. Robustness and Falsification

Evaluate:
- Alternative stress thresholds
- Alternative forecast horizons
- Different historical regimes
- Information availability lags
- False positives outside crises
- Sensitivity to sample start and end dates

Any alternative chosen after seeing results
must be labeled exploratory.

If incremental improvement is absent or
unstable, retain the null finding.

## 11. Data Rights and Publication Gate

ICE licensing clarification is pending.

Do not download or analyze restricted ICE
historical data before permitted use is
confirmed.

Do not commit or redistribute ICE source
time series.

Derived charts and statistics require
publication-rights clarification.

## 12. Freeze Decision

NOT FROZEN.

Open decisions:
1. Primary threshold and horizon
2. Forecast timestamp and data availability
3. Exact walk-forward folds and embargo
4. Model hyperparameters
5. Alert-frequency rule
6. Secondary credit outcome
7. Uncertainty estimation
8. Licensing permissions

No empirical backtest is authorized by
this review document.
