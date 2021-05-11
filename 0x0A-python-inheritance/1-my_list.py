#!/usr/bin/python3

"""
This module writes a class 'MyList' that inherits from 'list'
"""


class MyList(list):
    """Class that inherits from 'list'
    includes a method that prints the list, but in ascending order"""
    def print_sorted(self):
        """Prints the list in ascending order"""
        sort_list = []
        sort_list = self.copy()
        sort_list.sort()
        print("{}".format(sort_list))
