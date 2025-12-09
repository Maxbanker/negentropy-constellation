import argparse, json, os
from .engine import Orchestrator
from .models import Manifest
import yaml

def main():
    parser = argparse.ArgumentParser(prog="omega", description="OmegaLab Orchestrator CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    run_p = sub.add_parser("run", help="Run a decision using a YAML manifest")
    run_p.add_argument("manifest", help="Path to YAML manifest")
    run_p.add_argument("--audit", help="Path to write audit JSON", default=None)

    args = parser.parse_args()
    if args.cmd == "run":
        with open(args.manifest, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        manifest = Manifest(**data)
        orch = Orchestrator()
        decision = orch.decide(manifest)
        if args.audit:
            os.makedirs(os.path.dirname(args.audit), exist_ok=True)
            with open(args.audit, "w", encoding="utf-8") as out:
                out.write(decision.to_json())
        print(decision.to_json())

if __name__ == "__main__":
    main()
