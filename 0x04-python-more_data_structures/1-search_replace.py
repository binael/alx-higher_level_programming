#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replace elements in a given index number"""

    new_list = []

    for i in my_list:
        if i == search:
            new_list.append(replace)
        else:
            new_list.append(i)

    return new_list
