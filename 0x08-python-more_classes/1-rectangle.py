#!/usr/bin/python3
"""defining class Rectangle"""


class Rectangle:
    """class Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes new rectangle
        Args:
            width (int): width value of rectangle
            height (int): height value of rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """returns value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets new value of width
        Args:
            value (int): new value of width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets new value to height
        Args:
            value (int): new height value
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
