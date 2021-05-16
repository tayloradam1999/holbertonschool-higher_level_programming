#!/usr/bin/python3

"""
This module creates a class 'Base'
"""


import json
import os


class Base:

    """This class has a constructor and a private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of 'list_objs' to a file"""
        filename = cls.__name__ + ".json"
        my_list = []
        if list_objs is not None:
            for obj in list_objs:
                my_dict = cls.to_dictionary(obj)
                my_list.append(my_dict)
            j_str = cls.to_json_string(my_list)
        else:
            j_str = "[]"
        with open(filename, "w") as fh:
            fh.write(j_str)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation 'json_string'"""
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if len(dictionary) == 1:
            dummy = cls(1)
            dummy.update(**dictionary)
        else:
            dummy = cls(1, 1)
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        if os.path.exists(filename):
            with open(filename, 'r') as fh:
                j_str = fh.read()
            my_list = []
            my_list = cls.from_json_string(j_str)
            obj_list = []
            for items in my_list:
                dict_items = dict(items)
                obj = cls.create(**dict_items)
                obj_list.append(obj)
            return obj_list
        else:
            return my_list
