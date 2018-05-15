#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """check if object is an instance of class
    Args:
        obj(obj): object
        a_class(class): class
    Return:
        True: if the object is an instance of,
             or if the object is an instance of a class that
             inherited from, the specified class
    """
    if isinstance(obj, a_class):
        return True
    return False
