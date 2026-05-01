# Week 8 exercises: Evaluation & deployment

Reference: **`../../LEARNING_PATH.md`** (Month 2) and **`../../MAIN_EXPLANATION.md`**.

---

## A. Cross-validation

1. **3-fold vs 10-fold**  
   Same model and data: compare mean and std of CV scores for cv=3 vs cv=10.

2. **Stratified**  
   On imbalanced classification, compare `KFold` vs `StratifiedKFold` CV scores and variance.

3. **LOO**  
   On a tiny dataset (n < 50), run `LeaveOneOut()` and discuss computational cost vs KFold.

4. **Time series** (stretch)  
   Use `TimeSeriesSplit` on sequential data; explain why shuffled KFold would leak.

---

## B. Metrics

5. **Precision vs recall**  
   Fix a classifier; plot precision and recall vs threshold. Pick a threshold for a stated business goal.

6. **ROC and AUC**  
   Train two models; plot both ROC curves; compare AUC and discuss when ROC misleads (imbalance).

7. **Multi-class**  
   Report confusion matrix for Wine (3 classes); use `classification_report` with `average='macro'` vs `'weighted'`.

8. **Regression**  
   On a regression task, report MSE, RMSE, MAE, R² and interpret scale.

---

## C. Hyperparameter tuning

9. **GridSearchCV**  
   Tune SVM or Random Forest with a small grid; report `best_params_` and `best_score_`.

10. **Pipeline**  
    Build `Pipeline([('scaler', StandardScaler), ('clf', ...)])` and run GridSearchCV on pipeline parameters (`clf__C`, etc.).

11. **RandomizedSearchCV**  
    Use a larger distribution for at least one hyperparameter; compare best score to grid search time.

12. **Learning curve**  
    Plot `learning_curve` for a model; state whether more data would help.

---

## D. Deployment

13. **Save / load**  
    Fit a model + `StandardScaler`; save both with joblib; load in a second script and verify identical predictions.

14. **Flask (or FastAPI)**  
    Minimal `/predict` JSON endpoint that loads the saved model and returns class or probability.

15. **Versioning** (short answer)  
    List three things you would log when redeploying a model (data version, code hash, metrics, *etc.*).

---

## Mini project: End-to-end ML pipeline

From raw CSV to saved artifact and working prediction path.

**Required steps:**
1. Load and clean data; train/validation/test split strategy documented.
2. Preprocessing + model in a Pipeline.
3. Evaluation: metrics appropriate to problem (imbalance? state it).
4. `joblib.dump` final model (and preprocessor if separate).
5. Tiny API or CLI that accepts one row (or JSON) and outputs prediction.

**Stretch:** Dockerize the API.
