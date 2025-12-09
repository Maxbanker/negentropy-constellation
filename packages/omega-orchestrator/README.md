# OmegaLab Orchestrator

Author: **Steven Lanier** · Credit: **SEAL Division**

A safety-first agent/action controller that enforces **leak-first**, **conservation budgets**, **ethics thresholds**, and **tri-temporal guards** *before* any potentially risky action is executed.

## Features
- Deterministic, manifest-driven decisions
- Signed audit ledgers (JSON) explaining *why* an action was blocked/allowed
- Plug-in policies via YAML
- CLI and Python API

## Quickstart
```bash
pip install .
omega run examples/lab.yml --audit out/audit.json
```

## Manifest (example)
```yaml
# examples/lab.yml
seed: 42
intent: "start_reaction"
context:
  risk: 0.23
  uncertainty: 0.31
  ethics_energy: 0.55
resources:
  chem: true
policy:
  thresholds:
    budget_min: 0.0
    veil_min: 0.65
    ethics_min: 0.60
    tri_temporal_max_shear: 0.35
  budgets:
    export_budget: 0.1
  uncertainty:
    sigma: 0.31
  adversary_index: 0.05
```

## Decision
```bash
omega run examples/lab.yml --audit out/audit.json
cat out/audit.json
```

## License
Apache-2.0
