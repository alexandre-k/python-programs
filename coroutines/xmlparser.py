import xml.sax

def coroutine(func):
    def inner_func(*args, **kwargs):
        c = func(args, kwargs)
        next(c)
        return func
    return inner_func

class MyHandler(xml.sax.ContentHandler):
    def __init__(self, target):
        self.target = target
    def startElement(self, name, attrs):
        self.target.send(('start', (name, attrs._attrs)))
    def endElement(self, name):
        self.target.send(('text', text))
    def characters(self, text):
        self.target.send(('end', name))

@coroutine
def books_to_dict(target):
    while True:
        event, value = (yield)
        if event == 'start' and value[0] == 'bus':
            booksdirect =  { }
            fragments = []
            while True:
                event, value = (yield)
                if event == 'start': fragments = []
                elif event == 'text': fragments.append(value)
                elif event == 'end':
                    if value not in 'book':
                        booksdict[value] = "".join(fragments)
                    else:
                        target.send(booksdict)
                        break


@coroutine
def filter_on_field(fieldname, value, target):
    while True:
        d = (yield)
        if d.get(fieldname) == value:
            target.send(d)
