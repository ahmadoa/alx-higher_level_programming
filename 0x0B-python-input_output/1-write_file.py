#!/usr/bin/python3
"""defining write_file function"""


def write_file(filename="", text=""):
    """ writes a string to a file and returns number of chars written
    Args:
        filename: file name
        text: text to write to file
    Returns: number of chars written
    """
    with open(filename, "w", encoding="utf-8") as file:
        return (file.write(text))
