#!/usr/bin/python3

"""
This module contains a function that inserts 'new_string'
after every 'search_string'
"""


def append_after(filename="", search_string="", new_string=""):
    """Appends new_string after every search_string"""
    my_str = ""
    with open(filename, mode='r') as fh:
        for lines in fh:
            my_str = my_str + str(lines)
            if search_string in lines:
                my_str = my_str + new_string
    with open(filename, mode='w+') as fh:
        fh.write(my_str)
