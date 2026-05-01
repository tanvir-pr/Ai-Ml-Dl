# Week 5 exercises: Classification

Work through these after completing notebooks `01`–`04`. Theory context: **`../../LEARNING_PATH.md`** (Month 2).

---

## A. Logistic regression

1. **Decision boundary**  
   On a 2D synthetic dataset, plot the data and the line where `predict_proba` = 0.5. Label one side as class 0 and one as class 1.

2. **Regularization**  
   Compare `LogisticRegression(C=...)` (note: smaller `C` = stronger regularization in sklearn). Plot validation accuracy vs `C` on a log scale.

3. **Interpretation**  
   Fit logistic regression on a dataset with named features. Which coefficients are largest? Do signs make sense?

---

## B. K-Nearest Neighbors

4. **Effect of k**  
   For k = 1, 3, 11, 31 on the same scaled data, plot decision regions (e.g. `DecisionBoundaryDisplay`) or report CV accuracy.

5. **Scaling**  
   Repeat with raw vs `StandardScaler` features. Quantify how much accuracy changes.

6. **Distance**  
   Compare `metric='euclidean'` vs `metric='manhattan'` for the same k.

---

## C. Naive Bayes

7. **Text / spam**  
   Build a pipeline: `TfidfVectorizer` → `MultinomialNB` on SMS spam or similar. Report accuracy, precision, recall.

8. **Gaussian vs Multinomial**  
   On iris, use GaussianNB. On count-like features (integer bins), compare Multinomial with small counts.

9. **Independence assumption**  
   Write one paragraph: when does “naive” independence hurt NB?

---

## D. Support Vector Machines

10. **Kernels**  
    On the same 2D data, compare `linear`, `rbf`, `poly` (degree 2). Plot boundaries if possible.

11. **C and gamma**  
    For RBF SVM, grid a few values of `C` and `gamma`. When does the boundary become too wiggly?

12. **Training size**  
    Time fit for SVM as n grows (subsample 1k, 5k, 10k). Note SVM scaling concerns.

---

## E. Multi-class & imbalance

13. **OvR vs multinomial**  
    On `load_iris`, compare `multi_class='ovr'` vs `'multinomial'` for logistic regression (solver `lbfgs`).

14. **Imbalance**  
    Use `class_weight='balanced'` or undersampling. Compare before/after with precision and recall on minority class.

15. **Threshold**  
    Print precision–recall curve; choose a threshold that favors recall > 0.8 (if possible).

---

## F. Model comparison

16. **ROC**  
    On the same train/test split, fit logistic, KNN, NB, SVM; plot ROC curves on one figure.

17. **GridSearchCV**  
    Tune at least two hyperparameters on one model (e.g. SVM `C`, `gamma`) with 5-fold CV.

---

## Mini project: Spam detector

Build an email/SMS spam classifier using **Naive Bayes** or **logistic regression** with **TF-IDF** features.

**Deliverables:**
- Notebook or script with EDA (class balance), train/val split, metrics (precision/recall on spam class).
- Short README: how to run, what data file is expected.

**Stretch:** Compare to linear SVM on the same features.
