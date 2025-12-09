import numpy as np

def shannon_entropy(x, bins=32):
    if x.size == 0:
        return 0.0
    hist, _ = np.histogram(x, bins=bins, density=True)
    hist = hist[hist > 0]
    return -np.sum(hist * np.log(hist + 1e-12))

def compute_window_metrics(series):
    x = np.asarray(series, dtype=float)
    psi = 1.0 / (1.0 + shannon_entropy(x))
    if len(x) < 2:
        gamma = 0.0
        omega = 0.0
    else:
        dx = np.abs(np.diff(x))
        gamma = float(np.mean(dx))
        x0 = x - x.mean()
        omega = float(np.dot(x0[:-1], x0[1:]) / (np.dot(x0, x0) + 1e-12))
    psi = float(max(0.0, min(1.0, psi)))
    omega = float(max(-1.0, min(1.0, omega)))
    return psi, gamma, omega
