#!/usr/bin/python3
"""Prints a text, adding two newlines after some characters"""


def text_indentation(text):
    """
    Prints a text with 2 newlines after each of these characters: . ? :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    print(text.replace('. ', '.\n\n').replace(
        '? ', '?\n\n').replace(': ', ':\n\n'), end="")
