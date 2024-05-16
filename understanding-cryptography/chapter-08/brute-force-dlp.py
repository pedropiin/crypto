def brute_force(p, generator, pub_key):
    for i in range(2, p - 1):
        temp = pow(generator, i, p)
        if (temp == pub_key):
            print("The private key x is:", i)
            break

if __name__ == "__main__":
    p = 29
    generator = 2
    pub_key = 28
    brute_force(p, generator, pub_key)
    