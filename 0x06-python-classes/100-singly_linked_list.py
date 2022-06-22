#!/usr/bin/python3

"""Defining Node class"""


class Node:
    """Practice empty class

    Attributes:
        __data (int): Private data of square attribute

    """
    def __init__(self, data=0, next_node=None):
        """ defining the init functiom

        Args:
            data (int): for initializing the data attribute
            next_node (Node): next node on list

        """
        if isinstance(data, int):
            self.__data = data
        else:
            raise TypeError("data must be an integer")

        if isinstance(next_node, Node) or next_node is None:
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")

    def area(self):
        """ Method for calculating area of square"""

        return self.__data ** 2

    @property
    def data(self):
        """Data getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """Data setter
        Args:
            value (int): new value for data
        """
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("next_node must be a Node object")

    @property
    def next_node(self):
        """Next_node getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Next_node setter
        Args:
            value (Node): new value for Next_node
        """
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """SinglyLinkedList class

    Attributes:
        __head (Node): Private data of square attribute

    """
    def __init__(self):
        """ defining the init functiom

        Args:
            head (Node): Head of single list

        """
        self.__head = None

    def sorted_insert(self, value):
        """Adds a node to list in ordered manner
        Args:
            value (int): value to be added to list
        """

        if self.__head is None:
            self.__head = Node(value, None)
        else:
            __tmp = self.__head
            if __tmp.next_node is not None:
                __prev = None
                while __tmp.next_node is not None:
                    if value > __tmp.data:
                        __prev = __tmp
                        __tmp = __tmp.next_node
                    else:
                        __pres = Node(value, __tmp)
                        if __prev is not None:
                            __prev.next_node = __pres
                        else:
                            self.__head = __pres
                        break
                else:
                    if value > __tmp.data:
                        __pres = Node(value, None)
                        __tmp.next_node = __pres
                    else:
                        __pres = Node(value, __tmp)
                        if __prev is not None:
                            __prev.next_node = __pres
                        else:
                            self.__head = __pres
            else:
                if value > self.__head.data:
                    __pres = Node(value, None)
                    self.__head.next_node = __pres
                else:
                    __pres = Node(value, self.__head)
                    self.__head = __pres

    def __str__(self):
        """Prints representation of instance"""
        outp = ""
        tmp = self.__head
        while tmp is not None:
            outp += str(tmp.data)
            if tmp.next_node is not None:
                outp += "\n"
            tmp = tmp.next_node
        return outp
