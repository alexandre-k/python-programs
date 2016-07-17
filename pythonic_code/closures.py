def outer_func():
    message = 'Hi'

    def inner_func():
        print(message)

    return inner(func)

outer_func()
