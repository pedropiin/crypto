from Crypto.PublicKey import RSA

def solve():
    with open("./bruce_rsa.pub", "rb") as file:
        data = file.read()
        key = RSA.importKey(data)
        mod = key.n
        print(mod)


if __name__ == '__main__':
    solve()