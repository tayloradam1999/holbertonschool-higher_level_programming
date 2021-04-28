#!/bin/usr/python3
def multiple_returns(sentence):
    if not sentence:
        char = None
    else:
        length = len(sentence)
        char = sentence[:1]
    return (length, char)
