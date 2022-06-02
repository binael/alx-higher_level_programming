#!/usr/bin/python3

import hidden_4

def unhide():
    files = dir(hidden_4)

    for file in files:
        if file[:2] == "__":
            continue
        print("{:s}".format(file))


if __name__ == "__main__":

    unhide()
