#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    multi_dict = {}
    for key, val in a_dictionary.items():
        multi_dict.update({key: val * 2})
    return multi_dict
