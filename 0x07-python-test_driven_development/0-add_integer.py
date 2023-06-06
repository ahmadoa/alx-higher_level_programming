#!/usr/bin/python3
"""defining an addition function"""


def add_integer(a, b=98):
    """ function that adds 2 integers
    Args:
        a (int): first integer
        b (int): second integer

    Returns:
        Addition result of a & b
    """

    if type(a) != float and type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != float and type(b) != int:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
