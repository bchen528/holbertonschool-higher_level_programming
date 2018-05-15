#!/usr/bin/python3
def is_same_class(obj, a_class):
    """check if object is an instance of a_class
    Args:
        obj(obj): object
        a_class(class): class
    Return:
        True: if it is an instance of the given class
        False: if not an instance of given class
    """
    if type(obj) is a_class:
        return True
    return False
