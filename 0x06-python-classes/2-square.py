#!/usr/bin/python3
"""Defining new class Square"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Initiaizes new square

        Args:
            size (int): size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
