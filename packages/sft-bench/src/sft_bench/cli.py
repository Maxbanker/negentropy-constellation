import argparse, os, json
from .io import read_ndjson
from .models import ThresholdModel
from .metrics import compute_metrics as prf, compute_lead_time

def main():
    p = argparse.ArgumentParser(prog="sftbench", description="SFT Bench CLI")
    p.add_argument("--dataset", required=True, help="Path to folder with series.ndjson and labels.ndjson")
    p.add_argument("--model", choices=["threshold"], default="threshold")
    p.add_argument("--psi_min", type=float, default=0.35)
    p.add_argument("--gamma_max", type=float, default=0.8)
    p.add_argument("--omega_min", type=float, default=0.1)
    p.add_argument("--window", type=int, default=16)
    p.add_argument("--out", required=True)
    args = p.parse_args()

    series = list(read_ndjson(os.path.join(args.dataset, "series.ndjson")))
    labels = {int(o["step"]): int(o["collapse"]) for o in read_ndjson(os.path.join(args.dataset, "labels.ndjson"))}

    if args.model == "threshold":
        model = ThresholdModel(args.psi_min, args.gamma_max, args.omega_min, args.window)

    steps = []
    y_true = []
    y_pred = []
    for obj in series:
        step = int(obj["step"])
        steps.append(step)
        y_true.append(labels.get(step, 0))
        y_pred.append(model.predict(obj["values"]))

    metrics = prf(y_true, y_pred)
    metrics["mean_lead_time"] = compute_lead_time(steps, y_true, y_pred)
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump({"metrics": metrics, "config": vars(args)}, f, indent=2, sort_keys=True)
    print(f"Wrote {args.out}")
