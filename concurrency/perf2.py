from socket import socket, AF_INET, SOCK_STREAM
from time import time, sleep

sock = socket(AF_INET, SOCK_STREAM)

sock.connect(('localhost', 8080))

n = 0
from threading import Thread
def monitor():
    global n
    while True:
        sleep(1)
        print(n, 'req/sec')
        n = 0

Thread(target=monitor).start()
while True:
    sock.send(b'1')
    response = sock.recv(100)
    n +=1
