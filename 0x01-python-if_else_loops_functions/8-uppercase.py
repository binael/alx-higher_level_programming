#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        element = str[i]

        if (ord(element) >= ord('a')) and (ord(element) <= ord('z')):
            element = chr(ord(element) - 32)

        print("{}".format(element), end="")

    print("")
