from IPython.core.pylabtools import figsize
import numpy as np
from matplotlib import pyplot as plt
import numpy.random as rd

def generate_input_data(lambda_,pi_, N, K):
    figsize(12.5, 4)

    pi_ = list((pi_ * N).astype(int))
    input_data = np.zeros(0)
    for i in range(K):
        a = rd.poisson(lam=lambda_[i], size=pi_[i])
        input_data = np.r_[input_data, a]

    input_data = rd.permutation(input_data)

    return input_data

if __name__ == '__main__':
    input_data = generate_input_data(N=100)
    print(input_data)