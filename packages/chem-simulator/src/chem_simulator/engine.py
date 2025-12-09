import json, os, csv, hashlib, random
from typing import Dict, Any, List
import numpy as np
from .models import Manifest
from .metrics import compute_metrics
from .predicate import collapse_flag

def _landscape_energy(state, base=1.0):
    # Toy energy: quadratic with noise
    return base*(state**2)

def _apply_pulse(state: float, kind: str, magnitude: float) -> float:
    # Affect state differently per pulse kind
    if kind == "temp":
        return state + 0.3*magnitude
    if kind == "solvent":
        return state + 0.15*magnitude
    if kind == "light":
        return state + 0.2*magnitude
    return state

def run(manifest: Manifest, outdir: str) -> Dict[str, Any]:
    random.seed(manifest.seed)
    np.random.seed(manifest.seed)

    os.makedirs(outdir, exist_ok=True)
    series = []
    state = 0.0
    pulses_by_t = {p.t: p for p in manifest.pulses}

    # simulate
    for t in range(manifest.steps):
        # baseline drift
        state += 0.05 + np.random.normal(0, 0.01)
        # pulse?
        if t in pulses_by_t:
            p = pulses_by_t[t]
            state = _apply_pulse(state, p.kind, p.magnitude)
        # record toy observable (e.g., energy)
        series.append(_landscape_energy(state))

    prev = None
    alerts = 0
    telemetry_rows = []
    window = manifest.config.window
    for t in range(len(series)):
        w = series[max(0, t-window+1):t+1]
        psi, gamma, omega = compute_metrics(w, prev)
        pred = collapse_flag(psi, gamma, omega, manifest.config)
        alerts += int(pred)
        prev = w
        telemetry_rows.append([t, f"{psi:.6f}", f"{gamma:.6f}", f"{omega:.6f}", pulses_by_t.get(t).kind if t in pulses_by_t else "", int(pred)])

    # write CSV
    csv_path = os.path.join(outdir, "telemetry.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["t","psi","gamma","omega","pulse","predicate"])
        w.writerows(telemetry_rows)

    summary = {
        "seed": manifest.seed,
        "name": manifest.name,
        "steps": manifest.steps,
        "psi_min": manifest.config.psi_min,
        "gamma_max": manifest.config.gamma_max,
        "omega_min": manifest.config.omega_min,
        "alerts": alerts,
    }
    # manifest hash
    summary["manifest_hash"] = hashlib.sha256(json.dumps(manifest.model_dump(), sort_keys=True).encode()).hexdigest()

    with open(os.path.join(outdir, "summary.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, sort_keys=True)

    return {"csv": csv_path, "summary": summary}
