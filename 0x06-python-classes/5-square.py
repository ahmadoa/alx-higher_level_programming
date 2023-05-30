#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        """Initializes new square
        Args:
            size (int): size of square
        """
        self.__size == size

    @property
    def size(self):
        """returns size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets new value to size
        Args:
            value (int): new size value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must >= 0")
        self.__size = value

    def area(self):
        """returns area of square"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints area with character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(size + 1):
                for j in range(size + 1):
                    print("#")
                print()
