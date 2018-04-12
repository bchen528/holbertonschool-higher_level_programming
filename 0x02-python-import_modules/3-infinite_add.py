#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    sum = 0
    for i in range(1, len(argv)):
        sum = sum + int(argv[i])
    print("{:d}".format(sum))
