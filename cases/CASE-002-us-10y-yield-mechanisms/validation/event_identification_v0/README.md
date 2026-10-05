# CASE-002 Event Identification V0

## Purpose

Identify whether major U.S. Treasury yield moves around known macro/policy events are more consistent with:

- POLICY_PATH
- INFLATION_COMPENSATION
- TERM_PREMIUM_LONG_END
- MIXED
- INCONCLUSIVE

## Frozen event groups

1. FOMC policy events
2. CPI releases
3. PCE releases
4. Treasury Quarterly Refunding / supply events

## Historical sample

2023-01-01 through 2026-09-25.

## Evidence hierarchy

### Historical main evidence

Official daily rates data:

- DGS2
- DGS10
- DGS30
- DFII10
- T10YIE
- ACM 10Y term premium

Historical daily results are event-day associations, not strict intraday causal identification.

### Recent intraday confirmation

Where freely available:

- SHY
- IEF
- TLT
- TIP

Intraday proxy evidence does not replace official Treasury yield data.

## Event windows

For intraday confirmation:

- Main: T-10m to T+30m
- Robustness: T-10m to T+60m

FOMC statement/SEP and press conference are treated separately.

Treasury announcement and auction/result events are treated separately.

## Contamination rule

If another major scheduled event overlaps the identification window, mark:

contaminated = YES

and do not use the event as clean causal-identification evidence.

## Classification

Do not force classification.

Allowed states:

- POLICY_PATH
- INFLATION_COMPENSATION
- TERM_PREMIUM_LONG_END
- MIXED
- INCONCLUSIVE

No automatic thresholds are frozen yet.

## Important limitations

- DGS2 is policy-path-sensitive, not a direct measure of Fed expectations.
- T10YIE is inflation compensation, not pure expected inflation.
- ACM term premium is a model estimate and is used as secondary/ex-post evidence.
- DGS30 is a long-end diagnostic, not a pure term-premium measure.

## Classification Rule V0 — Frozen Before Labeling

The classification describes the **shape of the Treasury-market response**, not the event type itself.

For example, a CPI release is not automatically classified as INFLATION_COMPENSATION.

### POLICY_PATH

Use when:

- 10Y real yield moves in the same direction as the 10Y nominal yield.
- 2Y moves in the same direction as the 10Y yield.
- The absolute 2Y move is at least as large as the absolute 30Y move.
- The absolute real-yield move is larger than the absolute breakeven move.

Interpretation:

The move is more consistent with a policy-path-sensitive / real-rate repricing.

DGS2 is a proxy and is not treated as a direct measure of Fed expectations.

### INFLATION_COMPENSATION

Use when:

- 10Y breakeven moves in the same direction as the 10Y nominal yield.
- The absolute breakeven move is larger than the absolute real-yield move.

Interpretation:

The move is more consistent with inflation-compensation repricing.

T10YIE is not interpreted as pure expected inflation.

### TERM_PREMIUM_LONG_END

Use when:

- 30Y moves in the same direction as the 10Y yield.
- ACM 10Y term premium moves in the same direction as the 10Y yield.
- The absolute 30Y move is larger than the absolute 2Y move.
- The move is not dominated by inflation compensation.

Interpretation:

The move is more consistent with long-end / term-premium repricing.

ACM term premium is a model estimate, not a directly observed market price.

### MIXED

Use when:

- More than one classification pattern is simultaneously satisfied, or
- Policy-path and long-end signals are both strong enough that a single dominant mechanism cannot be cleanly identified.

### INCONCLUSIVE

Use when:

- No classification rule is satisfied.
- The 10Y move is effectively zero.
- Components strongly offset one another.
- Same-day market data are unavailable.
- The event is contaminated by another major event group.

### Important V0 rule

No absolute bp threshold is used in V0.

The purpose of V0 is to classify the **relative structure of the move**, not its size.

The classification rules must not be changed after viewing the resulting label distribution without creating a separately versioned specification.


## V0 Operational Clarification — Frozen Before First Label Run

This clarification was frozen before viewing any classification results.

For deterministic implementation:

1. If same-day data are unavailable or the event is contaminated:
   - INCONCLUSIVE

2. If the 10Y daily change is exactly 0 bp:
   - INCONCLUSIVE

3. Inflation evidence:
   - 10Y breakeven moves in the same direction as 10Y
   - |breakeven| > |real yield|

4. Policy-path evidence:
   - real yield moves in the same direction as 10Y
   - 2Y moves in the same direction as 10Y
   - |real yield| > |breakeven|

5. Long-end / term-premium evidence:
   - 30Y moves in the same direction as 10Y
   - ACM 10Y term premium moves in the same direction as 10Y
   - |real yield| >= |breakeven|

Classification order:

- Inflation evidence only -> INFLATION_COMPENSATION
- Policy evidence only -> POLICY_PATH
- Long-end evidence only -> TERM_PREMIUM_LONG_END
- Policy evidence AND long-end evidence -> MIXED
- Otherwise -> INCONCLUSIVE

No absolute basis-point threshold is introduced in V0.
