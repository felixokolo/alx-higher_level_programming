#!/usr/bin/python3
"""Reading and writing module"""


def class_to_json(obj):
    """function that returns the dictionary description
    with simple data structure (list, dictionary, string,
    integer and boolean) for JSON serialization of an object
     Args:
        obj (class): class object
    Returns: dictionary of attributes
    """

    return obj.__dict__
