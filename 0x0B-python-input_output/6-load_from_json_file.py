#!/usr/bin/python3
"""Reading and writing module"""

import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file
     Args:
        filename (str): json filename
    Returns: deserialized object file
    """

    if filename == None:
        return
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)