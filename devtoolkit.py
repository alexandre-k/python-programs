#Exercise from Python's class Development Toolkit by
#Raymond Hettinger

import math
import doctest

class Circle(object):
    """An advanced circle analytic toolkit
    >>> Circle.version
    '0.1'
    >>> mycircle = Circle(4)
    >>> mycircle.area()
    50.26548245743669
    """


    # Flyweight design pattern suppresses
    # the instance dictionary
    __slots__ = ['diameter']
    version = '0.1'

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        'Perform quadradute on a shape of uniform radius'
        return math.pi * self.radius ** 2.0

    def perimeter(self):
        return 2.0 * math.pi * self.radius

    @classmethod        # alternative constructor
    def from_bbd(cls, bbd):
        'Construct a circle from a bounding box diagonal'
        radius = bbd / 2.0 / math.sqrt(2.0)
        return Circle(radius)

    @staticmethod       # attach function to class
    def angle_to_grade(angle):
        'Convert angle in degree to a percentage angle'
        return math.tan(math.radians(angle)) * 100.0

    @property       # converted dotted access to method calls
    def radius(self):
        'Radius of a circle'
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0
