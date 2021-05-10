#!/usr/bin/python3
"""This module writes a class 'Square'.
Initalizes a private instance attribute 'size' with option '(self, size=0):'.
Property setter 'def size(self, value):' to set 'size'.
Property 'def size(self):' to retrieve 'size'.
Initalizes a public instance method 'def area(self):' that Returns the area.
Initalizes a public instance method 'def my_print(self):' that prints
in stdout the square with the character '#'.
Initalizes a private instance attribute 'position'.
Property setter 'def position(self, value):' to set the position.
Property 'def position(self):' to retrieve the position.
Optional size and optional position:
'def __init__(self, size=0, position=(0, 0)):'.
This module handles TypeErrors and ValueErrors."""


class Square:
    """Class that initalizes 'size' as a private instance attribute."""
    def __init__(self, size=0, position=(0, 0)):
        """init 'size' and 'position' for 'Square' Class."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """This def returns the size of a square."""
        return self.__size

    @size.setter
    def size(self, value):
        """This def sets the size of a square object.
        Raises a TypeError if size is not an integer.
        Raises a ValueError if size is < 0."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be > 0")
        else:
            self.__size = value

    @property
    def position(self):
        """This def returns the position within a square."""
        return self.__position

    @position.setter
    def position(self, value):
        """This def sets the position within a square.
        Raises a TypeError if not a tuple that contains
        2 position integers."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if min(value) < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """This def returns the area of the current Square object."""
        area = self.__size ** 2
        return area

    def my_print(self):
        """This def prints the square with the character '#' in stdout."""
        if self.__size is 0:
            print()
        else:
            for x in range(self.__position[1]):
                print()
            for x in range(self.__size):
                for z in range(self.__position[0]):
                    print(" ", end="")
                for y in range(self.__size):
                    print('#', end="")
                print()
