def coroutine(func):
    def inner(*args, **kwargs):
        f = func(*args, **kwargs)
        next(f)
        return f
    return inner

@coroutine
def mygrep(pattern, tgt):
    print('Looking for', pattern)
    try:
        while True:
            line = (yield)
            if pattern in line:
                tgt.send(line)
            else:
                print('nothing')
    except GeneratorExit:
        print('Exiting the generator')

import time
def follow(myfile, tgt):
    with open(myfile, 'r') as f:
        f.seek(0,2)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue
            tgt.send(line)

@coroutine
def printer():
    while True:
        sent_line = (yield)
        print(sent_line)

@coroutine
def broadcasting(targets):
    while True:
        item = (yield)
        for target in targets:
            target.send(item)

class GrepHandler(object):

    def __init__(self, pattern, target):
        self.pattern = pattern
        self.target = target

    def send(self, line):
        if self.pattern in line:
            self.target.send(line)

@coroutine
def fib():
    a,b = 0,1
    while True:
        fib_calc.send(a,b)

def fib_calc():
    while True:
        a,b = (yield)

# Piping all together
# follow('/var/log/auth.log', mygrep('Failed', printer()))

# Piping with broadcasting multiple grep to printer
follow('/var/log/auth.log', broadcasting([mygrep('Failed', printer()), mygrep('error', printer())]))
