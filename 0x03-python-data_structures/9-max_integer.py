#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    else:
        for i in range(len(my_list)):
            if (i == 0):
                largestNum = my_list[i]
                i = i + 1
            if my_list[i] > largestNum and i < len(my_list):
                largestNum = my_list[i]
        return largestNum
