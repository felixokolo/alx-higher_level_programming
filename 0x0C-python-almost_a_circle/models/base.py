#!/usr/bin/python3
"""Base class"""


class Base:
    """Base class definition
    Attributes:
        __nb_objects (int): private class attribute
    """
    __nb_objects = 0


    def __init__(self, id=None):
        """Init function for base class
        Args:
            id (int): Instance ID
        """
        if id is None:
            __nb_objects += 1
            self.id = __nb_objects
        else:
            self.id = id
