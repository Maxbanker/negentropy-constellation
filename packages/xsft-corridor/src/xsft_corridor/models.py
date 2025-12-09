from pydantic import BaseModel
from typing import Optional

class Policy(BaseModel):
    L_c: float = 0.2
    O_c: float = 0.92

class Budgets(BaseModel):
    export_budget: float = 0.0

class StateRef(BaseModel):
    before: str
    after: str

class Manifest(BaseModel):
    route: str
    policy: Policy = Policy()
    budgets: Budgets = Budgets()
    state: StateRef
    telemetry: bool = True
