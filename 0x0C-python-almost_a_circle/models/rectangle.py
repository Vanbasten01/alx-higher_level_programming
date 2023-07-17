#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    """ rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing a Rectangle class which inherits from
        Base class """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Returns: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ the setter method of width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Returns: the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ the setter method of the height of the rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Returns: the  x-coordinate of the rectangle's position.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ the setter method of x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Returns: the y-coordinate of the rectange's position
        """
        return self.__y

    @y.setter
    def y(self, value):
        """ the setter method of y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
            a method that returns the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """ a method that displays the rectangle on the console """
        print("{}".format("\n" * self.__y), end="")
        for i in range(self.__height):
            print("{}{}".format(" " * self.__x, self.__width * "#"), end="")
            print()

    def __str__(self):
        """
            a method that returns the string representaion of
            a rectangle.
        """
        return (
                f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}"
            )

    def update(self, *args, **kwargs):
        """
        a methof that Updates the rectangle's attributes.

        Args:
            *args: The positional arguments that can be used to update id,
                   width, height, x, and y in that order.
            **kwargs: The keyword arguments that can be used to update any
                   attribute by specifying the attribute name.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        a method that converts the rectangle to a dictionary representation.
        """
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x, "y": self.y}
