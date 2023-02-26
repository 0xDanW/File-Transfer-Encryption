from Crypto.Cipher import AES

# 16 bytes for both key and nonce
key = b"DanielWongYuHeng"
nonce = b"DanielWongIsCool"

cipher = AES.new(key, AES.MODE_EAX, nonce)
ciphertext = cipher.encrypt(b"Hello World!")

print(ciphertext)

cipher = AES.new(key, AES.MODE_EAX, nonce)
print(cipher.decrypt(ciphertext))