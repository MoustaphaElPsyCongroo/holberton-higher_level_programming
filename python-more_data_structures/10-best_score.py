#!/usr/bin/python3
def best_score(a_dictionary):
    result = None
    if a_dictionary:
        result = sorted(a_dictionary, key=a_dictionary.get, reverse=True)[0]
    return result
