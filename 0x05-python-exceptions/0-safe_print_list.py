#!/usr/bin/python3


"""
safe_print_list - prints x number of a list
my_list - lists containing any type of data
x - number of elements to print
Return: real number of elements printed
"""


def safe_print_list(my_list=[], x=0):
    try:
        idx = 0
        for val in range(x):
            print("{}".format(my_list[val]), end="")
            idx += 1
        print()
        return idx
    except IndexError:
        print()
        return idx
