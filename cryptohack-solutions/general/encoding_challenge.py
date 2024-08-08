from pwn import remote
import json
import base64
import codecs
import Cryptodome.Util.number as crypto

def solve():
    r = remote("socket.cryptohack.org", 13377, level="debug")

    count_stages = 0
    while (count_stages < 100):
        line = r.recvline()
        level = json.loads(line.decode())

        print("encoding received: ")
        print(level)
        
        if level["type"] == "base64":
            answer = base64.b64decode(level["encoded"]).decode()
        elif level["type"] == "hex":
            answer = bytes.fromhex(level["encoded"]).decode()
        elif level["type"] == "rot13":
            answer = codecs.decode(level["encoded"], 'rot_13')
        elif level["type"] == "bigint":
            answer = crypto.long_to_bytes(int(level["encoded"], 16)).decode()
        elif level["type"] == "utf-8":
            answer = "".join([chr(b) for b in level["encoded"]])

        print("decoded answer: ")
        print(answer)

        answer_packet = {"decoded": answer}
        request = json.dumps(answer_packet).encode()
        r.sendline(request)
        count_stages += 1

    req_flag = r.recvline()
    flag = json.loads(req_flag.decode())
    print(flag["flag"])

if __name__ == '__main__':
    solve()