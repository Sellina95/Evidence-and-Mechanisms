# 2021+ Fed-staff PIT coverage audit

Audit date: 2026-10-05. Scope: determine whether the frozen main Fed-staff-PIT Taylor-93-style series can be extended after 2020Q4 without changing its information set or output-gap concept. No alternative series is calculated here.

## Decision

**No PIT-safe, conceptually continuous extension is currently available for 2021Q1 onward.** The public Philadelphia Fed staff-gap workbook ends with `GBgap_201204`. The Federal Reserve's historical-materials index currently lists 2020 as its newest historical year. Because Tealbooks and the underlying staff information are released with about a five-year lag, the absence of a public 2021 staff-gap vintage is expected, but the approximate lag does not authorize inventing a release date or reconstructing a confidential series.

The main series therefore remains **2015Q2–2020Q4**. Later YPDGDP vintages do not solve the missing staff-gap input. No 2020 gap is carried forward and no latest-revised gap is backfilled.

## Source and availability ledger

| Candidate | Information owner / clock | Observed coverage or availability | Conceptual comparison with frozen staff gap | Decision |
|---|---|---|---|---|
| Philadelphia Fed `Greenbook_Output_Gap_DH_Web.xlsx` | Federal Reserve Board staff estimates used in constructing Tealbook forecasts; staff circulation date | Downloaded 2026-10-05; columns `GBgap_960321`–`GBgap_201204` | Same source and concept | **Eligible, but stops in 2020** |
| Federal Reserve historical FOMC materials | Confidential staff material made public later | Official index currently lists historical years through 2020; Tealbooks are distributed before meetings and historical materials are made public with about a five-year lag | Same institutional information set when released, but 2021 material is not currently present | **Cannot extend now** |
| Atlanta Fed real-time CBO output gaps | Public CBO potential GDP paired with the latest CBO vintage available at each BEA GDP release; Atlanta Fed construction rules | Available for recent quarters in the Taylor Rule Utility; update schedule is twice monthly | PIT-safe public alternative, but different institution, potential-output method, release clock and judgment set | **Do not splice into main; separate market-public design only** |
| CBO potential GDP vintages | Public CBO publications; irregular forecast/publication dates | Official 2021 outlook incorporated information available through 2021-01-12 and supplies potential-output estimates | Public CBO sustainable-output concept, not Board-staff judgmental gap | **Conceptually different** |
| FOMC SEP longer-run unemployment projections | FOMC participant projections released quarterly | Public contemporaneously; participant ranges/medians, not a staff output-gap series | Different variable and population; conversion needs an Okun coefficient and a new model choice | **Not comparable** |
| Philadelphia Fed SPF | Public survey with quarterly deadlines/releases | Current and historical real-GDP and price forecasts available | Panel forecasts do not supply the frozen Board-staff potential-output gap; deriving one would add a new model | **Not comparable** |
| Fleischman–Roberts / FRB-US model gap exposed by Atlanta Fed | Public model/code with Atlanta Fed estimation, revisions and nowcasts | Recent estimates available | Model-based, revised/extended inputs and Atlanta calculations; not the archived judgmental Tealbook staff gap | **Not a continuous extension** |

## Exact official evidence

1. [Philadelphia Fed output-gap page](https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/gap-and-financial-data-set) says the data contain real-time estimates and projections used by Board staff in constructing Tealbook/Greenbook forecasts. It also warns that some observations were reconstructed from incomplete or preliminary records and may contain errors. The downloaded file itself establishes the observed last vintage, `GBgap_201204`.
2. [Federal Reserve historical-materials description](https://www.federalreserve.gov/monetarypolicy/fomc_historical.htm) states that Tealbook A and B are Board-staff material distributed before regularly scheduled meetings and that meeting-related historical materials are made public with **about a five-year lag**.
3. [Federal Reserve historical-materials index](https://www.federalreserve.gov/monetarypolicy/fomc_historical_year.htm) lists **2020** as the newest available historical year at the audit date. The [2021 meeting calendar](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm) contains contemporaneous statements, minutes and SEP releases, but these are not the confidential staff output-gap vintages.
4. [Federal Reserve FEDS Note on real-time staff gaps](https://www.federalreserve.gov/econres/notes/feds-notes/real-time-historical-estimates-of-the-output-gap-20191015.html) defines the staff gap as the percent difference between actual and potential output, confirms that Board staff produce it for Tealbook forecasts eight times per year, and states that Tealbook projections are publicly released with a five-year lag.
5. [Atlanta Fed Taylor Rule Utility methodology](https://www.atlantafed.org/research-and-data/data/taylor-rule) says its real-time CBO gap pairs each BEA GDP estimate with the latest CBO potential-GDP estimate available at that release. It also documents special interpolation/extrapolation rules when CBO and BEA vintage bases differ. This is a credible public PIT construction, but those rules demonstrate why it is a different series rather than a continuation of the Board-staff gap.
6. [CBO's February 2021 outlook](https://www.cbo.gov/publication/56991) states that its forecast incorporated information available as of 2021-01-12 and defines the output gap relative to CBO potential GDP. This confirms a public 2021 vintage exists, while also identifying a different potential-output authority.

## Release-lag boundary

The phrase “about a five-year lag” is not an exact file-release calendar. As of the audit date, official availability is established by the files actually present, not by adding five years to a meeting date. A 2021 vintage becomes eligible for the frozen main series only after an official source publishes the corresponding Board-staff gap with enough vintage/date metadata to reproduce the existing selection rule.

## Reassessment trigger

Recheck the Philadelphia Fed output-gap workbook and Federal Reserve historical-materials index after an official 2021 historical release. If 2021 staff-gap vintages appear, append them without changing coefficients or earlier rows, preserve the new download separately with hashes, verify staff-date mappings, and rerun only the frozen construction. Until then, recent coverage remains unavailable rather than estimated.
