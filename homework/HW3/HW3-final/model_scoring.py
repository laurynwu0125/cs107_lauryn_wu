from Regression import LinearRegression as lg
from Regression import RidgeRegression as rr
from sklearn import datasets
from sklearn.model_selection import train_test_split


dataset = datasets.fetch_california_housing()
print(dataset['data'])
print(dataset['target'])
X_train, X_test, y_train, y_test = train_test_split(dataset['data'],
                                                    dataset['target'],
                                                    test_size=0.2,
                                                    random_state=42)

alpha = 0.1
model1 = lg()
model2 = rr()
model2.set_params(alpha=alpha)
models = [model1, model2]

for model in models:
    model.fit(X_train, y_train)
    print("R^2: ", model.score(X_test, y_test))
    print("Coefficient Parameter: ", model.get_params().get("coeff"))
    print("Intercept Parameter: ", model.get_params().get("intercept"))
