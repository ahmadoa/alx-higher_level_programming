#!/usr/bin/python3
def print_last_digit(number):
    last_digit = number - int(number / 10) * 10
    print("{:d}".format(last_digit), end="")
    return last_digit
