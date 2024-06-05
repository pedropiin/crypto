import os
import requests

def encrypt_flag():
    url = "https://aes.cryptohack.org/symmetry/encrypt_flag/"
    r = requests.get(url)
    return r.json()["ciphertext"]

def encrypt(plaintext, iv):
    url = f"https://aes.cryptohack.org/symmetry/encrypt/{plaintext}/{iv}/"
    r = requests.get(url)
    return r.json()["ciphertext"]

"""
From the encrypt_flag() function we get a ciphertext of the form:
ciphertext = iv || encrypted
and encrypted is of the form:
(first block): encrypted_i = ek(iv)[i] ^ flag[i]
(general block): encrypted_i = ek(ek(iv)) ^ flag[i]

Therefore, if we can pass the ciphertext as plaintext in the 
encrypt() function, together with the iv received, such that
the ciphertext returned will be:
ciphertext = ek(iv)[i] ^ og_ciphertext[i] = ek(iv)[i] ^ ek(iv)[i] ^ flag[i] = flag[i]
"""
def solve():
    ciphertext = encrypt_flag()
    iv = ciphertext[:32]
    encrypted = ciphertext[32:]

    plaintext = encrypt(encrypted, iv)
    print(bytes.fromhex(plaintext).decode("utf-8"))


if __name__ == "__main__":
    solve()