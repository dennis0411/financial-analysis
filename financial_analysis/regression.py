import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

X, y = make_regression(n_samples=1000, n_features=1, noise=20)

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

for degree in range(1, 5):
    model = make_pipeline(PolynomialFeatures(degree), linear_model.LinearRegression())
    model.fit(X_train, y_train)
    scores.append((model.score(X_test, y_test)))

print(scores)


# 多變量回歸

