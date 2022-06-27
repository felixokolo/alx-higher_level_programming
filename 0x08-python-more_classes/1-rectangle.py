#!/usr/bin/python3

"""Defining practice class"""


class Rectangle:
    """Practice Rectangle class

    Attributes:
        __width (int): Private width of rectangle
        __height (int): Private height of rectangle

    """
    def __init__(self, width=0, height=0):
        """ defining the init functiom

        Args:
            width (int): for initializing the width attribute
            height (int): for initializing the height attribute

        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__height = height
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Size setter
        Args:
            value (int): new value for size
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Size setter
        Args:
            value (int): new value for size
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value