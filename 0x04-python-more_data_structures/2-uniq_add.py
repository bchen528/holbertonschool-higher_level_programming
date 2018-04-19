#!/usr/bin/python3
def uniq_add(my_list=[]):
    no_dup = list(set(my_list))
    result = 0
    for i in range(len(no_dup)):
        result = result + no_dup[i]
    return result
