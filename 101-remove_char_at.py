#!/usr/bin/python3
def remove_char_at(str, n):
    strrem = ""
    
    for i in range(len(str)):
        if (i == n):
            continue
        strrem += str[i]

    return strrem
