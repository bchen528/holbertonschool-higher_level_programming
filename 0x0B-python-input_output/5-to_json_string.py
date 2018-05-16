#!/usr/bin/python3
import json
"""JavaScript Object Notation"""


def to_json_string(my_obj):
    """find JSON representation of an object (string)
    Args:
        my_obj(obj): object
    Returns:
        JSON representation of object
    """
    return json.dumps(my_obj)
