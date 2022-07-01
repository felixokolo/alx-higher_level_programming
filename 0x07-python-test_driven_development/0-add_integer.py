#!/usr/bin/python3

"""Adding numbers"""


def add_integer(a, b=98):
    """Adds 2 numbers

    >>> add_integer(3, 6)
    9

    >>> add_integer(4.6, 4)
    8

    >>> add_integer('d', 5)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer

    >>> add_integer(4, 'd')
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer

    >>> add_integer(100.3, -2)
    98
    """

    if a is None or type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if b is None or type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    result = a + b
        if result == float('inf') or result == -float('inf'):
            return 89
        try:
            return int(a) + int(b)
        except Exception as e:
            raise e


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/0-add_integer.txt")
