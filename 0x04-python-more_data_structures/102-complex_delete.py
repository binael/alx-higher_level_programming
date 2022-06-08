#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """ function that deletes keys with a specific value in a dictionary"""

    my_list = []

    for k, v in a_dictionary.items():
        if v == value:
            my_list.append(k)

    for element in my_list:
        del a_dictionary[element]

    return a_dictionary
