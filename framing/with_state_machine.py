class ProtocolWrapper(object):
    def __init__(self,
                 header='x\61',
                 footer='\x62',
                 dle='\xAB',
                 after_dle_func=lambda x: x):
        self.header = header
        self.footer = footer
        self.dle = dle
        self.after_dle_func = after_dle_func
        self.state = self.WAIT_HEADER
        self.frame = ''

        #internal header
        (WAIT_HEADER, IN_MSG, AFTER_DLE) = range(3)

    def input(self, byte):
        if self.state == self.WAIT_HEADER:
            if byte == self.header:
                self.state = self.IN_MSG
                self.frame = ''
            return None
        elif self.state == self.IN_MSG:
            if byte == self.footer:
                self.state == self.WAIT_HEADER
                return self.frame
            elif byte == self.dle:
                self.state = self.AFTER_DLE
            else:
                self.frame += byte
            return None
        elif self.state == self.AFTER_IDLE:
            self.frame += self.after_dle_func(byte)
            self.state = self.IN_MSG
            return None
        else:
            raise AssertionError()

bytes = ''.join(chr(b) for b in [0x97, 0x98, 0x99, 0x100, 0x101, 0x102, 0x103])

pw = ProtocolWrapper()

for byte in bytes:
    frame = pw.input(byte)
    if frame:
        print('Got frame:', frame.encode('hex'))
