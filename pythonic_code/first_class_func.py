def cube(x):
    return x**3

def my_map(func, args):
    result = []
    for i in args:
        result.append(func(i))
    return result

print(my_map(cube, [1,2,3,4,5]))

def cube(x):

    def better_display(msg):
        print(msg, x, ':', x**3)

    return better_display

cubic = cube(3)
cubic('Introducing the result for')

def adding_tag(tag):
    def wrapped_text(text):
        print('<{0}>{1}</{0}>'.format(tag, text))

    return wrapped_text

print_h1 = adding_tag('h1')
print_h1('My first title')


