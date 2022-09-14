#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    "Computes the square value of all integers of a matrix"
    result = None
    if matrix:
        result = list(list(map(lambda x: x**2, values)) for values in matrix)
    return result
