from pwn import remote
import json
import base64

def solve():
    connection = remote("socket.cryptohack.org", 13370, level="debug")

    # Treats the "No leaks" initial message
    connection.recvline().decode()

    # First unknown byte of the flag, because the first 7 are "crypto{"
    idx = 7
    flag = "crypto{"
    # Creating message request
    m = {"msg": "request"}
    while idx < 19:
        used_bytes = set({})
        while len(used_bytes) != 255:
            # Deal with the assertion error
            try: 
                # Sending the request
                connection.sendline(json.dumps(m).encode())

                # Receiving the response
                response_json = json.loads(connection.recvline().decode())
                ciphertext_base64 = response_json["ciphertext"]
                b_ciphertext = base64.b64decode(ciphertext_base64)

                # Add byte that appears in ciphertext to bytes that cannot be in the flag
                used_bytes.add(b_ciphertext[idx])
            except:
                pass
        ord_bytes = sorted(used_bytes)
        for i in range(1, len(ord_bytes)):
            if ord_bytes[i] != (ord_bytes[i - 1] + 1):
                flag += chr(ord_bytes[i] - 1)
        
        idx += 1

    flag += '}'
    print(flag)


if __name__ == '__main__':
    solve()