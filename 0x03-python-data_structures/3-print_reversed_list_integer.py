#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Reverse printing a  list of integers"""

    if my_list.isempty():
        return

    for i in reversed(my_list):
        print("{:d}".format(i))
