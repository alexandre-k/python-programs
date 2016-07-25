class Item(object):

    @property
    def name(self):
        if not hasattr(self, '_name'):
            self._name = ''
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def __init__(self, name='', value=None):
        self.name = name
        self.value = value

    def __str__(self):
        return "{}: {}".format(self.name, self.value)

item1 = Item("sword", 150)
item2 = Item('axe', 100)
print(item1)
print(item2)
