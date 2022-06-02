#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv

    length = len(argv)
    i = 1

    if length > 2:
        print("{:d} arguments:".format(length - 1))
    elif length == 2:
        print("{:d} argument:".format(length - 1))
    else:
        print("{:d} argument.".format(length - 1))

    while i < length:
        print("{:d}: {:s}".format(i, argv[i]))
        i += 1
