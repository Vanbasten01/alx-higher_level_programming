#!/usr/bin/python3
"""a module that contains 'to_json_string' function"""
import json


def to_json_string(my_obj):
    """ a funtion hat returns the JSON
    representation of an object (string).

    args:
        my_obj: the given object (strin).
    returns:
        the Json representation.
    """
    return json.dumps(my_obj)
