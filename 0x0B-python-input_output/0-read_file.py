#!/usr/bin/python3
"""a Mod that contains a function that reads and print
s the contents of a text file."""


def read_file(filename=""):
    """Reads a text file and prints it out.

    args:
        filename (str): the filename of the text file.

    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
