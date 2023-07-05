#!/usr/bin/python3
"""Defining a locked class
"""


class LockedClass:
    """Locked class that prevents
    the user from dynamically creating
    new instance attributes,
    """
    __slots__ = ("first_name")
