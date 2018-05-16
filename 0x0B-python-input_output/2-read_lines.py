#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    i = 0
    with open(filename, mode="r", encoding="utf-8") as a_file:
        if nb_lines <= 0:
            print(a_file.read(), end="")
        else:
            for a_line in a_file:
                if i < nb_lines:
                    print(a_line, end="")
                i += 1
