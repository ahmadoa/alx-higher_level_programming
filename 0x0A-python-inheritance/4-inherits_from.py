#!/usr/bin/python3
"""defining inherits_from module"""


def inherits_from(obj, a_class):
    """checks if an object is an instance of a class that inherited from
    a specified class

    Args:
        obj (any): object
        a_class: class to compare to

    Returns:
        True if obj is an instance of a_class
        False otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
