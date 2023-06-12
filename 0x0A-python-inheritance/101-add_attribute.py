#!/usr/bin/python3
"""defining add_attribute module"""


def add_attribute(obj, attr, value):
    """adds new attribute to an object if possible
    Args:
        obj : object where attribute is gon be added
        attr: attribute name
        value: attribute value
    """
    if not hasattr(obj, '__slots__') and not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    if hasattr(obj, '__slots__') and not hasattr(obj, attr):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
