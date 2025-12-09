import numpy as np
from observer_continuity.o_score import psd_sketch, o_score

def test_o_score_range():
    a = np.ones(128)
    b = np.ones(128) * 1.01
    s = o_score(a, b)
    assert 0.0 <= s <= 1.0
