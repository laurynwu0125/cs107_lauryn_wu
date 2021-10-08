import numpy as np

class Regression():
    def __init__(self):
        # initialize an empty dictionary
        raise NotImplementedError

    def get_params(self):
        # returns beta for the fitted model
        raise NotImplementedError

    def set_params(self, **kwargs):
        # manually set parameters of the linear model
        raise NotImplementedError

    def fit(self, X, y):
        # fits a linear model to X and y, stores best-fit parameters in params
        raise NotImplementedError

    def predict(self, X):
        # predict new values with the fitted model given X
        raise NotImplementedError

    def score(self, X, y):
        # returns the R^2 value of the fitted model
        raise NotImplementedError


class LinearRegression(Regression):
    def __init__(self):
        # initialize an empty dictionary
        self.params = {}

    def get_params(self):
        # returns beta for the fitted model
        return self.params

    def set_params(self, **kwargs):
        # manually set parameters of the linear model
        for key, value in kwargs.items():
            self.params[key] = value

    def fit(self, X, y):
        # fits a linear model to X and y, stores best-fit parameters in params
        dim1 = X.shape[0]
        dim2 = X.shape[1]
        onesVec = np.ones((dim1, 1))
        newX = np.append(X, onesVec, axis=1)
        transX = newX.T
        inverse = np.linalg.inv(np.matmul(transX, newX))
        beta = np.matmul(np.matmul(inverse, transX), y)
        self.params["coeff"] = beta[0:dim2]
        self.params["intercept"] = beta[dim2]

    def predict(self, X):
        # predict new values with the fitted model given X
        beta1 = self.params.get("coeff")
        beta0 = self.params.get("intercept")
        return np.matmul(X, beta1) + beta0

    def score(self, X, y):
        # returns the R^2 value of the fitted model
        predY = self.predict(X)
        origY = np.mean(y)
        SS_T = np.sum((y - origY)**2)
        SS_E = np.sum((y - predY)**2)
        squaredR = 1 - (SS_E / SS_T)
        return squaredR


class RidgeRegression(Regression):
    def __init__(self):
        # initialize an empty dictionary
        self.params = {}

    def get_params(self):
        # returns beta for the fitted model
        return self.params

    def set_params(self, **kwargs):
        # manually set parameters of the linear model
        for key, value in kwargs.items():
            self.params[key] = value

    def fit(self, X, y):
        # fits a linear model to X and y, stores best-fit parameters in params
        dim1 = X.shape[0]
        dim2 = X.shape[1]
        gamma = np.identity(dim2+1) * self.params.get("alpha")
        onesVec = np.ones((dim1, 1))
        newX = np.append(X, onesVec, axis=1)
        transX = newX.T
        matSum = np.matmul(transX, newX) + np.matmul(gamma.T, gamma)
        inverse = np.linalg.inv(matSum)
        beta = np.matmul(np.matmul(inverse, transX), y)
        self.params["coeff"] = beta[0:dim2]
        self.params["intercept"] = beta[dim2]


    def predict(self, X):
        # predict new values with the fitted model given X
        beta1 = self.params.get("coeff")
        beta0 = self.params.get("intercept")
        return np.matmul(X, beta1) + beta0

    def score(self, X, y):
        # returns the R^2 value of the fitted model
        predY = self.predict(X)
        origY = np.mean(y)
        SS_T = np.sum((y - origY)**2)
        SS_E = np.sum((y - predY)**2)
        print("SS_T", SS_T)
        print("SS_E", SS_E)
        squaredR = 1 - (SS_E / SS_T)
        return squaredR
