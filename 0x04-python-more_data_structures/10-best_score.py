#!/usr/bin/python3

def best_score(a_dictionary):
    best = ''
    last_val = 0
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    for key, value in a_dictionary.items():
        if value > last_val:
            last_val = value
            best = key
    return best
