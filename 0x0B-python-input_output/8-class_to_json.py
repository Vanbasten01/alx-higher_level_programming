#!/usr/bin/python3
""" a module that contains  "class_to_json" function """


def class_to_json(obj):
    """ a function that returns the dictionary description
    with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object.

    args:
        obj: an instance of a class.

    returns:
        a dictionary representing the object's attributes and their value.
    """
    return obj.__dict__
