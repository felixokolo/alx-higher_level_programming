#!/usr/bin/python3
"""Base class"""

import sys

sys.path.insert(0, 'models')
Base = __import__('base').Base

class Rectangle(Base):
    """Rectangle class definition
    """


    def __init__(self, width, height, x=0, y=0, id=None):
        """Init function for base class
        Args:
            width (float): Rectangle width
            height (float): Rectangle height
            x (float): Rectangle x position
            y (float): Rectangle y position
        """
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y


    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter
        Args:
            value (int): new value for width
        """
        if isinstance(value, int):
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")
 
 
    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter
        Args:
            value (int): new value for height
        """
        if isinstance(value, int):
            if value > 0:
                self.__height = value
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")


    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter
        Args:
            value (int): new value for x
        """
        if isinstance(value, int):
            if value >= 0:
                self.__x = value
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")
 
 
    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter
        Args:
            value (int): new value for y
        """
        if isinstance(value, int):
            if value >= 0:
                self.__y = value
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")


    def area(self):
        """Calculates the area of rectangle"""
        return self.height * self.width


    def display(self):
        """Displays the rectangle using #"""
        [print("") for i in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for i in range(self.x)]
            for j in range(self.width):
                print("#", end='')
            print("")


    def __str__(self):
        """String representation of rectangle"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"


    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute"""
        lent = len(args)
        if lent == 1:
            self.id = args[0]
        elif lent == 2:
            self.id, self.width = args
        elif lent == 3:
            self.id, self.width, self.height = args
        elif lent == 4:
            self.id, self.width, self.height, self.x, = args
        elif lent == 5:
            self.id, self.width, self.height, self.x, self.y = args
        elif lent > 0:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        if lent > 0:
            return
        else:
            self.id = kwargs.get('id', self.id)
            self.width = kwargs.get('width', self.width)
            self.height = kwargs.get('height', self.height)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)


    def to_dictionary(self):
        """Creates Dictionary representation"""
        return {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height, 'width': self.width}