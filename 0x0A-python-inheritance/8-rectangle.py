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
