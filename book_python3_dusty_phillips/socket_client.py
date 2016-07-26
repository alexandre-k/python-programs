import socket

client = socket.socket(AF_INET, SOCK_STREAM)
client.connect(('localhost',80))
print('Received: {0}'.format(client.recv(1024)))
client.close()
