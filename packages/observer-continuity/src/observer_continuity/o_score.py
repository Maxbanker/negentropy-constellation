import json, numpy as np
from typing import Dict

def psd_sketch(x: np.ndarray, k: int = 64) -> np.ndarray:
    x = np.asarray(x, dtype=float).ravel()
    if x.size == 0:
        return np.zeros(k)
    x = (x - x.mean()) / (x.std() + 1e-12)
    # FFT magnitude as PSD proxy
    spec = np.abs(np.fft.rfft(x))
    # downsample to fixed length k
    if spec.size < k:
        pad = np.zeros(k - spec.size)
        sketch = np.concatenate([spec, pad])
    else:
        idx = np.linspace(0, spec.size-1, num=k).astype(int)
        sketch = spec[idx]
    # normalize
    norm = np.linalg.norm(sketch) + 1e-12
    return sketch / norm

def o_score(before: np.ndarray, after: np.ndarray, k: int = 64) -> float:
    a = psd_sketch(before, k=k)
    b = psd_sketch(after, k=k)
    # cosine similarity (∈ [0,1])
    return float(np.dot(a, b) / ((np.linalg.norm(a)*np.linalg.norm(b))+1e-12))

def audit(before_path: str, after_path: str, threshold: float = 0.92) -> Dict:
    before = np.load(before_path)
    after = np.load(after_path)
    score = o_score(before, after)
    ok = bool(score >= threshold)
    return {
        "before_path": before_path, "after_path": after_path,
        "o_score": score, "threshold": threshold, "pass": ok
    }
