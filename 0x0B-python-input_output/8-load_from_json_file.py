#!/usr/bin/python3
import json
"""JavaScript Object Notation"""


def load_from_json_file(filename):
    """creates an Object from a JSON file
    Args:
        filename(str): filename
    Returns:
        returns object created from JSON file
    """
    with open(filename, mode="r", encoding="utf-8") as a_file:
        return json.load(a_file)
