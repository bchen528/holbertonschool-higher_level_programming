#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        s = ord(str[i])
        if s >= 97 and s <= 122:
            s = s - 32
        print("{:c}".format(s), end="")
    print('')
