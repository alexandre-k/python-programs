def mysum(*args):
    result = 0
    if len(args) == 0:
        return
    for n in args:
        print(n)
        result += n
    print(result)

mysum(5,7,8)

