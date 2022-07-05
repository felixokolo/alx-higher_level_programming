#!/usr/bin/python3
"""Reading and writing module"""

import json


def to_json_string(my_obj):
    """function that returns the JSON
    representation of an object (string)
    Args:
        my_obj (str): object to convert to json
        string
    Return: String representation of my_obj
    """

    if my_obj is None:
        return
    return json.dumps(my_obj)
