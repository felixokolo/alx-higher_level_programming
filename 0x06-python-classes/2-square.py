#!/usr/bin/python3

"""Defining practice class"""


class Square:
    """Practice empty class

    Attributes:
        __size (int): Private size of square attribute

    """
    def __init__(self, size=0):
        """ defining the init functiom

        Args:
            size (int): for initializing the size attribute

        """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
