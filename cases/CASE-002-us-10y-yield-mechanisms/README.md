# CASE-002 — U.S. 10Y Yield Mechanisms

**Status: OPEN — first staff-PIT Taylor comparison completed (2026-10-05)**
**Baseline freeze date: 2026-09-25 (Asia/Seoul)**

## 1. Observation

Question-first investigation of which existing mechanism explains nominal U.S. 10Y Treasury yield changes and when its explanatory power strengthens or fails. No new market observation is established at this stage. The 2Y and 30Y are diagnostics.

## 2. Baseline Framework

[Frozen Baseline Framework](baseline_framework.md) records prior expectations, expected transmission, assumptions, expected observations, and H1–H4 with falsification conditions.

Two separate decompositions organize the question:

- Nominal 10Y = real 10Y + inflation compensation.
- Nominal 10Y ≈ expected short-rate path + term premium.

Neither decomposition is itself a causal explanation. Taylor Rule reasoning is an auxiliary H1 baseline only.

## 3. Observed Deviation

The first quarterly Taylor comparison is available. Mechanism dominance and breakpoints remain unresolved. See [first results and audit](validation/taylor93/README.md) and [Research Question](question.md).

## 4. Research Question

**Which existing economic or financial mechanism best explains current movements in the U.S. 10-year Treasury yield; when did its explanatory power emerge, why did it emerge, and under what conditions does it strengthen or break down?**

[Research Question and Scope](question.md) defines the primary target, diagnostics, time-anchor limitations, planned comparison, and exclusions.

## 5. Competing Hypotheses

| Hypothesis | Mechanism | Status |
|---|---|---|
| H1 | Policy-expectations | OPEN |
| H2 | Term-premium / duration-risk | OPEN |
| H3 | Inflation-compensation | OPEN |
| H4 | Real-growth / equilibrium-real-rate | OPEN |

Claims, expected evidence, strengthening/break conditions, and falsification criteria are frozen in [Baseline Framework](baseline_framework.md). None is preferred or tested.

## 6. Data Requirements

The [Taylor execution addendum](validation/taylor93/design.md) fixes inputs, alignment and first-comparison metrics. Verified overlap is 2015Q2–2020Q4 (23 signals). The wider daily-mechanism investigation still requires its remaining empirical choices to be fixed before testing.

## 7. Evidence

[First Taylor-93-style comparison](validation/taylor93/README.md): source downloads, staff/public availability distinction, quarterly series, EFFR then 2Y/10Y comparisons, diagnostic rates and validation. Taylor is usually above actual EFFR; level co-movement is stronger than change co-movement. No causal or mechanism-dominance conclusion is established.

## 8. Historical Analogs — Optional

Not selected. Any later analog requires a selection rule that helps discriminate mechanisms; CASE-001 is motivation, not proof of a persistent regime.

## 9. Conclusion

Not reached. Confidence is not assessed. **UNKNOWN is valid** if available evidence cannot distinguish the explanations.

## 10. Framework Update

None. No reusable framework or update log is changed by this baseline freeze.

## 11. Closure

Status: OPEN
Closed: Not applicable
Reusable framework updated: NO

## Research Files

- [Baseline Framework](baseline_framework.md)
- [Research Question](question.md)
- [First Taylor comparison and audit](validation/taylor93/README.md)
- [Frozen Taylor alignment addendum](validation/taylor93/design.md)
- [Repository Case Template](../../templates/case_template.md)

This README preserves the eleven-stage workflow. The original baseline remains intact; no reusable framework update or GCF production change follows from this first comparison.
