#!/usr/bin/python3
"""Function module"""


class BaseGeometry:
    """Empty BaseGeometry"""

    def area(self):
        """Public class area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value


        Args:
            name (str): name of parm
            value (int): parm to vlaidate
        Return:
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/7-base_geometry.txt")
