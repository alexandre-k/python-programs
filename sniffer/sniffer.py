import socket
import struct
import textwrap

def receive():
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    while True:
        data, addr = sock.recvfrom(65536)
        if not data:
            break
        print('Got some data')
        receiver, sender, proto, = ethernet(data)
        print('Receiver: {}, Sender: {}, Proto: {}'.format(receiver, sender, proto))

def ethernet(data):
    receiver, sender, proto = struct.unpack('>6s 6s H',data[:14])
    # crc = struct('> l', data[:-4])
    print('proto modified:', socket.htons(proto))
    return receiver, sender, proto

#see details
def formatting_mac_addr(bytes_addr):
    bytes_addr = map('{:02x}'.format, bytes_addr)
    return ':'.join(bytes_str).upper()

def main():
    receive()

if __name__ == "__main__":
    main()


