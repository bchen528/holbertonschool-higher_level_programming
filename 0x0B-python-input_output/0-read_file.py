#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, mode="r", encoding="utf-8") as a_file:
        print(a_file.read(), end="")
