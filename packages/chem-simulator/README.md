# Symbolic Chemistry Simulator

Author: **Steven Lanier** · Credit: **SEAL Division**

Simulate entropy pulses (solvent, temperature, light) over a toy reaction energy landscape. Compute **ψ/γ/ω**, trigger an SFT-style collapse predicate, and export **CSV + JSON** telemetry bundles.

## Quickstart
```bash
pip install .
chemsim run examples/reaction.yaml --out out
cat out/telemetry.csv
```

## Predicate
Collapse if: `psi < psi_min` OR (`gamma > gamma_max` AND `omega < omega_min`).

## Artifacts
- `telemetry.csv`: t, psi, gamma, omega, pulse, predicate
- `summary.json`: counts, thresholds, seed, manifest hash

## License
Apache-2.0
