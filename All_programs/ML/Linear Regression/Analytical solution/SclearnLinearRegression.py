import numpy as np
import pandas as pd
import scipy.linalg as sla
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.linear_model import LinearRegression, Lasso, Ridge

from TestingModel import *
import PredictValues


sk_regression = LinearRegression()

sk_regression.fit(X_train[:, np.newaxis], y_train)

res = sk_regression.predict(X[:, np.newaxis])


plt.figure(figsize=(10, 7))
plt.plot(X, linear_expression(X), label='real', c='g')

plt.scatter(X_train, y_train, label='train')
plt.scatter(X_test, y_test, label='test')
#plt.plot(X, PredictValues.predictions, label='ours', c='r', linestyle=':')
plt.plot(X, res, label='sklearn', c='cyan', linestyle=':')

plt.title("Different Prediction")
plt.ylabel('target')
plt.xlabel('feature')
plt.grid(alpha=0.2)
plt.legend()
plt.show()
