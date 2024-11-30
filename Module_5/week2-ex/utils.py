import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1/(1 + np.exp(-x))


def predict(X, theta):
    pred = np.dot(X, theta)
    y_hat = sigmoid(pred)

    return y_hat


def compute_loss(y_hat, y):
    y_hat = np.clip(
        y_hat, 1e-7, 1 - 1e-7
    )
    return (-y*np.log(y_hat)-(1-y)*np.log(1-y_hat)).mean()


def compute_gradient(X, y, y_hat):
    return np.dot(
        X.T, (y_hat-y)/y.size
    )


def update_theta(theta, gradient, lr):
    return theta - gradient*lr


def compute_accuracy(X, y, theta):
    y_hat = predict(X, theta).round()
    acc = (y == y_hat).mean()

    return acc
