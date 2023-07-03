#!/usr/bin/python3

"""
Rectangle module
"""


class Rectangle:
    """
    Rectangle class
    """
    pass

    def __init__(self, width=0, height=0):
        """initializing an instance
        args:
            width: the width of the Rectangle
            height: the height of the Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter definition"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter
        args:
            value: the new value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter def"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter
        args:
            value: the new value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
