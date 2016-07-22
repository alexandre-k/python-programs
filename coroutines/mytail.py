import time
import os

def follow(somefile):
    with open(somefile, 'r') as tgt_file:
        tgt_file.seek(0,2)
        while True:
            line = tgt_file.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield line

def grep(func):
    def inner(*args, **kwargs):
        with open(args[0], 'r') as tgt_file:
            line = tgt_file.readline()
            if kwargs['search'] in line:
                send(line)
        return func
    return inner
@grep
def file_content(somefile, search=None):
    print(dir(file_content))
    yield line

def mygrep(pattern):
    with open(os.path.join('/var/log/', 'auth.log'), 'r') as tgt_file:
        line = tgt_file.readline()
        print('Looking for', pattern)
        while True:
            line = (yield)
            if pattern in line:
                print(line)


def main():
    # for i in mygrep('failed'):
    #     print(i)
    # for i in file_content(os.path.join('/var/log/', 'auth.log'), search='Failed'):
    #     print(i)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Stopped')
