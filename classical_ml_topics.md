# Classical Machine Learning Topics (Academic & Job Preparation)

> **Full explanations:** See `MAIN_EXPLANATION.md` for each topic's definition and use.

## 1. Fundamentals
- Supervised vs Unsupervised vs Semi-Supervised
- Regression vs Classification
- Bias-Variance Tradeoff
- Overfitting and Underfitting
- Train/Validation/Test Split
- Cross-Validation: K-Fold
- Cross-Validation: Stratified K-Fold
- Cross-Validation: Leave-One-Out
- Cross-Validation: Time Series (Walk-Forward)
- No Free Lunch Theorem
- Inductive Bias

## 2. Data Preprocessing
- Missing Data: Imputation (Mean, Median, Mode)
- Missing Data: Forward/Backward Fill
- Missing Data: Drop Rows/Columns
- Feature Scaling: Standardization (Z-score)
- Feature Scaling: Min-Max Normalization
- Feature Scaling: Robust Scaling
- Categorical Encoding: One-Hot Encoding
- Categorical Encoding: Label Encoding
- Categorical Encoding: Target Encoding
- Feature Engineering
- Feature Selection: Filter Methods
- Feature Selection: Wrapper Methods
- Feature Selection: Embedded Methods
- Outlier Handling
- Data Augmentation (for tabular)
- Train-Test Split Strategies

## 3. Linear Regression
- Simple Linear Regression
- Multiple Linear Regression
- Normal Equation (Closed-Form Solution)
- Least Squares
- Gradient Descent for Regression
- Stochastic Gradient Descent (SGD)
- Assumptions of Linear Regression
- Residual Analysis
- R² (Coefficient of Determination)
- Adjusted R²
- Polynomial Regression
- Regularization: Ridge (L2)
- Regularization: Lasso (L1)
- Regularization: Elastic Net
- Multicollinearity
- Feature Importance in Linear Models

## 4. Classification Algorithms
- Logistic Regression (Binary)
- Logistic Regression (Multi-class: OvR, Softmax)
- Decision Boundary
- K-Nearest Neighbors (KNN)
- KNN: Choice of k
- KNN: Distance Metrics (Euclidean, Manhattan)
- Naive Bayes (Gaussian, Multinomial, Bernoulli)
- Bayes' Theorem in Naive Bayes
- Support Vector Machines (SVM)
- SVM: Linear Kernel
- SVM: RBF (Gaussian) Kernel
- SVM: Polynomial Kernel
- SVM: C Parameter and Margin
- SVM: Kernel Trick
- Imbalanced Data: SMOTE
- Imbalanced Data: Class Weights
- Imbalanced Data: Oversampling/Undersampling
- Multi-class Classification: One-vs-Rest
- Multi-class Classification: One-vs-One

## 5. Tree-Based Models
- Decision Trees
- CART Algorithm
- Splitting: Entropy
- Splitting: Gini Impurity
- Splitting: Information Gain
- Pruning: Pre-pruning
- Pruning: Post-pruning
- Random Forests (Bagging)
- Random Forests: Bootstrap Sampling
- Random Forests: Feature Subspace
- Gradient Boosting
- XGBoost
- LightGBM
- CatBoost
- AdaBoost
- Stacking (Stacked Generalization)
- Feature Importance
- Partial Dependence Plots

## 6. Unsupervised Learning
- K-Means Clustering
- K-Means: Elbow Method
- K-Means: Silhouette Score
- K-Means++ (Initialization)
- Hierarchical Clustering
- Hierarchical: Agglomerative
- Hierarchical: Divisive
- Hierarchical: Linkage (Single, Complete, Average, Ward)
- Dendrogram
- DBSCAN
- DBSCAN: Density-Based
- Gaussian Mixture Models (GMM)
- Dimensionality Reduction
- PCA (Principal Component Analysis)
- PCA: Variance Explained
- PCA: SVD Connection
- t-SNE (Visualization)
- UMAP
- Anomaly Detection: Isolation Forest
- Anomaly Detection: One-Class SVM
- Anomaly Detection: Local Outlier Factor (LOF)
- Customer Segmentation
- Clustering Evaluation: Silhouette, Davies-Bouldin

## 7. Model Evaluation Metrics
- Classification: Accuracy
- Classification: Precision
- Classification: Recall (Sensitivity)
- Classification: F1-Score
- Classification: Specificity
- Classification: Confusion Matrix
- Classification: ROC Curve
- Classification: AUC-ROC
- Classification: Precision-Recall Curve
- Classification: AUC-PR
- Classification: Log Loss
- Classification: Cohen's Kappa
- Regression: MSE (Mean Squared Error)
- Regression: RMSE (Root Mean Squared Error)
- Regression: MAE (Mean Absolute Error)
- Regression: R²
- Regression: MAPE
- Multi-class: Macro/Micro/Weighted Averages
- Ranking: Precision@k, Recall@k
- Ranking: NDCG (Normalized Discounted Cumulative Gain)
- Ranking: Mean Reciprocal Rank (MRR)

## 8. Hyperparameter Tuning
- Grid Search
- Random Search
- Bayesian Optimization
- Hyperband
- Optuna
- Learning Curves
- Validation Curves

## 9. Model Deployment & MLOps
- Model Serialization (Pickle, Joblib)
- Save/Load with Preprocessing
- Pipeline Creation
- API Deployment (Flask, FastAPI)
- Model Versioning
- A/B Testing
- Model Monitoring
- Retraining Strategies
