#!/usr/bin/python3

"""
This modules creates a new class 'Square'
Initializes the 'size' of 'Square'
"""


class Square:
    """This class initializes 'size' as a private instance attribute"""
    def __init__(self, size=0):
        """Raises TypeError if size is not an integer
        Raises ValueError if size is less than 0"""
        self.__size = size

    @property
    def size(self):
        """This function returns the size of a 'square'"""
        return self.__size

    @size.setter
    def size(self, value):
        """This function sets the size of a 'square'
        Throws Type and Value errors"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """This function returns the area of a 'square'"""
        area = self.__size ** 2
        return area

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()
