# CPDO Construction & Credit-Risk Modelling

**Collaborative university research · Quantitative finance · Credit spreads · Monte Carlo simulation · Dynamic leverage · Stress testing**

> **Research prototype, not a validated pricing, credit-rating or trading model.** Results depend on simplifying assumptions and have material unresolved modelling limitations.

## Research question

How can a dynamically leveraged structured-credit product appear resilient under ordinary spread conditions while suffering severe losses under a large credit-spread shock?

This project studies **Constant Proportion Debt Obligations (CPDOs)** through stochastic credit-spread modelling, dynamic exposure, cash-flow assumptions and portfolio net-asset-value (NAV) simulations.

## Project contents

| Resource | Description |
|---|---|
| [CIR + empirical-jump notebook](notebooks/01_cir_jump_cpdo.ipynb) | Original research model with revised exploratory default-loss logic |
| [Regime-switching notebook](notebooks/02_regime_switching_experimental.ipynb) | Alternative log-OU and regime-based approach; experimental |
| [Corrected-model results](docs/CORRECTED_RESULTS.md) | Selected exploratory outputs and important caveats |
| [Corrections and validation notes](docs/CORRECTIONS_AND_VALIDATION.md) | Changes made and remaining model risks |
| [Original submission report](docs/report_original_submission.md) | Historical submission, preserved for context |
| [Results audit](docs/RESULTS_AUDIT.md) | Inconsistencies and claims requiring verification |
| [Recorded results](docs/VALIDATION_RESULTS.json) | Machine-readable simulation summary |

## Selected exploratory results

The revised CIR/jump prototype was previously run with **2,000 simulated paths per scenario**, using seed **123**. A “default” in this model means crossing a simulated NAV floor; it is **not** equivalent to legal issuer default or an external rating classification.

| Scenario | NAV-floor event | Cash-out event | Mean final NAV |
|---|---:|---:|---:|
| Base case | 1.10% | 0.00% | 43.24 |
| Permanent +150 bp shock at year 3 | 99.80% | 0.00% | 10.03 |
| Initial spread of 200 bp | 0.00% | 10.45% | 81.71 |

These are exploratory model outputs, **not real-world default forecasts**. They are retained as previously recorded results and are not independently verified by the lightweight integrity test.

## Method overview

1. Inspect historical investment-grade credit-spread and interest-rate observations (locally sourced inputs are not redistributed here).
2. Estimate a mean-reverting CIR-style spread process and empirical jump component.
3. Simulate dynamic leverage, carry, coupon obligations, spread mark-to-market and NAV triggers.
4. Explore baseline and hypothetical shock scenarios.
5. Identify model risk, data limitations and inconsistencies between the submitted report and computed outputs.

## Repository layout

```text
notebooks/  Two research notebooks
docs/       Original report, corrected results, audit and validation notes
data/       Instructions only; no licensed market-data files
tests/      Basic checks on recorded results
```

## Reproduction

1. Install dependencies: `python -m pip install -r requirements.txt`.
2. Obtain source data **from an authorized provider**. Place the files under `data/` with the names referenced in the notebooks. The files are intentionally excluded from this repository.
3. Open Jupyter from the repository root and run the notebook cells in order.
4. The regime-switching notebook requires `data/Market Risk.xlsx`, also not redistributed.
5. Run the lightweight integrity check with `python -m pytest -q`.

**Reproducibility status:** Notebook code has passed syntax parsing and selected simulation sections were executed previously with local inputs. Full end-to-end execution from a clean environment using independently authorized data has not been established. The basic pytest check validates the format/range of recorded values only; it does not validate financial mathematics.

## Material limitations

- The CDX calibration dataset available to the original study begins in 2011 and excludes the 2007–2009 global financial crisis.
- The revised simulator may count the same reference-name default more than once; default dependence and persistent survivor accounting are not fully modelled.
- Spread mark-to-market and realized credit-default losses may be treated inconsistently or double-counted.
- CIR diffusion and empirical-jump calibration may overlap in their treatment of large spread moves.
- Interest-rate, coupon, settlement and stress-shock mechanics are simplified.
- The alternative regime-switching model is experimental and uses different event definitions; its outputs are not directly comparable.
- No external credit rating, validated probability of default or investment conclusion is established.

See [corrected results](docs/CORRECTED_RESULTS.md) and [corrections and validation](docs/CORRECTIONS_AND_VALIDATION.md) for details.

## Collaboration and attribution

This was a **university group project**. It is presented as collaborative work, not as an individual project. Individual contributor names and precise task allocations have not been confirmed for this public version. Group materials are included only on the basis of the user's confirmation that sharing permission was obtained.

No raw CSV or Excel market datasets, presentation binaries or prior repository Git history are included. No open-source license is granted by this repository; reuse permissions should be agreed by the project contributors.

**Not investment advice.**
