#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replace elements in a given index number"""

    new_list = my_list[:]

    new_list[search] = replace

    return new_list
