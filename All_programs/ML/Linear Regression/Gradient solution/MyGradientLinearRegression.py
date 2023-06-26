import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


class MyGradientLinearRegression:
    def __init__(self, fit_intercept=True):
        self.fit_intercept = fit_intercept
        self.w = None

    def fit(self, X, y, lr=0.01, max_iter=100):
        n, k = X.shape

        if self.w is None:
            self.w = np.random.randn(k + 1 if self.fit_intercept else k)

        X_train = np.hstack((X, np.ones((n, 1)))) if self.fit_intercept else X
        self.losses = []

        for iter_num in range(max_iter):
            y_pred = self.predict(X)
            self.losses.append(mean_squared_error(y_pred, y))

            grad = self._calc_gradient(X_train, y, y_pred)

            assert grad.shape == self.w.shape, f'gradient shape {grad.shape} is not equal weight shape {self.w.shape}'
            self.w = self.w - lr * grad

        return self

    def predict(self, X):
        n, k = X.shape
        X_test = np.hstack((X, np.ones((n, 1)))) if self.fit_intercept else X
        y_pred = X_test @ self.w
        return y_pred

    @staticmethod
    def _calc_gradient(X, y, y_pred):
        grad = 2 * (y_pred - y)[:, np.newaxis] * X
        grad = grad.mean(axis=0)
        return grad

    def get_losses(self):
        return self.losses

    def get_weights(self):
        return self.w


#  -------------data generation---------------
def linear_expression(x):
    return 5 * x + 6


objects_num = 50
X = np.linspace(-5, 5, objects_num)
y = linear_expression(X) + np.random.randn(objects_num) * 5

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.5)

#  ------------testing------------------------

regressor = MyGradientLinearRegression(fit_intercept=True)
res = regressor.fit(X_train[:, np.newaxis], y_train, max_iter=100).get_losses()
predictions = regressor.predict(X_test[:, np.newaxis])
w = regressor.get_weights()
print(res[-1], w)


plt.figure(figsize=(10, 5))
plt.plot(X, linear_expression(X), label='real', c='g')

plt.scatter(X_train, y_train, label='train')
plt.scatter(X_test, y_test, label='test')
plt.plot(X, regressor.predict(X[:, np.newaxis]), label='predicted', c='r')

plt.grid(alpha=0.2)
plt.legend()
plt.show()



