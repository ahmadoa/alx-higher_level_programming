#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    mulTUPSUM = 0
    mulSUM = 0

    for tpl in my_list:
        mulTUPSUM += tpl[0] * tpl[1]
        mulSUM += tpl[1]

    return mulTUPSUM / mulSUM
