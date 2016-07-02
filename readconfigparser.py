from backports import configparser2

readconfig = configparser2.ConfigParser()
readconfig.read('example.ini')
print(readconfig.sections())
