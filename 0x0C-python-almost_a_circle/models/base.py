#!/usr/bin/python3
"""Base class"""

import json


class Base:
    """Base class definition
    Attributes:
        __nb_objects (int): private class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Init function for base class
        Args:
            id (int): Instance ID
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        Args:
            cls (str): object class
            list_objs (list): list of base objects
        """

        lst = []
        if list_objs is None or cls is None:
            strd = '[]'
        else:
            for ls in list_objs:
                lst.append(ls.to_dictionary())
            strd = Base.to_json_string(lst)
        with open(cls.__name__ + '.json', 'w', encoding="utf-8") as f:
            f.write(strd)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        lst = []
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        Args:
            dictionary (str):  a double pointer to a dictionary
        """

        new = cls(2, 2)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances
        """

        ret = []
        try:
            with open(cls.__name__ + '.json', 'r', encoding="utf-8") as f:
                dic_lst = Base.from_json_string(f.read())
        except FileNotFoundError:
            return []
        for dic in dic_lst:
            ret.append(cls.create(**dic))
        return ret