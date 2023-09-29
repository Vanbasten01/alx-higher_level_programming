#!/usr/bin/python3
"""a Module that defines "find_peak" function"""


def binary_peak_finder(my_list, left, right):
    """A helper function to find a peak using binary search"""
    if left == right:
        return my_list[left]
    mid = (left + right) // 2
    if my_list[mid + 1] > my_list[mid]:
        return binary_peak_finder(my_list, mid + 1, right)
    else:
        return binary_peak_finder(my_list, left, mid)


def find_peak(list_of_integers):
    """ a function that finds a peak
        in a list of unsorted integers.
    """
    n = len(list_of_integers)
    if n == 0:
        return
    if n == 1:
        return list_of_integers[1]
    return binary_peak_finder(list_of_integers, 0, n - 1)
