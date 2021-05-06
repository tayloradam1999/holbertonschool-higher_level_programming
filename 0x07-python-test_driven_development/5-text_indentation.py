#!/usr/bin/python3

"""This module defines a text-indentation fuction.
text - The text to print as a string."""


def text_indentation(text):
    """Prints text with two new lines after each '.', '?', and ':'.
    Raises a TypeError if:
        text is not a string
    There should be no space at the beginning or at the end of
    each printed line."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_str = ""
    new_str2 = ""
    new_str3 = ""

    text_list = text.split(". ")
    for chars in range(len(text_list)):
        if chars < len(text_list) - 1:
            new_str += text_list[chars] + '.\n\n'
        else:
            new_str += text_list[chars]

    text_list2 = new_str.split("? ")
    for chars in range(len(text_list2)):
        if chars < len(text_list2) - 1:
            new_str2 += text_list2[chars] + '?\n\n'
        else:
            new_str2 += text_list2[chars]

    text_list3 = new_str2.split(": ")
    for chars in range(len(text_list3)):
        if chars < len(text_list3) - 1:
            new_str3 += text_list3[chars] + ':\n\n'
        else:
            new_str3 += text_list3[chars]

    print("{}".format(new_str3), end="")
