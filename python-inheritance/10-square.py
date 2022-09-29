#!/usr/bin/python3
"Rectangle class."
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    "Square, inherits from Rectangle"

    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        "Get the square's area"
        return (self.__size * self.__size)
