#!/usr/bin/python3
"Append to the end of a file"


def append_write(filename="", text=""):
    "Appends a string at the end of a file"
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
