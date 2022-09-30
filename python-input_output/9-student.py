#!/usr/bin/python3
"A Student class"


class Student:
    "Student class"

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        "Gets the dictionary representation of a Student instance"
        return self.__dict__
