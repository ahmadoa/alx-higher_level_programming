#!/usr/bin/python3
"""defining rectangle class"""


class Rectangle:
    """class Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes new rectangle
        Args:
            width (int): value of width
            height (int): height value of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """returns width value of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets new width value
        Args:
            value (int): new width value
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns height value of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets new height value
        Args:
            value (int): new height value
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns rectangle's area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns rectangle's perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2 + self.__height * 2)

    def __str__(self):
        """returns printable representation of rectangle with #"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        printable = []
        for i in range(self.__height):
            for j in range(self.__width):
                printable.append("#")
            if i != self.__height - 1:
                printable.append("\n")
        return ("".join(printable))
