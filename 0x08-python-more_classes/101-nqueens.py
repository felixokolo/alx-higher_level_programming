#!/usr/bin/python3

"""Defining practice class"""

import sys

n = len(sys.argv)

if n != 2:
    print("Usage: nqueens N")
    exit(1)
if not sys.argv[1].isnumeric():
    print("N must be a number")
    exit(1)
num = int(sys.argv[1])
if num < 4:
    print("N must be at least 4")
