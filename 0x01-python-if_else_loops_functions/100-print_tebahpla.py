#!/usr/bin/python3

for num in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format(num if num % 2 == 0 else num - 32), end='')
