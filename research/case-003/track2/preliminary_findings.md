# CASE-003 — Track 2 Preliminary Findings

Status: CLOSED — EXPLORATORY
Data: Chicago Fed NFCICREDIT and NFCIRISK
Original ICE hypothesis: NOT TESTED

## Research question

Does NFCI Credit provide incremental early-warning information
about future NFCI Risk deterioration?

## Results

### Historical walk-forward: 1990–2025

- Model A (Risk only) RMSE: 0.10284
- Model B (Risk + Credit) RMSE: 0.10282
- Overall RMSE improvement: approximately 0.02%
- Model B improved RMSE in 25 of 36 individual years.

### Large future Risk increases

- Test observations: 1,878
- Events: 34 (1.81%)
- ROC-AUC: A 0.7966 / B 0.7636
- PR-AUC: A 0.3548 / B 0.3373

Adding Credit worsened event-discrimination metrics.

### Historical threshold crossings

- 2008: Risk crossed 5 weeks before Credit.
- 2020: Risk crossed 1 week before Credit.

Thresholds were illustrative and series-specific.

### Weekly change lead-lag correlation

- Full historical sample: strongest at lag -2, r=0.561
- 1990–2025: strongest at lag -1, r=0.825
- 2007–2009: strongest at lag -1, r=0.911
- 2020: strongest at lag -1, r=0.965

Negative lag means Risk changes earlier than Credit changes.
These are descriptive, post-hoc lag selections, not proof of
statistical significance, causation, or real-time predictability.

Independent date-based alignment checks matched the original
lag calculations; weekly first differences also matched.

## Interpretation

The tested NFCI Credit features did not demonstrate robust
incremental early-warning value over NFCI Risk alone.

This is a provisional negative finding, not proof that no
predictive relationship exists.

## Limitations

- Revised historical series, not verified point-in-time vintages
- Publication timing and data availability not modeled
- Pre-publication backcast history included
- Related NFCI subindices may share information
- Overlapping four-week targets
- No statistical significance or uncertainty assessment
- Model and threshold choices not comprehensively validated
- No independent credit-default outcome tested

## Decision

Close Track 2 exploratory work without further model tuning.

Return to original CASE-003:
ICE BofA CCC & Below OAS minus BB OAS versus aggregate HY OAS.

The original ICE hypothesis remains UNTESTED.
Do not treat Track 2 findings as evidence for or against it.

Historical ICE data collection and use remain subject to
licensing clarification.
