import numpy as np


def compute_probability(X, w):
    z_function = np.dot(X, w)
    probability = 1. / (1 + np.exp(z_function))
    return probability