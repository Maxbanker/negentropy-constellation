# XSFT Export Corridor

Author: **Steven Lanier** · Credit: **SEAL Division**

Open an audited corridor for state transfer with **leak (L)**, **export budget (B_export)**, and **invariance (O-score)** checks. Emits a **signed receipt**.

## Gate conditions (proxy)
- Allow iff: `L < L_c` **and** `B_export ≥ 0` **and** `O_score ≥ O_c`

## Quickstart
```bash
pip install .
xsft open examples/corridor.yml --out out/receipt.json
cat out/receipt.json
```

## Manifest
```yaml
route: "lab→analysis"
policy: {{ L_c: 0.2, O_c: 0.92 }}
budgets: {{ export_budget: 0.1 }}
state:
  before: "examples/before.npy"
  after:  "examples/after.npy"
telemetry: true
```

## License
Apache-2.0
