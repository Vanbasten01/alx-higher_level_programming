#!/usr/bin/python3
"""square class mod"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ a class that inherits from "Rectangle" """
    def __init__(self, size):
        """intializer
        args:
            size (int) = the width or the height of the square.
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """ a method that returns the area of a square"""
        return self.__size**2

    def __str__(self):
        return f"[Rectangle] {self.__size}/{self.__size}"
