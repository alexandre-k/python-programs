import sqlite3
import sys

PATH = sys.path[0]
DB_PATH = PATH + '/db/'

connection = sqlite3.connect(DB_PATH + 'credentials.db')

def get_credentials(username):
    global connection
    with connection:
        cred = connection.execute('select username, password from credentials where username="{}"'.format(username))
        return cred.fetchall()[0]

#username, password = get_credentials('k.alex@fsolution.co.jp')


