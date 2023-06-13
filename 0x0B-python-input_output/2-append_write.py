#!/usr/bin/python3
"""defining append_write function"""


def append_write(filename="", text=""):
    """adds string to already existing file
    Args:
        filename: file name
        text: text to add to file
    Returns: number of chars added
    """
    with open(filename, "a", encoding="utf-8") as file:
        return (file.write(text))
