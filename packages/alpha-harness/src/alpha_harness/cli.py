import argparse, json, yaml, os
from .models import Manifest
from .runner import run_manifest, replay

def main():
    p = argparse.ArgumentParser(prog="alpha", description="Alpha Harness CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("run")
    r.add_argument("manifest")
    r.add_argument("--out", required=True)

    rp = sub.add_parser("replay")
    rp.add_argument("telemetry")
    rp.add_argument("--check", action="store_true")

    args = p.parse_args()
    if args.cmd == "run":
        m = Manifest(**yaml.safe_load(open(args.manifest, "r", encoding="utf-8")))
        out = run_manifest(m)
        os.makedirs(os.path.dirname(args.out), exist_ok=True)
        json.dump(out, open(args.out, "w", encoding="utf-8"), indent=2, sort_keys=True)
        print(f"Wrote {args.out}")
    elif args.cmd == "replay":
        ok = replay(args.telemetry, check=args.check)
        print("OK" if ok else "FAIL")

if __name__ == "__main__":
    main()
