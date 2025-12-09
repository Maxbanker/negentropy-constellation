import numpy as np
from xsft_corridor.engine import o_score, leak_estimate

def test_o_score_range():
    a = np.ones(128); b = a*1.01
    s = o_score(a, b)
    assert 0.0 <= s <= 1.0

def test_leak_nonnegative():
    a = np.ones(128); b = a*1.01
    L = leak_estimate(a, b)
    assert L >= 0.0
