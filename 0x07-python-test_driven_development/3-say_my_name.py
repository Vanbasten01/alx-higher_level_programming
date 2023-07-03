#!/usr/bin/python3
"""this module contains a function
that prints 'My name is <first name> <last name>'
"""


def say_my_name(first_name, last_name=""):
    """a function that prints
    'My name is <first name> <last name>'

    args:
        first_name: the first_name of the person.
        last_name: the last name of the person.
    raise:
        TypeError: in case we are passing a different
        data type than str as argument.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
