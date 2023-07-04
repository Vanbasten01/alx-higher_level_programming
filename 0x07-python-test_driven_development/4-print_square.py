#!/usr/bin/python3
"""this module contains a function that prints a square
with the character "#"
"""


def print_square(size):
    """
    a function that prints a square
    with the character "#"
    args:
        size: the size of length of the square.

    raises:
        TypeError if the size is not an integer.
        ValueError if size is less than 0.

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
