if __name__ == "__main__":
    mod = 53
    primitives = []
    for i in range(1, mod):
        for j in range(1, mod):
            temp = pow(i, j, mod)
            if (temp == 1):
                if (j != (mod - 1)):
                    break
                else:
                    primitives.append(i)
    print(primitives)
