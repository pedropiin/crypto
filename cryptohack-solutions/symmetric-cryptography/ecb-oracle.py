from Cryptodome.Cipher import AES
import codecs
import requests
import string

"""
We don't have access to the key. Therefore we can't encrypt the same way as the 
challenge. To have a ECB Oracle, we need to send requests to CryptoHack. This way
we get access to the encryption of any plaintext we wish, without having access
to the key.
"""
def encrypt(plaintext):
    url = "https://aes.cryptohack.org/ecb_oracle/encrypt/"
    r = requests.get(url + plaintext + '/')
    return r.json()["ciphertext"]


"""
Let's represent a byte from our flag as 'X', a filler byte as '0' and a padding byte as 'P'.
First, our encryption is of the form "XXXXXXXXXXXXPPPP"
Suppose we encrypt only adding a single byte '0' to the input. This way, our plaintext will 
be: "0XXXXXXXXXXXXPPP". When encrypted, it will give us a certain ciphertext "????????????????"
If we add another filler byte, it will be of the form: "00XXXXXXXXXXXXPP". 
If we keep adding filler bytes until it surpasses the block size, the amount of padding bytes
will increase so that it completes the next block, e.g.: "00000XXXXXXXXXXX XPPPPPPPPPPPPPPP"
(ECB needs an amount of bytes that is an exact multiple of the block size).
Therefore, when the ammount of bytes of the cyphertext increases, we know that we have a flag
byte in the next block. 
Therefore, we know that the block size is the difference between the original ciphertext size
and the new one, and, in the same way, we get that the flag size is equivalent to the block
size minus the number of filler bytes added.
"""
def get_flag_size():
    count = 1
    initial_len = len(encrypt("00"))

    while True:
        count += 1
        filler_bytes = "00" * count
        it_len = len(encrypt(filler_bytes))
        
        if (it_len != initial_len):
            break

    block_size = (it_len - initial_len) / 2 # Divided by two because one byte == 2 hex chars
    flag_size = initial_len / 2 - count
    num_blocks = (it_len - initial_len) / block_size 
    return flag_size, block_size


"""
We know that block size == 16. Therefore, if we add 15 '0's to the input, the only byte 
remaining in the first block will be the first byte from the flag, i.e.:
"000000000000000X XXXXXXXXXXXXXX...". Now we need to save the ciphertext of the first
block using this method.
If we encrypt the same 15 '0's adding an arbitrary byte at the end, and we try every
single possible byte, eventually we'll find the correct one that gives us the same
ciphertext for the first block as the expected ciphertext, that is, the one with only
the 15 '0's.
Now, we only need to do this process for every single byte of the flag. For this, after
we get the first correct byte, we now only add 14 '0's, and the plaintext will be
"00000000000000KX XXXXXXXXXX...", with 'K' being the correct flag byte. 
This functions does this process iteratively until it gets all the correct bytes of the
flag.
"""
def brute_force():
    flag_size, block_size, num_blocks = get_flag_size()
    alfabet = '_'+'@'+'}'+'{'+string.digits+string.ascii_lowercase+string.ascii_uppercase

    flag = ''
    count = 0;
    while count < flag_size:
        filler_bytes = "0" * (int)((block_size * num_blocks) - 1 - len(flag))
        # Encoding it to 31 bytes, so the only byte remaining in the second block is the first byte from the flag
        expected = encrypt(filler_bytes.encode().hex()) # 03eff7012116b5d36bae4ed4a78a4b23b4d6cad6bb7e0612a52f2ae2cf1758a0fd230d718c90a734d95ba5f40d4673b0e4cca6d439dfcba20c69a03549ffbe7b

        for char in alfabet:
            attempt = filler_bytes + flag + char
            print(attempt)
            it = encrypt(attempt.encode().hex())
            if (it[:64] == expected[:64]):
                flag += char
                break
        
        count += 1
    
    return flag


if __name__ == "__main__":
    print(brute_force())