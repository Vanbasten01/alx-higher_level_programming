#!/usr/bin/python3
"""Add attributes module"""


def add_attribute(obj, name, value):
    """Adds attributes to the given object

    Args:
        obj (object): the given object.
        name (object): the given name.
        value (object): the given object.

    Raises:
        TypeError: if the object can’t have new attribute.
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
