#!/usr/bin/python3

"""
This module writes a string to a textfile and returns
the number of characters written
"""


def write_file(filename="", text=""):
    """Writes a string to a textfile and returns number of chars written"""
    with open(filename, mode='w', encoding="UTF-8") as fh:
        fh.write(text)
        chars = len(text)
    return chars
