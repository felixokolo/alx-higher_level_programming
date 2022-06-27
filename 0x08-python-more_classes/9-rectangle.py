#!/usr/bin/python3

"""Defining practice class"""


class Rectangle:
    """Practice Rectangle class

    Attributes:
        __width (int): Private width of rectangle
        __height (int): Private height of rectangle
        number_of_instances (int): keeps number of instances
        print_symbol(any): for representation

    """
    number_of_instances = 0
    print_symbol = '#'


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
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Calculates area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Calculates perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Returns string representation of instance"""
        ret = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                ret += str(self.print_symbol)
            if i != self.__height - 1:
                ret += "\n"
        return ret
    def __repr__(self):
        """Returns string representation to recreate instance"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """called when deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares 2 rectangles"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Defines a square instance
         Args:
            size (int): new value for size
        """
        return cls(size, size)