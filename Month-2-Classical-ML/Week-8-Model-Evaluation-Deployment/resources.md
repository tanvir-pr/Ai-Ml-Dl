# Week 8 resources: Evaluation & deployment

## Model selection & validation
- **Cross-validation:** https://scikit-learn.org/stable/modules/cross_validation.html
- **StratifiedKFold, TimeSeriesSplit:** sklearn `model_selection`
- **Learning curves:** https://scikit-learn.org/stable/modules/learning_curve.html

## Metrics
- **Classification metrics:** https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics
- **Regression metrics:** MSE, RMSE, MAE, R² in same guide
- **ROC-AUC:** `roc_auc_score`, `RocCurveDisplay`

## Tuning
- **GridSearchCV:** https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html
- **RandomizedSearchCV:** for large search spaces
- **Pipeline:** https://scikit-learn.org/stable/modules/compose.html#pipeline

## Persistence & serving
- **joblib:** https://joblib.readthedocs.io/
- **Flask:** https://flask.palletsprojects.com/
- **FastAPI** (alternative): https://fastapi.tiangolo.com/

## MLOps (next steps)
- **MLflow** (tracking, registry): https://mlflow.org/
- **Docker** intro: containerize API for reproducible deploy

## Videos
- StatQuest: Cross validation, ROC and AUC, Precision-Recall

## Reading
- Géron — end-to-end project, model tuning, deployment chapter
