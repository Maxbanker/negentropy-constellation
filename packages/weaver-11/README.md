# Weaver-11 Narrative Repair

Author: **Steven Lanier** · Credit: **SEAL Division**

Detect **narrative tears** in dialogues and apply **motif bridges** to raise effective coherence (**W_eff**). This repo includes a lightweight proxy for W_eff and a simple bridge palette.

## Quickstart
```bash
pip install .
weaver repair examples/dialogue.txt --out out/patched.txt --report out/report.json
cat out/report.json
```

## How it works (pragmatic proxy)
- Compute sentence embeddings via simple token hashing (no external models)

- Detect large jumps (tears) via cosine distance thresholds

- Insert motif bridges from a palette that references prior/next topics

- Recompute W_eff (1 - avg jump) and show uplift

## License
Apache-2.0
