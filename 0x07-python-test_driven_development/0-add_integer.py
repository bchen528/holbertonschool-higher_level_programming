#!/usr/bin/python3
"""
Adding integers
"""


def add_integer(a, b=98):
    """ adding two integers
    Args:
        a (int): integer value
        b (int): integer value if specified, otherwise 98
    Returns:
        sum of two integers
    Raises:
        TypeError: if either a or b are not integers
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
