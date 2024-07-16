if __name__ == "__main__":
    # RSA Starter 1
    print(pow(101, 17, 22663))

    # RSA Starter 2
    print(pow(12, 65537, 17 * 23))

    # RSA Starter 3
    p = 857504083339712752489993810777
    q = 1029224947942998075080348647219
    tot_p = p - 1
    tot_q = q - 1
    tot_n = tot_p * tot_q
    print(tot_n)

    # RSA Starter 4
    p = 857504083339712752489993810777
    q = 1029224947942998075080348647219
    e = 65537
    tot_n = (p - 1) * (q - 1)
    d = pow(e, -1, tot_n)
    print(d)

    # RSA Starter 5
    c = 77578995801157823671636298847186723593814843845525223303932
    m = pow(c, d, p * q)
    print(m)