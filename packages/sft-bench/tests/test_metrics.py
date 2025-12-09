from sft_bench.metrics import compute_metrics
def test_prf_keys():
    m = compute_metrics([1,0,1],[1,0,0])
    assert set(m.keys()) == {"precision","recall","f1"}
