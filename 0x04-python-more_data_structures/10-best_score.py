#!/bin/bash/python3

def best_score(a_dictionary):
    """Returns the key with the maximum value"""

    if a_dictionary:
        best = list(a_dictionary.keys())[1]

        for key in a_dictionary.keys():
            if a_dictionary[key] > a_dictionary[best]:
                best = key
    else:
        return None

    return best
