import socket
import struct
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '45.32.13.245'
PORT = 80
format = struct.Struct('!I')

def recvall(sock, length):
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('Socket closed')
        data += more
    print(data)
    return data

def get(sock):
    lendata = recvall(sock, format.size)
    print(lendata)
    (length,) = format.unpack(lendata)
    return recvall(sock, length)

def put(sock, message):
    sock.send(format.pack(len(message)) + message)

if 'server' in sys.argv:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    print('listening at {}'.format(s.getsockname()))
    sc, sockname = s.accept()
    print('Accepted connection from {}'.format(sockname))
    sc.shutdown(socket.SHUT_WR)
    while True:
        message = get(sc)
        if not message:
            break
        print('message says: {}'.format(repr(message)))
        sc.close()
        s.close()
elif 'client' in sys.argv:
    s.connect((HOST,PORT))
    s.shutdown(socket.SHUT_RD)
    print(s, 'Beautiful is better than uggly.')
    s.close()

