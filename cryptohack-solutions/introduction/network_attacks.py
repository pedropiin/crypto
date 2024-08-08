from pwn import remote
import json

def solve():
    r = remote("socket.cryptohack.org", 11112, level="debug")
    
    m = {"buy": "flag"}
    m_packet = json.dumps(m).encode()
    r.sendline(m_packet)

    line = r.readline()
    flag = json.load(line.decode())

    print(flag)


if __name__ == '__main__':
    solve()