#!/usr/bin/python3
class MyInt(int):
    """creates a class MyInt"""
    def __eq__(self, other):
        """invert == to !="""
        return False

    def __ne__(self, other):
        """invert != to =="""
        return True
