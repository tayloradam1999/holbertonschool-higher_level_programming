#!/usr/bin/python3

"""
This module writes a class 'Student'
"""


class Student:
    """Student class that is defined by
    -first_name
    -last_name
    -age"""
    def __init__(self, first_name, last_name, age):
        """Constructor for 'Student' class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary representation of a 'Student' instance
        -if 'attrs' is a list of strings, only attribute names contained
        in this list must  be retrieved
        -otherwise, all attributes must be retrieved"""
        if isinstance(attrs, list):
            my_dict = {}
            for x in attrs:
                if hasattr(self, x):
                    my_dict[x] = getattr(self, x)
            return my_dict
        return self.__dict__
