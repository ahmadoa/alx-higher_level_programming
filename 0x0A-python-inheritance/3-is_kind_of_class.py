#!/usr/bin/python3
"""defining is_kind_of_class module"""


def is_kind_of_class(obj, a_class):
    """checks if an object is an instance or subclass of a class

    Args:
        obj (any): object
        a_class : class

    Returns:
        True if obj is an instance or is a subclass of a_class
        False otherwise
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
