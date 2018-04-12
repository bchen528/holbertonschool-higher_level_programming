#!/usr/bin/python3
import hidden_4 as hidden
if __name__ == "__main__":
    for name in dir(hidden):
        if name[0:2] != "__":
            print("{:s}".format(name))
