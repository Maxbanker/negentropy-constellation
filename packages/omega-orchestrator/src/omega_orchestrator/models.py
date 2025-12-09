from typing import Optional, Dict, Any
from pydantic import BaseModel

class Policy(BaseModel):
    thresholds: Dict[str, float]
    budgets: Dict[str, float] = {}
    uncertainty: Dict[str, float] = {}
    adversary_index: float = 0.0

class Manifest(BaseModel):
    seed: int = 0
    intent: str
    context: Dict[str, float] = {}
    resources: Dict[str, Any] = {}
    policy: Policy
    outputs: Optional[Dict[str, str]] = None
