#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key in dict(filter(lambda x: x[1] == value, a_dictionary.items())):
        del a_dictionary[key]
    return a_dictionary
