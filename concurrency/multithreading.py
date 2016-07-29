import threading
import sys
import random

def Splitter(words):
    mylist = words.split()
    newList = []
    while(mylist):
        newList.append(mylist.pop(
            random.randrange(0,(len(mylist)))
            ))
    print(''.join(newList))

if __name__ == "__main__":
    sentence = 'I am doing some test with a random function'
    threadnum = 5
    threadlist = []

    print('Starting....\n')
    sys.stdout.flush()
    for i in range(threadnum):
        t = threading.Thread(target=Splitter, args=(sentence,))
        t.start()
        threadlist.append(t)

    print('\nThread Count: ' +
            str(threading.activeCount()))
    sys.stdout.flush()
    print('Exiting...\n')
