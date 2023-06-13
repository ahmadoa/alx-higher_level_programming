#!/usr/bin/python3
"""defining read_file function"""


def read_file(filename=""):
    """reads the content of a file and prints line by line
    Args:
        filename: filename to read
    """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
