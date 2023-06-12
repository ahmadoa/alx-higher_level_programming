#!/usr/bin/python3
"""defining class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represents Rectangle"""
    def __init__(self, width, height):
        """ initializes rectangle instance """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """ represents printable format of print"""
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
