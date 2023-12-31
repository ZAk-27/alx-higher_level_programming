#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    if (isinstance(roman_string, str)) is False:
        return 0

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
    nextR = ""
    num = 0
    for i in range(len(roman_string)):
        if roman_string[i] in roman.keys():
            key = roman_string[i]
            if i < len(roman_string) - 1:
                nextR = roman_string[i + 1]
            if i == len(roman_string) - 1:
                num += roman[key]
            elif roman[key] < roman[nextR]:
                num -= roman[key]
            else:
                num += roman[key]
    return num
