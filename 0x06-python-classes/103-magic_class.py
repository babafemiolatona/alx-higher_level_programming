#!/usr/bin/python3
import math
"""Magic Class"""


class MagicClass:
    """Magic Class"""
    def __init__(self, radius):
        """Initializes a new instance of the Magic Class"""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self._MagicClass__radius = radius

    def area(self):
        """Calculates and returns the area of the circle"""
        return math.pi * self._MagicClass__radius ** 2

    def circumference(self):
        """Calculates and returns the circumference of the circle"""
        return 2 * math.pi * self._MagicClass__radius
