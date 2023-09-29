#!/usr/bin/python3
"""a Module that defines "find_peak" function"""


def find_peak(list_of_integers):
    """ a function that finds a peak
        in a list of unsorted integers.
    """
    if not list_of_integers:
        return None
    my_list = list_of_integers[:]
    if len(my_list) == 1:
        return my_list[0]
    if len(my_list) == 2:
        return max(my_list)
    prev = 0
    for index, num in enumerate(my_list):
        if index:
            prev = my_list[index - 1]
        if index < len(my_list) - 1:
            nxt = my_list[index + 1]
        if prev <= num >= nxt:
            return num
