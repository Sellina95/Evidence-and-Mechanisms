# CASE-003 — Data Source Inventory V1

Status: PROVISIONAL — NOT FROZEN
Scope: Source discovery and metadata only.
No empirical analysis or ICE historical data ingestion authorized.

## 1. Required ICE BofA OAS Series

| Role | FRED ID | Series |
|---|---|---|
| Baseline predictor | BAMLH0A0HYM2 | US High Yield OAS |
| Predictor component | BAMLH0A1HYBB | BB High Yield OAS |
| Diagnostic | BAMLH0A2HYB | B High Yield OAS |
| Predictor component | BAMLH0A3HYC | CCC & Below High Yield OAS |
| Track B outcome | BAMLC0A4CBBB | BBB US Corporate OAS |

All series are ICE Data Indices products.

CCC-BB differential = CCC OAS - BB OAS.
Original OAS units: percent.
Convert to basis points by multiplying by 100.

## 2. Historical Source Discovery

Historical FRED TXT snapshots were identified through
Internet Archive / Wayback Machine.

The first four HY series were previously located.
Their archived endpoints differ and require validation.

BBB archive candidate:

https://web.archive.org/web/20230924194354id_/https://fred.stlouisfed.org/data/BAMLC0A4CBBB.txt

Reported by Grok:
- First observation date: 1996-12-31
- Last observation date: 2023-09-21
- Date rows: 7,062
- Missing observations: 86
- Valid observations: approximately 6,976
- Frequency: daily
- Units: percent

These metadata are externally reported, not independently
validated within this repository.

## 3. Recent BBB Data

FRED series:
https://fred.stlouisfed.org/series/BAMLC0A4CBBB

Grok-reported recent coverage:
2023-10-23 through 2026-10-19.

There is a gap between the reported historical and recent
segments, with no directly overlapping observations.

Do not assume the segments are revision-consistent.
Do not interpolate or forward-fill the gap.
Do not calculate trailing or forward windows across it.

## 4. Joint Sample Integrity

The five archived series have different ending dates.

Before any empirical analysis:
- Determine the actual common-date intersection.
- Verify units and missing observations.
- Check duplicates and date alignment.
- Check publication and decision-time availability.
- Prevent trailing and forward windows from crossing gaps.
- Preserve source provenance and revision uncertainty.

## 5. Research Architecture

Track A:
Predict future HY OAS widening.
BB OAS widening is a diagnostic outcome.

Track B:
Predict future BBB OAS widening.

Both tracks compare:
Model A: HY OAS level + trailing change.
Model B: Model A + CCC-BB level + trailing change.

Same eligible dates, same evaluation folds.

Mechanical overlap and common macro shocks must be
distinguished from genuine incremental predictive information.

## 6. Licensing Gate

ICE licensing and permitted research/publication uses
remain unresolved.

Historical archive accessibility does not establish
permission to use or redistribute ICE data.

Until written clarification:
- Do not ingest restricted historical observations.
- Do not run empirical backtests using those observations.
- Do not commit raw or reconstructed ICE series.
- Do not publish derived empirical charts or statistics.

Protocol design and source metadata documentation may continue.

## 7. Remaining Gates

1. ICE written licensing clarification.
2. Independent source and metadata verification.
3. Common sample and missing-data audit.
4. Walk-forward, purge, and embargo design.
5. Outcome threshold calibration policy.
6. Protocol freeze before empirical testing.
