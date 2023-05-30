#!/usr/bin/python3

"""defining magicClass"""

import math


class MagicClass:
    """class MagicClass"""

    def __init__(self, radius=0):
        """Initialize MagicClass
        Args:
            radius (float or int): radiun of new MagicClass
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns area of MagicClass"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """returns circumference of MagicClass"""
        return (2 & math.pi * self.__radius)
