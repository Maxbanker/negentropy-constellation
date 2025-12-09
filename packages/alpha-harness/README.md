# Alpha v5 Harness SDK

Author: **Steven Lanier** · Credit: **SEAL Division**

An opinionated, deterministic harness for experiments: **state → gates → routes → telemetry**.

Provides manifest-driven replays and signed telemetry bundles.

## Quickstart
```bash
pip install .
alpha run examples/drift.yml --out out/telemetry.json
alpha replay out/telemetry.json --check
```

## Manifest (example)
```yaml
seed: 123
scenario: drift
steps: 12
gates:
  ethics_min: 0.6
  veil_min: 0.65
routes:
  export_budget: 0.1
```

## Telemetry schema
Each step emits: `run_id, seed, t, psi, gamma, omega, veil, budget, ethics, decision, reason, hash`.

## License
Apache-2.0
