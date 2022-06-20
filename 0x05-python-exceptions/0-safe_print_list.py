#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        counter = 0
        for i in my_list:
            counter += 1
        a = my_list[x]
    except IndexError:
        x = counter

    for i in range(x):
        print(my_list[i], end="")
    print("")
    return x
