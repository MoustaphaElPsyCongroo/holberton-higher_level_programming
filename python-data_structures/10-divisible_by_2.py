#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = None
    if my_list not in (None, []):
        result = [True if i % 2 == 0 else False for i in my_list]
    return result
