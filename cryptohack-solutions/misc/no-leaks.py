from pwn import remote
import json
import base64

def solve():
    r = remote("socket.cryptohack.org", 13370, level="debug")

    initial_message = r.recvline().decode()
    print("Initial message:", initial_message)

    m = {"msg": "request"}
    m_packet = json.dumps(m).encode()
    r.sendline(m_packet)

    response = r.recvline()
    response_json = json.loads(response.decode())

    # In case of "leaky" ciphertext, the server gives us an error
    while not response_json["ciphertext"]:
        m = {"msg": "request"}
        m_packet = json.dumps(m).encode()
        r.sendline(m_packet)

        response = r.recvline()
        response_json = json.loads(response.decode())

    encoded_ciphertext = response_json["ciphertext"]
    print(encoded_ciphertext)

    b_ciphertext = base64.b64decode(encoded_ciphertext)
    print(b_ciphertext)
    
    inv = b'1' * len(b_ciphertext)
    print(inv)
    b_flag = bytes([a ^ b for a, b in zip(b_ciphertext, inv)])
    flag = b_flag.decode("utf-8")
    print(flag)


if __name__ == '__main__':
    solve()