from pwn import remote
import json

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
Bob will calculate A^b to get the key with whatever it gets
as a value for A, as long as it thinks its Alice's public value. 
The same goes for Alice: it will calculate B^a with whatever
value for B it gets.
The only way to decrypt the flag is to also have the secret shared
key, but manipulating A or B and passing a modification of either of
these values will always maintain the private values 'a' and/or 'b' 
in the equation, making it impossible for me to calculate the secret key.
Therefore, we can pass the value "0x0" as Alice's public key to Bob and
the same as Bob's public key to Alice, such that they will, respectively,
calculate 0^b = 0^a = 0 = k, making the private key acessible.
"""
def solve():
    r = remote("socket.cryptohack.org", 13371, level="debug")

    # Alice's info
    r.recvuntil(b'Intercepted from Alice: ')
    data = json.loads(r.recvline())
    p = data["p"]
    g = data["g"]
    A = data["A"]

    # Sending to Bob
    r.recvuntil(b'Send to Bob: ')
    r.sendline(json.dumps({"p": p, "g": g, "A": "0x0"}))

    # Bob's info
    r.recvuntil(b'Intercepted from Bob: ')
    data = json.loads(r.recvline())
    B = data["B"]

    #Sending to Alice
    r.recvuntil(b'Send to Alice: ')
    r.sendline(json.dumps({"B": "0x0"}))

    # Final info
    r.recvuntil(b'Intercepted from Alice: ')
    data = json.loads(r.recvline())
    iv = data["iv"]
    ciphertext = data["encrypted_flag"]

    print(decrypt_flag(0, iv, ciphertext))


if __name__ == '__main__':
    solve()