from Crypto.PublicKey import RSA

def solve():
    with open("privacy_enhanced_mail.pem", "rb") as file:
        data = file.read()
        key = RSA.importKey(data)
        private_key = key.d
        print(private_key)

if __name__ == '__main__':
    solve()