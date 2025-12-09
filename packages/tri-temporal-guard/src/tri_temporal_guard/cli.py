import argparse, yaml, json, os
from .models import Manifest
from .guard import decide_step

def main():
    p = argparse.ArgumentParser(prog="tguard", description="Tri‑Temporal Guard CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("step", help="Evaluate one step timing tuple")
    s.add_argument("manifest")
    s.add_argument("--out", required=True)

    args = p.parse_args()
    if args.cmd == "step":
        m = Manifest(**yaml.safe_load(open(args.manifest, "r", encoding="utf-8")))
        d = decide_step(m)
        os.makedirs(os.path.dirname(args.out), exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as f:
            json.dump(d, f, indent=2, sort_keys=True)
        print(f"Wrote {args.out} ({d['action']})")

if __name__ == "__main__":
    main()
