#!/usr/bin/python3
"""
    script that does binary search on an array to find peak
"""


def find_peak(list_of_integers):
    """
    This is finding a peak, any peak. lol why not just use max or sort??
    """
    if list_of_integers is None or len(list_of_integers) is 0:
        return None
    if len(list_of_integers) is 1:
        return list_of_integers[0]
    mid = int(len(list_of_integers) / 2)
    l = list_of_integers[0]
    r = list_of_integers[-1]
    if l > list_of_integers[1]:
        return l
    if r > list_of_integers[-2]:
        return r
    if list_of_integers[mid] < list_of_integers[mid+1]:
        # if mid is less than next then we want to recurse right side
        return find_peak(list_of_integers[mid+1:])
    if list_of_integers[mid] < list_of_integers[mid-1]:
        # if mid is less than the one before
        return find_peak(list_of_integers[:mid])
    # else if mid is bigger than or equal to both then that is a peak
    return list_of_integers[mid]
    """
    MY CODE IS SHIT LMAO
    if len(list_of_integers) >= 3:
        if (list_of_integers[mid-1] < list_of_integers[mid]) and (
                list_of_integers[mid] > list_of_integers[mid+1]):
            return list_of_integers[mid]
        else:
            if l > r:
                # print("WENT LEFT")
                return find_peak(list_of_integers[:mid])
            else:
                # print("WENT RIGHT")
                return find_peak(list_of_integers[mid:])
    elif list_of_integers[0] > list_of_integers[1]:
        # print("THE PIE IS IN")
        return list_of_integers[0]
    else:
        # print("I CAUGHT A POKEMON")
        return list_of_integers[1]
    """
