#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    new_dict = a_dictionary.copy()
    for key, val in new_dict.items():
        if val == value:
            a_dictionary.pop(key)
    return a_dictionary
