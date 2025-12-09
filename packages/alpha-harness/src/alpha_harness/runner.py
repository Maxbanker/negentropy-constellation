import json, random, time, os
from typing import List, Dict, Any
from .models import Manifest
from .metrics import compute_window_metrics
from .utils import stable_hash

def _veil(sigma: float, eps_adv: float) -> float:
    return (1.0/(1.0+max(0.0, sigma))) * (1.0 - max(0.0, min(1.0, eps_adv)))

def simulate_series(steps: int, drift_at: int = 7) -> List[float]:
    s = []
    val = 0.0
    for t in range(steps):
        val += 0.1 + (0.0 if t < drift_at else 0.5)  # drift step
        s.append(val + random.gauss(0, 0.01))
    return s

def run_manifest(m: Manifest) -> Dict[str, Any]:
    random.seed(m.seed)
    series = simulate_series(m.steps)
    sigma = 0.3
    eps = 0.05
    budget = float(m.routes.get("export_budget", 0.0))
    ethics_min = float(m.gates.get("ethics_min", 0.6))
    veil_min = float(m.gates.get("veil_min", 0.65))
    ethics = 0.55  # demo

    telemetry = []
    run_id = stable_hash({"seed": m.seed, "scenario": m.scenario, "time": int(time.time())})
    window = []
    for t, v in enumerate(series):
        window.append(v)
        psi, gamma, omega = compute_window_metrics(window[-16:])
        veil = _veil(sigma, eps)

        allow = True
        reasons = []
        if ethics < ethics_min:
            allow = False
            reasons.append("ethics_below_threshold")
        if veil < veil_min:
            allow = False
            reasons.append("veil_below_threshold")
        if budget < 0.0:
            allow = False
            reasons.append("budget_negative")

        rec = {
            "run_id": run_id, "seed": m.seed, "t": t,
            "psi": psi, "gamma": gamma, "omega": omega,
            "veil": veil, "budget": budget, "ethics": ethics,
            "decision": "allow" if allow else "block", "reason": reasons
        }
        rec["hash"] = stable_hash(rec)
        telemetry.append(rec)
    return {"manifest": m.model_dump(), "telemetry": telemetry}

def replay(path: str, check: bool = True) -> bool:
    data = json.load(open(path, "r", encoding="utf-8"))
    # In a real system, recompute hashes; here we just verify hash field presence
    ok = all("hash" in r for r in data.get("telemetry", []))
    return ok
