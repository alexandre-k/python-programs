import socket, sys, re

def tcp_server():
    max_conn = 5
    buffer = 4096

    try:
        print("[+] On which do you wish to start the proxy server? Example: port 80 or 8080")
        port = int(input())
    except KeyboardInterrupt:
        print("\n[+] Program exiting")
        sys.exit()

    try:
        print('[+] Initializing the socket')
        proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('45.32.13.245', port)
        proxy.bind(server_address)
        proxy.listen(max_conn)
        print('[+] Server started on', proxy.getsockname)
    except Exception as e:
        print("\n[+] The program terminated while initializing the socket:", e)
        sys.exit(2)


    while True:
        try:
            client_connection, client_address = proxy.accept()
            data = connection.recv(buffer)
            client_handler = threading.Thread(target=client, args=(data,))
        except KeyboardInterrupt:
            print("\n[+] Proxy server exiting")
            proxy.close()

    return connection,address,data

def client_handler(data):
    try:
        extract_fqdn = re.compile(r'(?:http://)(?P<fqdn>[a-zA-Z0-9-_\.]+/)')
        target_server = extract_fqdn.search(data.split('\n')[0].decode('utf-8'))
        port = 80
        address = socket.gethostbyfqdn(target_server)
        client_netsock = (address, port)
    except Exception as e:
        print('\n[+] Exiting because of an error:', e)

    return netsock



def tcp_client(client_netsock,client_connection,client_address,client_data):
    while True:
        try:
            target = socket.socket(AF_INET, socket.SOCK_STREAM)
            target_conn, target_addr = target.accept()
            target_conn.sendall(client_data)
            target_data = target_conn.recv(buffer)
                print(data)
                if data:
                    client_netsock.send(target_data)
                else:
                    break
        except KeyboardInterrupt:
            print("Closing the connection")
            target_conn.close()

