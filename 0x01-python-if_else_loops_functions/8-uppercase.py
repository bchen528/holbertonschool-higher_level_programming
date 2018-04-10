#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        s = ord(str[i])
        if s >= 97 and s <= 122:
            s = s - 32
        if i == len(str) - 1:
            print("{:c}".format(s))
        else:
            print("{:c}".format(s), end="")
