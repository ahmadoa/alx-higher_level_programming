#!/usr/bin/python3
def print_last_digit(number):
    last_digit = number - int(number / 10) * 10
    print("{:d}".format(abs(last_digit)), end="")
    return abs(last_digit)
