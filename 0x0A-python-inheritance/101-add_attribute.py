#!/usr/bin/python3
def add_attribute(o, name="", given_name=""):
    obj = o
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, given_name)
