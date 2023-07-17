#!/usr/bin/python3
"""Square Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class which inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializing a Square instance"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """a method that returns the size"""
        return self.width

    @size.setter
    def size(self, value):
        """ a setter method that sets the the size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.width = value
        self.height = value

    def __str__(self):
        """it returns the string representation of an object """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

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
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ amethod that converts the attributtes to a dictionary """
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
