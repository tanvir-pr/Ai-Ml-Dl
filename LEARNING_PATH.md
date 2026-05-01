# How to use this course (single guide)

Everything you need to **set up**, **navigate**, and **study** the 12-week path in one place.

---

## 1. Setup (once)

```bash
cd ML-DL-Learning
python -m venv ml_env
# Windows: ml_env\Scripts\activate
# Mac/Linux: source ml_env/bin/activate

pip install -r requirements.txt
jupyter lab
```

- **Python:** 3.9+ recommended.  
- **Editor:** Jupyter Lab, VS Code with Jupyter extension, or Cursor.

---

## 2. How the repo is organized (only 3 folders to remember)

| Folder | Weeks | What you learn |
|--------|-------|----------------|
| `Month-1-Foundations/` | 1–4 | Python, math, NumPy/Pandas, plots, statistics, linear regression |
| `Month-2-Classical-ML/` | 5–8 | Classification, trees, unsupervised, metrics & deployment |
| `Month-3-Deep-Learning/` | 9–12 | Neural nets, CNNs, NLP/transformers, advanced topics & capstone |

**Inside almost every week folder:**

1. Numbered **`01_*.ipynb`, `02_*.ipynb`, …** — open in order; that is the lesson.  
2. **`exercises.md`** — practice after the notebooks.  
3. **`mini_project.md`** — one applied project.  
4. **`resources.md`** — links for deeper reading.  
5. **`README.md`** — week overview (some weeks).

**Optional:** `Resources/cheatsheets/` (e.g. NumPy).

---

## 3. What to do each week

1. Open that week’s folder.  
2. Run notebooks **in numeric order**.  
3. Do **`exercises.md`**.  
4. Start **`mini_project.md`** when ready.  
5. Use **`resources.md`** if you want videos or docs.

**Interview / exam prep (optional):** read **`MAIN_EXPLANATION.md`** for short definitions of topics.

**Books (optional):** *Grokking Deep Learning* (hands-on from scratch); [Deep Learning Book](https://www.deeplearningbook.org/) (Goodfellow et al., free online).

---

## 4. Full curriculum (all weeks)

### Month 1 — `Month-1-Foundations/`

| Week | Folder | Notebooks (run in order) |
|------|--------|---------------------------|
| 1 | `Week-1-Python-Math-Basics/` | `01_python_refresher` → `02_linear_algebra` → `03_calculus_basics` |
| 2 | `Week-2-NumPy-Pandas-Matplotlib/` | `01_numpy_fundamentals` → `02_pandas_data_manipulation` → `03_data_visualization` |
| 3 | `Week-3-Statistics-Probability/` | `01_descriptive_statistics` → `02_probability_theory` → `03_hypothesis_testing` |
| 4 | `Week-4-Linear-Regression/` | `01_simple_linear_regression` → `02_multiple_regression` → `03_gradient_descent` → `04_regularization` |

### Month 2 — `Month-2-Classical-ML/`

| Week | Folder | Notebooks (run in order) |
|------|--------|---------------------------|
| 5 | `Week-5-Classification-Algorithms/` | `01_logistic_regression` → `02_knn_algorithm` → `03_naive_bayes` → `04_svm` |
| 6 | `Week-6-Tree-Based-Models/` | `01_decision_trees` → `02_random_forests` → `03_gradient_boosting` → `04_feature_importance` |
| 7 | `Week-7-Unsupervised-Learning/` | `01_kmeans_clustering` → `02_hierarchical_clustering` → `03_pca_dimensionality_reduction` → `04_anomaly_detection` |
| 8 | `Week-8-Model-Evaluation-Deployment/` | `01_cross_validation` → `02_metrics` → `03_hyperparameter_tuning` → `04_model_deployment` |

### Month 3 — `Month-3-Deep-Learning/`

| Week | Folder | Notebooks (run in order) |
|------|--------|---------------------------|
| 9 | `Week-9-Neural-Networks-Basics/` | `01_perceptron` → `02_mlp_from_scratch` → `03_backpropagation` → `04_tensorflow_keras_intro` → `05_pytorch_intro` |
| 10 | `Week-10-CNNs-Computer-Vision/` | `01_convolution_operations` → `02_cnn_architectures` → `03_transfer_learning` → `04_image_augmentation` → `05_object_detection` |
| 11 | `Week-11-RNNs-NLP/` | `01_text_preprocessing` → `02_rnn_lstm_gru` → `03_attention_mechanism` → `04_transformers` → `05_sentiment_analysis` |
| 12 | `Week-12-Advanced-DL-Capstone/` | `01_gans` → `02_autoencoders` → `03_reinforcement_learning_intro` → `04_model_optimization` + **`capstone_project.md`** |

---

## 5. Files at the repo root (what matters)

| File | Purpose |
|------|---------|
| **`README.md`** | Short intro + link here |
| **`LEARNING_PATH.md`** | **This file** — your study map |
| **`MAIN_EXPLANATION.md`** | Topic explanations for revision / interviews |
| **`requirements.txt`** | Python packages |

Ignore **`.git/`** (Git internals). Ignore any `*_executed.ipynb` copies if present — learn from the main `.ipynb` without `_executed`.

---

## 6. Rough time budget

About **10–20 hours per week** depending on depth. Month 3 is often heavier (deep learning).

Start at **Week 1** and move forward in order unless your course already skipped ahead.
