#!/usr/bin/python3

"""
Pascal Triangle module
Contains a function that returns a Pascal Triangle of a given size
"""


def pascal_triangle(n):
    """Returns a list of integers representing a Pascal's triangle"""

    triangle = []
    if n <= 0:
        return triangle

    for i in range(n):
        triangle.append([])
        triangle[i].append(1)
        for j in range(1, i + 1):
            triangle[i].append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        if (i != 0):
            triangle[i].append(1)
    return(triangle)
