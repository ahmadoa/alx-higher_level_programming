#!/usr/bin/python3
def no_c(my_string):
    new_string = ''
    for el in my_string:
        if el != 'c' and el != 'C':
            new_string += el
    return new_string
