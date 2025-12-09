def collapse_flag(psi, gamma, omega, cfg):
    return (psi < cfg.psi_min) or (gamma > cfg.gamma_max and omega < cfg.omega_min)
