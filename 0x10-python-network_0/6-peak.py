#!/usr/bin/python3


def find_peak(list_of_integers):

    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    mid_idx = int(len(list_of_integers) / 2)

    if mid_idx != len(list_of_integers) - 1:
        if list_of_integers[mid_idx - 1] < list_of_integers[mid_idx] and\
           list_of_integers[mid_idx + 1] < list_of_integers[mid_idx]:
            return list_of_integers[mid_idx]
    else:
        if list_of_integers[mid_idx - 1] < list_of_integers[mid_idx]:
            return list_of_integers[mid_idx]
        else:
            return list_of_integers[mid_idx - 1]

    if list_of_integers[mid_idx - 1] > list_of_integers[mid_idx]:
        a_list = list_of_integers[0:mid_idx]
    else:
        a_list = list_of_integers[mid_idx + 1:]

    return find_peak(a_list)
