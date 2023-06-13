#!/usr/bin/python3
"""defining append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file after a search_string is found"""
    lines = []
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            if search_string in lines[i]:
                lines[i:i + 1] = [lines[i], new_string]
                i += 1
            i += 1

    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(lines)
