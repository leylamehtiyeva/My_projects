from MyLinearRegression import *

#  --------Testing----------


def linear_expression(x):
    return 5 * x + 6

# based on features, generate target values with some noise

objects_num = 50
X = np.linspace(-5, 5, objects_num)
y = linear_expression(X) + np.random.randn(objects_num) * 5
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.5)

plt.figure(figsize=(10, 7))
plt.plot(X, linear_expression(X), label='real', c='g')
plt.scatter(X_train, y_train, label='train', c='b')
plt.scatter(X_test, y_test, label='test', c='orange')

plt.title("Generated dataset")
plt.grid(alpha=0.2)
plt.legend()
plt.show()