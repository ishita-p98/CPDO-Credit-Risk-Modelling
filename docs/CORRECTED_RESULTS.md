# Corrected-model results — exploratory only

**Status: not independently financially validated.** The values below were recorded in an earlier local review of the revised CIR + empirical-jump prototype using 2,000 simulated paths per scenario and random seed 123. The source datasets are not included in this public repository. These values are historical recorded outputs, not a fresh run performed from this clean public repository.

| Scenario | NAV-floor event | Cash-out event | Mean final NAV |
| --- | ---: | ---: | ---: |
| Base case | 1.10% | 0.00% | 43.24 |
| Permanent +150 bp spread-level shift at year 3 | 99.80% | 0.00% | 10.03 |
| Initial spread 200 bp | 0.00% | 10.45% | 81.71 |

A NAV-floor event is a model-defined trigger, not a legal issuer default or external rating classification. A 0% observed rate in 2,000 paths does not establish a zero underlying probability.

## Validation evidence and limits

Earlier local checks included syntax parsing, selected model-cell execution, chart generation and a test of recorded-result structure. They do not prove that the entire notebooks run from a fresh environment, nor do they validate the model's financial assumptions. The alternative regime-switching model had only a limited smoke test.

## Material model risks

1. **Repeated defaults:** the revised CIR simulator can sample default events for names that may already have defaulted.
2. **Dependence:** independent name-level default sampling does not model systemic default correlation.
3. **Spread/default accounting:** spread mark-to-market and realized default losses may be combined inconsistently or double-counted.
4. **Diffusion and jumps:** CIR volatility was estimated from observations that include large moves, then an empirical jump component was added; tail variation may be double-counted.
5. **Product mechanics:** interest rates, coupon timing, roll costs, settlement and NAV triggers are simplified.
6. **Stress construction:** the permanent +150 bp shock is a hypothetical scenario, not a calibrated reconstruction of the 2007–2009 crisis.
7. **Historical coverage:** the CDX sample supplied to the original study starts in 2011, excluding the global financial crisis.
8. **Ratings:** these simulations do not establish any AAA/B rating or reproduce an external rating methodology.

The prototype is suitable as a methodological research exercise with limitations stated prominently, not as a validated credit-risk, pricing or trading model.
