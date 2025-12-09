import yaml, os, json, tempfile
    from chem_simulator.models import Manifest
    from chem_simulator.engine import run

    def test_run_outputs_csv_and_summary():
        m = Manifest(**yaml.safe_load("""
seed: 1
name: t
steps: 12
pulses: []
config: {psi_min: 0.35, gamma_max: 0.8, omega_min: 0.1, window: 8}
"""))
        with tempfile.TemporaryDirectory() as td:
            out = run(m, td)
            assert os.path.exists(out["csv"])
            assert "alerts" in out["summary"]
