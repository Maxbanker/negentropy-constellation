import argparse, yaml, json, os
from .models import Manifest
from .engine import decide

def main():
    p = argparse.ArgumentParser(prog="ethics", description="BC‑REP Ethics Gate CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("score", help="Score an action manifest")
    s.add_argument("manifest")
    s.add_argument("--out", required=True)

    args = p.parse_args()
    if args.cmd == "score":
        m = Manifest(**yaml.safe_load(open(args.manifest, "r", encoding="utf-8")))
        d = decide(m)
        os.makedirs(os.path.dirname(args.out), exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as f:
            json.dump(d, f, indent=2, sort_keys=True)
        print(f"Wrote {args.out} (allow={d['allow']})")

if __name__ == "__main__":
    main()
