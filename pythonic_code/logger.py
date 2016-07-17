def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs)
        )
        return orig_func(*args, **kwargs)
    return wrapper

@my_logger
def display_info(name, age):
    print('My name is {} and I am {} yo'.format(name, age))

display_info(name='alex', age=29)

def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func, t2))
        return result

    return wrapper

@my_logger
@my_timer
def display_info2(name, age):
    print('my name is {}'.format(name))

display_info2(name='alex', age=30)
print(display_info2.__name__)
