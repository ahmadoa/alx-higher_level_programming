#!/usr/bin/python3
"""Defining a string printing function"""


def say_my_name(first_name, last_name=""):
    """function that prints a string

    Args:
        first_name (str): first name
        last_name (str): last name

    Raises:
        TypeError: if first_name or last_name is not a string
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
