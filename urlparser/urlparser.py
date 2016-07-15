class urlParser:
    def __init__(self, url):
        protocol, site = url.split('://')
        self.protocol = protocol
        self.site = site.split('/')
