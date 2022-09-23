#!/usr/bin/python3
"""Prints a text, adding two newlines after some characters"""


def text_indentation(text):
    """
    Prints a text with 2 newlines after each of these characters: . ? :
    There should be no space at the beginning or end of each printed line
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    print(" ".join(text.split()).replace('.', '.\n\n').replace(
        '?', '?\n\n').replace(':', ':\n\n').replace("\n ", "\n"), end="")
