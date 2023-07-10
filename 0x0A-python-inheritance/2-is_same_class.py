#!/usr/bin/python3
""" a mod that contains a function if an object is exactly an instance
of a specified class """


def is_same_class(obj, a_class):
    """
    a funtion the checks if an object is an instance
    of a specified class or not.

    args:
        obj: the object to check.
        a_class: the class to check if "obj" is an instance of.
    returns:
        True in case of it is an instance otherwise False.
    """

    return type(obj) == a_class
