from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from financial_analysis import data


param_test = {'n_estimators':range(10, 101, 10), 'min_samples_leaf':range(5, 31, 5), 'max_depth':range(5, 20)}
model = RandomForestClassifier(random_state=50, min_samples_leaf=10)
gridsearch = GridSearchCV(estimator=model, n_jobs=-1, param_grid=param_test, cv=5)
gridsearch_result = gridsearch.fit(data.X, data.y)

print(f"最佳準確率 : {gridsearch_result.best_score_},最佳參數組合 : {gridsearch_result.best_params_}")
