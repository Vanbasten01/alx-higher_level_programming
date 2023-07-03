#!/usr/bin/python3
"""This module contains a function that returns the sum of 2 integers"""


def add_integer(a, b=98):
    """adds two integers a and b.i

    Args:
        a (int or float): The first integer.
        b (int or float, optional): The second integer.

    Raises:
        TypeError: When passing an unexpected data type.

    Returns:
        int: The sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
