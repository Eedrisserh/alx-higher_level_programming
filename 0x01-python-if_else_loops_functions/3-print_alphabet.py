#!/usr/bin/python3
import string

letters = string.ascii_letters
for i in range(26):
    if i != 'q' or i != 'e':
        print("{}".format(letters[i]), end="")
