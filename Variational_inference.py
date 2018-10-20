import numpy as np
import numpy.random as rd
import scipy.special as sp


def Variational_inference(x, N, K, cnt):
    x_in = x.reshape(1, N)
    s = np.zeros((K, N))
    eta_ = np.zeros((K, N))
    a = np.random.rand(K, 1)
    b = np.random.rand(K, 1)
    alpha = np.random.rand(K, 1)
    lambda_ = np.random.rand(K, 1)
    pi_ = np.random.rand(K, 1)
    a_i = np.random.rand(K, 1)
    b_i = np.random.rand(K, 1)
    alpha_i = np.random.rand(K, 1)

    # calculate parameter
    for i in range(cnt):
        # calculate eta
        eta_ = np.exp(x_in * (sp.digamma(a) - np.log(b)) - (a / b) + (sp.digamma(alpha) - sp.digamma(np.sum(alpha))))
        if i == 1:
            eta_ = np.random.rand(K, N)
        eta_ = eta_ / np.sum(eta_, axis=0)
        # sampling s
        s = np.identity(K)[list(np.argmax(eta_, axis=0))].T

        # calculate a, b
        a = eta_.dot(x_in.T) + a_i
        b = np.sum(eta_, axis=1).reshape(K, 1) + b_i
        # sampling lambda
        lambda_ = rd.gamma(list(a.T[0]), list((1./b.T[0]))).reshape(K, 1)

        # calculate alpha
        alpha = np.sum(eta_, axis=1).reshape(K, 1) + alpha_i
        # sampling pi
        pi_ = rd.dirichlet(list(alpha.T[0])).reshape(K, 1)

    lambda_ = list(lambda_.T[0])
    pi_ = pi_.T[0]
    print('final lambda:', lambda_)
    print('final pi:', pi_)

    return lambda_, pi_

