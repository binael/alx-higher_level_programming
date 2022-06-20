#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        div = a / b
        print("Inside result: {:.1f}".format(div))
    except Exception:
        div = None
        print("Inside result: {}".format(div))
    finally:
        return(div)
