import os
import requests
from datetime import datetime, timedelta
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from pwn import xor

def check_admin(cookie, iv):
    url = f"https://aes.cryptohack.org/flipping_cookie/check_admin/{cookie}/{iv}/"
    r = requests.get(url)
    try:
        return r.json()["flag"]
    except:
        return r.json()["error"]

def get_cookie():
    url = "https://aes.cryptohack.org/flipping_cookie/get_cookie/"
    r = requests.get(url)
    return r.json()["cookie"]

def solve():
    cookie = get_cookie()
    iv = cookie[:32]
    encrypted = cookie[32:]
    prefix = b"admin=False;expi"
    new_text = b"admin=True;expi"

    fake_iv = xor(xor(bytes.fromhex(iv), prefix), new_text)
    flag = check_admin(encrypted, fake_iv.hex())

    return flag


if __name__ == "__main__":
    """
    ciphertext = iv || ek(pad(cookie))
        y0 = ek(IV ^ prefix)
        y1 = ek(y0 ^ suffix) = ek((IV ^ prefix) ^ suffix)
    
    plaintext
        x0 = dk(y0) ^ IV = dk(ek(IV ^ prefix)) ^ IV = prefix
        x1 = dk(y1) ^ y0 = dk(ek((IV ^ prefix) ^ suffix) ^ ek(IV ^ prefix) = IV ^ prefix ^ suffix ^ ek(IV ^ prefix)

    Therefore, we only need to use the IV as the following:
    fake_iv = IV ^ prefix ^ admin=True
    ==> x0 = dk(y0) ^ fake_iv = IV ^ prefix ^ fake_iv = IV ^ prefix ^ IV ^ prefix ^ admin=True = admin=True

    """

    flag = solve()
    print(flag)

