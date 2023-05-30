#!/usr/bin/python3
class Square:

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): size of square
        """
        self.__size = size

    def area(self):
        """returns area of square"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """returns size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
