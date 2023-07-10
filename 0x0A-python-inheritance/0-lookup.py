#!/usr/bin/python3
"""lookup function"""


def lookup(obj):
    """
    a function the returns the list of the available
    attributes and methods of an object.

    args:
        obj: the object to get the attributes and methods
        from.
    returns:
        a list of the available attributes and methods.
    """
    return dir(obj)
