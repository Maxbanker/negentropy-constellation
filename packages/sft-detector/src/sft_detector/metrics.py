import numpy as np

def shannon_entropy(x, bins=32):
    if x.size == 0:
        return 0.0
    hist, _ = np.histogram(x, bins=bins, density=True)
    hist = hist[hist > 0]
    return -np.sum(hist * np.log(hist + 1e-12))

def compute_metrics(window, prev_window=None):
    window = np.asarray(window, dtype=float)
    psi = 1.0 / (1.0 + shannon_entropy(window))  # inverse-entropy proxy (0..1-ish)
    if prev_window is None or len(prev_window) == 0:
        gamma = 0.0
    else:
        prev = np.asarray(prev_window, dtype=float)
        L = min(len(window), len(prev))
        gamma = float(np.mean(np.abs(window[:L] - prev[:L])))
    # omega: lag-1 autocorr proxy
    if len(window) < 2:
        omega = 0.0
    else:
        x = window - window.mean()
        num = np.dot(x[:-1], x[1:])
        den = np.dot(x, x) + 1e-12
        omega = float(num / den)
    # clamp
    psi = float(max(0.0, min(1.0, psi)))
    omega = float(max(-1.0, min(1.0, omega)))
    return psi, gamma, omega
