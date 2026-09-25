# CASE-002 — Data Source Inventory

## Purpose

This file defines the initial evidence inventory for CASE-002 before empirical analysis begins.

The objective is to identify which datasets are required to discriminate among the competing hypotheses defined in the baseline framework and empirical protocol.

No hypothesis is preferred at this stage.

The presence of an available dataset is not sufficient reason to include it. Each dataset must have a specific explanatory role.

---

## Core Daily Dataset

### 1. U.S. 10-Year Treasury Yield

- Series: DGS10
- Source: Federal Reserve / FRED
- Frequency: Daily
- Type: Market-observed / official constant-maturity series
- Role: Primary dependent variable
- Hypotheses tested: H1, H2, H3, H4

Use:

Daily changes in the nominal 10-year Treasury yield are the primary outcome to be explained.

---

### 2. U.S. 2-Year Treasury Yield

- Series: DGS2
- Source: Federal Reserve / FRED
- Frequency: Daily
- Type: Market-observed / official constant-maturity series
- Role: Policy-sensitive front-end diagnostic
- Primary hypothesis: H1 — Policy Expectations

Use:

The 2-year yield is used as a diagnostic proxy for expected monetary-policy-path repricing.

A 10Y move accompanied by a similar-direction 2Y move is more consistent with a policy-path explanation than a long-end-only move.

Limitations:

The 2Y yield is not a pure measure of expected future policy rates and may itself contain term-premium and liquidity effects.

---

### 3. U.S. 30-Year Treasury Yield

- Series: DGS30
- Source: Federal Reserve / FRED
- Frequency: Daily
- Type: Market-observed / official constant-maturity series
- Role: Long-duration diagnostic
- Primary hypothesis: H2 — Term Premium / Duration Risk

Use:

The 30-year yield helps determine whether movements are concentrated in the long end of the curve.

Disproportionate long-end movement may indicate changing duration-risk compensation rather than only policy-path repricing.

---

### 4. 10-Year Breakeven Inflation Rate

- Series: T10YIE
- Source: Federal Reserve / FRED
- Frequency: Daily
- Type: Market-derived inflation-compensation measure
- Role: Inflation-compensation diagnostic
- Primary hypothesis: H3 — Inflation Compensation

Use:

The series is used to determine whether nominal 10Y yield movements are associated with changes in inflation compensation.

Interpretation:

Nominal 10Y ≈ real 10Y + inflation compensation.

Limitations:

Breakeven inflation reflects both expected inflation and inflation-risk / liquidity premia and should not be interpreted as a pure inflation-expectation measure.

---

### 5. 10-Year Treasury Inflation-Indexed Security Yield

- Series: DFII10
- Source: Federal Reserve / FRED
- Frequency: Daily
- Type: Market-observed real-yield proxy
- Role: Real-yield decomposition
- Primary hypotheses: H3 and H4

Use:

The 10-year real yield is used to identify whether nominal Treasury movements are primarily real-rate moves rather than inflation-compensation moves.

A nominal 10Y move with stable breakevens and a similar-sized real-yield move strengthens the case for a real-rate mechanism.

Limitations:

TIPS yields may contain liquidity effects and are not identical to a model-pure expected real-rate path.

---

### 6. 10-Year Treasury Term Premium

- Series: 10-year term-premium estimate
- Source: Federal Reserve Bank of New York
- Model: ACM-style Treasury term-premium estimate
- Frequency: Daily
- Type: Model-based estimate
- Role: Long-duration risk-compensation diagnostic
- Primary hypothesis: H2 — Term Premium / Duration Risk

Use:

The series is used to determine whether changes in the nominal 10-year Treasury yield are associated with changes in estimated term premium.

Important limitation:

Term premium is latent and cannot be directly observed.

The estimate is model-dependent and must not be treated as a direct market price or a uniquely identified causal factor.

---

## Hypothesis-to-Core-Data Map

| Hypothesis | Primary Evidence | Core Diagnostic |
|---|---|---|
| H1 — Policy Expectations | DGS2 | DGS10 |
| H2 — Term Premium / Duration Risk | NY Fed 10Y term premium | DGS30, curve behavior |
| H3 — Inflation Compensation | T10YIE | DFII10 |
| H4 — Real Growth / Equilibrium Real Rate | DFII10 | DGS10 |

---

## Secondary Evidence — Not Yet Frozen

The following datasets may be added if they materially improve discrimination among H1-H4.

They are not part of the initial core dataset.

### Policy Path

- Fed funds futures
- SOFR futures
- OIS-implied policy path
- FOMC projections

Potential role:

Separate expected short-rate repricing from broader front-end yield movement.

Status: TBD

---

### Inflation Expectations

- 5y5y forward inflation compensation
- inflation swaps

Potential role:

Distinguish short-horizon inflation repricing from longer-horizon inflation expectations.

Status: TBD

---

### Treasury Supply / Duration Risk

- Treasury auction results
- issuance composition
- quarterly refunding announcements
- weighted-average maturity / duration supply measures

Potential role:

Test whether increases in duration supply are associated with term-premium repricing.

Status: TBD

---

### Federal Reserve Balance Sheet / QT

- SOMA holdings
- Treasury runoff
- reserve balances

Potential role:

Test whether changes in official duration absorption affect long-end risk compensation.

Status: TBD

---

### Interest-Rate Volatility

- MOVE Index or comparable rate-volatility measure

Potential role:

Test whether higher rate uncertainty is associated with higher term premium.

Status: TBD

---

### Growth / Real-Rate Evidence

- growth-surprise indicators
- productivity data
- real GDP revisions
- investment / demand indicators

Potential role:

Test whether real-yield movements coincide with changes in growth expectations.

Status: TBD

---

### Equilibrium Real Rate

- Laubach-Williams / Holston-Laubach-Williams r-star estimates
- other Federal Reserve equilibrium-real-rate estimates

Potential role:

Provide medium- and long-run context for H4.

Important limitation:

r-star estimates are model-based, low-frequency, and subject to revision.

They should not be treated as a daily market driver.

Status: Secondary / contextual only

---

## Source Classification

Each dataset must be classified as one of:

- Market-observed
- Market-derived
- Official administrative data
- Model-based estimate
- Event data
- Survey / expectation measure

Model-based and market-derived measures must not be presented as directly observed causal variables.

---

## Frequency Rule

Daily frequency is preferred for the core market dataset.

Variables with lower native frequency must remain at their original frequency unless a specific transformation is justified.

Quarterly or event-level data must not be mechanically interpolated into daily observations.

---

## Revision Rule

For each secondary dataset, the following must be recorded before use:

- whether historical observations are revised;
- whether vintage data are available;
- whether the analysis uses current revised values or real-time values.

If revision status materially affects interpretation, the dataset must be treated separately.

---

## Inclusion Rule

A secondary series will be added only if it helps distinguish among competing mechanisms.

A dataset will not be included solely because it is available or commonly used.

---

## Inventory Status

Core dataset: PROVISIONALLY FROZEN

Secondary evidence: OPEN

Next step:

Verify exact source URLs, series identifiers, availability, start dates, and revision properties before data collection begins.
