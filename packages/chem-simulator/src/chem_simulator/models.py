from typing import List, Dict, Any
from pydantic import BaseModel

class Pulse(BaseModel):
    t: int
    kind: str  # 'solvent' | 'temp' | 'light'
    magnitude: float  # 0..1

class Config(BaseModel):
    psi_min: float = 0.35
    gamma_max: float = 0.8
    omega_min: float = 0.1
    window: int = 16

class Manifest(BaseModel):
    seed: int = 0
    name: str = "demo"
    steps: int = 48
    pulses: List[Pulse] = []
    config: Config = Config()
