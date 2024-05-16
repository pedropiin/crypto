from Crypto.Util import *
from pwn import xor
from binascii import unhexlify

def single_byte_xor(input, key):
    if len(chr(key)) != 1:
        raise "KEY LENGTH EXCEPTION: In single_byte_xor key must be 1 byte long!"

    output = b''
    for b in input:
        output += bytes([b ^ key])

    try:
        return output.decode("utf-8")
    except:
        return "Cannot Decode some bytes"

if __name__ == "__main__":
    hidden_hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
    hidden_bytes = bytes.fromhex(hidden_hex)

    # results = []
    for i in range(256):
        print(f"Brute-force num {i}")
        print("-----")
        # resp = xor(hidden_bytes, i.to_bytes(1))
        # try:
            # results.append(resp.decode("utf-8"))
        # except:
            # results.append("_")
        print(xor(hidden_bytes, i.to_bytes(1)))
        # print("-----")

    # print(xor(b"ydim"))
    # for elem in results:
    #     print(elem)

    # print(xor(b"sncg", 10))
    # print(bytes([115 ^ 10]))
    # print(bytes([110 ^ 10]))
    # print(bytes([99 ^ 10]))
    # print(bytes([103 ^ 10]))
    # sncg
    # 115 