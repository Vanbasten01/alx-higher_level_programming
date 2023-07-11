#!/usr/bin/python3
"""Module contains a write_file function"""


def write_file(filename="", text=""):
    """ a function that writes a string to a text file (UTF8)
    and returns the number of characters written.

    args:
        filename: the file to write in.
        text: the string to write.
    returns:
        number of the characters written.
    """
    with open(filename, "w", encoding="UTF8") as f:
        nwrite = f.write(text)
        return nwrite
