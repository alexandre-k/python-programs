from scapy.all import *

class Scanner(object):

    def __init__(self, dest):
        self.dest = dest

    def syn(self):
        syn = IP(src='45.32.13.245', dst=self.dest)/TCP(flags='S')
        synack = sr1(syn)


