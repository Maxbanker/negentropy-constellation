import json, time, hashlib
from .models import Manifest

def score(E: float, sigma: float, eps_adv: float) -> float:
    # E_safe = E * (1/(1+sigma)) * (1 - eps_adv)
    return float(E * (1.0/(1.0+max(0.0, sigma))) * (1.0 - max(0.0, min(1.0, eps_adv))))

def decide(m: Manifest):
    E   = float(m.context.get("E", 1.0))
    sig = float(m.context.get("sigma", 0.0))
    adv = float(m.context.get("eps_adv", 0.0))
    E_safe = score(E, sig, adv)
    allow = bool(E_safe >= m.policy.E_c)
    decision = {
        "allow": allow,
        "metrics": {"E": E, "sigma": sig, "eps_adv": adv, "E_safe": E_safe},
        "thresholds": {"E_c": m.policy.E_c},
        "action": m.action,
        "timestamp": time.time()
    }
    decision["signature"] = hashlib.sha256(json.dumps(decision, sort_keys=True).encode()).hexdigest()
    return decision
