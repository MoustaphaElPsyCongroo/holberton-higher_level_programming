#!/usr/bin/python3
def islower(c):
    "Checks for lowercase character"
    ordc = ord(c)

    if ordc >= 97 and ordc <= 122:
        return True
    return False
