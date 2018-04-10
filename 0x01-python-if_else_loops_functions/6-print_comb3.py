#!/usr/bin/python3
for x in range(0, 90):
    if x != 89:
        if x % 10 > x / 10:
            print("{:02d}".format(x), end=", ")
    else:
        print("{:d}".format(x))
