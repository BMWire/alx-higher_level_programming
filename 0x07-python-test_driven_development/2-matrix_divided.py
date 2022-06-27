#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.
It supplies one function, matrix_divided(matrix, div).
"""


def matrix_divided(matrix, div):
    "Return a new matrix"
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix(list of lists) of integers/floats)")
        size = None
    for element in matrix:
        if type(element) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(element)
        elif size != len(element):
            raise TypeError("Each row of the matrix must have the same size")
        for i in element:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in element] for element in matrix]
