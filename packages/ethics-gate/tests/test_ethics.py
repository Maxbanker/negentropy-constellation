from ethics_gate.engine import score
def test_score_monotonicity():
    assert score(0.8, 0.0, 0.0) > score(0.8, 0.5, 0.0)
    assert score(0.8, 0.0, 0.1) > score(0.8, 0.0, 0.9)
