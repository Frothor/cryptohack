#!/usr/bin/env python3

key1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key1XorKey2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
#key2 = int(key1, 16) ^ int(key1XorKey2, 16)
key2XorKey3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
#key3 = key2 ^ int(key2XorKey3, 16)
flagXorRest = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
flag = int(key1, 16) ^ int(key2XorKey3, 16) ^ int(flagXorRest, 16)

print(bytearray.fromhex(hex(flag)[2::]).decode())