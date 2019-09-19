#!/usr/bin/python3


def uniq_add(my_list=[]):
    unique_list = []
    for x in my_list:
        if x not in unique_list:
            unique_list.append(x)
    return sum(unique_list)
