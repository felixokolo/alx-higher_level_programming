#!/usr/bin/python3
"""Reading and writing module"""

import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a
    text file, using a JSON representation
     Args:
        my_obj (str): object to write to json
        file
        filename (str): json filename
    """

    if my_obj is None or filename is None:
        return
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
