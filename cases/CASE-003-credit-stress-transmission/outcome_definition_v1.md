# CASE-003 — Credit Stress Outcome Definition V1

Date: 2026-10-21
Status: PROPOSED — NOT FROZEN
Empirical results consulted: NONE
ICE licensing: PENDING

## 1. Forecast Horizon

Candidate horizon: 20 trading days.

At each decision date t, evaluate future
observations t+1 through t+20.

## 2. Future Maximum Spread Widening

For an outcome spread S:

FutureWidening(t) =
max[S(t+1), ..., S(t+20)] - S(t)

The outcome is the largest widening relative
to the decision-date spread.

This is not the spread change on day t+20.

## 3. Track A — HY Internal Stress

Primary candidate outcome:
Future maximum widening in aggregate HY OAS.

Additional diagnostic:
Future maximum widening in BB OAS.

Aggregate HY contains the rating segments used
in the CCC–BB predictor.

Therefore mechanical overlap and contemporaneous
common shocks must be explicitly assessed.

## 4. Track B — Investment-Grade Stress

Candidate outcome:
Future maximum widening in BBB OAS.

This is a separate outcome and does not
replace Track A.

BBB widening is not by itself evidence of
causal transmission from lower-rated HY bonds.

## 5. Stress Threshold

Candidate:
90th percentile of future maximum widening
calculated using eligible historical training
observations only.

Apply the training-derived threshold to the
subsequent out-of-sample evaluation window.

Record the threshold for each evaluation fold.

Do not calculate the threshold from the full
historical sample.

## 6. Information Leakage Controls

- No future observations in predictors.
- No test-window observations in training thresholds.
- Exclude training labels whose forward windows
  overlap the test period.
- Fit preprocessing on training observations only.
- Use the same forecast dates for both models.

## 7. Interpretation

Track A:
Incremental warning of broad HY deterioration.

Track B:
Incremental warning of BBB deterioration.

Both:
Predictive evidence, not proof of contagion.

A positive result in one track does not
establish success in the other.

## 8. Unresolved Before Freeze

- Exact BBB series and licensing
- Training/evaluation fold dates
- Minimum training sample
- Label embargo and overlap handling
- Model hyperparameters
- Statistical uncertainty
- Alert-rate calibration
- Fixed-threshold robustness checks

No empirical testing is authorized by this
proposed outcome definition.
