#!/usr/bin/python3

import hidden_4


def unhide():

    for files in dir(hidden_4):
        if files[:2] != "__":
            print("{:s}".format(files))


if __name__ == "__main__":

    unhide()
