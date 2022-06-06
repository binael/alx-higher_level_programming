#!/usr/bin/python3

def multiple_returns(sentence):
    """Returns a tuple of string length  and its first character"""

    if not sentence:
        s = None
    else:
        s = sentence[0]

    return (len(sentence), s)
