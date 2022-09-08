#!/usr/bin/python3
from sys import argv

result = 0

if __name__ == "__main__":
    for i, arg in enumerate(argv):
        if i == 0:
            continue
        result += int(arg)
    print(result)
