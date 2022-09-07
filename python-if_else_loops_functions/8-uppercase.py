#!/usr/bin/python3
def uppercase(str):
    "Prints a string in uppercase"
    strupp = ""

    for c in str:
        ordc = ord(c)
        if ordc >= 97 and ordc <= 122:
            strupp += (chr(ordc - 32))
        else:
            strupp += c
    print(strupp)
