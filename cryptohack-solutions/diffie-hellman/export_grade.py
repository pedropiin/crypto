from pwn import remote
from json import loads, dumps
from sympy.ntheory import discrete_log

# --- Copied from the challenge "Deriving Symmetric Keys---
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

# --- Solution ---

"""
In this challenge we are just a passive listener in the exchange
of public keys and values. But Alice and Bob first define the 
security parameters that they will both use, and that we can change.
By changing the only avaiable method to Diffie-Hellman with 64 bit keys, 
it makes it really easy to calculate the DLP and get the private values
of both Alice and Bob. After that, we just need to calculate the 
private key and decrypt the flag.
"""
def solve():
    r = remote("socket.cryptohack.org", 13379, level="debug")

    # Receiving DH Formats
    r.recvuntil(b'Intercepted from Alice: ')
    data = loads(r.recvline())

    formats = data["supported"]
    new_formats = []
    new_formats.append(formats[5])

    # Sending formats do Bob
    r.recvuntil(b'Send to Bob: ')
    r.sendline(dumps({"supported": new_formats}))

    # Receiving answer from Bob
    r.recvuntil(b'Intercepted from Bob: ')
    data = loads(r.recvline())

    # Sending answer to Alice
    r.recvuntil(b'Send to Alice: ')
    r.sendline(dumps(data))

    # Alice's info
    r.recvuntil(b'Intercepted from Alice: ')
    data = loads(r.recvuntil(b'}'))
    p = data["p"]
    g = data["g"]
    A = data["A"]

    # Bob's info
    r.recvuntil(b'Intercepted from Bob: ')
    data = loads(r.recvuntil(b'}'))
    B = data["B"]

    # Ciphertext
    r.recvuntil(b'Intercepted from Alice: ')
    data = loads(r.recvuntil(b'}'))
    iv = data["iv"]
    ciphertext = data["encrypted_flag"]

    # Calculating the key and decrypting
    a = discrete_log(int(p, 16), int(A, 16), int(g, 16))
    b = discrete_log(int(p, 16), int(B, 16), int(g, 16))
    k = pow(int(g, 16), a*b, int(p, 16))
    print(decrypt_flag(k, iv, ciphertext))

if __name__ == '__main__':
    solve()