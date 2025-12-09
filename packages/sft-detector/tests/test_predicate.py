from sft_detector.predicate import collapse_flag

def test_or_predicate():
    cfg = {"psi_min": 0.5, "gamma_max": 1.0, "omega_min": 0.2}
    assert collapse_flag(psi=0.1, gamma=0.0, omega=1.0, cfg=cfg) is True  # psi low
    assert collapse_flag(psi=0.9, gamma=2.0, omega=0.0, cfg=cfg) is True  # gamma high & omega low
    assert collapse_flag(psi=0.9, gamma=0.1, omega=0.9, cfg=cfg) is False
