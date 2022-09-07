#!/usr/bin/python3
def uppercase(str):
    "Prints a string in uppercase"
    strupp = ""

    for c in str:
        ordc = ord(c)
        if ordc in range(97, 123):
            strupp += (chr(ordc - 32))
        else:
            strupp += c
    print("{}".format(strupp))
