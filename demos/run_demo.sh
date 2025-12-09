#!/usr/bin/env bash
set -euo pipefail

mkdir -p out

echo "== Ethics Gate =="
ethics score packages/ethics-gate/examples/action.yml --out out/decision.json
cat out/decision.json || true

echo "== Temporal Guard =="
tguard step packages/tri-temporal-guard/examples/times.yml --out out/guard.json
cat out/guard.json || true

echo "== Omega Orchestrator =="
omega run packages/omega-orchestrator/examples/lab.yml --audit out/omega_audit.json
cat out/omega_audit.json || true

echo "== Chemistry Simulator =="
chemsim run packages/chem-simulator/examples/reaction.yaml --out out/chem
ls -l out/chem
head -n 5 out/chem/telemetry.csv || true

echo "== SFT Detector =="
sftdetect stream packages/sft-detector/examples/series.ndjson --config packages/sft-detector/examples/config.yml --out out/alerts.csv --labels packages/sft-detector/examples/labels.ndjson
head -n 5 out/alerts.csv || true

echo "== XSFT Corridor =="
xsft open packages/xsft-corridor/examples/corridor.yml --out out/receipt.json
cat out/receipt.json || true

echo "== SFT Bench ==""
sftbench eval --dataset packages/sft-bench/examples/ts --model threshold --psi_min 0.35 --gamma_max 0.8 --omega_min 0.1 --window 16 --out out/bench.json
cat out/bench.json || true

echo "Demo complete. Artifacts are in ./out"
