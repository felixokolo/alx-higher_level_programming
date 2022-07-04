#!/usr/bin/python3
"""Function module"""


def is_same_class(obj, a_class):
    """ Lookup function that returns a list of attr
    Args:
        obj (object): object to check
        a_class (object): class to compare
    """

    if isinstance(obj, a_class) and type(obj) == a_class:
        return True
    else:
        return False
