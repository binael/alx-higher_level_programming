#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """ Deletes elements at give index"""

    if idx < 0 or idx > len(my_list):
        return my_list

    my_list = my_list[:idx + 1] + my_list[idex + 1:]

    return my_list
