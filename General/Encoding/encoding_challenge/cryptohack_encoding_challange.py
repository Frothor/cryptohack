from Crypto.Util.number import bytes_to_long, long_to_bytes
from pwn import *
import json
import base64
import codecs

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

received = json_recv()
flagIsPresent =  "flag" in received
while not flagIsPresent:
    decoded = ''
    algo = received["type"]
    encoded = received["encoded"]
    print("Received type: ")
    print(algo)
    print("Received encoded value: ")
    print(encoded)
    if algo == "base64":
        decoded = base64.b64decode(encoded).decode()
    elif algo == "hex":
        decoded = bytearray.fromhex(encoded).decode()
    elif algo == "rot13":
        decoded = codecs.decode(encoded, "rot_13")
    elif algo == "bigint":
        num = int(encoded, 16)
        decoded = long_to_bytes(num).decode()
    elif algo == "utf-8":
        decoded = "".join(chr(o) for o in encoded)

    to_send = {
        "decoded": decoded
    }
    json_send(to_send)

    received = json_recv()
    flagIsPresent =  "flag" in received

print("Here is the FLAG!:")
print(received["flag"])