#!/usr/bin/python3
"""defining class LockedClass"""


class LockedClass:
    """class that let's the user create an instance only if first_name
    attribute is called
    """

    __slots__ = ["first_name"]
