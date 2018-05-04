#!/usr/bin/python3
"""
prints "My name is"
"""


def say_my_name(first_name, last_name=""):
    """prints "My name is"

    Args:
        first_name (str): first name
        last_name (str): last name

    Raises:
        TypeError: if either first_name or last_name are not strings
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
