<!-- Status Badges -->
[![Monorepo Demo CI](https://github.com/<OWNER>/<REPO>/actions/workflows/ci-demo.yml/badge.svg?branch=main)](https://github.com/<OWNER>/<REPO>/actions/workflows/ci-demo.yml)

# Negentropy Constellation — Monorepo

Author: **Steven Lanier** · Credit: **SEAL Division**

A unified workspace bundling ten packages:

1. omega-orchestrator
2. sft-detector
3. alpha-harness
4. observer-continuity
5. chem-simulator
6. weaver-11
7. ethics-gate
8. tri-temporal-guard
9. xsft-corridor
10. sft-bench

## Shared Telemetry Schema
See `tooling/schema/telemetry.schema.json`.

## End-to-End Demo
Run `demos/run_demo.sh` to:
- Score an action with `ethics`
- Evaluate temporal shear with `tguard`
- Decide with `omega`
- Simulate a chemistry run with `chemsim`
- Detect collapse with `sftdetect`
- Open a corridor with `xsft`
- Evaluate a baseline with `sftbench`

## Docker-Compose
`docker-compose.yml` builds images for each package and runs a demo job.

## Local Dev
```bash
# From monorepo root
python -m venv .venv && source .venv/bin/activate
pip install -e packages/omega-orchestrator -e packages/sft-detector -e packages/alpha-harness -e packages/observer-continuity -e packages/chem-simulator -e packages/weaver-11 -e packages/ethics-gate -e packages/tri-temporal-guard -e packages/xsft-corridor -e packages/sft-bench

# Run the demo
bash demos/run_demo.sh
```
