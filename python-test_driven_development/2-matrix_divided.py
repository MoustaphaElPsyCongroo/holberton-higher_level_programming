#!/usr/bin/python3
"""Divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix
    params:
        matrix: A list of lists of integers or floats
        div: The number to divide each elements of the matrix to

    returns: A new matrix with all elements divided
    """
    firstLen = 0
    result = []

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for i, li in enumerate(matrix):
        inner = []
        if not isinstance(li, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if i == 0:
            firstLen += len(li)
        if firstLen != len(li):
            raise TypeError("Each row of the matrix must have the same size")
        for elem in li:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be\
 a matrix (list of lists) of integers/floats")
            inner.append(round(elem / div, 2))
        result.append(inner)
    return result
