"""
Implementation of the Extended Euclidean Algorithm (EEA).
INPUT:
n1, n2 = integers to find its gcd and coefficients of 
        Bézout's identity.
OUTPUT:
gcd, u, v = gcd of both numbers and its coefficients.
"""
def extended_euclidean_algorithm(n1, n2):
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    while n2 != 0:
        quoc = n1 // n2
        rem = n1 % n2
        n1 = n2
        n2 = rem
        s0, s1 = s1, s0 - quoc * s1
        t0, t1 = t1, t0 - quoc * t1

    gcd = n1
    u = s0
    v = t0
    return gcd, u, v


"""
Recursive implementation of the euclidean algorithm 
for computing gcd.
"""
def euclidean_algorithm(n1, n2):
    rem = n1 % n2
    if rem == 0:
        return n2
    else: 
        return euclidean_algorithm(n2, rem)


if __name__ == "__main__":
    n1 = 66528
    n2 = 52920
    print(extended_euclidean_algorithm(n1, n2))