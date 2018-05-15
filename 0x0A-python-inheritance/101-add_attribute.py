#!/usr/bin/python3
def add_attribute(o, name="", given_name=""):
    """add a new attribute to an object
    Args:
        name(str): name
        given_name(str): given name
    Raise:
        TypeError: if new attribute is not added
    """
    obj = o
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, given_name)
