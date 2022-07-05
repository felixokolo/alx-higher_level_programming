#!/usr/bin/python3
"""Reading and writing module"""


def read_file(filename=""):
    """function that reads a text file (UTF8)
    and prints it to stdout
    Args:
        filename (str): file to read
    """

    if filename == "":
        return
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
