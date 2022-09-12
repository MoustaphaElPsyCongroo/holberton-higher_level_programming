#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_cp = my_list.copy()
    if idx in range(len(my_list)):
        list_cp[idx] = element
    return list_cp
