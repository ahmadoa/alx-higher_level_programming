#!/usr/bin/python3
"""
lookup - returns list of attributes and methods of an object
@obj: object
Return: a list of attributes and methods
"""


def lookup(obj):
    """lookup function"""
    return dir(obj)
