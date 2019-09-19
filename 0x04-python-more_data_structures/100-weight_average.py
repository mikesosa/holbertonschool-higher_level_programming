#!/usr/bin/python3
def weight_average(my_list=[]):
    last = 0
    domminant = 0

    if not my_list:
        return None
    for i in my_list:
        last += i[-1]
    domminant = sum([a * b for a, b in my_list])
    return domminant / last
