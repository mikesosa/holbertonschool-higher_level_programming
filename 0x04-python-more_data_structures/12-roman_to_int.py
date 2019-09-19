#!/usr/bin/python3
def my_dic(i):
    num_rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for x, y in num_rom.items():
        if i == x:
            return y
    return 0


def roman_to_int(roman_string):
    n = 0
    future = 0
    present = 0

    if roman_string is None:
        return 0
    if len(roman_string) is 1:
        return my_dic(roman_string[0])
    for i in range(0, len(roman_string) - 1):
        present = my_dic(roman_string[i])
        future = my_dic(roman_string[i + 1])
        if present >= future:
            n += present
        elif present < future:
            n -= present
    n += future
    return n
