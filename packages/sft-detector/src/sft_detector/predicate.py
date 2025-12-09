from typing import Dict

def collapse_flag(psi: float, gamma: float, omega: float, cfg: Dict[str, float]) -> bool:
    psi_min = float(cfg.get("psi_min", 0.3))
    gamma_max = float(cfg.get("gamma_max", 0.8))
    omega_min = float(cfg.get("omega_min", 0.2))
    return (psi < psi_min) or (gamma > gamma_max and omega < omega_min)
