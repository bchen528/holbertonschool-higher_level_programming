#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is not None:
        new = list(my_list)
        for i in my_list:
            if i % 2 == 0:
                new[i] = True
            else:
                new[i] = False
        return new
