# Mini Project: House Price Prediction

## Overview
Build a regression model to predict house prices using the California Housing dataset.

## Objectives
1. Load and explore data
2. Feature engineering
3. Train linear regression (multiple, polynomial)
4. Apply regularization (Ridge, Lasso)
5. Evaluate with cross-validation
6. Compare models

## Dataset
```python
from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing()
```

## Steps
1. EDA and correlation analysis
2. Train-test split, scaling
3. Baseline: LinearRegression
4. Try polynomial features
5. Ridge and Lasso with CV for alpha
6. Final model selection and evaluation

## Deliverables
- Jupyter notebook
- Model comparison table
- Visualization of predictions vs actual
- Summary of best approach
