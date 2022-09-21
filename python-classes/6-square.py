#!/usr/bin/python3
"""Defines a Square class with private attributes"""


class Square:
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Square constructor"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for the size property"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size property"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Getter for the position property"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position property"""
        error = 0
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            for i in value:
                if not isinstance(i, int) or i < 0:
                    error = 1
                    raise TypeError(
                        "position must be a tuple of 2 positive integers")
                    break
            if error == 0:
                self.__position = value

    def area(self):
        """Gets the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square"""
        if self.__size == 0:
            print("")
        for p in range(self.__position[1]):
            print("")
        for j in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for i in range(self.__size):
                if i == self.__size - 1:
                    print("#")
                else:
                    print("#", end="")
