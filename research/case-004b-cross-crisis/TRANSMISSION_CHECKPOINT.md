# CASE-004B — Cross-Crisis Transmission Checkpoint

Status: INTERIM RESEARCH CHECKPOINT — NOT FINAL

## Research objective

Identify recurring financial-system vulnerabilities across banking
crises, investigate the ordering and transmission of financial signals,
and eventually test conditional mechanisms of shock amplification.

## Findings so far

Credit/GDP expansion is the strongest recurring historical leading
indicator candidate identified in this research.

Earlier within-country/era comparisons, country-cluster bootstrap,
chronological holdout, and global-financial-crisis exclusions provide
supporting historical association evidence.

The chronological holdout AUC for credit alone was 0.718.
Excluding test index years 2005–2009, its AUC was 0.750.
These results are retrospective and not real-time predictive claims.

## Transmission sequence evidence

JST crisis markers: 88 across the historical sample.
Modern crisis markers (1981 onward): 23.
Modern crisis markers excluding 2007–2009: 10.

In the modern ex-GFC matched-control comparison,
pre-crisis changes from T-5 to T-1 yielded:

| Indicator | Paired median gap | Positive pairs |
|---|---:|---:|
| Credit/GDP | +9.692 percentage points | 9/10 |
| Loan/Deposit ratio | +13.002 ratio points | 8/10 |
| Real house price | +19.600 percentage points | 8/10 |
| Noncore funding | +0.032 variable units | 5/10 |
| Bank capital ratio | +0.232 variable units | 7/10 |

These comparisons are descriptive, not causal. Controls were selected
retrospectively using quiet periods without nearby crisis markers.
Per-indicator matching may select different control years.

Aggregate event-time medians do not establish within-crisis temporal
ordering. Globally shared episodes are correlated.

## Mechanism experiments

Simple rate-rise and house-price-decline amplification tests did not
establish the hypothesized additional damage from prior credit expansion.

Housing interaction with country/year fixed effects:
- Full history: +0.7873, 95% CI [0.0709, 1.5037]
- Excluding 2005–2009: +1.0589, CI [0.1865, 1.9314]
- Modern 1981–2017: -0.1198, CI [-0.7280, 0.4883]

No causal amplification mechanism is established.

Trilemma-IV exploratory first-stage, with country/year fixed effects:
- Full sample: clustered Wald t-squared = 3.010
- Modern 1981 onward: clustered Wald t-squared = 2.805

The instrument's exact construction and identifying assumptions
remain unverified; weak-instrument concerns remain.

## Open limitations

- JST crisis-marker definitions and release vintages
- Real-time information availability and data revisions
- Global crisis dependence and overlapping outcomes
- Small numbers of independent modern crisis episodes
- Retrospective control selection
- Institution-level mechanism and causal identification
- Independent validation of any future pathway model

## Next investigation

Within-event ordering of credit, funding, balance-sheet and asset-price
changes, followed by comparisons against resilient/non-crisis episodes.

Do not treat credit expansion as a universally required first event.
Do not modify GCF production or previously frozen evidence.
