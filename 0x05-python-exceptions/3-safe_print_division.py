#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        div = a / b
    except:
        div = None
    finally:
        print("inside result: {}".format(div))
        return(div)
