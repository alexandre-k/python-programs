from socket import socket, AF_INET, SOCK_STREAM
from time import time

sock = socket(AF_INET, SOCK_STREAM)

sock.connect(('localhost', 8080))

while True:
    start = time()
    sock.send(b'20')
    response = sock.recv(100)
    end = time()
    print(end-start)
