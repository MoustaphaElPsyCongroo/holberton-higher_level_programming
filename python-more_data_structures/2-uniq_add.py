#!/usr/bin/python3
def uniq_add(my_list=[]):
    "Adds all unique integers in a list"
    if my_list:
        return sum(set(my_list))
    return 0
