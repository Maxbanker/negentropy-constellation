import math

def compute_metrics(y_true, y_pred):
    tp = sum(1 for t,p in zip(y_true, y_pred) if t==1 and p==1)
    fp = sum(1 for t,p in zip(y_true, y_pred) if t==0 and p==1)
    fn = sum(1 for t,p in zip(y_true, y_pred) if t==1 and p==0)
    prec = tp / (tp + fp + 1e-12)
    rec  = tp / (tp + fn + 1e-12)
    f1   = 2*prec*rec / (prec + rec + 1e-12)
    return {"precision": float(prec), "recall": float(rec), "f1": float(f1)}

def compute_lead_time(steps, y_true, y_pred):
    # First alert time before first collapse
    t_collapses = [s for s,t in zip(steps, y_true) if t==1]
    t_alerts    = [s for s,p in zip(steps, y_pred) if p==1]
    if not t_collapses or not t_alerts:
        return 0.0
    lead = t_alerts[0] - t_collapses[0]
    return float(max(0.0, -lead)) if lead > 0 else float(-lead)
