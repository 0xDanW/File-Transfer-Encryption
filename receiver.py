import socket
import tqdm
from Crypto.Cipher import AES

key = b"DanielWongYuHeng"
nonce = b"DanielWongIsCool"

cipher = AES.new(key, AES.MODE_EAX, nonce)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen()

client, addr = server.accept()

file_name = client.recv(1024).decode()
print(file_name)
file_size = client.recv(1024).decode()
print(file_size)

file = open()