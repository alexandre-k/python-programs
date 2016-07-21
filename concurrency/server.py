from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from threading import Thread
from concurrent.futures import ProcessPoolExecutor as Pool
from fib import fib

pool = Pool(4)

def fib_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = sock.accept()
        print('Connection from', addr)
        Thread(target=handler, args=(client,), daemon=True).start()

buf = []
def handler(client):
    while True:
        req = client.recv(100)
        if req:
            n = int(req)
            future = pool.submit(fib, n)
            result = future.result()
            # result = fib(n)
            response = str(result).encode('ascii') + b'\n'
            client.send(response)
        else:
            print('Bye')
            break
    print('Closed')

fib_server(('127.0.0.1', 8080))
