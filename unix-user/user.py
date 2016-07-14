import subprocess
import random
import string
import re


class User(object):

    def __init__(self, username, firstname, lastname, password=None):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.password = password

    def add(self):
        pass

    def remove(self):
        pass

    def gen_pwd(self):
        pwd = list()
        pool_char = string.ascii_letters + string.digits
        for char in (pwd.choice(pool) for i in range(0,13)):
           pwd.append(char)
        return pwd.join(',')

def main():
    with open('db.txt', 'r') as userdb:

        for row in userdb:
            newuser = User(username=row[1],
                           firstname=row[2],
                           lastname=row[3],
                           )

if __name__ == '__main__':
    main()
