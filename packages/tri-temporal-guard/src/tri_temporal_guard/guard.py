import json, time, hashlib
from .models import Manifest

def compute_shear(t_plan: float, t_exec: float, t_story: float) -> float:
    vals = [max(1e-6, t_plan), max(1e-6, t_exec), max(1e-6, t_story)]
    ratio = max(vals)/min(vals)
    shear = ratio - 1.0
    return max(0.0, min(1.0, shear))

def decide_step(m: Manifest):
    shear = compute_shear(m.t_plan, m.t_exec, m.t_story)
    action = "allow"
    reason = []
    if shear > m.policy.shear_max:
        action = "quarantine"
        reason.append("shear_exceeds_max")
    elif shear > m.policy.shear_warn:
        action = "throttle"
        reason.append("shear_warn_exceeded")
    decision = {
        "action": action,
        "shear": shear,
        "thresholds": {"shear_warn": m.policy.shear_warn, "shear_max": m.policy.shear_max},
        "timestamp": time.time()
    }
    decision["signature"] = hashlib.sha256(json.dumps(decision, sort_keys=True).encode()).hexdigest()
    return decision
