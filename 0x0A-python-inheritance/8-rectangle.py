#!/usr/bin/python3
"""defining Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ represents Rectangle class which inherits from BaseGeometry"""
    def __init__(self, width, height):
        """initializes Rectangle

        Args:
            width: width of rectangle
            height: width of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
