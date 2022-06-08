#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replace elements in a given index number"""

    new_list = my_list[:]

    for i in range(len(my_list)):
        if new_list[i] == search:
            new_list[search] = replace

    return new_list
