# Tri‑Temporal Guard

Author: **Steven Lanier** · Credit: **SEAL Division**

Library/CLI to detect **temporal shear** across three axes—**planning (t_plan)**, **execution (t_exec)**, and **narrative (t_story)**—and decide to **allow/throttle/quarantine** steps.

## Shear metric (proxy)
`shear = max(t_plan, t_exec, t_story) / max(1e-6, min(t_plan, t_exec, t_story)) - 1`
- If `shear > shear_max` → quarantine
- Else if `shear > shear_warn` → throttle
- Else → allow

## Quickstart
```bash
pip install .
tguard step examples/times.yml --out out/guard.json
cat out/guard.json
```

## License
Apache-2.0
