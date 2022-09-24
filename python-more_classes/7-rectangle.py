#!/usr/bin/python3
"Creates a Rectangle class"


class Rectangle:
    "Creates a Rectangle class"
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        "Rectangle constructor"
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        "Rectangle destructor"
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    def __str__(self):
        "String representation of Rectangle"
        height = self.height
        width = self.width
        stri = ""

        for i in range(height):
            for j in range(width):
                if j == width - 1 and i != height - 1:
                    stri += f"{str(self.print_symbol)}\n"
                else:
                    stri += str(self.print_symbol)
        return stri

    def __repr__(self):
        "Formal string representation of Rectangle"
        return f"Rectangle({self.width}, {self.height})"

    @property
    def width(self):
        "Getter for width instance attribute"
        return self.__width

    @width.setter
    def width(self, value):
        "Setter for width instance attribute"
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        "Getter for height instance attribute"
        return self.__height

    @height.setter
    def height(self, value):
        "Setter for width instance attribute"
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        "Gets the Rectangle instance area"
        return self.height * self.width

    def perimeter(self):
        "Get the Rectangle instance perimeter"
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)
