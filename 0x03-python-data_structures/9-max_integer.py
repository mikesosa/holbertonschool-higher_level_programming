#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) is 0:
        return None
    i = len(my_list) - 1
    while i > 1:
        j = 0
        while j < i:
            if my_list[j] > my_list[j + 1]:
                result = my_list[j]
            j += 1
        i -= 1
    return result
