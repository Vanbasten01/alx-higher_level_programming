#!/usr/bin/python3
"""
    Base Module
"""

import json


class Base:
    """ the Base class which will be inherited by all other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base object.

        Args:
            id (int, optional)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            it serializes a list of dictionaries to a Json string.

            args:
                list_dictionaries: a list of dictionaries to be serialized.

            Returns:
                a Json string if list_dictionaries is not empty otherwise [].
        """
        return json.dumps(list_dictionaries) if list_dictionaries else "[]"
