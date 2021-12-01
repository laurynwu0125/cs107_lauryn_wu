import sqlite3
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer

def save_to_database(model_id, model_desc, db, model, X_train, X_test, y_train, y_test):
    params = model.get_params()
    # insert the parameters into the db
    for key in params.keys():
        vals_to_insert = (model_id, model_desc, key, params.get(key))
        cursor.execute('''INSERT INTO model_params
                    (id, desc, param_name, value)
                    VALUES (?, ?, ?, ?)''', vals_to_insert)
    coefs = model.coef_[0]   # coefficients of the model
    intercept = model.intercept_[0]   # intercept of the model
    features = model.feature_names_in_     # list of model features
    # insert the coefficients into db
    for i in range(len(features)):
        vals_to_insert = (model_id, model_desc, features[i], coefs[i])
        cursor.execute('''INSERT INTO model_coefs
                    (id, desc, feature_name, value)
                    VALUES (?, ?, ?, ?)''', vals_to_insert)
    # insert the intercept into db
    vals_to_insert = (model_id, model_desc, 'intercept', intercept)
    cursor.execute('''INSERT INTO model_coefs
                (id, desc, feature_name, value)
                VALUES (?, ?, ?, ?)''', vals_to_insert)

    # get the model's training score and testing score
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)
    # insert the scores into db
    vals_to_insert = (model_id, model_desc, train_score, test_score)
    cursor.execute('''INSERT INTO model_results
                (id, desc, train_score, test_score)
                VALUES (?, ?, ?, ?)''', vals_to_insert)
    db.commit()

if __name__ == "__main__":
    db = sqlite3.connect('regression.sqlite')
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS model_params")
    cursor.execute("DROP TABLE IF EXISTS model_coefs")
    cursor.execute("DROP TABLE IF EXISTS model_results")
    # create new tables with appropriate fields
    cursor.execute('''CREATE TABLE model_params (
                   id INTEGER NOT NULL,
                   desc TEXT,
                   param_name TEXT,
                   value)''')
    db.commit()
    cursor.execute('''CREATE TABLE model_coefs (
                   id INTEGER NOT NULL,
                   desc TEXT,
                   feature_name TEXT,
                   value REAL)''')
    db.commit()
    cursor.execute('''CREATE TABLE model_results (
                   id INTEGER NOT NULL,
                   desc TEXT,
                   train_score REAL,
                   test_score REAL)''')
    db.commit()

    # Load data
    data = load_breast_cancer()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = data.target

    # Split into train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=87)

    # Fit model
    baseline_model = LogisticRegression(solver='liblinear')
    baseline_model.fit(X_train, y_train)
    model_id = 1
    model_desc = "Baseline model"
    save_to_database(model_id, model_desc, db, baseline_model, X_train, X_test, y_train, y_test)

    # reduced logistic regression model
    feature_cols = ['mean radius', 'texture error', 'worst radius',
                'worst compactness', 'worst concavity']

    X_train_reduced = X_train[feature_cols]
    X_test_reduced = X_test[feature_cols]

    reduced_model = LogisticRegression(solver='liblinear')
    reduced_model.fit(X_train_reduced, y_train)
    model_id = 2
    model_desc = "Reduced model"
    save_to_database(model_id, model_desc, db, reduced_model, X_train_reduced, X_test_reduced, y_train, y_test)

    # model with L1 penalty
    penalized_model = LogisticRegression(solver='liblinear', penalty='l1', random_state=87, max_iter=150)
    penalized_model.fit(X_train, y_train)
    model_id = 3
    model_desc = "L1 penalty model"
    save_to_database(model_id, model_desc, db, penalized_model, X_train, X_test, y_train, y_test)

    # database queries
    query = '''SELECT id, MAX(test_score) FROM model_results'''
    q = cursor.execute(query).fetchall()[0]
    best_id, best_score = q
    print("Best model id:", best_id)
    print("Best validation score:", best_score)

    # get all the feature names and values of the best model
    query = '''SELECT feature_name, value FROM model_coefs WHERE id=3'''
    q = cursor.execute(query).fetchall()
    coef = []
    for tup in q:
        feature, value = tup
        if feature == 'intercept':
            intercept = value
        else:
            coef.append(value)
        print(feature, ":", value)

    # reproduce the test score
    test_model = LogisticRegression(solver='liblinear')
    test_model.fit(X_train, y_train)
    # Manually change fit parameters
    test_model.coef_ = np.array([coef])
    test_model.intercept_ = np.array([intercept])
    test_score = test_model.score(X_test, y_test)
    print(f'Reproduced best validation score: {test_score}')

    db.commit()
    db.close()
