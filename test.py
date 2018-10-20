import numpy as np
from matplotlib import pyplot as plt
from Poisson_distribution import Poisson_distribution
from generate_input_data import generate_input_data
from Gibbs_sampling import Gibbs_sampling
from Variational_inference import Variational_inference

if __name__ == '__main__':
    class_num = int(input('Class Number : '))
    data_num = int(input('Data Number : '))
    cnt_num = int(input('Max Iterator : '))
    lambda_ = []
    for k in range(class_num):
        lambda_ += [int(input('lambda[' + str(k) + ']:'))]
    pi_ = np.zeros(class_num)
    for k in range(class_num):
        pi_[k] = float(input('pi[' + str(k) + ']:'))
    gibbs_ = int(input('Do Gibbs Sampling [Yes:1, No:0] : '))
    variational_ = int(input('Do Variational Inference [Yes:1, No:0] : '))

    o_x, o_y = Poisson_distribution(lambda_, pi_, K=class_num)
    fig = plt.figure()
    plt.bar(o_x, o_y, alpha=0.6, width=4.5, lw="3")
    plt.xticks(o_x + 5.4, o_x)
    plt.ylabel("Probability of $k$")
    plt.xlabel("$k$")
    plt.title("Probability mass function of a Original Poisson random variable")
    # plt.savefig("Original_Poisson.png")
    plt.show()

    x_in = generate_input_data(lambda_, pi_, data_num, class_num)
    print(x_in.shape)
    fig = plt.figure()
    plt.hist(x_in, bins=20, range=(0, 100))
    plt.title('Probability mass function of a Sampling Poisson random variable')
    plt.xlabel('x')
    plt.ylabel('freq')
    # plt.savefig("Sampling_Poisson.png")
    plt.show()

    if gibbs_:
        s_lambda_, s_pi_ = Gibbs_sampling(x_in, N=data_num, K=class_num, cnt=cnt_num)
        s_x, s_y = Poisson_distribution(s_lambda_, s_pi_, K=class_num)
        fig = plt.figure()
        plt.bar(s_x, s_y, alpha=0.6, width=4.5, lw="3")
        plt.xticks(s_x + 5.4, s_x)
        plt.ylabel("Probability of $k$")
        plt.xlabel("$k$")
        plt.title("Probability mass function of a Gibbs Sampling Poisson random variable")
        # plt.savefig("Gibbs_Sampling_Poisson.png")
        plt.show()

    if variational_:
        v_lambda_, v_pi_ = Variational_inference(x_in, N=data_num, K=class_num, cnt=cnt_num)
        v_x, v_y = Poisson_distribution(v_lambda_, v_pi_, K=class_num)
        fig = plt.figure()
        plt.bar(v_x, v_y, alpha=0.6, width=4.5, lw="3")
        plt.xticks(v_x + 5.4, v_x)
        plt.ylabel("Probability of $k$")
        plt.xlabel("$k$")
        plt.title("Probability mass function of a Variational Inference Poisson random variable")
        # plt.savefig("Variational_Inference_Poisson.png")
        plt.show()