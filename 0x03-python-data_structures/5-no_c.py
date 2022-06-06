#!/usr/bin/python3

def no_c(my_string):
    """that removes all characters c and C from a string"""

    new_string = ""

    for s in my_string:
        if s in "cC":
            continue
        new_string += s

    return new_string
