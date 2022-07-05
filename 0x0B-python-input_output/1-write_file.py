#!/usr/bin/python3
"""Reading and writing module"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8)
    and returns the number of characters written
    Args:
        filename (str): file to read
        text (str): text to write
    """

    if filename == "":
        return
    with open(filename, 'w', encoding="utf-8") as f:
        n = f.write(text)
    return n
