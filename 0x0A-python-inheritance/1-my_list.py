#!/usr/bin/python3
class MyList(list):
    """creates a subclass Mylist of superclass list"""
    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
