#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        flag = 1
        largestVal = 0
        largestKey = ""
        for key in a_dictionary:
            if flag == 1:
                largestNum = a_dictionary[key]
                largestKey
                flag = 0
            if a_dictionary[key] > largestNum:
                largestNum = a_dictionary[key]
                largestKey = key
        return largestKey
    else:
        return None
