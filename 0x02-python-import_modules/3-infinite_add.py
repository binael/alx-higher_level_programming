#!/usr/bin/python3

def inf_add(argv):
    length = len(argv) - 1
    i = 1
    total = 0

    while i <= length:
        total += int(argv[i])
        i += 1

    print(total)


if __name__ == "__main__":

    import sys
    inf_add(sys.argv)
