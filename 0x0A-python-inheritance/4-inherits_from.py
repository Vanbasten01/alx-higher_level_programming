#!/usr/bin/puthon3
""" a mod that contains a function that checks if
if an object is an instance of a class that inherited
(directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    a function that checks if an obj is an instance of a class
    that inherited from a specified class.

    args:
        obj: the object to check.
        a_class: the class to check if an obj is an instance of.
    returns:
        True otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
