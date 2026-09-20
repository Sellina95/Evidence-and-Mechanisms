# CASE-001 — Cross-Asset Event Tape

## Event Definition

- Event: September 2026 FOMC policy decision
- Decision date: 2026-09-16
- Announcement time: 2:00 p.m. ET
- Policy action: +25 bp
- Target range: 3.75%–4.00%

## Objective

Reconstruct the cross-asset response around the September 2026 FOMC decision before attempting to explain the mechanism.

The purpose of this event tape is to distinguish:

- immediate announcement effects,
- same-day repricing,
- next-day continuation or reversal,
- maturity-specific Treasury responses,
- and cross-asset divergence.

No causal explanation is accepted at this stage.

## Event Windows

| Window | Definition |
|---|---|
| Pre-FOMC | Market state immediately before the 2:00 p.m. ET announcement |
| Announcement | Immediate post-2:00 p.m. ET response |
| Same-Day Close | September 16 market close |
| +1D | September 17 |
| +2D | September 18 |

## Cross-Asset Tape

| Window | UST 2Y | UST 10Y | UST 30Y | USD | S&P 500 | Nasdaq | BTC | EM FX |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Pre-FOMC (Sep 15 close) | 4.67% | 5.00% | 5.36% | TBD | 7,585.73 | 25,981.57 | TBD | TBD |
| Event Day (Sep 16 close) | 4.74% | 5.01% | 5.35% | ↑ ~0.7% | 7,552.14 | 25,978.43 | TBD | TBD |
| +1D (Sep 17 close) | 4.67% | 4.94% | 5.29% | ↓ slightly | 7,637.74 | 26,418.30 | TBD | TBD |
| +2D (Sep 18 close) | 4.76% | 5.01% | 5.34% | TBD | 7,650.50 | 26,522.55 | ↑ 5.9% on day | TBD |

## Provenance

### Data Contract v0.1

#### Event authority
- FOMC decision and timestamp: Federal Reserve
- Event timestamp: 2026-09-16 14:00 ET

#### U.S. Treasury yields
- Primary source: U.S. Department of the Treasury Daily Treasury Par Yield Curve Rates
- Series: 2Y, 10Y, 30Y
- Unit: percent yield
- Daily comparison: level and basis-point change
- Intraday announcement response: separate market-source evidence where available
- Do not treat daily Treasury observations as exact 2:00 p.m. event prices.

#### Risk assets / FX
- S&P 500 and Nasdaq: index levels / percentage returns
- USD: broad dollar index, exact series to be fixed before calculation
- Bitcoin: USD price, with timestamp convention explicitly stated
- EM FX: individual currency pairs rather than an undefined aggregate; currencies to be selected before calculation

#### Window discipline
- Pre-FOMC baseline: 2026-09-15 close
- Event day: 2026-09-16
- +1D: 2026-09-17
- +2D: 2026-09-18
- Intraday announcement observations must be labeled separately from daily-close observations.

## Initial Observations

TBD

## Interpretation

**LOCKED until event reconstruction is complete.**