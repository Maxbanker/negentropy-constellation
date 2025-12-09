import argparse, yaml, json, os
from .models import Manifest
from .engine import open_corridor

def main():
    p = argparse.ArgumentParser(prog="xsft", description="XSFT Export Corridor CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("open", help="Open a corridor and emit a signed receipt")
    s.add_argument("manifest")
    s.add_argument("--out", required=True)

    args = p.parse_args()
    if args.cmd == "open":
        m = Manifest(**yaml.safe_load(open(args.manifest, "r", encoding="utf-8")))
        rec = open_corridor(m)
        os.makedirs(os.path.dirname(args.out), exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as f:
            json.dump(rec, f, indent=2, sort_keys=True)
        print(f"Wrote {args.out} (allow={rec['allow']})")

if __name__ == "__main__":
    main()
