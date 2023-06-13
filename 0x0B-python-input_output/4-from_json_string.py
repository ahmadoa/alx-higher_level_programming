#!/usr/bin/python3
"""defining from_json_string function"""
import json


def from_json_string(my_str):
    """ returns an object represented by a json string
    Args:
        my_str: json string to represent
    Returns: object
    """
    return json.loads(my_str)
