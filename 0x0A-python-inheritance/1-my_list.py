#!/usr/bin/python3
"""this mud contains a class "MyList that inherits from "list" """


class MyList(list):
    """  MyList class """
    def print_sorted(self):
        """a method that prints
        a sorted list.
        """

        print(sorted(self))
