#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if not sentence:
        char = None
    else:
        char = sentence[:1]
    return (length, char)
