# Observer Continuity Kit

Author: **Steven Lanier** · Credit: **SEAL Division**

Tools to compute an **O-score** and verify continuity when migrating agent state between models/substrates.
- PSD (power spectral density) sketches for states
- Cosine-similarity based O-score
- Pass/Fail gate with report

## Quickstart
```bash
pip install .
oc audit examples/before.npy examples/after.npy --threshold 0.92 --out out/report.json
cat out/report.json
```

## O-score (pragmatic proxy)
- Normalize states

- Compute PSD sketch via FFT

- Compare with cosine similarity ∈ [0,1]


## License
Apache-2.0
