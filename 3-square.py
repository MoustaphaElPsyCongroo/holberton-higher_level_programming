#!/usr/bin/python3
"""Defines a Square class with private attributes"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Square constructor"""
        self.set_size(size)

    def area(self):
        """Gets the current square area"""
        return self.__size * self.__size

    def set_size(self, size):
        """Setter for the size property"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
