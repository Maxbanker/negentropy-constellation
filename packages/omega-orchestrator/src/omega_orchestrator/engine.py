import json, hashlib, random, time
from dataclasses import dataclass, asdict
from typing import Dict, Any
from .models import Manifest, Policy

@dataclass
class Decision:
    allow: bool
    reasons: list
    metrics: Dict[str, float]
    manifest_hash: str
    timestamp: float

    def to_json(self):
        return json.dumps(asdict(self), indent=2, sort_keys=True)

class Orchestrator:
    def __init__(self):
        pass

    @staticmethod
    def _veil(sigma: float, eps_adv: float) -> float:
        # Veil = 1/(1+sigma) * (1 - adversary_index)
        return (1.0/(1.0+max(0.0, sigma))) * (1.0 - max(0.0, min(1.0, eps_adv)))

    @staticmethod
    def _tri_temporal_shear(t_plan: float, t_exec: float, t_story: float) -> float:
        # Simple shear proxy = max pairwise ratio - 1, clamped [0, 1.0]
        vals = [max(1e-6, t_plan), max(1e-6, t_exec), max(1e-6, t_story)]
        ratios = [max(vals)/min(vals)]
        shear = ratios[0] - 1.0
        return max(0.0, min(1.0, shear))

    def decide(self, manifest: Manifest) -> Decision:
        # Deterministic seed
        random.seed(manifest.seed)

        thr = manifest.policy.thresholds
        sigma = manifest.policy.uncertainty.get("sigma", 0.0)
        eps_adv = manifest.policy.adversary_index
        budget = manifest.policy.budgets.get("export_budget", 0.0)
        ethics_energy = manifest.context.get("ethics_energy", 1.0)

        # Temporal axes (if provided), else default to ~1
        t_plan = manifest.context.get("t_plan", 1.0)
        t_exec = manifest.context.get("t_exec", 1.0)
        t_story = manifest.context.get("t_story", 1.0)

        veil = self._veil(sigma, eps_adv)
        shear = self._tri_temporal_shear(t_plan, t_exec, t_story)

        allow = True
        reasons = []

        if budget < thr.get("budget_min", 0.0):
            allow = False
            reasons.append("budget_negative")

        if veil < thr.get("veil_min", 0.0):
            allow = False
            reasons.append("veil_below_threshold")

        if ethics_energy < thr.get("ethics_min", 0.0):
            allow = False
            reasons.append("ethics_below_threshold")

        if shear > thr.get("tri_temporal_max_shear", 1.0):
            allow = False
            reasons.append("tri_temporal_shear_exceeded")

        manifest_hash = hashlib.sha256(json.dumps(manifest.model_dump(), sort_keys=True).encode()).hexdigest()
        metrics = {
            "veil": veil,
            "export_budget": budget,
            "ethics_energy": ethics_energy,
            "tri_temporal_shear": shear
        }
        return Decision(allow=allow, reasons=reasons, metrics=metrics, manifest_hash=manifest_hash, timestamp=time.time())
