import argparse, json, os
from .weaver import repair_dialogue

def main():
    p = argparse.ArgumentParser(prog="weaver", description="Weaver-11 CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("repair")
    r.add_argument("dialogue", help="path to text file")
    r.add_argument("--threshold", type=float, default=0.35)
    r.add_argument("--out", required=True, help="path to write patched text")
    r.add_argument("--report", required=True, help="path to write JSON report")

    args = p.parse_args()
    if args.cmd == "repair":
        text = open(args.dialogue, "r", encoding="utf-8").read()
        rep = repair_dialogue(text, threshold=args.threshold)
        os.makedirs(os.path.dirname(args.out), exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(rep["patched_text"])
        os.makedirs(os.path.dirname(args.report), exist_ok=True)
        with open(args.report, "w", encoding="utf-8") as f:
            json.dump({k:v for k,v in rep.items() if k != "patched_text"}, f, indent=2, sort_keys=True)
        print(f"Wrote {args.out} and {args.report} (uplift={rep['uplift']:.4f})")
