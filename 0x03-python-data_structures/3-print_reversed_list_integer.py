#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Reverse printing a  list of integers"""

    if not my_list:
        return

    for i in reversed(my_list):
        print("{:d}".format(i))
