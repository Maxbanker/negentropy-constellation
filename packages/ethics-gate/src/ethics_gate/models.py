from pydantic import BaseModel
from typing import Dict

class Policy(BaseModel):
    E_c: float = 0.6

class Manifest(BaseModel):
    action: str
    context: Dict[str, float]  # E, sigma, eps_adv
    policy: Policy
