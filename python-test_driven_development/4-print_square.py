#!/usr/bin/python3
"""Prints a square"""


def print_square(size):
    """Prints a square of size <size>"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            if (j < size - 1):
                print("#", end="")
            else:
                print("#")
