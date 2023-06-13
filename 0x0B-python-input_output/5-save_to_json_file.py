#!/usr/bin/python3
"""defining save_to_json_file function"""


def save_to_json_file(my_obj, filename):
    """writes an object to a file
    Args:
        my_obj: object
        filename: name of file
    """
    with open(filename, "w") as jfile:
        json.dump(my_obj, jfile)
