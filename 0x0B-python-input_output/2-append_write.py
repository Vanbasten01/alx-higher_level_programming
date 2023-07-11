#!/usr/bin/python3
"""Module contains a append_write function"""


def append_write(filename="", text=""):
    """ a function that appends a string at the end of a text
    file (UTF8) and returns the number of characters added.

    args:
        filename: the file to add in.
        text: the string to append.
    returns:
        number of the characters added.
    """
    with open(filename, "a", encoding="UTF8") as f:
        nwrite = f.write(text)
        return nwrite
