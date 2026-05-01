# Week 8: Model evaluation & deployment

**Month 2 · Classical machine learning**

## Purpose
Measure models **honestly**, **tune** without test leakage, and **ship** a trained artifact — the bridge between experiments and practice (MLOps intro).

## Topics covered (in order)

| # | Notebook | Focus |
|---|----------|--------|
| 1 | `01_cross_validation.ipynb` | K-fold, stratified K-fold, LOO concepts |
| 2 | `02_metrics.ipynb` | Accuracy, precision, recall, F1, ROC-AUC, confusion matrix |
| 3 | `03_hyperparameter_tuning.ipynb` | GridSearchCV, parameter grids, nested ideas |
| 4 | `04_model_deployment.ipynb` | joblib save/load, API sketch |

## Learning outcomes
- Explain **why** the test set is used once and **how** CV approximates generalization.
- Pick **metrics** for imbalance (e.g. F1, PR-AUC) vs balanced accuracy.
- Build a **Pipeline** and tune it with `GridSearchCV` / `RandomizedSearchCV`.
- Serialize a model and describe a simple **HTTP predict** endpoint.

## Files in this folder
- **Notebooks:** `01_` … `04_`
- **`exercises.md`** — learning curves, pipelines, Flask, threshold tuning.
- **`mini_project.md`** — end-to-end pipeline + API.
- **`resources.md`** — sklearn model selection & metrics, Flask.

## Extended theory
See **`../../LEARNING_PATH.md`** (Month 2, Week 8).

## Time estimate
**12–15 hours**
