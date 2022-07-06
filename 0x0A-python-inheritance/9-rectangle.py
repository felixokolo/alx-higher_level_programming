#!/usr/bin/python3
"""Function module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Empty Rectangle"""

    def __init__(self, width, height):
        """Init method"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Public class area"""
        return self.__height * self.__width

    def __str__(self):
        """String representatiom"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
