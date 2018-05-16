#!/usr/bin/python3
import json
"""JavaScript Object Notation"""


def from_json_string(my_str):
    """find an object (Python data structure) represented by a JSON string
    Args:
        my_str(str): a string
    Returns:
        an object (Python data structure) represented by a JSON string
    """
    return json.loads(my_str)
