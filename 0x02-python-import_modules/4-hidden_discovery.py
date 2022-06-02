#!/usr/bin/python3

import hidden_4


def unhide():
    files = dir(hidden_4)

    for fil in files:
        if fil[:2] == "__":
            continue
        print("{:s}".format(fil))


if __name__ == "__main__":

    unhide()
