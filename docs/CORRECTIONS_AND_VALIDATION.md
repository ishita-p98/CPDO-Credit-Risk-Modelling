# Corrections and validation notes

## Changes in the revised research draft

- Replaced the original CIR default-intensity expression `spread / (10,000 × LGD × risky_duration)` with the flat-hazard approximation `spread / (10,000 × LGD)`. This changes the assumptions and materially affects downstream outputs.
- Removed an apparent second multiplication by the monthly time step in the experimental regime-model cash-interest calculation.
- Added a simplified independent-name binomial default-loss approximation to the regime-model prototype. It does not track persistent survivors or correlated defaults.
- Clarified that the +150 bp year-3 CIR stress is a permanent additive spread-level shift.

## Re-execution previously recorded

| Metric | Earlier implementation | Revised prototype |
|---|---:|---:|
| CIR base NAV-floor event (10,000 paths) | 0.00% | 0.85% |
| CIR base cash-out | 34.99% | 0.05% |
| CIR base mean final NAV | 119.25 | 43.562 |
| CIR permanent +150 bp year-3 stress NAV-floor event | 40.57% | 99.75% |
| CIR stress cash-out | 3.73% | 0.00% |
| CIR stress mean final NAV | 44.516 | 10.025 |

A subsequent 2,000-path run recorded 1.10% base NAV-floor events and 99.80% in the stress case. The earlier regime model smoke test used only 300 paths and is not adequate for tail-probability estimation.

## What remains unvalidated

- Flat CDS hazard approximations are not a substitute for a calibrated credit portfolio default model.
- Default events do not persistently remove names from the reference basket; independent sampling also omits correlated defaults.
- Spread mark-to-market and realized default loss accounting need an internally consistent credit-index P&L treatment.
- Diffusion and jump calibration may overlap in tail risk.
- The regime model uses different default definitions and coupon assumptions; its results are not directly comparable to the CIR notebook.
- Full end-to-end notebook execution, sensitivity sweeps, optimization and all figure regeneration have not been independently reproduced from a clean environment with non-redistributed source data.
- No simulated rating should be presented as a rating opinion.

These are research-stage corrections, not a claim that the financial model is now correct.
