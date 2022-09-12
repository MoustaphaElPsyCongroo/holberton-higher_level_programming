#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for m in matrix:
        print(" ".join("{:d}".format(d) for d in m))
