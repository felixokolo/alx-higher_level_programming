#!/usr/bin/python3
"""Reading and writing module"""

import json


def from_json_string(my_str):
    """function that returns an object
    (Python data structure) represented by a JSON string
    Args:
        my_str (str): string to deserialize
    Return: Deserialized object
    """

    if my_str is None or my_str == "":
        return
    return json.loads(my_str)