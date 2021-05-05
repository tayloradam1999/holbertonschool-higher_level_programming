#!/usr/bin/python3
"""This module writes a class 'Square'.
Initalizes a private instance attribute 'size' with option (self, size=0):.
Property setter 'def size(self, value):' to set 'size'.
Property 'def size(self):' to retrieve 'size'.
Initalizes a public instance method 'def area(self):' that Returns the area.
Initalizes a public instance method 'def my_print(self):' that prints
in stdout the square with the character '#'.
This module handles TypeErrors and ValueErrors."""


class Square:
    """Class that initalizes 'size' as a private instance attribute."""
    def __init__(self, size=0):
        """init 'size' for 'Square' Class."""
        self.__size = size

    @property
    def size(self):
        """This def returns the size of a square."""
        return self.__size

    @size.setter
    def size(self, value):
        """This def sets the size of a square object.
        'Size' must be an int, otherwise raise a TypeError.
        If 'size' is less than 0, raise a ValueError."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be > 0")
        else:
            self.__size = value

    def area(self):
        """This def returns the area of the current Square object."""
        area = self.__size ** 2
        return area

    def my_print(self):
        """This def prints the square with the character '#' in stdout."""
        if self.__size is 0:
            print()
        for x in range(self.__size):
            for y in range(self.__size):
                print('#', end="")
            print()
