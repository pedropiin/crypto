from Crypto.Util.number import long_to_bytes

"""
From the "salty.py" file given by the challenge, it's given that the public key 'e' = 1.
The only possible inverse of 1 in any modulus is 1. So, it's trivial that the private
key 'd' = 1 as well. From it, just decrypt it as usual with RSA.
"""
def solve():
    n = 110581795715958566206600392161360212579669637391437097703685154237017351570464767725324182051199901920318211290404777259728923614917211291562555864753005179326101890427669819834642007924406862482343614488768256951616086287044725034412802176312273081322195866046098595306261781788276570920467840172004530873767                                                                  
    e = 1
    ciphertext = 44981230718212183604274785925793145442655465025264554046028251311164494127485

    d = 1
    plaintext = pow(ciphertext, d, n)
    flag = long_to_bytes(plaintext).decode()

    print(flag)


if __name__ == '__main__':
    solve()