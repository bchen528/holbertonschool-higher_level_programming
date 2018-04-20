#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    result = []
    weights = []

    for tup in my_list:
        result.append(tup[0] * tup[1])
        weights.append(tup[1])

    return sum(result) / sum(weights)
