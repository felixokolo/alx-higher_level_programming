#!/usr/bin/python3
""" My class module
"""


class Student:
    """ My class
    """

    score = 0

    def __init__(self, first_name, last_name, age):
        """ Initialization function
        Args:
            first_name (str): First name of student
            last_name (str): Last name
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """method  that retrieves a dictionary
        representation of a Student instance

        Args:
            attrs (list): list of strings to return
        """
        ret = self.__dict__
        if type(attrs) == list:
            return {a: ret[a] for a in ret if a in attrs}
        return ret
