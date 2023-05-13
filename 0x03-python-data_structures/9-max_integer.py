#!/usr/bin/python3
def max_integer(my_list=[]):
    maxINT = 0
    if len(my_list) == 0:
        return "None"
    else:
        for i in range(len(my_list)):
            if my_list[i] > maxINT:
                maxINT = my_list[i]
        return maxINT
