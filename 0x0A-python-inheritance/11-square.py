#!/usr/bin/python3
"""defining class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represents subclass of Rectangle Square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """returns area of square"""
        return self.__size ** 2

    def __str__(self):
        """ returns square description """
        return str("[Square] {}/{}".format(self.__size, self.__size))
