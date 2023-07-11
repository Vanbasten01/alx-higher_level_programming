#!/usr/bin/python3
""" a module that contains a Student class"""


class Student:
    """ class definition """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ a method retrieves a dictionary representation
        of a Student instance."""
        if isinstance(attrs, list) and all(isinstance(e, str) for e in attrs):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__
