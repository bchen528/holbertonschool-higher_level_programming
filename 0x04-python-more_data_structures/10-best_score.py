#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    flag = 1
    for key in a_dictionary:
        if flag == 1:
            largestVal = a_dictionary[key]
            largestKey = key
            flag = 0
        if a_dictionary[key] > largestVal:
            largestVal = a_dictionary[key]
            largestKey = key
    return largestKey
