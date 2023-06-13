#!/usr/bin/python3
"""defining load_from_json_file function"""
import json


def load_from_json_file(filename):
    """loads an object from json file
    Args:
        filename: name of file
    """
    with open(filename, "r") as jfile:
        obj = json.load(jfile)
        return obj
