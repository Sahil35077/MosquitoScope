# Final Model — Test Set Evaluation (enhanced class-weighted training)

**Generated:** 2026-06-23T14:05:41.253750+00:00

## Config
- Model: convnextv2_tiny @ 288px
- Trial ID: 3
- Class weights: sqrt_balanced
- CV mean accuracy: 0.7386
- CV mean F1 macro: 0.6922

## Test results (with TTA)
- Accuracy: 0.7403
- F1 (macro): 0.7060
- F1 (weighted): 0.7347

## Confusion matrix
```
[[ 4  0  0 ...  0  0  0]
 [ 0  4  1 ...  0  0  0]
 [ 0  1 14 ...  0  0  0]
 ...
 [ 0  0  0 ...  5  0  0]
 [ 0  0  0 ...  0  7  1]
 [ 0  0  0 ...  0  0 10]]
```