#!/usr/bin/python3
"""this module contains "load_from_json_file" function. """
import json


def load_from_json_file(filename):
    """ a function that creates an Object from
    a “JSON file”.

    args:
        filename: the Json file to convert.
    """
    with open(filename, "r") as f:
        return json.load(f)
