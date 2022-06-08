#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """ Print dictionary with keys sorted """

    k = sorted(list(a_dictionary.keys()))

    for element in k:
        print(f"{element}: {a_dictionary[element]}")
