import sys
import paramiko
from datetime import datetime

class Machine(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.agent = paramiko.SSHClient()
        self.agent.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self, machine):
        print('Establishing SSH connection to {}'.format(machine))
        sys.stdout.flush()
        print(machine, self.username, self.password)
        self.agent.connect(machine, self.username, self.password)

    def create_channel(self, machine):
        self.connect_agent(machine)
        channel = ssh.invoke_shell()
        print('Interactive SSH connection established')
        sys.stdout.flush()
        stdin = channel.makefile('wb')
        stdout = channel.makefile('rb')
        return stdin, stdout

    def send_cmd(self, stdin, stdout, input_file):
        self.invoke_shell(machine)
        with open('cmd', 'r') as file:
            stdin.write(input_file)
            data = stdout.read().decode('utf-8')
        with open(machine + current_date(), 'w') as log:
            log.write(data)

    def list_dir(self, remote_dir):
        sftp = self.agent.open_sftp()
        sftp.chdir(remote_dir)
        for filename in sorted(sftp.listdir()):
            print(filename)

    def retrieve(self, remote_file):
        sftp.get(remote_file, remote_file)





    @staticmethod
    def current_date():
        today = datetime.today()
        return today.strftime('%Y%M%d')

