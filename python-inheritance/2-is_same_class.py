#!/usr/bin/python3
"""
Write a function that returns True if the object is exactly an instance of the
specified class ; otherwise False.

Prototype: def is_same_class(obj, a_class):
You are not allowed to import any module
"""


def is_same_class(obj, a_class):
    "Returns true if the object is exactly an instance of the specified class"
    return type(obj) == a_class
