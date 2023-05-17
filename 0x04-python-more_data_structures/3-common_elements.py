#!/usr/bin/python3

def common_elements(set_1, set_2):
    common = []
    for elmi in set_1:
        for elmj in set_2:
            if elmi == elmj:
                common.append(elmi)
    return common
