#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """ Modifies a  list and storing in a new list"""

    if idx < 0 or idx >= len(my_list):
        return my_list

    new_list = []

    for i in range(len(my_list)):
        if i == idx:
            new_list.append(element)
            continue
        new_list.append(i)

    return new_list
