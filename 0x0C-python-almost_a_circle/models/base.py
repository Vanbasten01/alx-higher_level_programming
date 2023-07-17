#!/usr/bin/python3
"""
    Base Module
"""

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
