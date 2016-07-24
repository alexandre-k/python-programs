import cPickel as pickle
from coroutine import *

@coroutine
def sendto(f):
    try:
        while True:
            item = (yield)
            pickle.dump(item, f)
            f.flush()
    except StopIteration:
        f.close()

def recvfrom(f, target):
    try:
        while True:
            item = pickle.load(f)
            target.send(item)
    except EOFError:
        target.close()

if __name__ =="__main__":
    import xml.sax
    from cosax import EventHandler
    from buses import *

    # Parses xml file, send it to a dictionary, then send the dictionary across
    # the pipe
    import subprocess
    p = subprocess.Popen(['python', 'busproc.py'], stdin=subprocess.PIPE)
    xml.sax.parse('allroutes.xml',
            EventHandler(
                buses_to_dicts(
                    sendto(p.stdin)
                    )
                ))

    # In the file busproc.py, we have the rest of the process
    import sys
    from subproc import recvfrom
    from buses import *
    recvfrom(sys.stdin,
            filter_on_field('route', '22'))
