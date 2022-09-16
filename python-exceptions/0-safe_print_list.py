#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        if x == 0:
            return 0
        for i, e in enumerate(my_list):
            print(e, end='')
            if i == x - 1:
                break
        print("")
        return i + 1
    except ValueError as err:
        print("Error:", err)
