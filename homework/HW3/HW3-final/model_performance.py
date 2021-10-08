from Regression import LinearRegression as lg
from Regression import RidgeRegression as rr
from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

dataset = datasets.fetch_california_housing()
print(dataset['data'])
print(dataset['target'])
X_train, X_test, y_train, y_test = train_test_split(dataset['data'],
                                                    dataset['target'],
                                                    test_size=0.2,
                                                    random_state=42)

model1 = lg()
model2 = rr()
models = [model1, model2]
r2matrix = []
alphas = np.arange(.01, 11, 0.5)

for model in models:
    r2arr = []
    for alpha in alphas:
        model.set_params(alpha=alpha)
        model.fit(X_train, y_train)
        r2 = model.score(X_test, y_test)
        r2arr.append(r2)
    print("R^2: ", r2arr)
    r2matrix.append(r2arr)

plt.plot(alphas, r2matrix[0], 'r', alphas, r2matrix[1], 'b')
plt.xlabel(r'$\alpha$')
plt.ylabel(r'$R^2$ score')
plt.title(r'$R^2$ vs. $\alpha$ Model Performance')
plt.legend(['Linear Regression', 'Ridge Regression'])
plt.show()
