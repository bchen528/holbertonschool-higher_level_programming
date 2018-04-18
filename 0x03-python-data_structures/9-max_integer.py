#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    for i in range(len(my_list)):
        if i == 0:
            largestNum = my_list[i]
            i = i + 1
        if i < len(my_list) and my_list[i] > largestNum:
            largestNum = my_list[i]
    return largestNum
