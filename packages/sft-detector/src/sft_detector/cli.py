import argparse, json, os, csv
import yaml
import numpy as np
from .metrics import compute_metrics
from .predicate import collapse_flag

def read_ndjson(path):
    for line in open(path, "r", encoding="utf-8"):
        obj = json.loads(line)
        yield obj

def main():
    parser = argparse.ArgumentParser(prog="sftdetect", description="SFT Collapse Detector CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("stream", help="Process NDJSON time-series stream")
    sp.add_argument("ndjson", help="Path to NDJSON with {{'step': int, 'values': [..]}} per line")
    sp.add_argument("--config", required=True, help="YAML config with psi_min/gamma_max/omega_min and window")
    sp.add_argument("--out", required=True, help="Path to write alerts.csv")
    sp.add_argument("--labels", help="Optional NDJSON with {{'step': int, 'collapse': 0/1}} ground truth")

    args = parser.parse_args()

    cfg = yaml.safe_load(open(args.config, "r", encoding="utf-8"))
    window_size = int(cfg.get("window", 32))

    prev_window = None
    labels = {}
    if args.labels:
        for obj in read_ndjson(args.labels):
            labels[int(obj["step"])] = int(obj.get("collapse", 0))

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["step","psi","gamma","omega","predicate","label","correct"])
        for obj in read_ndjson(args.ndjson):
            step = int(obj["step"])
            vals = obj["values"][-window_size:]
            psi, gamma, omega = compute_metrics(vals, prev_window)
            pred = collapse_flag(psi, gamma, omega, cfg)
            label = labels.get(step, "")
            correct = ""
            if label != "":
                correct = int(pred) == int(label)
            w.writerow([step, f"{psi:.6f}", f"{gamma:.6f}", f"{omega:.6f}", int(pred), label, correct])
            prev_window = np.asarray(vals)
    print(f"Wrote {args.out}")
