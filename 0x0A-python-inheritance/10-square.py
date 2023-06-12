#!/usr/bin/python3
"""Defining subclass Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ represents Square subclass of Rectangle class"""
    def __init__(self, size):
        """initializes a square
        Args:
            size: size of square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ returns area of square """
        return self.__size ** 2
