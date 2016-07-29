import threading
import time
import random
import queue as Queue

class Producer:
    def __init__(self):
        self.food = ['ham', 'soup', 'salad']
        self.nextTime = 0

    def run(self):
        global q
        while (time.clock() < 10): #while less than 10 sec
            if (self.nextTime < time.clock()): # if threshold passed
                f = self.food[random.randrange( #randomly get a food
                    len(self.food)
                    )]
                q.put(f) # we put this food in the queue
                print('Adding' + f)
                self.nextTime += random.random() # generates a number between 0 and 1

class Consumer:
    def __init__(self):
        self.nextTime = 0
    def run(self):
        global q
        while (time.clock < 10):
            if (self.nextTime < time.clock() and not q.empty()): # if threshold passed and queue not empty
                f = q.get()
                print('Removing ' + f)
                self.nextTime += random.random() * 2

if __name__ == "__main__":
    q = Queue.Queue(10)
    p = Producer()
    c = Consumer()
    pt = threading.Thread(target=p.run, args=())
    ct = threading.Thread(target=c.run, args=())
    pt.start()
    ct.start()
