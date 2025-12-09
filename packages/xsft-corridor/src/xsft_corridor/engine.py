import json, time, hashlib
import numpy as np
from .models import Manifest

def cosine(a, b):
    na = np.linalg.norm(a); nb = np.linalg.norm(b)
    if na == 0 or nb == 0:
        return 0.0
    return float(np.dot(a, b) / (na*nb + 1e-12))

def o_score(before, after):
    # Normalize, PSD-like magnitude via rfft
    a = np.abs(np.fft.rfft((before - before.mean()) / (before.std()+1e-12)))
    b = np.abs(np.fft.rfft((after  - after.mean())  / (after.std()+1e-12)))
    return cosine(a, b)

def leak_estimate(before, after):
    # Proxy: relative L2 difference saturated to [0,1]
    diff = np.linalg.norm(before - after) / (np.linalg.norm(before) + 1e-12)
    return float(max(0.0, min(1.0, diff)))

def open_corridor(m: Manifest):
    before = np.load(m.state.before).astype(float).ravel()
    after  = np.load(m.state.after ).astype(float).ravel()

    O = o_score(before, after)
    L = leak_estimate(before, after)
    B = float(m.budgets.export_budget)

    allow = (L < m.policy.L_c) and (B >= 0.0) and (O >= m.policy.O_c)
    receipt = {
        "route": m.route,
        "allow": bool(allow),
        "metrics": {"O_score": O, "L": L, "B_export": B},
        "thresholds": {"O_c": m.policy.O_c, "L_c": m.policy.L_c},
        "timestamp": time.time()
    }
    receipt["signature"] = hashlib.sha256(json.dumps(receipt, sort_keys=True).encode()).hexdigest()
    return receipt
