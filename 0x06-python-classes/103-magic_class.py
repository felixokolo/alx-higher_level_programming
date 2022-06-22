#!/usr/bin/python3

import math

"""Defining MagicClass class"""


class MagicClass:
    """Practice empty class

    Attributes:
        __radius (int): Private size of radius attribute

    """
    def __init__(self, radius=0):
        """ defining the init functiom

        Args:
            radius (int): for initializing the radius attribute

        """
        if isinstance(radius, int) or  isinstance(radius, float):
            self.__radius = radius
        else:
            self.__radius = None
            raise TypeError("radius must be a number")

    def area(self):
        """ Method for calculating area of square"""

        return math.pi * self.__radius ** 2

    def circumference(self):
        """ Method for calculating circumference of square"""

        return math.pi * self.__radius * 2
