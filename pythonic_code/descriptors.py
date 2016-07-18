class Circle(object):
    '''
    Problem: the circumference does not change
    >>> mycircle = Circle(2)
    >>> mycircle.circumference
    12.56
    >>> mycircle.radius = 3
    >>> mycircle.circumference
    12.56
    '''
    PI = 3.14
    def __init__(self,radius):
        self.radius = radius
        self.circumference = 2 * radius * self.PI


class Circle2(object):
    PI = 3.14
    def __init__(self, radius):
        self.radius = radius

    @property
    def circumference(self):
        return 2 * self.radius * self.PI

mycircle2 = Circle2(2)
