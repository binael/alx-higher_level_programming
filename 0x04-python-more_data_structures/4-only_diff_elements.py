#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """List of distinc set elements"""

    return list(set_1.union(set_2) - set_1.intersection(set_2))
