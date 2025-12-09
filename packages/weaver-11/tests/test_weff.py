from weaver_11.weaver import compute_weff, repair_dialogue

def test_repair_increases_weff():
    text = "A topic about A. Now something unrelated X. Back to A detail."
    rep = repair_dialogue(text, threshold=0.2)
    assert rep["weff_after"] >= rep["weff_before"]
