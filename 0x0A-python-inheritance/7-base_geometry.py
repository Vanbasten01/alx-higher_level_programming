#!/usr/bin/python3
""" a mod that contains an empty class "BaseGeometry"."""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """a public instance method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ a method that validates an integer.

        args:
            name (str) : the given Name.
            value (int) : the given Value.
        raise:
            TypeError: if "value" is not an int.
            ValueError: if value is less or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
