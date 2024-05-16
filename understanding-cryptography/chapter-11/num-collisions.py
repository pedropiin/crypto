import math

def calc_prob(n, prob):
    return pow(2, n / 2) * math.sqrt(math.log(1 / (1 - prob)))

if __name__ == "__main__":
    n = 160
    prob = 0.1
    t = calc_prob(n, prob)
    print("The approximate number of hashes to have a ", prob, " probability of collision with a hash function of output len ", n, " is ", t)