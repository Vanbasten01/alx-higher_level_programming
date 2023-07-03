#!/usr/bin/python3
"""this module contains a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """a function that divides all elments
    of a matrix.

     Args:
        matrix (list[list[int/float]]): list of list for integer or float.
        div (int/float): an integer or float as divider.

    Raises:
        TypeError: if the list is not a list of list of integer or float.
        TypeError: if each row of the matrix doesn't have the same size.
        TypeError: if the div not a number.
        ZeroDivisionError: if div is a 0.

    Returns:
        (list[list]): a matrix with same size of the given matrix.
    """

    if not isinstance(matrix, list) or not all\
    (isinstance(inner, list) for inner in matrix):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    row_size = len(matrix[0])
    for inner in matrix:
        if any(not isinstance(e, (int, float)) for e in inner):
            raise TypeError(
                    "matrix must be a matrix (\
                            list of lists) of integers/floats")
        if row_size != len(inner):
            raise TypeError(
                    "Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i/div, 2) for i in row] for row in matrix]
