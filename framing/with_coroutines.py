def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start

@coroutine
def unwrap_protocol(header='\x61',
                    footer='\x62',
                    dle='\xAB',
                    after_dle_func=lambda x: x,
                    target=None):
    while True:
        byte = (yield)
        frame = ''
        if byte == header: #  capture the whole frame
            while True:
                byte = (yield)
                if byte == footer: # accumulate the bytes until a footer is encountered
                    target.send(frame)
                    break
                elif byte == dle:
                    byte = (yield)
                    frame += after_dle_func
                else:
                    frame += byte

@coroutine
def frame_receiver():
    while True:
        frame = (yield)
        print('Got frame:', bytes(frame, 'utf-8'))

def main():
    bytes = ''.join(
            chr(b) for b in [97, 98, 99, 100, 101, 102, 103]
            )
    print(bytes)

    unwrapper = unwrap_protocol(target = frame_receiver())

    for byte in bytes:
        print(byte)
        frame = unwrapper.send(byte)
    print(frame)

if __name__ == "__main__":
    main()
