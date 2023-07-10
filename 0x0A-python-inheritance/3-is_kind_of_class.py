#!/usr/bin/python3
"""a mod that contains a function that checks if an obj is
an instance of, or if the object is an
instance of a class that inherited from.
"""


def is_kind_of_class(obj, a_class):
    """
     a function that checks if an obj is an instance of or if
     it is an instance of a class that inherited from.

     args:
        obj: the object to check.
        a_class: the class to check if the obj is an instance of.

    """

    return isinstance(obj, a_class)
