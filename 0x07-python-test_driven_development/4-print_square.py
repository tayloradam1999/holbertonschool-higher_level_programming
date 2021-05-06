#!/usr/bin/python3

"""This module defines a square-printing function.
size: Height and width of the square."""


def print_square(size):
    """Defines a square-printing function.
    Raises a TypeError if:
        Size is not an integer
    Raises a ValueError if:
        Size is < 0"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        for y in range(size):
            print("#", end="")
        print()
