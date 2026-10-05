# CASE-002 — Daily Competing-Mechanisms Specification

**Status: FROZEN BEFORE DAILY RESULTS**

**Freeze date: 2026-10-05 (Asia/Seoul)**

**Data endpoint: 2026-09-25**

**Estimation status: NOT RUN**

## A. What the first pass explains

The dependent variable is the change in the U.S. nominal 10-year Treasury constant-maturity yield between consecutive dates in the common analysis sample:

`d10_t = 100 × (DGS10_t - DGS10_{t-1})`

- Frequency: daily observations published in percent.
- Analysis unit: basis points (bp); multiplying a percentage-point change by 100 converts it to bp.
- Main outcome: daily bp change, not the yield level.
- `t-1`: the immediately preceding date in the frozen common-date sample, not necessarily the preceding calendar day.
- Interpretation: the move over one common observation interval. Weekend and holiday intervals remain valid but must be identified through an `interval_calendar_days` audit field.

The first pass measures same-interval association. It does not establish a structural cause, forecast the yield, identify an onset date, or create a production signal.

## B. Five operational mechanisms

The H1–H5 labels below are the operational order for this daily comparison. The frozen conceptual baseline remains unchanged: daily H2 implements its real-yield channel, daily H3 its inflation-compensation channel, daily H4 its term-premium channel, and daily H5 adds a curve-specific diagnostic.

| ID | Mechanism | Frozen regressor | Unit and timing | Data class | Expected coefficient sign | Permitted claim |
|---|---|---|---|---|---|---|
| H1 | Policy-path / front-end repricing | `d2_t = 100 × (DGS2_t - DGS2_{t-1})` | Same interval, bp | Market-observed official curve estimate | Positive | Front-end co-movement consistent with policy-path repricing |
| H2 | Real-yield repricing | `dreal10_t = 100 × (DFII10_t - DFII10_{t-1})` | Same interval, bp | Market-observed official TIPS curve estimate | Positive | Portion of the nominal move associated with the real-yield leg |
| H3 | Inflation-compensation repricing | `dbreakeven10_t = 100 × (T10YIE_t - T10YIE_{t-1})` | Same interval, bp | Derived market measure | Positive | Portion associated with breakeven inflation compensation |
| H4 | Term-premium repricing | `dacmtp10_t = 100 × (ACMTP10_t - ACMTP10_{t-1})` | Same interval, bp | Model-estimated | Positive | Co-movement with the current-vintage ACM model estimate |
| H5 | Long-end / curve-specific repricing | `d30_t = 100 × (DGS30_t - DGS30_{t-1})` | Same interval, bp | Market-observed official curve estimate | Positive | Long-end co-movement consistent with a broad or long-end rate move |

`DGS2` is a policy-sensitive front-end **proxy**, not a direct observation of Federal Reserve expectations. It also reflects term premium, macro expectations, liquidity, and other pricing effects. `DGS30` is likewise a long-end proxy, not a pure term-premium measure.

The H.15 constant-maturity series are official estimates derived from traded Treasury quotes and a fitted curve. “Market-observed” in this classification distinguishes them from a latent-variable model estimate; it does not mean each tenor is the closing yield of one fixed security.

### Curve diagnostics

Two slopes may be reported as diagnostics:

- `d_2s10s_t = d10_t - d2_t`
- `d_10s30s_t = d30_t - d10_t`

They are not sixth and seventh competing regressors. Each contains the dependent variable mechanically, so its correlation or regression fit against `d10_t` would be circular. They may describe where on the curve a move occurred, with no independent explanatory ranking.

No lagged regressor is in the first pass. No same-day/lag search, lead search, smoothing, rolling window, coefficient tuning, modern Taylor sensitivity, or recent Taylor extension is allowed after results are viewed. The already completed staff-PIT Taylor-93 test remains a separate quarterly H1 auxiliary baseline.

## C. Frozen comparison rule

### Sources and endpoint

| Series | Exact source | Native frequency | Source availability / revision note |
|---|---|---|---|
| DGS2 | Federal Reserve Board H.15 via FRED: `https://fred.stlouisfed.org/series/DGS2` | Daily | Public daily series; FRED states observations are subject to revision |
| DGS10 | Federal Reserve Board H.15 via FRED: `https://fred.stlouisfed.org/series/DGS10` | Daily | Public daily series; FRED states observations are subject to revision |
| DGS30 | Federal Reserve Board H.15 via FRED: `https://fred.stlouisfed.org/series/DGS30` | Daily | Discontinued 2002-02-18 and reintroduced 2006-02-09; subject to revision |
| DFII10 | Federal Reserve Board H.15 via FRED: `https://fred.stlouisfed.org/series/DFII10` | Daily | Public daily TIPS constant-maturity series; subject to revision |
| T10YIE | Federal Reserve Bank of St. Louis via FRED: `https://fred.stlouisfed.org/series/T10YIE` | Daily | Derived from DGS10 and DFII10; subject to revision |
| ACMTP10 | Federal Reserve Bank of New York ACM term-premium dataset: landing page `https://www.newyorkfed.org/research/data_indicators/term-premia-tabs`; workbook `https://www.newyorkfed.org/medialibrary/media/research/data_indicators/ACMTermPremium.xls` | Daily published estimates | Current-vintage model output; historical real-time vintages are not assumed available |

The frozen calendar boundary is **2006-02-09 through 2026-09-25 inclusive**. The start is the DGS30 reintroduction date, which prevents H5 from using a shorter or discontinuous sample. The endpoint matches the CASE-002 baseline cutoff and prevents later observations from entering this first comparison.

Before estimation, save the raw downloads unchanged and record URL, retrieval timestamp with timezone, file name, file hash, source update date if supplied, units, and native frequency. The processed file must retain the level columns, current date, prior common date, and calendar-day interval.

### Common-date construction

1. Parse dates without forward-filling, interpolation, or replacement of missing values with zero.
2. Restrict every level series to the frozen calendar boundary.
3. Form the strict intersection of dates for which all six levels—DGS10 and the five regressors—are non-missing.
4. Sort that common-date table by date.
5. Difference every series between the same two consecutive common dates and convert all changes to bp.
6. Drop the first common level row because no preceding common observation exists.
7. Do not delete an interval because it spans a weekend, holiday, or other gap. Report the distribution and maximum of `interval_calendar_days`; investigate any unusual gap as a data-quality issue before reading model results.

This construction gives every univariate comparison exactly the same dates and change horizon. A missing observation in any one series removes that date for all mechanisms. No pairwise-complete samples are permitted in the main table.

“Same-day” means the same source-labeled observation date. These public daily series are not assumed to share a synchronized intraday timestamp or market close. The first pass therefore supports daily association only, not intraday ordering. Raw-file metadata must preserve any timestamp or release-time information the sources provide.

### Estimation and metrics

For each mechanism `k`, run one OLS regression with an intercept:

`d10_t = alpha_k + beta_k × x_k,t + error_k,t`

The first-pass output table must keep the fixed H1–H5 order and report:

1. Pearson correlation between `d10_t` and `x_k,t`;
2. univariate OLS R-squared;
3. estimated coefficient and whether its sign matches the pre-specified positive sign;
4. sample count `N`.

Also report the common first and last change dates and confirm that `N` is identical in all five rows. Means, standard deviations, and gap diagnostics may be reported only as data-quality context. Do not construct a composite score, choose a winner from R-squared alone, or reorder the table by the observed result.

Univariate comparison is the frozen first pass. A multivariate regression is excluded because the variables overlap economically, and some overlap mechanically. The previously proposed 20- and 60-day rolling diagnostics are deferred; they are not part of this first-pass freeze and cannot be added after viewing these results without a new dated pre-analysis addendum.

## D. Interpretation limits and failure modes

### Decomposition is not an independent contest

FRED defines 10-year breakeven inflation from the nominal and inflation-indexed 10-year constant-maturity series. With matched values:

`DGS10 = DFII10 + T10YIE`

and therefore, apart from publication precision or data handling:

`d10 = dreal10 + dbreakeven10`.

H2 and H3 are consequently decomposition channels. Their correlations and univariate R-squared values describe how variation is divided between correlated components; they do not give two independently identified causal models. A high fit for either cannot be compared in the same causal sense with H1, H4, or H5. The processed-data audit must verify the identity residual and stop if it is materially inconsistent with source rounding.

### Correlation and multicollinearity

- DGS2 and DGS30 are points on the same Treasury curve as DGS10, so common level, slope, and market shocks can make their changes highly correlated.
- DFII10 and T10YIE are structurally tied to DGS10 and can be correlated with each other through offsetting or common shocks.
- ACMTP10 is estimated from a Treasury yield curve. It is not statistically independent of DGS10, DGS2, or DGS30.
- The ACM model's fitted-yield convention and underlying zero-coupon curve differ from the H.15 constant-maturity outcome. Its change is a related model estimate, not an exact DGS10 accounting component.

These relationships are why the first pass is descriptive and univariate. A later multivariate design would require a separate freeze, an identification argument, and collinearity diagnostics before results are examined.

### PIT and claim-strength classification

| Class | Series | PIT / revision status | Maximum claim strength in this pass |
|---|---|---|---|
| Market-observed official curve estimates | DGS2, DGS10, DGS30, DFII10 | Public contemporaneously at daily frequency, but this study uses current downloaded histories; corrections or revisions remain possible and no ALFRED vintage reconstruction is claimed | Same-interval market co-movement |
| Derived market measure | T10YIE | Derived from current-vintage DGS10 and DFII10; inherits source revisions and contains inflation risk and relative-liquidity effects | Inflation-compensation association, not pure expected inflation |
| Model-estimated | ACMTP10 | Latent ACM estimate using a term-structure model; current historical file can change when data or estimation are updated, and is not treated as a real-time vintage archive | Association with an ex-post/current-vintage model estimate, not a contemporaneously tradable signal or causal proof |

The Federal Reserve notes that term premium cannot be directly inferred from market prices, different models can diverge, estimates can be sensitive to sample choice, and confidence intervals can be wide. H4 must therefore be labeled **MODEL ESTIMATE** in every results table and chart. Its fit cannot be used to claim that investors observed or traded the published historical estimate in real time.

## E. Next execution gate

The next task may only:

1. download and hash the six frozen sources;
2. build and audit the strict common-date changes;
3. verify the nominal/real/breakeven identity residual;
4. calculate the five frozen correlations and univariate regressions;
5. report coefficient sign and identical sample count;
6. show the two curve slopes only as diagnostics; and
7. publish the result with these interpretation limits.

It must not tune lags or windows, add sensitivities, rank causal winners, integrate GCF, set thresholds, or generate a production signal.
