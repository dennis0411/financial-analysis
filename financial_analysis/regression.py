import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split


X, y = make_regression(n_samples=100,n_features=1,noise=20)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

regr = linear_model.LinearRegression()
regr.fit(X_train, y_train)

w_0 = regr.intercept_
w_1 = regr.coef_

score_train = regr.score(X_train, y_train)
score_test = regr.score(X_test, y_test)

print(w_0, w_1, score_train, score_test)