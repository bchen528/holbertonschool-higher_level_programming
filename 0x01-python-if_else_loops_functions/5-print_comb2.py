#!/usr/bin/python3
for x in range(0, 100):
    if x < 10:
        print("{:d}{:d}".format(0, x), end=", ")
    else:
        if x != 99:
            print("{:d}".format(x), end=", ")
        else:
            print("99")
