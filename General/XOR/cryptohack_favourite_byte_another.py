from binascii import unhexlify,hexlify
cipher='73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'

cipher_bytes=unhexlify(cipher)

for xor_key in range(256):
	decoded=bytes([i^xor_key for i in cipher_bytes]).decode(errors='ignore')
	if decoded.isprintable():
		print(decoded)