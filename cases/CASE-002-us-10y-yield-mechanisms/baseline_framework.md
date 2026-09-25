# CASE-002 — Baseline Framework

**Status: FROZEN BEFORE CASE-002 INVESTIGATION**
**Baseline freeze date: 2026-09-25 (Asia/Seoul)**
**Stage: framework freeze only; no data collected or hypotheses tested.**

## Prior Expectation

Changes in the U.S. nominal 10-year Treasury yield can reflect revised expected short rates, inflation compensation, and compensation for bearing duration risk. Their relative explanatory importance may vary across conditions and horizons. No single mechanism is preferred in advance.

The primary target is the **daily change in the nominal 10Y Treasury yield, in basis points**. The 2Y and 30Y yields are diagnostics for curve transmission, not alternative primary targets. Yield levels may supply context but are not the primary regression outcome.

CASE-001 motivates asking whether a mechanism extends beyond an event window. Its findings are prior context, not independently verified evidence for CASE-002 or grounds for preferring H2.

## Two Decompositions — Not Causes

### 1. Nominal / Real / Inflation Compensation

`Nominal 10Y yield = Real 10Y yield + 10Y inflation compensation`

For matched nominal and TIPS yield measures, inflation compensation is defined as their spread (breakeven inflation). This is an accounting decomposition of those selected measures. Maturity, instrument construction, and observation time must be aligned before comparison.

Inflation compensation is not pure expected inflation: it also reflects inflation risk compensation and relative liquidity or other instrument effects. A TIPS real yield is not a direct observation of the equilibrium real rate; expected real short rates, real risk premia, and liquidity can all matter.

### 2. Expected Short-Rate Path / Term Premium

`Nominal 10Y yield ≈ expected average nominal short-rate path over 10 years + nominal 10Y term premium`

This is a term-structure decomposition under a specified model and instrument convention. Expectations and term premium are estimated, not separately observed. Model choice, revisions, and approximation or measurement residuals must be recorded. The nominal term premium is not the same thing as a real term premium.

These are **two views of the same yield, not four additive independent components**. Inflation news can affect both expected policy rates and term premium; real-yield changes can reflect both expectations and risk compensation. Do not add contributions across the two decompositions or treat overlapping components as independent explanatory regressors.

Neither decomposition establishes a cause. “Term premium rose” identifies an estimated component; it does not establish whether supply, QT, uncertainty, auction risk, or duration demand caused the move. An exact accounting fit is not evidence of causal explanatory power.

## Expected Transmission

Conditional paths, holding competing channels approximately stable:

- H1: unexpected hawkish policy information → expected future short-rate path rises → nominal 10Y rises; dovish information reverses this path.
- H2: greater net duration supply or uncertainty / weaker duration demand → required duration-risk compensation rises → long-end yields rise; stronger demand or lower uncertainty reverses this path.
- H3: higher expected inflation or inflation-risk compensation → inflation compensation rises → nominal 10Y rises, unless offset elsewhere.
- H4: stronger expected real growth or a higher perceived equilibrium real rate → expected future real short rates rise → real 10Y and nominal 10Y rise, unless offset elsewhere.

Opposing channels can offset each other. A rate decision already priced in is not automatically a policy shock. Conditions listed below are predictions to test, not descriptions of the current market.

## Key Assumptions

1. Changes are compared over aligned trading days, timestamps, maturities, and publication vintages; missing or stale observations are not treated as zero changes.
2. Surprises and revisions to expectations matter more than announced levels alone. Information available at the time must be separated from later revisions.
3. Model estimates and market proxies contain uncertainty. The 2Y is not a pure policy-expectations measure, and the 30Y is not a pure duration-risk measure.
4. H1–H4 can coexist and overlap. Conditional dominance is testable; mutual exclusivity is not assumed.
5. Correlation, an accounting identity, and an in-sample fit cannot alone identify a causal mechanism or its onset.

## Expected Observations

| Variable / Indicator | Conditional expected behavior | Reason / limitation |
|---|---|---|
| Primary: daily Δ nominal 10Y | Responds to the net effect of competing channels | No unconditional directional prediction |
| Diagnostic: Δ2Y and 10Y–2Y slope | Front-end response helps assess H1 transmission | 2Y also contains risk and liquidity effects |
| Diagnostic: Δ30Y and 30Y–10Y slope | Long-end response helps assess duration and long-horizon channels | Curve shape alone cannot identify H2 or H4 |
| Δ real 10Y and Δ inflation compensation | Locate the nominal move across the first decomposition | Do not identify growth or inflation expectations by themselves |
| Estimated path and term-premium changes | Locate the nominal move across the second decomposition | Depend on the model; avoid circular attribution |

## Competing Hypotheses and Falsification Conditions

Falsification applies to a hypothesis's claim to explain the selected window, not to the universal existence of the mechanism. A single offsetting day is insufficient to reject a mechanism. Persistent contrary evidence after accounting for measurement uncertainty and competing channels weakens it; missing identifying evidence leaves it UNRESOLVED.

### H1 — Policy-Expectations Mechanism

**Claim:** Repricing of the expected Fed short-rate path is the leading explanation of nominal 10Y changes in the evaluated window.

**If true, expected evidence:** Independently measured policy-path surprises or revisions precede or coincide with directionally consistent 10Y moves; the 2Y diagnostic and the estimated expectations component broadly corroborate the transmission.

**Conditions expected to strengthen it:** Unexpected policy communication or macro releases materially changing the anticipated policy path, with relatively stable duration-risk and liquidity conditions.

**What would weaken or falsify it:** Repeated substantial 10Y moves with little or oppositely signed independent policy-path repricing; 10Y variation concentrated in risk compensation; or failure of the path signal to add explanatory value against competing mechanisms in pre-specified comparisons. A near-term policy instrument alone cannot establish the full ten-year expected path.

**Conditions under which dominance may break:** Policy decisions are already priced in, or supply, uncertainty, and long-end demand shocks offset or dominate policy repricing.

**Taylor Rule:** Auxiliary baseline for H1 only. Its inflation-gap / activity-gap policy response can organize a conditional expected policy reaction. It is not the main explanation, an observed Fed reaction function, or a direct model of the 10Y yield. Coefficients, gap estimates, and the equilibrium real rate are uncertain; any numerical specification must be fixed before testing.

**Status: OPEN**

### H2 — Term-Premium / Duration-Risk Mechanism

**Claim:** Changes in required compensation for bearing duration risk are the leading explanation, potentially transmitted through Treasury supply, QT, uncertainty, volatility, auction risk, or duration demand.

**If true, expected evidence:** Term-premium estimates broadly agree on relevant changes, and independent, timed supply / demand / uncertainty evidence supports the proposed risk-compensation channel. Long-end diagnostics help distinguish it from simple policy-path repricing.

**Conditions expected to strengthen it:** Unexpected net duration supply, reduced risk-bearing capacity, elevated uncertainty, or weak long-duration demand.

**What would weaken or falsify it:** Term-premium changes are small or opposite to the predicted contribution across credible specifications; independently measured policy expectations explain the moves better; or the proposed supply / demand / uncertainty trigger occurs after the repricing or lacks corroboration. A model residual labeled term premium is insufficient evidence of the trigger.

**Conditions under which dominance may break:** Strong offsetting duration demand, falling uncertainty, or dominant policy-path news. If models disagree materially, attribution remains UNRESOLVED.

**Status: OPEN**

### H3 — Inflation-Compensation Mechanism

**Claim:** Repricing of expected inflation and/or inflation risk, transmitted through inflation compensation, is the leading explanation of nominal 10Y changes.

**If true, expected evidence:** Inflation-compensation changes account for a material, directionally consistent portion of the nominal move, with independent inflation news or expectations evidence and checks for relative liquidity distortions.

**Conditions expected to strengthen it:** Persistent inflation surprises, de-anchoring concerns, or changes in inflation uncertainty, without a larger offset from real yields.

**What would weaken or falsify it:** Inflation compensation is repeatedly flat or moves opposite to nominal 10Y while real yields account for the movement; apparent breakeven changes are mainly instrument/liquidity effects; or independent evidence fails to corroborate inflation repricing. Flat breakevens weaken this compensation-channel claim but do not rule out inflation news acting through H1 or H2.

**Conditions under which dominance may break:** Anchored long-run inflation expectations, transitory inflation shocks, or real-rate / policy-path adjustments dominating the nominal response.

**Status: OPEN**

### H4 — Real-Growth / Equilibrium-Real-Rate Mechanism

**Claim:** Revisions to expected real growth, productivity, or the equilibrium real rate are the leading explanation through expected future real short rates.

**If true, expected evidence:** Real-yield changes align with independently documented revisions to real-growth or longer-run real-rate expectations; the transmission survives checks for policy surprises, real risk premia, and TIPS liquidity.

**Conditions expected to strengthen it:** Persistent changes to perceived growth prospects or productivity that plausibly alter expected real-rate paths beyond near-term policy news.

**What would weaken or falsify it:** Real yields do not respond consistently to the proposed revisions; nominal moves are mainly inflation compensation; or policy repricing, risk premia, or liquidity explain the real-yield moves without independent support for growth / equilibrium-rate revisions. A higher TIPS yield alone does not establish a higher equilibrium real rate.

**Conditions under which dominance may break:** Growth news is temporary, policy reactions offset its effect, or duration-risk / liquidity shocks dominate. An equilibrium-rate estimate too uncertain to distinguish H4 from H1/H2 leaves H4 UNRESOLVED.

**Status: OPEN**

## Freeze Boundary

This freezes the question's conceptual baseline, conditional transmission, competing hypotheses, and falsification logic. It does not claim that a complete empirical protocol or a winning mechanism has been established.

Before later data collection, separately freeze the exact observation endpoint, sample dates, sources, transformations, model vintages, comparison metrics, materiality thresholds, and onset/break criteria described in [Research Question](question.md). Log dated amendments and their rationale; do not silently rewrite this prior baseline after examining results.

No evidence assessment, conclusion, or reusable framework update is made here. **UNKNOWN is valid** if mechanisms cannot be distinguished.
