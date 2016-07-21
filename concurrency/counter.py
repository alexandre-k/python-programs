def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args)
        next(cr)
        return cr
    return start

@coroutine
def generator_counter():
    count = 10
    while True:
        c = yield count
        count -=1
        if count == 0:
            return

for i in generator_counter():
    print(i)
