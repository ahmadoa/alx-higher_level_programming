#!/usr/bin/python3
"""Defining text printing function"""


def text_indentation(text):
    """function that prints two lines from a text if char is . or ? or :

    Args:
        text (str): the text

    Raises:
        TypeError: if text is not a string
    """
    index = 0
    if type(text) != str:
        raise TypeError("text must be a string")

    while index < len(text) and text[index] == ' ':
        index++

    while index < len(text):
        print(text[index], end="")
        if text[index] == "\n" or text[index] in ".?:":
            if text[index] in ".?:":
                print("\n")
            index++
            while index < len(text) and text[index] == ' ':
                index++
            continue
        index++
