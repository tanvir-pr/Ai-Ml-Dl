# Week 6 exercises: Tree-based models

Use **`../../LEARNING_PATH.md`** and **`../../MAIN_EXPLANATION.md`** for definitions of entropy, Gini, bagging, and boosting.

---

## A. Decision trees

1. **Depth vs accuracy**  
   Plot train and validation accuracy vs `max_depth` for `DecisionTreeClassifier` on a noisy dataset. Where does overfitting start?

2. **Entropy vs Gini**  
   Fit two trees: `criterion='entropy'` vs `'gini'`. Compare depth, accuracy, and speed.

3. **Splits**  
   Print `feature_importances_` for a shallow tree. Do they match what you expect from EDA?

---

## B. Random forests

4. **n_estimators**  
   Plot OOB score or CV accuracy vs number of trees (e.g. 10 … 200).

5. **max_features**  
   Try `sqrt`, `log2`, 0.3 of feature count for `max_features`. What changes?

6. **Overfitting**  
   Compare single deep tree vs Random Forest on the same data. Which generalizes better?

---

## C. Gradient boosting (XGBoost / LightGBM / CatBoost)

7. **Learning rate vs n_estimators**  
   Fix a rough budget: try `learning_rate=0.1` with more trees vs `0.03` with more trees. Compare early stopping if available.

8. **max_depth**  
   How does boosting behave with very deep base learners vs shallow?

9. **Subsampling**  
   Turn on row subsampling (`subsample` in XGBoost / similar). Effect on bias and variance?

---

## D. Comparison & interpretation

10. **Feature importance**  
    Compare `RandomForest` impurity-based importance with **permutation importance** on the same model.

11. **Partial dependence**  
    Plot partial dependence for one numeric feature (sklearn `PartialDependenceDisplay`).

12. **Imbalanced data**  
    Use `class_weight='balanced'` or scale_pos_weight / SMOTE; optimize for **recall** on fraud-like data.

---

## E. Ensembles (stretch)

13. **CV**  
    5-fold CV compare: Decision Tree (limited depth), Random Forest, GradientBoosting or XGBoost.

14. **Stacking**  
    Combine logistic regression + random forest with a meta-learner (sklearn `StackingClassifier`).

15. **AdaBoost**  
    Fit `AdaBoostClassifier` and compare to a small gradient boosting model.

---

## Mini project: Credit card fraud

Use an **imbalanced** transaction dataset.

**Goals:**
- High recall for fraud (or justify a precision–recall tradeoff).
- Compare at least two of: Random Forest, XGBoost, LightGBM.
- Document preprocessing and metrics (confusion matrix, AUC-PR if imbalance severe).
