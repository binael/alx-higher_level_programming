#!/usr/bin/python3

def remove_char_at(str, n):
    my_str = ""

    for i in range(len(str)):
        if i == n:
            continue

        my_str += str[i]

    return (my_str)
