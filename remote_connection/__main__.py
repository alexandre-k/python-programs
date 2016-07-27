from connection import Machine
from credentials import get_credentials

#targets = ['45.32.13.245']
targets = ['mars.yowassupbro.com']

def main():
    global targets
    username, password = get_credentials('laozi')
    remote_host = Machine(username, password)
    for target in targets:
        remote_host.connect(target)
        # stdin, stdout = remote_host.create_channel(target, input_file)
        # slb.send_cmd(stdin, stdout, input_file)
        remote_host.list_dir('/home/laozi/')

if __name__ == '__main__':
    main()

