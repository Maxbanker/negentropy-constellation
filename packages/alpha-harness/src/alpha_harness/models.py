from typing import Dict, Any
from pydantic import BaseModel

class Manifest(BaseModel):
    seed: int = 0
    scenario: str = "drift"
    steps: int = 10
    gates: Dict[str, float] = {}
    routes: Dict[str, float] = {}
