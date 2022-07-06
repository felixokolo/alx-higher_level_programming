#!/usr/bin/python3
"""List inheritance module"""


class MyList(list):
    """Modified List class
    Attributes:
        """
    def print_sorted(self):
        """Prints a list in sorted form"""
        if self.__len__ == 0:
            print([])
            return
        new = sorted(self)
        print(new)


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/1-my_list.txt")
