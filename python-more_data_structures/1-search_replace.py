#!/usr/bin/python3
def search_replace(my_list, search, replace):
    "Replaces all occurences of an element by another in a new list"
    result = []
    if my_list:
        result = [replace if s == search else s for s in my_list]
    return result
