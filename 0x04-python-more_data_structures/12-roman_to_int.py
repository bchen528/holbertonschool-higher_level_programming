#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return None

    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    flag = 0
    sum = 0

    for i in range(len(roman_string)):
        if roman_string[i] == 'I':
            flag = 1
        elif roman_string[i] == 'V':
            sum = sum + d['V']
        elif roman_string[i] == 'X':
            sum = sum + d['X']
        elif roman_string[i] == 'L':
            sum = sum + d['L']
        elif roman_string[i] == 'C':
            sum = sum + d['C']
        elif roman_string[i] == 'D':
            sum = sum + d['D']
        elif roman_string[i] == 'M':
            sum = sum + d['M']

        if flag == 1:
            if roman_string[i] == 'I':
                sum = sum + d['I']
            elif roman_string[i] == 'V':
                sum = sum + d['V'] - d['I']
            elif roman_string[i] == 'X':
                sum = sum + d['X'] - d['I']
            elif roman_string[i] == 'L':
                sum = sum + d['L'] - d['I']
            elif roman_string[i] == 'C':
                sum = sum + d['C'] - d['I']
            elif roman_string[i] == 'D':
                sum = sum + d['D'] - d['I']
            elif roman_string[i] == 'M':
                sum = sum + d['M'] - d['I']
            flag = 0
    return sum
