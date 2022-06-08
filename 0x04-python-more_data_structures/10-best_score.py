#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns the key with the maximum value"""

    if a_dictionary:
        best = max(list(a_dictionary.values()))

        for key in a_dictionary.keys():
            if a_dictionary[key] == best:
                return key

    else:
        return None
