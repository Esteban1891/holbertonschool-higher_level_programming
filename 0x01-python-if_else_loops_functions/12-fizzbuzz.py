#!/usr/bin/python3


def fizzbuzz():
    for n in range(1, 100 + 1):
        if n % 3 == 0 and n % 5 == 0:
            number = "FizzBuzz"
        elif n % 3 == 0:
            number = "Fizz"
        elif n % 5 == 0:
            number = "Buzz"
        else:
            number = str(n)

        print("{:s}".format(number), end=' ')
