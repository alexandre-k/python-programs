import os
import fnmatch
import re

def countdown(n):
    if n > 0:
        print('Counting down from', n)
        yield n
        yield from countdown(n - 1)
    return


def fizzbuzz(n,p):
    if n < p+1:
        if n % 3 == 0:
            print('Fizz')
        if n % 5 == 0:
            print('Buzz')
        if n % 15 == 0:
            print('FizzBuzz')
        else:
            print(n)
        increment = lambda n: n+1
        yield from fizzbuzz(increment, p)
    return

def check_bsdinstall_log(filename):
    with open(os.path.join('/var/log/') + filename, 'r') as logfile:
        setting_column = (line.rstrip(':').split() for line in logfile if 'zfs' in line)
        zfs_setting = (' '.join(setup[2:]) for setup in setting_column if 'zfs' in setup)
        for line in zfs_setting:
            print(line)

# check_bsdinstall_log('bsdinstall_log')

def walking_dir(somedir):
    dircontent = (filelist for path, dirlist, filelist in os.walk(somedir))
    for info in dircontent:
        print(info)
# walking_dir('/usr/home/laozi/python-programs')

def find(somefile):
    for path, dirlist, filelist in os.walk('/usr/home/laozi'):
        for name in fnmatch.filter(filelist, somefile):
            yield os.path.join(path, name)

def grep(pattern, somefile):
    searchfor = re.compile(r'{}'.format(pattern))
    for line in somefile:
        yield line
