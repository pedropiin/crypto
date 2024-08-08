def solve():
    base = 12
    expo = 65537
    p = 17
    q = 23
    print(pow(base, expo, p * q))

if __name__ == "__main__":
    solve()