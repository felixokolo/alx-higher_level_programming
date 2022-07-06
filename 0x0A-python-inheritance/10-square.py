#!/usr/bin/python3
"""Function module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Empty Square"""

    def __init__(self, size):
        """Init method"""
        Rectangle.__init__(self, size, size)
        self.__size = size

    def area(self):
        """Public class area"""
        return self.__size ** 2