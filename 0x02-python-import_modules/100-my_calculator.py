#!/usr/bin/python3

from calculator_1 import add, sub, mul, div


def calculate(argv):
    """A basic calculator"""

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if argv[2] not in "-+/*":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if argv[2] == "+":
        print("{:d} {:s} {:d} = {:d}".format(a, argv[2], b, add(a, b)))
    elif argv[2] == "-":
        print("{:d} {:s} {:d} = {:d}".format(a, argv[2], b, sub(a, b)))
    elif argv[2] == "*":
        print("{:d} {:s} {:d} = {:d}".format(a, argv[2], b, mul(a, b)))
    else:
        print("{:d} {:s} {:d} = {:d}".format(a, argv[2], b, div(a, b)))


if __name__ == "__main__":

    import sys

    calculate(sys.argv)
