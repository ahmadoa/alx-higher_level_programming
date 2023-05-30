#!/usr/bin/python3
"""Defining new class Square"""


class Square:
    """class Square
    Attributes:
        __size (int): size of square
        __position (tuple): position of square in 2df space
    """

    def __init__(self, size=0, position=(0, 0)):
        """initializes new square
        Args:
            size (int): size of new square
            position (tuple): position of new square
        """
        self.size = size
        self.position = position

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): size of a side of square
        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def size(self):
        """gets value of size"""
        return self.__size

    @property
    def position(self):
        """gets value of position
        Returns:
            The position of the square in 2d space
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter of __position
        Args:
            value (tuple): position of the square
        Returns:
            None
        """
        if (not all(el >= 0 for el in value) or
                len(value) != 2 or
                not isinstance(value, tuple) or
                not all(isinstance(el, int) for el in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns area of square
        Returns
            The area of the square
        """
        return (self.__size * self.__size)

    def my_print(self):
        """prints square with the # character"""
        if self.__size == 0:
            print()
            return

        for i in range(0, self.__position[1]):
            print()
        for j in range(self.__size):
            print("".join([" " for k in range(self.__position[0])]), end="")
            print("".join(["#" for z in range(self.__size)]))
