#!/usr/bin/python3
def roman_to_int(roman_string):
    "Converts a Roman numeral to an integer"
    result = 0
    numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string and isinstance(roman_string, str):
        strlen = len(roman_string)
        for i, s in enumerate(roman_string):
            raw_num = numbers[s]
            if i < strlen - 1 and raw_num < numbers[roman_string[i + 1]]:
                result -= raw_num
            else:
                result += raw_num
    return result
