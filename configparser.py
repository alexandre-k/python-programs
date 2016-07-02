from backports import configparser2

config = configparser2.ConfigParser()
config['Default'] = {'ServerAliveInternal': '45',
                    'Compression': 'yes',
                    'CompressionLevel': '9'}
config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
with open('example.ini', 'w') as myfile:
    config.write(myfile)

