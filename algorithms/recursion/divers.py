def double(x):
    if x == 0:
        return x
    return double(x - 1) + 2

print(double(8))

def triangle(x):
    print(x)
    if x == 0:
        return 0
    return triangle(x-1) + x

for n in range(0,20):
    print(triangle(n))
