from .features import compute_metrics

class ThresholdModel:
    def __init__(self, psi_min=0.35, gamma_max=0.8, omega_min=0.1, window=16):
        self.psi_min = psi_min
        self.gamma_max = gamma_max
        self.omega_min = omega_min
        self.window = window
        self._prev = None

    def predict(self, values):
        vals = values[-self.window:]
        psi, gamma, omega = compute_metrics(vals, self._prev)
        self._prev = vals
        return int((psi < self.psi_min) or (gamma > self.gamma_max and omega < self.omega_min))
