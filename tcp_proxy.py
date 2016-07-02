import socket, threading,sys


def tcp_server(local_host, local_port, remote_host, remote_port, receive_first):

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((local_host,local_port))
    except:
        print("Failed to bind ", local_host, " to ", local_port)
        sys.exit(0)

    print("Listening on ", local_host,":", local_port)

    server.listen(5)

    while True:
        try:
            client_socket, addr = server.accept()
            print("Received connection from", addr[0], ":", addr[1])

            proxy_thread = threading.Thread(target=proxy, args=(client_socket, remote_host, remote_port, receive_first))
            proxy_thread.start()
            print("Thread started")
        except KeyboardInterrupt:
            print("interrupted")
            server.close()

def proxy(client_socket, remote_host, remote_port, receive_first):
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    remote_socket.connect((remote_host, remote_port))

    CRLF = "\r\n\r\n"
    remote_socket.send("GET / HTTP/1.0%s \r\n\r\n".encode('utf-8'))

    if receive_first:
        remote_buffer = receive_from(remote_socket)
        print("Remote buffer: ", remote_buffer)

        if len(remote_buffer):
            print("Sending ", len(remote_buffer), "bytes to localhost")
            client_socket.send(remote_buffer)

    while True:
        local_buffer = receive_from(client_socket)

        if len(local_buffer):
            print("Received ", len(local_buffer), "bytes from localhost")
            print("Local buffer: ", local_buffer)

            remote_socket.send(local_buffer)
            print("Sent local_buffer to remote host")

        remote_buffer = receive_from(remote_socket)

        if len(remote_buffer):
            print("Received ", len(remote_buffer), " bytes from remote.")
            print("Remote buffer: ", remote_buffer)

            client_socket.send(remote_buffer)

            print("Sent to localhost")

        if not len(local_buffer):
            client_socket.close()
            remote_socket.close()
            print("no more data")
            break


def receive_from(connection):
    buffer = ""
    connection.settimeout(2)

    try:
        while True:
            data = connection.recv(4096)

            if not data:
                break

            buffer += data

    except:
        pass
    return buffer

def main():
    remote_host = "www.google.com"
    remote_port = 80
    local_host = "127.0.0.1"
    local_port = 8080
    receive_first = True
    tcp_server(local_host,local_port, remote_host, remote_port,receive_first)

if __name__ == "__main__":
    main()
