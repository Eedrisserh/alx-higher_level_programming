#!/usr/bin/python3
import string

letters = string.ascii_letters
for i in range(26):
    if letters[i] != "q" and letters [i] != "e":
        print("{}".format(letters[i]), end="")
