from tri_temporal_guard.guard import compute_shear
def test_shear_zero_when_equal():
    assert abs(compute_shear(1.0,1.0,1.0)) < 1e-9
