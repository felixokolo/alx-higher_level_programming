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
        if isinstance(size, int) or isinstance(size, float):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be a number")

    def area(self):
        """ Method for calculating area of square"""

        return self.__size ** 2

    @property
    def size(self):
        """Size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Size setter
        Args:
            value (int): new value for size
        """
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def __gt__(self, other):
        """Greater than comparison
        Args:
            other (Square): instance to compare
        """
        return self.__size > other.size

    def __ge__(self, other):
        """Greater than or equal comparison
        Args:
            other (Square): instance to compare
        """
        return self.__size >= other.size

    def __lt__(self, other):
        """Less than comparison
        Args:
            other (Square): instance to compare
        """
        return self.__size < other.size

    def __le__(self, other):
        """Less than or equal comparison
        Args:
            other (Square): instance to compare
        """
        return self.__size <= other.size

    def __eq__(self, other):
        """Equal comparison
        Args:
            other (Square): instance to compare
        """
        return self.__size == other.size

    def __ne__(self, other):
        """Not equal comparison
        Args:
            other (Square): instance to compare
        """
        return self.__size != other.size
