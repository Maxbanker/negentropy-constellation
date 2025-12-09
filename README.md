<!-- Status Badges -->
[![Monorepo Demo CI](https://github.com/Maxbanker/negentropy-constellation/actions/workflows/ci-demo.yml/badge.svg?branch=main)](https://github.com/Maxbanker/negentropy-constellation/actions/workflows/ci-demo.yml)

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

## Support Matrix: Simulations ↔ Frameworks

| Package / Sim | Role in the stack | Framework claims it reinforces | How it supports (testable assertions) | Outputs / Metrics | Real-world payoff |
|---|---|---|---|---|---|
| **alpha-harness** | Deterministic experiment runner | **Alpha v5.0**, **ERF** | Manifests → identical runs (seeded); telemetry hashes stay stable across replays. | Telemetry JSON (`run_id`, ψ/γ/ω, hashes) | Reproducibility proof; audit/paper baselines. |
| **sft-detector** | Collapse early-warning | **SFT v5.6**, **ERF v4.4** | Predicate fires when ψ↓ or (γ↑ & ω↓); lead-time measurable. | Alerts CSV; ψ/γ/ω streams; lead-time | “Tripwire” for drift/collapse. |
| **chem-simulator** | Entropy-pulse sandbox | **Symbolic Gravity v3.5**, **SFT v5.6** | Pulses (temp/solvent/light) change curvature; ψ/γ/ω respond predictably. | Telemetry CSV; summary JSON | Safe lab proxy for gate tuning. |
| **weaver-11** | Narrative coherence repair | **FCWF v3.1**, **OFT-11** | Tear detection via cosine drop; bridges raise W_eff. | Patched text; uplift; tear indices | Reduces long-form drift. |
| **observer-continuity (oc)** | Identity integrity check | **OISF v4.0**, **I-Point v3.0** | PSD-cosine continuity ≥ threshold across handoffs. | JSON (O-score, pass/fail) | Safer model swaps/migrations. |
| **ethics-gate** | Quantified ethics gating | **BC-REP v3.5** | \(E_{safe} = E·(1/(1+σ))·(1−ε_{adv}) ≥ E_c\) ⇒ permit; signed rationale. | Decision JSON (metrics, signature) | Evidence-backed allow/deny. |
| **tri-temporal-guard** | Time-axis sanity check | **Hyperverse v9.1**, **ERF** | Shear = max/min − 1; warn/max ⇒ throttle/quarantine. | Guard JSON (shear, action, signature) | Prevents desync failures. |
| **xsft-corridor** | Leak-aware export receipts | **X-Space FT v3.0**, **OISF**, **ERF** | Allow iff L<L_c ∧ B_export≥0 ∧ O_score≥O_c; signed receipt. | Receipt JSON (O, L, B, decision) | Provable safe exports. |
| **omega-orchestrator** | Action governance runtime | **ERF**, **Symbolic Gravity**, **BC-REP** | Aggregates veil, ethics, budgets, shear → allow/block/throttle/quarantine with audit hash. | Audit JSON (decisions, reasons, hashes) | Explainable control plane. |
| **sft-bench** | Standardized evaluation | **SFT v5.6**, **ERF** | Reproducible P/R/F1 and mean lead-time on datasets. | Results JSON | Comparable progress tracking. |

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
