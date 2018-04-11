#!/usr/bin/python3
def fizzbuzz():
    i = 1
    while i < 101:
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            if i != 100:
                print("Buzz", end=" ")
            else:
                print("Buzz", end="")
        else:
            print("{:d}".format(i), end=" ")
        i = i + 1
