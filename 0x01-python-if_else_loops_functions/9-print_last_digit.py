#!/usr/bin/python3
def print_last_digit(number):
    if num < 0:
        num *= -1
    rem = num % 10
    print("{:d}".format(rem), end="")
    return rem
