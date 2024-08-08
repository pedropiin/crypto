from Cryptodome.Cipher import AES
import hashlib

"""
Function from the exercise that decrypts the ciphertext with AES 
given a certain key
"""
def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}


"""
Brute-forcing AES with all the possible words as keys.
Note that the key is a hash of a random word obtained in
'/usr/share/dict/words'. Therefore, we have a 'small'
sample space of keys to check.
"""
def brute_force(ciphertext, words):
    for w in words:
        test_key = hashlib.md5(w.encode()).hexdigest()
        plaintext = decrypt(ciphertext, test_key)

        try:
            ascii_pt = bytearray.fromhex(plaintext["plaintext"]).decode()
            if ("crypto" in ascii_pt):
                print(ascii_pt)
        except:
            continue
        
if __name__ == "__main__":
    # Ciphertext given by the challenge
    ciphertext = "c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"
    
    # List of words used in the challenge to derive the key
    with open("/usr/share/dict/words") as f:
        words = [w.strip() for w in f.readlines()]

    brute_force(ciphertext, words)

