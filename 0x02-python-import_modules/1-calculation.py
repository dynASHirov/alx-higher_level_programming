#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    y = 10
    x = 5
    print("{:d} + {:d} = {:d}".format(y, x, add(y, x)))
    print("{:d} - {:d} = {:d}".format(y, x, sub(y, x)))
    print("{:d} * {:d} = {:d}".format(y, x, mul(y, x)))
    print("{:d} / {:d} = {:d}".format(y, x, div(y, x)))
