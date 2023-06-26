import numpy as np
import pandas as pd
import scipy.linalg as sla
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Lasso, Ridge

#  --------Analytical solution----------


class MyLinearRegression:
    def __init__(self, fit_intercept=True):
        self.fit_intercept = fit_intercept  # do we consider bias or not

    def fit(self, X, y):
        n, k = X.shape

        X_train = X
        if self.fit_intercept:
            X_train = np.hstack((X_train, np.ones((n, 1))))

        self.w = np.linalg.inv(X_train.T @ X_train) @ X_train.T @ y

        return self

    def predict(self, X):

        n, k = X.shape
        X_test = X
        if self.fit_intercept:
            X_test = np.hstack((X, np.ones((n, 1))))

        y_pred = X_test @ self.w

        return y_pred

    def get_weights(self):
        return self.w






