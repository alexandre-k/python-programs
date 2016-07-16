def classic_fib(limit):
    nums = []
    current, nxt = 0,1

    while nxt < limit:
        current, nxt = nxt, nxt + current
        nums.append(current)

    return nums

def gen_fib():
    current, nxt = 0,1
    while True:
        current, nxt = nxt, current+nxt
        yield current

def even_fibonacci():
    for n in gen_fib():
        if n % 2 == 0:
            yield n

def composed_generators():
    for e in even_fibonacci():
        if e % 3 == 0:
            yield e
def main():
    print('Classic Fibonacci')
    for i in classic_fib(100000000000):
        print(i, end=', ')

    print('\n#################################\n')
    print('With generator')
    for i in composed_generators():
        print(i, end=', ')
        if i > 10000000000000000000000000000000000000000000000000:
            print('\n')
            break

if __name__ == "__main__":
    main()
