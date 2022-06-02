#!/usr/bin/python3

def check_args(argv):

    length = len(argv)
    i = 1

    if length > 2:
        print("{:d} arguments:".format(length - 1))
    elif length == 2:
        print("{:d} argument:".format(length - 1))
    else:
        print("{:d} argument.".format(length - 1))
        return

    while i < length:
        print("{:d}: {:s}".format(i, argv[i]))
        i += 1

if __name__ == "__main__":

    import sys
    check_args(sys.argv)
