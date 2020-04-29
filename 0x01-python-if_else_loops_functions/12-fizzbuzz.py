#!/usr/bin/python3


def fizzbuzz():
    for num in range(1, 100 + 1):
        if num % 3 == 0 and num % 5 == 0:
            n = "FizzBuzz"
        if num % 3 == 0:
            n = "Fizz"
            if num % 5 == 0:
                n = "Buzz"
            else:
                n = num(str)

                print("{:s}".format(n), end='')
