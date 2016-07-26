from urllib.request import urlopen

class WebPage:
    def __init__(self, url):
        self.url = url
        self._content = None

    @property
    def content(self):
        if not self._content:
            print('Retrieving webpage')
            self._content = urlopen(self.url).read()
        return self._content


class Silly:
    @property
    def silly(self):
        print('you are getting silly')
        return self._silly

    @silly.setter
    def silly(self, value):
        print('You are making silly {}'.format(value))
        self._silly = value

    @silly.deleter
    def silly(self):
        print('Unsetting silly')
        del self._silly

class AverageList(List):
    @property
    def average(self):
        return sum(self) / len(self)


