def solve():
    p = 857504083339712752489993810777
    q = 1029224947942998075080348647219
    tot_n = (p - 1) * (q - 1)
    
    d = pow(e, -1, tot_n)

    c = 77578995801157823671636298847186723593814843845525223303932
    m = pow(c, d, p * q)
    print(m)


if __name__ == '__main__':
    solve()