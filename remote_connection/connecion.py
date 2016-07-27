from datetime import datetime

class Machine(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.agent = paramiko.SSHClient()
        self.agent.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect_agent(self, machine):
        print('Establishing SSH connection to {}'.format(machine))
        try:
            self.agent.connect(machine, self.username, self.password)
        except paramiko.ssh_exception as err:
            print('Got this error:', err)
        channel = ssh.invoke_shell()
        print('Interactive SSH connection established')
        stdin = channel.makefile('wb')
        stdout = channel.makefile('rb')
        return stdin, stdout

    def send_cmd(self, stdin, stdout, input_file):
        with open('cmd', 'r') as file:
            stdin.write(input_file)
            stdout.read().decode('utf-8')
        with open(machine + current_date()) as log:
            log


    @staticmethod
    def current_date():
        today = datetime.today()
        return today.strftime('%Y%M%d')

