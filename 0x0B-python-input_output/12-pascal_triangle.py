#!/usr/bin/python3
"""Pascal's Triangle Module"""


def pascal_triangle(n: int):
    """Returns a list of lists of numbers representing the Pascal's triangle.

    Args:
        n (int): number of rows.

    Return:
        [] if n <= 0 otherwise
        list of lists of numbers.

    """
    if n <= 0:
        return []

    triangles = [[1]]
    for _ in range(1, n):
        row = triangles[-1]
        curr = [1]
        curr.extend(row[i] + row[i + 1] for i in range(len(row) - 1))
        curr.append(1)
        triangles.append(curr)

    return triangles
