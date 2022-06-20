#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        div = a / b
        print("inside result: {:.1f}".format(div))
    except Exception:
        div = None
        print("inside result: {}".format(div))
    finally:
        return(div)
