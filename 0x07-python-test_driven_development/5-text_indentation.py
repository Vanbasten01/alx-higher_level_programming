#!/usr/bin/python3
"""this module contains a function that prints
a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """
    a function that prints a text with 2 new lines after
    each of these characters: ., ? and :
    args:
        text: the text to be indented

    raises:
        TypeError if text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_str = ""
    for i in text:
        new_str += i
        if i in ".?:":
            print(new_str.lstrip(), end="\n\n")
            new_str = ""
    print(new_str.lstrip(), end="")
