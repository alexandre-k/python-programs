def fizzbuzz(limit):
    for num in range(1, limit):
        if num % 15 == 0:
            yield 'Fizzbuzz'
        elif num % 3 == 0:
            yield 'Fizz'
        elif num % 5 == 0:
            yield 'Buzz'
        else:
            yield num

for i in fizzbuzz(100):
    print(i)
