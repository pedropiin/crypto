from Crypto.PublicKey import RSA

def solve():
    with open("./2048b-rsa-example-cert.der", "rb") as file:
        data = file.read()
        key = RSA.importKey(data)
        mod = key.n
        print(mod)


if __name__ == '__main__':
    solve()