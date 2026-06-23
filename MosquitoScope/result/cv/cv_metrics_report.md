# Hyperparameter Search + 5-Fold CV (enhanced class-weighted)

**Generated:** 2026-06-23T13:51:08.440235+00:00
**Output folder:** `results_class_weight/cv`
**Model:** convnextv2_tiny @ 288px
**Class weights:** `sqrt_balanced` + focal loss (gamma=2.0)

## Hyperparameter grid searched
- learning_rate: [3e-05, 5e-05, 0.0001]
- batch_size: [8, 16]
- weight_decay: [0.01, 0.05]
- Total trials: 12

## Best trial
- Trial ID: 3
- Learning rate: **5e-05**
- Batch size: **8**
- Weight decay: **0.01**
- Epochs: **24**
- CV mean accuracy: 0.7386 ± 0.0174
- CV mean F1 macro: 0.6922 ± 0.0158

## All trials (sorted by accuracy)
- Trial 3: lr=5e-05, bs=8, wd=0.01 | acc=0.7386 | f1=0.6922 **<- BEST**
- Trial 4: lr=5e-05, bs=8, wd=0.05 | acc=0.7370 | f1=0.6923
- Trial 2: lr=3e-05, bs=8, wd=0.05 | acc=0.7337 | f1=0.6926
- Trial 1: lr=3e-05, bs=8, wd=0.01 | acc=0.7337 | f1=0.6910
- Trial 11: lr=0.0001, bs=16, wd=0.01 | acc=0.7321 | f1=0.6864
- Trial 5: lr=0.0001, bs=8, wd=0.01 | acc=0.7288 | f1=0.6765
- Trial 6: lr=0.0001, bs=8, wd=0.05 | acc=0.7280 | f1=0.6776
- Trial 9: lr=5e-05, bs=16, wd=0.01 | acc=0.7256 | f1=0.6813
- Trial 12: lr=0.0001, bs=16, wd=0.05 | acc=0.7239 | f1=0.6782
- Trial 10: lr=5e-05, bs=16, wd=0.05 | acc=0.7231 | f1=0.6710
- Trial 7: lr=3e-05, bs=16, wd=0.01 | acc=0.7134 | f1=0.6659
- Trial 8: lr=3e-05, bs=16, wd=0.05 | acc=0.7003 | f1=0.6543

## Per-fold results (best trial)

### Fold 1
- Best epoch: 24
- Accuracy: 0.7398
- F1 (macro): 0.6769

### Fold 2
- Best epoch: 25
- Accuracy: 0.7602
- F1 (macro): 0.7085

### Fold 3
- Best epoch: 13
- Accuracy: 0.7073
- F1 (macro): 0.6696

### Fold 4
- Best epoch: 26
- Accuracy: 0.7469
- F1 (macro): 0.7044

### Fold 5
- Best epoch: 24
- Accuracy: 0.7388
- F1 (macro): 0.7017