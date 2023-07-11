#!/usr/bin/python3
"""a module that contains "save_to_json_file" function """
import json


def save_to_json_file(my_obj, filename):
    """  a function that writes an Object to a text file,
    using a JSON representation.

    args:
        my_obj: the obj to convert.
        filename: the given filename.
    """
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
