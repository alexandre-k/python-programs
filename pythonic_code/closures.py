def outer_func(msg):
    def inner_func():
        print(msg)

    return inner_func()

hi_func = outer_func('hi')

bye_func = outer_func('bye')

hi_func()
bye_func()