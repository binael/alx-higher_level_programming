#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """function that adds 2 tuples"""

    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
