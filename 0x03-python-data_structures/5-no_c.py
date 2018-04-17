#!/usr/bin/python3
def no_c(my_string):
    s = ""
    copy = list(my_string)
    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            del copy[i]
    return s.join(copy)
