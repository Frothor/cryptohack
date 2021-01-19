#!/usr/bin/env python3

from binascii import unhexlify

hex_str = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
input_bytes = unhexlify(hex_str)

def xor_with_single_byte(input, key):
    output = b''
    for b in input:
        output += bytes([b ^ key])

    try:
        return output.decode("utf-8")
    except:
        return "meh"

flag = ''
for i in range(256):
    result = xor_with_single_byte(input_bytes, i)
    if "crypto{" in result:
        flag = result
        break
print("FLAG:")
print(flag)