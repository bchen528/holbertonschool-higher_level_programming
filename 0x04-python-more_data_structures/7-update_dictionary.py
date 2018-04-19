#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    flag = 0
    for oldKey in a_dictionary:
        if oldKey == key:
            a_dictionary[oldKey] = value
            flag = 1
    if flag == 0:
        a_dictionary[key] = value
    return a_dictionary
