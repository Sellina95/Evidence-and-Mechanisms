# CASE-003 — Credit Stress Outcome Architecture

Date: 2026-10-21
Status: DECIDED IN PRINCIPLE — NOT FROZEN
Empirical results consulted: NONE
ICE licensing: PENDING

## Research Decision

Evaluate two separate credit-stress transmission tracks.

### Track A — Within High Yield

Question:
Does CCC–BB provide incremental advance warning
of subsequent deterioration in the broader HY market?

Candidate outcomes:
- Future aggregate HY OAS widening
- Future BB OAS widening

Important limitations:
- Aggregate HY contains CCC and BB constituents.
- BB is directly included in the CCC–BB predictor.
- Mechanical overlap and shared market shocks
  must be evaluated.
- Predictive improvement is not proof of contagion.

### Track B — High Yield to Investment Grade

Question:
Does CCC–BB provide incremental advance warning
of subsequent investment-grade credit deterioration?

Candidate outcome:
- Future BBB-rated investment-grade OAS widening

Important limitations:
- BBB is outside the HY rating categories.
- BBB deterioration may reflect common macro shocks,
  not transmission from CCC-rated issuers.
- Absence of BBB deterioration does not imply
  absence of HY stress.

## Required Baseline Comparison

Model A:
Aggregate HY OAS level and trailing change.

Model B:
Model A plus CCC–BB level and trailing change.

Use identical forecast timestamps and evaluation
samples within each track.

Report Track A and Track B separately.

## Secondary Equity Validation

Evaluate future S&P 500 declines as a distinct
market-risk application.

Equity results do not substitute for either
credit-stress track.

## Unresolved Before Protocol Freeze

1. Exact outcome series for each track
2. Stress thresholds and forecast horizons
3. Decision-time information availability
4. Model and walk-forward specification
5. Overlapping-outcome leakage controls
6. Statistical uncertainty and false-alert rules
7. Data provenance, coverage and licensing

No empirical test has been performed.

## Research Boundaries

No ICE source data use pending license clarification.
No restricted data redistribution.
No GCF Production changes.
