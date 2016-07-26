import socket
import gzip
from io import BytesIO

class GzipSocket:
    def __init__(self, socket):
        self.socket = socket

    def send(self, data):
        buf = BytesIO()
        zipfile = gzip.GzipFile(fileobj=buf, mode='w')
        zipfile.write(data)
        zipfile.close()
        self.socket.send(buf.getvalue())

    def close(self):
        self.socket.close()

class LogSocket:
    def __init__(self, socket):
        self.socket = socket

    def send(self, data):
        print('Sending {0} to {1}'.format(data, self.socket.getpeername()[0]))
        self.socket.send(data)

    def close(self):
        self.socket.close()


def respond(client):
    response = input('Enter a value')
    client.send(bytes(response, 'utf-8'))
    client.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 80))
server.listen(1)
try:
    while True:
        client, addr = server.accept()
        # Without decorator
        # respond(client)
        # With a decorator
        # respond(LogSocket(client))
        if log_send: # checks a hypothetical configuration variable named log_send
            client = LoggingSocket(client)
        if client.getpeername()[0] in compress_hosts: # checks if in list of addresses known
            client = GzipSocket(client)
        respond(client)
finally:
    server.close()
