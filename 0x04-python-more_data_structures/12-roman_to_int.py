#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return None

    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    flag = 0
    num = []

    for i in range(len(roman_string)):
        if flag == 1:
            if roman_string[i] == 'I':
                num.append(d['I'] + d['I'])
            elif roman_string[i] == 'V':
                num.append(d['V'] - d['I'])
            elif roman_string[i] == 'X':
                num.append(d['X'] - d['I'])
            elif roman_string[i] == 'L':
                num.append(d['L'] - d['I'])
            elif roman_string[i] == 'C':
                num.append(d['C'] - d['I'])
            elif roman_string[i] == 'D':
                num.append(d['D'] - d['I'])
            elif roman_string[i] == 'M':
                num.append(d['M'] - d['I'])
            flag = 0
        else:
            if roman_string[i] == 'I':
                flag = 1
            elif roman_string[i] == 'V':
                num.append(d['V'])
            elif roman_string[i] == 'X':
                num.append(d['X'])
            elif roman_string[i] == 'L':
                num.append(d['L'])
            elif roman_string[i] == 'C':
                num.append(d['C'])
            elif roman_string[i] == 'D':
                num.append(d['D'])
            elif roman_string[i] == 'M':
                num.append(d['M'])
    return sum(num)
