from Cryptodome.Cipher import AES
import requests

def encrypt():
    url = "https://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/"
    req = requests.get(url)
    ciphertext = req.json()["ciphertext"]
    return ciphertext


def decrypt(ciphertext):
    url = "https://aes.cryptohack.org/ecbcbcwtf/decrypt/"
    req = requests.get(url + ciphertext + '/')
    plaintext = req.json()["plaintext"]
    return plaintext

"""
Let's call: the ith block of plaintext xi,
            the ith block of ciphertext yi,
            the initialization vector iv,
            the ith block of ECB decrypted ciphertext bi,
            the encryption function ek(),
            the decryption function dk().

We know that y1 = ek(x1 xor iv),
            y2 = ek(x2 xor y1) = ek(x2 xor (x1 xor iv))
            y3 = ek(x3 xor y2) = ek(x3 xor (x2 xor (x1 xor iv)))

In the same way: b1 = dk(y1) = dk(ek(x1 xor iv)) = x1 xor iv
                b2 = dk(y2) = dk(ek(x2 xor y1)) = x2 xor y1 = x2 xor (x1 xor iv)
                b3 = dk(y3) = dk(ek(x3 xor y2)) = x3 xor y2 = x3 xor (x2 xor (x1 xor iv))

Therefore, we can easily get the plaintext through:
    b2 xor y1 = (x2 xor y1) xor y1 = x2 xor (y1 xor y1) = x2 xor 0 = x2
    b3 xor y2 = (x3 xor y2) xor y2 = ... = x3
"""
def solve():
    # Encrypted with CBC
    ciphertext = encrypt()

    y1 = ciphertext[:32]       # First block of ciphertext
    y2 = ciphertext[32:64]     # Second block of ciphertext
    y3 = ciphertext[64:]       # Third block of ciphertext

    # Decrypted with EBC 
    decrypted = decrypt(ciphertext)

    b1 = decrypted[:32]        # First block of 16 bytes of decrypted ciphertext
    b2 = decrypted[32:64]      # Second block of 16 bytes of decrypted ciphertext
    b3 = decrypted[64:]        # Third block of 16 bytes of decrypted ciphertext

    x2 = hex(int(b2, 16) ^ int(y1, 16))
    x3 = hex(int(b3, 16) ^ int(y2, 16))

    x2_ascii = bytearray.fromhex(x2[2:]).decode()
    x3_ascii = bytearray.fromhex(x3[2:]).decode()

    flag = x2_ascii + x3_ascii
    return flag

if __name__ == "__main__":
    flag = solve()
    print(flag)