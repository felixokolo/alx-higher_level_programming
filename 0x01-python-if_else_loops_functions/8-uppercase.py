#!/usr/bin/python3

def uppercase(str):
    d = ' '
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            d = chr(ord(c) - 32)
        else:
            d = c
        print("{}".format(d), end="")
