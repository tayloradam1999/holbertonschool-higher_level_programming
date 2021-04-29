#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    my_dict = a_dictionary.copy()
    my_dict.update((x, y * 2) for x, y in my_dict.items())
    return my_dict
