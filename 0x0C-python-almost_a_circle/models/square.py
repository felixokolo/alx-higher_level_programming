#!/usr/bin/python3
"""Base class"""

import sys

sys.path.insert(0, 'models')
Rectangle = __import__('rectangle').Rectangle

class Square(Rectangle):
    """Square class definition
    """


    def __init__(self, size, x=0, y=0, id=None):
        """Init function for base class
        Args:
            size (float): Square size
            x (float): Rectangle x position
            y (float): Rectangle y position
            id (int): Base id
        """
        Rectangle.__init__(self,size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter
        Args:
            value (int): new value for size
        """
        self.width = value
        self.height = value



    def __str__(self):
        """String representation of square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"


    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute"""
        lent = len(args)
        if lent == 1:
            self.id = args[0]
        elif lent == 2:
            self.id, self.size = args
        elif lent == 3:
            self.id, self.size, self.x = args
        elif lent == 4:
            self.id, self.size, self.x, self.y, = args
        elif lent > 0:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        if lent > 0:
            return
        else:
            self.id = kwargs.get('id', self.id)
            self.size = kwargs.get('size', self.size)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)



    def to_dictionary(self):
        """Creates Dictionary representation"""
        return {'x': self.x, 'y': self.y, 'id': self.id, 'size': self.size}