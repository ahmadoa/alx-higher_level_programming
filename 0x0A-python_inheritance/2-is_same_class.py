#!/usr/bin/python3
"""defining is_same_class module"""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a class

    Args:
        obj (any): object to check
        a_class : class to be matched with

    Returns:
        True if object is of a_class type
        False otherwise
    """
    if type(obj) == a_class:
        return True
    return False
