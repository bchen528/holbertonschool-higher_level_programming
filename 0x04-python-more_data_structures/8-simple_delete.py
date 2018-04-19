#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    flag = 0
    for oldKey in a_dictionary:
        if oldKey == key:
            flag = 1
    if flag == 1:
        del a_dictionary[key]
    return a_dictionary
