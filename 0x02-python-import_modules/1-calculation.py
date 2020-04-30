#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
a = 10
b = 5
print("{:d} + {:d} = {:d}".format(add, sub, mul, div, add(a, b)))
print("{:d} - {:d} = {:d}".format(add, sub, mul, div, sub(a, b)))
print("{:d} * {:d} = {:d}".format(add, sub, mul, div, mul(a, b)))
print("{:d} / {:d} = {:d}".format(add, sub, mul, div, div(a, b)))
