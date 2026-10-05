# CASE-002 Recent Intraday Confirmation V0

## Purpose

This is a limited recent confirmation layer for the frozen daily event study.

It does not replace the historical daily evidence and is not treated as standalone causal identification.

ETF returns are market proxies:

- SHY: short Treasury proxy
- IEF: intermediate Treasury proxy
- TLT: long Treasury proxy
- TIP: TIPS proxy

Bond ETF prices generally move inversely to yields.

## Coverage

- Events with at least one usable intraday proxy: 10
- Events with all four proxies available: 6
- Events with partial proxy coverage: 4

The recent sample is small because Yahoo/yfinance intraday history is limited.

Missing ETF observations are not imputed or substituted.

## Available Events

- FOMC_STATEMENT_20260729 | COMPLETE | SHY 0.048968% | IEF -0.037499% | TLT -0.322211% | TIP 0.057037%
- FOMC_PRESS_20260729 | COMPLETE | SHY 0.061017% | IEF 0.069637% | TLT -0.256982% | TIP 0.107660%
- FOMC_STATEMENT_20260916 | COMPLETE | SHY -0.170458% | IEF -0.263193% | TLT 0.049253% | TIP -0.311234%
- FOMC_PRESS_20260916 | COMPLETE | SHY -0.098465% | IEF -0.287535% | TLT -0.294901% | TIP -0.313990%
- CPI_20260714 | PARTIAL | SHY 0.109984% | IEF 0.278522% | TLT 0.165238% | TIP NA%
- CPI_20260812 | PARTIAL | SHY 0.035274% | IEF 0.053700% | TLT -0.102999% | TIP NA%
- CPI_20260911 | PARTIAL | SHY -0.010803% | IEF 0.263129% | TLT 0.753962% | TIP NA%
- PCE_20260730 | COMPLETE | SHY -0.012195% | IEF -0.042923% | TLT -0.229054% | TIP -0.023841%
- PCE_20260826 | PARTIAL | SHY -0.048727% | IEF NA% | TLT -0.225938% | TIP NA%
- TREASURY_REFUNDING_20260805 | COMPLETE | SHY -0.013315% | IEF -0.117754% | TLT -0.192377% | TIP -0.018679%

## Interpretation Boundary

These intraday observations are confirmation proxies only.

They may help distinguish response timing — especially FOMC statement versus press conference — but they do not provide a full historical intraday causal-identification sample.

