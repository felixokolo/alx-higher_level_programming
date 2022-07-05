#!/usr/bin/python3
"""Reading and writing module"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a
    text file (UTF8) and returns the number of characters added
    Args:
        filename (str): file to read
        text (str): text to write
    """

    if filename == "":
        return
    with open(filename, 'a', encoding="utf-8") as f:
        n = f.write(text)
    return n
