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

def html_tag(tagged_text):
    def wrapped_text(*args, **kwargs):
        return '<{0}>{1}<{0}/>'.format(args, tagged_text)
    return wrapped_text

@html_tag
def some_html(name, age):
    return 'my name is {0} and my age is {1}'.format(name, age)
