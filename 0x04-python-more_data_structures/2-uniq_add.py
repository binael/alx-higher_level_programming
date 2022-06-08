#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Adds unique elements in a list"""

    sum = 0
    my_set = set(my_list)

    for i in my_set:
        sum += i

    return sum
