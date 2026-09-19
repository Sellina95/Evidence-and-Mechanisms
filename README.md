# Evidence and Mechanisms

An empirical research lab for testing explanations of economic, financial, and market phenomena.

## Purpose

This repository investigates concrete observations, anomalies, and questions by comparing prior expectations with empirical evidence.

The objective is not to produce trading signals, forecasts, or a continuously operated monitoring system.

Each case follows a bounded research process:

**Observation → Baseline Framework → Expected Transmission → Observed Deviation → Competing Hypotheses → Evidence → Conclusion → Framework Update**

A case may end without a definitive explanation. **UNKNOWN is a valid conclusion.**

## Research Principles

### 1. Question First

Research begins with a specific observation or question.

Data is selected because it helps answer that question, not because it is available.

### 2. Baseline Freeze

The baseline framework and expected transmission are recorded before explanatory investigation.

This preserves the distinction between prior expectation and hindsight.

### 3. Competing Hypotheses

Cases should consider at least two plausible explanations when multiple mechanisms could explain the observation.

The purpose is not to construct the most convincing narrative, but to discriminate among mechanisms.

### 4. Falsification Required

Each hypothesis should state what evidence would weaken, reject, or require reassessment of it.

### 5. Evidence Before Narrative

Observed facts, interpretation, and unresolved uncertainty should remain distinguishable.

Evidence should constrain the explanation rather than merely decorate it.

### 6. UNKNOWN Is Valid

If available evidence cannot distinguish among competing explanations, the case should remain unresolved.

No causal story is required for closure.

### 7. No Production Obligation

Cases are bounded research investigations.

They do not require:

- recurring data pipelines
- dashboards
- CI/CD
- scheduled automation
- daily updates
- deployment
- permanent operational maintenance

A case ends when the research question has been investigated to the useful limit of the available evidence.

## Repository Structure

- `cases/` — bounded empirical investigations
- `frameworks/` — reusable explanatory frameworks supported by completed cases
- `templates/case_template.md` — standard research workflow
- `framework_updates/update_log.md` — material revisions to reusable frameworks

## Research Lifecycle

```text
Observation
    ↓
Baseline Framework
    ↓
Expected Transmission
    ↓
Observed Deviation
    ↓
Research Question
    ↓
Competing Hypotheses
    ↓
Falsification Conditions
    ↓
Question-Driven Data
    ↓
Evidence
    ↓
Conclusion
    ↓
Framework Update
    ↓
Close
```

The repository is designed to improve explanatory frameworks through evidence, not to force every observation into an existing model.
