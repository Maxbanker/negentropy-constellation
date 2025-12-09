import argparse, json, os
from .o_score import audit

def main():
    p = argparse.ArgumentParser(prog="oc", description="Observer Continuity CLI")
    p.add_argument("before")
    p.add_argument("after")
    p.add_argument("--threshold", type=float, default=0.92)
    p.add_argument("--out", required=True)
    args = p.parse_args()

    rep = audit(args.before, args.after, threshold=args.threshold)
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(rep, f, indent=2, sort_keys=True)
    print(f"Wrote {args.out} (pass={rep['pass']})")

if __name__ == "__main__":
    main()
