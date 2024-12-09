import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from nltk.tokenize import TweetTokenizer


def sigmoid(x):
    return 1/(1 + np.exp(-x))


def predict(x, theta):
    pred = np.dot(x, theta)
    y_hat = sigmoid(pred)

    return y_hat


def compute_loss(y_hat, y):
    y_hat = np.clip(
        y_hat, 1e-7, 1 - 1e-7
    )
    return (-y*np.log(y_hat)-(1-y)*np.log(1-y_hat)).mean()


def compute_gradient(x, y, y_hat):
    return np.dot(
        x.T, (y_hat-y)/y.size
    )


def update_theta(theta, gradient, lr):
    return theta - gradient*lr


def compute_accuracy(x, y, theta):
    y_hat = predict(x, theta).round()
    acc = (y == y_hat).mean()

    return acc


def text_normalize(text):
    # remove RT
    text = re.sub(r'^RT[\s]+', '', text)

    # remove hyperlink
    text = re.sub(r'http?:\/\/.*[\r\n]*', '', text)

    # remove hastag
    text = re.sub(r'#', '', text)

    tokenizer = TweetTokenizer(
        preserve_case=False,
        strip_handles=True,
        reduce_len=True
    )

    text_tokens = tokenizer.tokenize(text)

    return text_tokens
