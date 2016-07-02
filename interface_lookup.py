'''
Program to look for the associated IP adddress for each interface
Using ifconfig as a shell command
'''
import re,subprocess

def main():
    print('please, enter a vlan ID or interface name:')
    interface = input()
    interface_lookup(interface)

def interface_lookup(interface):
    ifconfig_list = subprocess.Popen('ifconfig',shell=True,stdout=subprocess.PIPE)
    output_ifconfig = ifconfig_list.stdout.read()
    interface_ip = re.compile(r"(?:\n|^)([a-zA-Z0-9]+)(?::).*?([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})", re.DOTALL)
    result = interface_ip.findall(output_ifconfig.decode('utf-8'))
    for i in range(0,len(result)-1):
        if str(interface) in result[i]:
            print(result[i])

if __name__ == "__main__":
    main()

