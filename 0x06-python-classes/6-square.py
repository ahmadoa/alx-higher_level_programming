#!/usr/bin/python3
"""Defining new class Square"""


class Square:
    """class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """initializes new square"""
        self.__size = size
        self.__position = position

    @size.setter
    def size(self, value):
        """sets new value for size
        Args:
            value (int): new value of size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def size(self):
        """gets value of size"""
        return self.__size

    @property
    def position(self):
        """gets value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets new value to position"""
        if not all(el >= 0 for el in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns area of square"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints square with the # character"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
