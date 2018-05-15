#!/usr/bin/python3
def inherits_from(obj, a_class):
    """checks if obj is an instance of subclass of a_class
    Args:
        obj(obj): object
        a_class(class): class
    Returns:
        True: if object is an instance of subclass of a_class
        False: if object is not an instance of a subclass of a_class
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
