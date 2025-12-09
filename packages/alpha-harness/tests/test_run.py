import json, yaml, os, tempfile
    from alpha_harness.models import Manifest
    from alpha_harness.runner import run_manifest

    def test_run_manifest_outputs_records():
        m = Manifest(**yaml.safe_load("""
seed: 1
scenario: drift
steps: 5
gates: {ethics_min: 0.6, veil_min: 0.65}
routes: {export_budget: 0.1}
"""))
        out = run_manifest(m)
        assert "telemetry" in out
        assert len(out["telemetry"]) == 5
