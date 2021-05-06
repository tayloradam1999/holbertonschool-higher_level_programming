#!/usr/bin/python3

"""
This module defines a class 'Rectangle' that
defines a rectangle based on '0-rectangle.py'
"""


class Rectangle:
    """Defines a rectangle with a private instance attribute 'width'
    and 'height'
    Defines public class varibale 'number_of_instances' that
    increases by 1 whenever '__init__" is called, and
    decreases bv 1 whenever '__del__' is called."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area
        Raises TypeErrors if:
            rect_1 is not an instance of 'Rectangle'
            rect_2 is not an instance of 'Rectangle'
        Returns rect_1 if both have the same area"""
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("ect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("ect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    def __str__(self):
        """Prints our rectangle"""
        str2 = ""
        if self.height == 0 or self.width == 0:
            return ""
        for i in range(self.height):
            str2 += str(self.print_symbol) * self.width
            if i < self.height - 1:
                str2 = str2 + "\n"
        return str2

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return 'Rectangle(%d, %d)' % (self.width, self.height)

    def __del__(self):
        """Prints the message 'Bye Rectangle...' when an instance of
        'Rectangle' is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
        return Rectangle.number_of_instances

    @property
    def width(self):
        """Property getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter for width that raises Type and Value errors"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter for height that raises Type and Value errors"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public instance method that returns the rectangle's area"""
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """Public instance method that returns the rectangle's perimeter
        If height or width is 0, perimeter is 0"""
        perim = 0
        if self.__width == 0 or self.__height == 0:
            return perim
        else:
            perim = (self.__width * 2) + (self.__height * 2)
            return perim
