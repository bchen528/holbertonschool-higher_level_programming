#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    r = (abs(number) % 10) * -1
    if r > 5:
        print("Last digit of {:d} is {:d} and is greater than 5"
              .format(number, r))
    elif r == 0:
        print("Last digit of {:d} is {:d} and is 0".format(number, r))
    elif r < 6:
        print("Last digit of {:d} is {:d} and is less than 6 and not 0"
              .format(number, r))
else:
    if number % 10 > 5:
        print("Last digit of {:d} is {:d} and is greater than 5"
              .format(number, number % 10))
    elif number % 10 == 0:
        print("Last digit of {:d} is {:d} and is 0"
              .format(number, number % 10))
    elif number % 10 < 6:
        print("Last digit of {:d} is {:d} and is less than 6 and not 0"
              .format(number, number % 10))
