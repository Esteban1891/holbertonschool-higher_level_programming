#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    argc = len(argv)
    op = {'+', '-', '*', '/'}

    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if not argv[2] in op:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif argv[2] == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif argv[2] == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
        else:
            print("{} / {} = {}".format(a, b, div(a, b)))
