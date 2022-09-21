#!/usr/bin/python3
def uppercase(str):
    for i in str:
        c = ord(i)
        print("{:c}".format(c - 32))
