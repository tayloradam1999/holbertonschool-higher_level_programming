#!/usr/bin/python3

"""
This module reads a text file and prints it to stdout
"""


def read_file(filename=""):
    """Reads a text file and prints to stdout"""
    with open(filename, encoding="UTF-8") as fh:
        print(fh.read(), end="")
