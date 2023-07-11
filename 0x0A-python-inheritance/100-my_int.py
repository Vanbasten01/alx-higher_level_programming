#!/usr/bin/python3
"""MyInt Module"""


class MyInt(int):
    """Defines a rebel class MyInt."""

    def __init__(self, value: int):
        self.value = value

    def __eq__(self, integer):
        self._validate(integer)
        return not self.value == int(integer)

    def __ne__(self, integer):
        self._validate(integer)
        return not self.value != int(integer)

    def _validate(self, value):
        """Checks if a value is an int.

        Args:
            value (int): the Value to be checked.

        Raises:
            TypeError: If value is not an int or a MyInt instance.
        """
        if not isinstance(value, (int, MyInt)):
            raise TypeError("Can only compare integer or MyInt object types!")
