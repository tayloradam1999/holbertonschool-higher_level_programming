#!/usr/bin/python3

"""
This module appends a string at the end of a text file and
returns the number of characters added
"""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file"""
    with open(filename, mode='a', encoding="UTF-8") as fh:
        fh.write(text)
        chars = len(text)
    return chars
