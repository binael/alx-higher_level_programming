#!/usr/bin/python3

def def magic_calculation(a, b):

    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)

        for i in range(4, 6):
            c = add(i, c)
        return (c)
    else:
        return sub(a, b)
