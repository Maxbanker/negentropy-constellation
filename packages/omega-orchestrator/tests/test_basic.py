import yaml, json
    from omega_orchestrator.models import Manifest
    from omega_orchestrator.engine import Orchestrator

    def test_blocked_by_ethics():
        manifest = Manifest(**yaml.safe_load("""
seed: 1
intent: test
context: {ethics_energy: 0.4}
resources: {}
policy:
  thresholds: {ethics_min: 0.6, veil_min: 0.0, budget_min: 0.0, tri_temporal_max_shear: 1.0}
  budgets: {export_budget: 0.1}
  uncertainty: {sigma: 0.0}
  adversary_index: 0.0
"""))
        d = Orchestrator().decide(manifest)
        assert d.allow is False
        assert any('ethics_below_threshold' in r for r in d.reasons)
