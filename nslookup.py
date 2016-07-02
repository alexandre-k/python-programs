#!/usr/bin/env python
import socket,re

def convert_to_decimal(ip):
    octets = ip.split('.')
    decimal = int(octets[0])*16777216 + int(octets[1])*65536 + int(octets[2])*256 + int(octets[3])
    return decimal

def convert_to_octets(decimal):
    a = int(decimal / 16777216)
    b = int(decimal / 65536) % 256
    c = int(decimal / 256) % 256
    d = int(decimal % 256)
    ip = str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d)
    return ip

def get_fqdn(ip):
    decimal = convert_to_decimal(ip)
    ip_format = convert_to_octets(decimal)
    resolved_ip = socket.gethostbyaddr(ip_format)
    print('===> I got %s for %s\n' %(resolved_ip[0], resolved_ip[2]))


def get_ip(fqdn):
    resolved_name = socket.gethostbyname(fqdn)
    print('===> I got %s for %s\n'  %(resolved_name, fqdn))


def main():
    while True:
        print("Enter an IP address or a DNS name:")
        ip_or_hostname = input()
        isIP = re.compile(r'\d+\.\d+\.\d+\.\d+')
        if isIP.match(ip_or_hostname):
            get_fqdn(ip_or_hostname)
        else:
            get_ip(ip_or_hostname)

if __name__ == '__main__':
    main()
