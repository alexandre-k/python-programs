def count(wrapped):
    def inner(*args, **kwargs):
        inner.counter += 1
        return wrapped(*args, **kwargs)
    inner.counter = 0
    return inner

def timer(wrapped):
    from time import time
    def inner(*args, **kwargs):
        t = time()
        ret = wrapped(*args, **kwargs)
        print(time() - t)
        return ret
    return inner

@count
def myfunc():
    print('myfunc')

@timer
def myotherfunc():
    print('myotherfunc')

