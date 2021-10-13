import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import mean_squared_error

from financial_analysis import data

X, y = make_regression(n_samples=1000, n_features=1, noise=30)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

regr = linear_model.LinearRegression()
regr.fit(X_train, y_train)

w_0 = regr.intercept_
w_1 = regr.coef_

score_train = regr.score(X_train, y_train)
score_test = regr.score(X_test, y_test)

print(w_0, w_1, score_train, score_test)


# 圖像檢視
# plt.scatter(X_train, y_train, color='black')
# plt.scatter(X_test, y_test, color='red')
# plt.plot(X_test, regr.predict(X_test), color='blue')
# plt.show()


# Gradient Decent
def gd():
    alpha = 0.01
    repeats = 100
    w0 = 0
    w1 = 0
    errors = []
    points = []
    for j in range(repeats):
        error_sum = 0
        squared_error_sum = 0
        error_sum_x = 0
        for i in range(len(X_train)):
            predict = w0 + (X_train[i] * w1)
            squared_error_sum = squared_error_sum + (y_train[i] - predict) ** 2
            error_sum = error_sum + y_train[i] - predict
            error_sum_x = error_sum_x + (y_train[i] - predict) * X_train[i]
        w0 = w0 + (alpha * error_sum)
        w1 = w1 + (alpha * error_sum_x)
        errors.append(squared_error_sum / len(X_train))

    predicts = []
    mean_error = 0

    for i in range(len(X_test)):
        predict = w0 + (X_test[i] * w1)
        predicts.append(predict)

    return w0, w1, predicts


# 多項式回歸

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=52)

scores = []

for degree in range(1, 6):
    model = make_pipeline(PolynomialFeatures(degree), linear_model.LinearRegression())
    model.fit(X_train, y_train)
    scores.append((model.score(X_test, y_test)))

print(scores)

# 多變量回歸
A, b = make_regression(n_samples=1000, n_features=5, noise=50)
A_train, A_test, b_train, b_test = train_test_split(A, b, test_size=0.3, random_state=0)
multiregr = linear_model.LinearRegression()
multiregr.fit(A_train, b_train)
print(multiregr.score(A_train, b_train), multiregr.score(A_test, b_test))

# Lasso & Ridge
A, b = make_regression(n_samples=1000, n_features=10, noise=10)
A_train, A_test, b_train, b_test = train_test_split(A, b, test_size=0.3, random_state=0)

clf_lasso = linear_model.Lasso(alpha=0.1)
clf_lasso.fit(A_train, b_train)

clf_Ridge = linear_model.Ridge(alpha=0.1)
clf_Ridge.fit(A_train, b_train)

scores = []

for degree in range(1, 6):
    model = make_pipeline(PolynomialFeatures(degree), clf_Ridge)
    model.fit(X_train, y_train)
    scores.append((model.score(X_test, y_test)))

print(scores)

# Logistic Regression
X_train, X_test, y_train, y_test = train_test_split(data.X, data.y, test_size=0.3)
logistic = linear_model.LogisticRegression()
logistic.fit(X_train, y_train)
logistic.predict(X_test)
logistic.predict_proba(X_test)
print(logistic.score(X_test, y_test))

# Bayesian Classifier
X_train, X_test, y_train, y_test = train_test_split(data.X, data.y, test_size=0.3)
modelg=GaussianNB()  # 高斯適用連續變數
modelg.fit(X_train, y_train)
print(modelg.score(X_test, y_test))

modelm=MultinomialNB()  # 多項式貝氏分類適用離散變數
modelm.fit(X_train, y_train)
print(modelm.score(X_test, y_test))

modelb=BernoulliNB(binarize=[5.8, 3, 4.35, 1.3])  # 柏努力貝氏分類適用二元資料，特徵不是 0 就是 1，binarize 代表切分基準
modelb.fit(X_train, y_train)
print(modelb.score(X_test, y_test))

