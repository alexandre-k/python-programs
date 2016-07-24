from threading import Thread
from Queue import Queue
from coroutine import coroutine


@coroutine
def threaded(target):
    messages = Queue()
    def run_target():
        while True:
            item = mesages.get()
            if item is GeneratorExit:
                target.close()
                return
            else:
                target.send(item)
    Thread(target=run_target).start()
    try:
        while True:
            item = (yield)
            messages.put(item)
    except GeneratorExit:
        messages.put(GeneratorExit)

if __name__ == '__main__':
    import xml.sax
    from cosax import EventHandler
    from buses import *

    xml.sax.parse('allroutes.xmll', EventHandler(
        buse_to_dicts(
            threaded(
                filter_on_field('route', '22',
                filter_on_field('direction', 'North Bound',
                bus_locations()))
                )
            )
        ))
