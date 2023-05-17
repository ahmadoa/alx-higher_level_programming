#!/usr/bin/python3

def uniq_add(my_list=[]):
    res = 0
    for elm in set(my_list):
        res += elm
    return res
