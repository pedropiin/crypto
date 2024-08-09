from pwn import remote
import json
from deriving_symmetric_keys import decrypt_flag

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