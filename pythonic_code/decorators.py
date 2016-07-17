def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

def decorator_function(message):
    def wrapper_function():
        print(message)
    return wrapper_function

hi_func = outer_function('Hi!')
bye_func = outer_function('Bye!')

# def html_tag(tag):
#     def wrapped_text(**kwargs):
#         return '<{0}>{1}<{0}/>'.format(tag, kwargs)
#     return wrapped_text

# @html_tag('h1')
# def some_html(name=None, age=None):
#     return 'my name is {0} and my age is {1}'.format(name, age)

def decorator_func(original_func):
    def wrapper_func(**kwargs):
        print('wrapper executed before: ', original_func.__name__)
        return original_func
    return wrapper_func

class decorator_class(object):
    def __init__(self, original_func):
        self.decorated_func = original_func

    def __call__(self, **kwargs):
        print('wrapper executed before: {}'.format(self.decorated_func.__name__))
        return self.decorated_func(**kwargs)

@decorator_class
def display_info(name=None, age=None):
    print('display_info ran with {}, {}'.format(name, age))

display_info(name='alex', age=29)

