# SFT-Collapse Detector

Author: **Steven Lanier** · Credit: **SEAL Division**

A small, fast library/CLI that computes **ψ (psi), γ (gamma), ω (omega)** from time-series windows and applies an **SFT collapse OR-predicate** for early warning.

## ψ/γ/ω (pragmatic proxies)
- ψ: normalized inverse-entropy (higher = more coherent)

- γ: drift magnitude (change between adjacent windows)

- ω: autocorrelation/coherence proxy (lag-1)

## Predicate (configurable)
Collapse if: `psi < psi_min` **OR** (`gamma > gamma_max` **AND** `omega < omega_min`).

## Quickstart
```bash
pip install .
sftdetect stream examples/series.ndjson --config examples/config.yml --out out/alerts.csv
```

## Outputs
- `alerts.csv` with step, psi, gamma, omega, predicate, and lead_time (if labels supplied)

## License
Apache-2.0
