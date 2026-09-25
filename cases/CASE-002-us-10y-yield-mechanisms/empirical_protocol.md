# CASE-002 — Empirical Protocol

## Purpose

This protocol defines the evidence required to evaluate competing explanations for movements in the U.S. 10-year Treasury yield.

The protocol is frozen before examining the full empirical results.

The objective is not to maximize model fit or select the most persuasive narrative.

The objective is to determine which mechanism best explains observed 10-year yield movements, when that explanatory relationship becomes visible, and under what conditions it weakens or breaks.

---

## Primary Outcome

Primary variable:

- Daily change in the U.S. 10-year nominal Treasury yield

Notation:

Δ10Y

The analysis focuses on changes rather than yield levels in order to reduce the risk of attributing common trends or non-stationary movements to a causal mechanism.

---

## Diagnostic Yields

The following are used as diagnostics rather than primary targets:

- 2-year Treasury yield
- 30-year Treasury yield

Interpretation:

- 2Y is used primarily to diagnose policy-path repricing.
- 30Y is used primarily to diagnose long-duration and term-premium behavior.

These yields are not treated as substitutes for the 10Y target.

---

## Core Decompositions

Two decompositions are used as diagnostic frameworks.

### Inflation decomposition

Nominal 10Y
=
Real 10Y
+
Inflation compensation

This identifies whether a nominal yield move is primarily associated with changes in real yields or inflation compensation.

It does not by itself identify the underlying cause.

### Term-structure decomposition

Nominal 10Y
≈
Expected future short-rate path
+
Term premium

This identifies whether a long-rate move is primarily associated with expected policy-path repricing or changing compensation for duration risk.

It does not by itself identify the ultimate driver of either component.

---

## Competing Hypotheses

### H1 — Policy Expectations

Claim:

Changes in the 10-year Treasury yield are primarily driven by repricing of the expected future short-rate path.

### Primary evidence

- 2-year Treasury yield
- Fed funds futures and/or OIS / SOFR-implied policy path

### Supporting evidence

- FOMC projections
- policy-sensitive front-end rates
- meeting-specific repricing

### Evidence supporting H1

H1 is supported when:

- 10Y moves in the same direction as the expected policy path;
- 2Y and other policy-sensitive rates move consistently with the 10Y;
- changes in expected short rates account for a meaningful portion of the 10Y move.

### Evidence weakening H1

H1 is weakened when:

- 10Y moves materially while the expected policy path is approximately unchanged;
- 10Y and 2Y move in opposite directions without a clear policy explanation;
- most of the move appears in term-premium or long-duration components.

### Falsification condition

A sustained period in which large 10Y moves occur without corresponding policy-path repricing would reject policy expectations as the dominant explanation for that period.

---

### H2 — Term Premium / Duration Risk

Claim:

Changes in the 10-year Treasury yield are primarily driven by changing compensation for holding long-duration Treasury exposure.

### Primary evidence

- model-based 10Y term premium estimate

### Supporting evidence

- 10s30s and 2s10s curve behavior
- long-end relative moves
- Treasury issuance / duration supply
- auction outcomes
- Federal Reserve balance-sheet runoff / QT
- interest-rate volatility

### Evidence supporting H2

H2 is supported when:

- the 10Y moves closely with the estimated term premium;
- the long end moves disproportionately relative to the policy-sensitive front end;
- changes in supply, auction risk, volatility, or duration demand are consistent with the direction of term-premium repricing.

### Evidence weakening H2

H2 is weakened when:

- term-premium estimates remain stable while the 10Y moves materially;
- the move is concentrated in policy-sensitive maturities;
- inflation compensation or expected short rates explain most of the move.

### Falsification condition

A sustained period in which 10Y changes are large but term-premium estimates and long-end relative behavior remain stable would reject term premium as the dominant explanation for that period.

---

### H3 — Inflation Compensation

Claim:

Changes in the 10-year nominal Treasury yield are primarily driven by changes in expected inflation or inflation-risk compensation.

### Primary evidence

- 10-year breakeven inflation

### Supporting evidence

- 5y5y inflation compensation or inflation swaps, if available
- inflation data surprises
- commodity and energy-price shocks

### Evidence supporting H3

H3 is supported when:

- nominal 10Y moves are accompanied by similar-direction movements in breakeven inflation;
- a meaningful portion of the nominal yield move is accounted for by inflation compensation;
- inflation-related shocks coincide with the move.

### Evidence weakening H3

H3 is weakened when:

- nominal 10Y moves materially while breakeven inflation is approximately unchanged;
- the move is concentrated in real yields;
- inflation-related shocks fail to produce corresponding inflation-compensation repricing.

### Falsification condition

A sustained period of large 10Y moves with approximately stable inflation compensation would reject inflation compensation as the dominant explanation for that period.

---

### H4 — Real Growth / Equilibrium Real Rate

Claim:

Changes in the 10-year Treasury yield are primarily driven by changes in real-rate expectations associated with growth, productivity, or the equilibrium real rate.

### Primary evidence

- 10-year real Treasury yield

### Supporting evidence

- growth-surprise indicators
- productivity data
- r* estimates
- real-rate-sensitive macro releases

### Evidence supporting H4

H4 is supported when:

- nominal 10Y moves are primarily real-yield moves;
- growth or productivity repricing is consistent with the direction of the real-yield move;
- inflation compensation remains relatively stable.

### Evidence weakening H4

H4 is weakened when:

- real yields are stable while nominal yields move materially;
- most of the move is explained by inflation compensation or policy-path repricing;
- changes in growth or productivity expectations are inconsistent with the rate move.

### Falsification condition

A sustained period in which 10Y moves materially while real yields and growth-related proxies remain stable would reject the real-growth / equilibrium-real-rate mechanism as the dominant explanation for that period.

---

## Evidence Frequency

Default frequency:

- daily for market prices and yield decompositions

Additional frequencies may be used when required by the native frequency of the evidence:

- event-level for FOMC decisions and Treasury auctions;
- weekly or monthly for selected supply and positioning measures;
- quarterly or model-vintage frequency for productivity and r* estimates.

Lower-frequency variables must not be mechanically forced into a daily framework.

---

## Sample Design

The analysis will use:

1. a recent-regime window to identify the mechanism currently associated with 10Y moves;
2. a broader historical window to determine when that relationship emerged and whether it is persistent or episodic.

Exact sample dates and rolling-window lengths will be frozen after source frequency and availability are verified.

They will not be chosen based on which specification produces the strongest fit.

---

## Onset Definition

The onset of a mechanism is the earliest period in which:

- its primary proxy begins to move consistently with Δ10Y;
- the relationship persists beyond isolated event days;
- competing mechanisms do not explain the same move more directly.

Onset is not defined by a single visually convenient date.

If the evidence does not identify a clear transition, onset remains UNKNOWN.

---

## Break Definition

A mechanism is considered to weaken or break when one or more of the following occur:

- Δ10Y moves materially without a corresponding move in the mechanism's primary proxy;
- the sign of the historical relationship reverses;
- residual variation rises materially;
- another mechanism accounts for the move more directly;
- the relationship becomes dependent on a new condition not present in the earlier regime.

A break may be temporary, event-specific, or persistent.

These cases should be distinguished where possible.

---

## Assessment Labels

Each hypothesis will be assigned one of the following statuses:

- SUPPORTED
- PARTIALLY SUPPORTED
- WEAKENED
- REJECTED
- UNRESOLVED

UNKNOWN remains a valid final result.

---

## Data-Selection Rule

Data will be collected only if it helps distinguish among H1-H4.

The presence of an available dataset is not sufficient reason to include it.

Every series must have a stated role in discriminating among competing mechanisms.

---

## Pre-Analysis Freeze

Before empirical collection begins, the following must be frozen:

- primary outcome
- diagnostic yields
- hypothesis-to-evidence mapping
- primary and supporting proxies
- onset criteria
- break criteria
- sample-design principles

The following remain open until data availability is verified:

- exact sample start date
- exact historical comparison window
- exact rolling-window length
- secondary proxy inclusion

Protocol status: DRAFT — PRE-DATA FREEZE
