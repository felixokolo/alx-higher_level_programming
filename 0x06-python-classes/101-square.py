#!/usr/bin/python3

"""Defining practice class"""


class Square:
    """Practice empty class

    Attributes:
        __size (int): Private size of square attribute

    """
    def __init__(self, size=0, position=(0, 0)):
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
        self.position = position

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
            [print("") for i in range(0, self.__position[1])]
            for i in range(self.__size):
                [print(" ", end="") for j in range(0, self.__position[0])]
                for j in range(self.__size):
                    print("#", end="")
                else:
                    print("")

    @property
    def position(self):
        """Get/set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Setter """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __str__(self):
        """Prints representation of instance"""
        outp = ""
        if self.__size == 0:
            return outp + "\n"
        else:
            for i in range(0, self.__position[1]):
                outp += "\n"
            for i in range(self.__size):
                for j in range(0, self.__position[0]):
                    outp += " "
                for j in range(self.__size):
                    outp += "#"
                else:
                    if i < self.__size - 1:
                        outp += "\n"
        return outp
