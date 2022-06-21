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
            
    def my_print(self):
        """prints square"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                else:
                    print("")