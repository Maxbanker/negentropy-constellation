import argparse, yaml, os, json
from .models import Manifest, Pulse, Config
from .engine import run

def main():
    p = argparse.ArgumentParser(prog="chemsim", description="Symbolic Chemistry Simulator CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("run")
    r.add_argument("manifest", help="reaction.yaml")
    r.add_argument("--out", required=True, help="output directory")

    args = p.parse_args()
    if args.cmd == "run":
        data = yaml.safe_load(open(args.manifest, "r", encoding="utf-8"))
        m = Manifest(**data)
        out = run(m, args.out)
        print(json.dumps(out["summary"], indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
