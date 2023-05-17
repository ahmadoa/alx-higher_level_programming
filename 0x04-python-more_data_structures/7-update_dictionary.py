#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    dict_copy = a_dictionary.copy()
    dict_copy.update({key: value})
    return dict_copy
