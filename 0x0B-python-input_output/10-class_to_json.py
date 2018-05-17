#!/usr/bin/python3
def class_to_json(obj):
    """returns the dictionary description with simple data structure
        (list, dictionary, string, integer and boolean) for JSON serialization
        of an object
    Args:
        obj(obj): object
    Returns:
        dictionary description for JSON serialization of an object
    """
    return obj.__dict__
