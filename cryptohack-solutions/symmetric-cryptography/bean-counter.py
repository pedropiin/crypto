import requests

def encrypt():
    url = "https://aes.cryptohack.org/bean_counter/encrypt"
    req = requests.get(url)
    ciphertext = req.json()["encrypted"]
    return ciphertext

def xor(a, b):
    return bytes(x ^ y for x,y in zip(a, b))


"""
Looking at the code given by the challenge, we note that 
the StepUpCounter object is initialized with step_up = False. But
its clear that this values never changes. This way, the 
attribute 'value' will never be changed and, therefore, neither
will the IV during the whole encryption. This means that each block
of the image is only xored with the same keystream every time.

To get this keystream, we can use the fact that the image 
is a PNG, and, therefore, it has a known header. Looking at
the wikipedia page for PNG, we can get the value of the first
16 bytes of the header, and xor it with the first 16 bytes of 
the ciphertext to get the keystream. 

After that, the only thing left to do is to xor the keystream
with each block of the ciphertext, giving us the whole plaintext.
"""
def solve():
    ciphertext = encrypt()

    png_header = bytes.fromhex("89504e470d0a1a0a0000000d49484452")
    bCiphertext = bytes.fromhex(ciphertext)

    keystream_block = xor(png_header, bCiphertext[:16])
    full_keystream = keystream_block * (len(ciphertext) // 16)

    bPlaintext = xor(bCiphertext, full_keystream)

    with open("./flag.png", "wb") as file:
        file.write(bPlaintext)

if __name__ == "__main__":
    solve()