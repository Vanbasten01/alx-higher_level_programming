#!/usr/bin/python3
"""a module that contains 'from_json_string' function"""
import json


def from_json_string(my_str):
    """  a function that returns an object
    (Python data structure) represented by a JSON string.
    args:
        my_str: the given json string.
    returns:
        the Python object.
    """
    return json.loads(my_str)
