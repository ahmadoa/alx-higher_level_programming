#!/usr/bin/python3
def uppercase(str):
    res = ""
    for c in str:
        if ord(c) <= 122 and ord(c) >= 97:
            res += chr(ord(c) - 32)
        else:
            res += c
    print("{:s}".format(res))
