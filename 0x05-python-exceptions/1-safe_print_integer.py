#!/usr/bin/python3

def safe_print_integer(value):
    try:
        a = int(value)
    except ValueError:
        return False
    else:
        print("{:d}".format(a))
        return True
