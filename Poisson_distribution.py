from IPython.core.pylabtools import figsize
import numpy as np
from matplotlib import pyplot as plt
import scipy.stats as stats

def Poisson_distribution(lambda_, pi_, K):
    figsize(12.5, 4)

    poi = stats.poisson
    pi_ = list(pi_)
    a = np.arange(0, 101, 5)
    b = np.zeros(21)

    for k in range(K):
        b += pi_[k] * poi.pmf(a, lambda_[k])

    return a, b

if __name__ == '__main__':
    lambda_ = [1]
    pi_ = np.oens(1)
    x, y = Poisson_distribution(lambda_, pi_, K=1)
