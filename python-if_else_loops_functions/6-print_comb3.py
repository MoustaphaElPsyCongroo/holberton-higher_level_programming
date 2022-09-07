#!/usr/bin/python3
for d in range(9):
    for l in range(d + 1, 10):
        if (d == 8):
            print("{}{}".format(d, l))
        else:
            print("{}{},".format(d, l), end=' ')
