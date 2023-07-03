#!/usr/bin/python3

"""
Rectangle module
"""


class Rectangle:
    """
    Rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            else:
                return rect_2

    def __init__(self, width=0, height=0):
        """initializing an instance
        args:
            width: the width of the Rectangle
            height: the height of the Rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """returns the Rectangle's area"""
        return self.__width * self.__height

    def perimeter(self):
        """ returns the Rectangle's perimetre"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """it prints the rectangle with the character '#' """
        strr = ""
        if self.__height == 0 or self.__width == 0:
            return strr
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    strr += str(self.print_symbol)
                if i < self.height - 1:
                    strr += "\n"
            return strr

    def __repr__(self):
        """representation of Rectangle"""
        return "Rectangle""({}, {})".format(self.width, self.height)

    def __del__(self):
        """ it prints a message when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
