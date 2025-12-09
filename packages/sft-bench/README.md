# SFT Bench & Leaderboard (local)

Author: **Steven Lanier** · Credit: **SEAL Division**

A lightweight, local benchmark for **collapse prediction**. It ships with small toy datasets and metrics: **precision, recall, F1, and mean lead-time**.

## Model protocol
A model is any Python module exposing: `predict(window: list[float]) -> int` returning 1 if collapse predicted else 0.
You can also use the built-in `threshold` model via CLI flags.

## Quickstart
```bash
pip install .
sftbench eval --dataset examples/ts --model threshold --psi_min 0.35 --gamma_max 0.8 --omega_min 0.1 --window 16 --out out/results.json
cat out/results.json
```

## Dataset format
Folder with two NDJSON files:

- `series.ndjson` lines: `{{"step": int, "values": [..]}}`

- `labels.ndjson` lines: `{{"step": int, "collapse": 0|1}}`

## Metrics
- Precision/Recall/F1 over steps

- Mean lead-time (first alert time minus first collapse time per sequence, clipped at 0 if late)

## License
Apache-2.0
