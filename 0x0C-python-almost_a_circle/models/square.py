#!/usr/bin/python3

"""
This module creates a class 'Square'
"""


from models.rectangle import Rectangle
import inspect


class Square(Rectangle):

    """Square class that inherits from 'Rectangle'"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor method that calls the super class
        This super call will use the logic of the __init__ of
        the 'Rectangle' class"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Returns our attributes values"""
        return '[Square] (%d) %d/%d - %d' % (self.id, self.x,
                                             self.y, self.size)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square instance"""
        my_dict = {}
        for i in inspect.getmembers(self):
            if not i[0].startswith('_'):
                if not inspect.ismethod(i[1]):
                    if i[0] != "height" or i[0] != "width" or\
                       i[0] != "to_json_string":
                        my_dict[i[0]] = i[1]
        return my_dict

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args is None or len(args) == 0:
            for i in kwargs:
                if hasattr(self, i):
                    setattr(self, i, kwargs[i])
        largs = list(args)
        latts = ["id", "size", "x", "y"]
        for i in range(len(largs)):
            setattr(self, latts[i], largs[i])

    @property
    def size(self):
        """Getter method for size"""
        return self.__width

    @size.setter
    def size(self, size):
        """Setter method for size"""
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        elif size <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = size
            self.__height = size
