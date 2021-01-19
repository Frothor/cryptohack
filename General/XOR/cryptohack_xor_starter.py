#!/usr/bin/env python3
s = "label"
key = 13
flag = "".join(chr(ord(c) ^ key) for c in s)

print("crypto{" + flag + "}")