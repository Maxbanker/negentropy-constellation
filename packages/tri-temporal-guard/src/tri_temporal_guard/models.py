from pydantic import BaseModel

class Policy(BaseModel):
  shear_warn: float = 0.25
  shear_max: float = 0.5

class Manifest(BaseModel):
  t_plan: float
  t_exec: float
  t_story: float
  policy: Policy = Policy()
