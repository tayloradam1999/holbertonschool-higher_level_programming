#!/usr/bin/python3

"""
This module creates a class 'Rectangle'
"""


from models.base import Base


class Rectangle(Base):
    """This is a class that inherits from 'Base'
    This class has 4 private instance attributes
    This class also has a constructor"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor method"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Property getter for width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Property setter for width with validator"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """Property getter for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Property setter for width with validator"""
        if not isinstance(height, int):
            raise TypeError("width must be an integer")
        elif height <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """Property getter for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Property setter for x with validator"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x <= 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """Property getter for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Property setter for y with validator"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y <= 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
