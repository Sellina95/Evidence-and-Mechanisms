# CASE-002 — Research Question

## Initial Observation / Motivation

This case begins with a question about the conditional explanatory power of existing mechanisms, not a newly verified market anomaly. CASE-001 motivates investigating whether an event-window explanation extends to a broader regime. Its findings and the prior conversation's numerical claims are not imported as CASE-002 evidence.

## Scope

- Market: U.S. Treasury yields.
- Primary target: daily changes in the **nominal 10Y Treasury yield**, measured in basis points.
- Diagnostics: 2Y and 30Y changes, 10Y–2Y and 30Y–10Y slopes; not co-primary outcomes.
- “Current” is anchored to the baseline freeze date, **2026-09-25 (Asia/Seoul)**, not a rolling reference to whenever the file is read. No current yield level or direction is asserted.
- The empirical endpoint must later be fixed to the latest complete U.S. trading session whose required observations were available at the freeze cutoff. Record exact timestamps and availability; do not assume same-calendar-day closes were available in Korea.
- Exact cutoff time, sample start, history for onset detection, and source availability are **not yet specified**. Freeze them in a dated empirical protocol before collecting or examining CASE-002 data.

## Observed Deviation — Not Yet Established

| Variable / Indicator | Expected | Observed | Match / Break / Unclear |
|---|---|---|---|
| Daily Δ nominal 10Y | Conditional net transmission of H1–H4 | Not collected | Unclear |
| 2Y / 30Y diagnostics | Curve patterns conditional on the active mechanism | Not collected | Unclear |
| Both 10Y decompositions | Locate the move without identifying its cause | Not collected | Unclear |

**Breakpoint:** UNKNOWN. Neither an onset date nor a regime break has been identified.

## Primary Research Question

**Which existing economic or financial mechanism best explains current movements in the U.S. 10-year Treasury yield; when did its explanatory power emerge, why did it emerge, and under what conditions does it strengthen or break down?**

현재 미국 10년 국채금리의 움직임을 가장 잘 설명하는 기존 경제·금융 메커니즘은 무엇인가? 그 설명력은 언제부터, 왜 나타났으며, 어떤 조건에서 강화되고 어떤 조건에서 깨지는가?

“Best explains” means comparative explanatory performance plus evidence discriminating the proposed transmission from rivals. It does not mean the highest fit obtained by regressing a yield on its own accounting components. A conditional combination or UNKNOWN is admissible.

## Planned Comparison — Not Executed

1. Use daily yield changes, rather than yield-level regressions, as the primary outcome. Preserve levels only as context.
2. Compare H1–H4 over a common sample with **20- and 60-trading-day rolling windows** as complementary short- and medium-window diagnostics. Small windows limit precision; correlated proxies cannot establish causal dominance.
3. In the later pre-data protocol, specify independent mechanism proxies, a simple benchmark, parameter limits, out-of-sample or held-out comparisons, fit/error metrics, and uncertainty treatment. Report incremental explanatory value, timing, sign consistency, and contradictory evidence; no single metric establishes causation.
4. Pre-specify how persistent an improvement must be to count as onset and how deterioration or failed transmission counts as a break. Require robustness across windows and relevant measurement specifications. Do not pick dates or thresholds after seeing a favorable result. Overlapping rolling windows are not independent confirmations.
5. Establish why a mechanism gained explanatory power using independently timed changes in its enabling conditions, not a post-hoc label for a fitted breakpoint. Distinguish statistical fit changes from causal identification.
6. Separate mixed mechanisms, offsetting contributions, and unavailable evidence from rejection. Do not force H1–H4 into mutually exclusive buckets. A break in a dominance claim need not invalidate the underlying mechanism everywhere.

## Question-Driven Data Requirements — Deferred

No datasets have been requested, downloaded, or analyzed for this case. The list below specifies evidence needs only; exact providers, series, timestamps, vintages, and windows remain for the pre-data protocol.

| Evidence needed | Hypothesis tested | Why needed | Source / window / frequency |
|---|---|---|---|
| Matched nominal 10Y, real 10Y, and inflation compensation | H3 / H4; common outcome | Locate nominal moves and inspect measurement effects | To freeze; aligned daily observations |
| 2Y / 30Y yields and curve slopes | H1 / H2 / H4 diagnostics | Check maturity-specific transmission | To freeze; same daily sample |
| Policy-path pricing and timestamped policy surprises | H1 versus H2 / H4 | Independent evidence of expected policy repricing | To freeze; daily plus selected event timestamps |
| Term-structure model estimates and documented vintages | H1 versus H2 | Separate estimated path and premium with model uncertainty | To freeze; aligned frequency, no artificial daily interpolation |
| Net duration supply, QT, auction information, demand, uncertainty | H2 | Identify a cause beyond a term-premium residual | To freeze; publication/event timing respected |
| Independent inflation expectations/news and liquidity checks | H3 | Separate inflation repricing from breakeven distortions | To freeze; native release frequency |
| Real-growth/productivity revisions and real-rate expectations | H4 versus H1 / H2 | Distinguish expected real rates from premia | To freeze; real-time vintages and native frequency |

## Out of Scope

- Data collection, empirical estimation, charts, hypothesis ranking, and conclusions at this stage.
- Trading signals, price forecasts, portfolio recommendations, or a continuous monitoring system.
- Explaining all maturities or all cross-asset movements as primary outcomes.
- Treating the Taylor Rule as the main 10Y explanation; it is only an H1 auxiliary baseline.
- Treating a decomposition, a model residual, or CASE-001's interpretation as causal proof.

## Constraint and Next Gate

The [Baseline Framework](baseline_framework.md) is frozen before CASE-002 explanatory investigation. H1–H4 remain **OPEN**. Complete and freeze the empirical protocol before any later evidence work; then establish observed movements before explaining them. **UNKNOWN is a valid eventual conclusion.**
