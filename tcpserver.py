import socket
from struct import pack, unpack


class TCPServer():
    def __init__(self):
        '''
        Create a socket, make it reusable, include IP headers,
        and receive all packages by enabling promiscuous mode
        '''
        self.sock = socket.socket(socket.AF_INET,
                                  socket.SOCK_RAW,
                                  socket.SOCK_STREAM)

        self.sock.setsockopt(socket.SOL_SOCKET,
                             socket.SO_REUSEADDR, 1)

        self.sock.setsockopt(socket.IPPROTO_IP,
                             socket.IP_HDRINCL, 1)

    def bind(self, host, port):
        '''
         Bind the socket to the desired port
        '''
        print('Binding {} to {}'.format(host, port))
        self.sock.bind((host, port))

    def listen(self, socket):
        '''
         Put the socket into listening mode
        '''
        print('The server is now listening')
        socket.listen(5)


    def receive(self):
        conn, addr = self.sock.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(4096)
                if not data: break
                print('\'got some data')
                conn.send(data)
                return data

def main():
    target_host = "45.32.13.245"
    target_port = 9999
    server = TCPServer()
    server.bind(target_host, target_port)

if __name__ == "__main__":
    main()
