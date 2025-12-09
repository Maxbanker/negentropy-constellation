# BC‑REP Ethics Gate

Author: **Steven Lanier** · Credit: **SEAL Division**

A standalone service/CLI that computes an ethics score for a proposed action, combining **ethics energy (E)**, **uncertainty (σ)**, and **adversary index (ε_adv)** into a gated decision with signed rationale.

## Scoring (pragmatic proxy)
`E_safe = E * (1/(1+σ)) * (1 - ε_adv)` → **permit** iff `E_safe ≥ E_c`

## Quickstart
```bash
pip install .
ethics score examples/action.yml --out out/decision.json
cat out/decision.json
```

## Manifest fields
```yaml
action: "publish_lab_results"
context: {{ E: 0.72, sigma: 0.31, eps_adv: 0.05 }}
policy:  {{ E_c: 0.60 }}
```

## License
Apache-2.0
