def find_factors(n):
    if (n % 2):
        step = 2
    else:
        step = 1
    factors = []
    for i in range(1, int(n * 0.5) + 1, step):
        if (n % i == 0):
            factors.append(i)

    return factors

def find_primitives(mod):
    primitives = []
    factors = find_factors(mod - 1)
    prim = True

    for i in range(1, mod):
        for j in factors:
            temp = pow(i, j, mod)
            if (temp == 1):
                prim = False
                break
        if (prim):
            primitives.append(i)
        prim = True
    
    return primitives

if __name__ == "__main__":
    mod = 24691
    primitives = find_primitives(mod)
    print(primitives)
