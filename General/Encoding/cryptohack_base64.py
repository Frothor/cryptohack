#!/usr/bin/env python3

import base64

hexStr = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

#decode() used to get rid of printing bytes literals: b'......'
print(base64.b64encode(bytearray.fromhex(hexStr)).decode())