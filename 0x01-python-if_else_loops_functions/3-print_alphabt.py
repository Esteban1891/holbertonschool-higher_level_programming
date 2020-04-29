#!/usr/bin/python3
for letter in range(97, 123):
    if letter == 'q' or letter == 'e':
        continue


print("{:c}".format(letter), end='')
