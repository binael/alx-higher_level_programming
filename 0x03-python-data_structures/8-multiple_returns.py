#!/usr/bin/python3

def multiple_returns(sentence):
    """Returns a tuple of string length  and its first character"""

    if not sentence:
        return None

    return (len(sentence), sentence[0])
