#!/usr/bin/python3
"""
This is the "100-matrix_mul" module.
It supplies one function, matrix_mul(m_a, m_b)
which multiplies two matrices(lists of lists of integers/floats)
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices(lists of lists of integers/floats)"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    list_one = len(m_a)
    if list_one == 0:
        raise ValueError("m_a can't be empty")
    list_two = None
    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
        if list_two is None:
            list_two = len(i)
            if list_two == 0:
                raise ValueError("m_a can't be empty")
        if list_two != len(i):
            raise TypeError("each row of m_a must should be of the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_a should contain only integers or floats")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    list_three = None
    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_b must be a list of lists")
        if list_three is None:
            list_three = len(i)
            if list_three == 0:
                raise ValueError("m_b can't be empty")
        if list_three != len(i):
            raise TypeError("each row of m_b must should be of the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_b should contain only integers or floats")
    if list_two != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    matrix = []
    for i in range(list_one):
        list = []
        for j in range(list_three):
            n = 0
            for k in range(list_two):
                n += m_a[i][k] * m_b[k][j]
            list.append(n)
        matrix.append(list)
    return matrix
