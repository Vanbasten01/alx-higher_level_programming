#!/usr/bin/python3
"""this module contains "append_after" function """


def append_after(filename="", search_string="", new_string=""):
    """ a function that inserts a line of text to a file,
    after each line containing a specific string.

    args:
        filename: the given file name.
        search_string: the specific string.
        new_string: the new added string.

    """
    with open(filename, "r+") as f:
        string = ""
        for line in f:
            string += line
            if search_string in line:
                string += new_string
        f.seek(0)
        f.write(string)
