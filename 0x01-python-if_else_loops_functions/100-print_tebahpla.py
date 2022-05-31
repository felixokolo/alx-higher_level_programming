#!/usr/bin/python3
for i in range(26):
    print("{}".format(chr(ord('z') - 32 * (i % 2) - i)), end="")
