#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """ function that deletes keys with a specific value in a dictionary"""

    new_dict = {}

    for k, v in a_dictionary.items():
        if v == value:
            continue
        new_dict.setdefault(k, v)

    a_dictionary = new_dict

    return a_dictionary
