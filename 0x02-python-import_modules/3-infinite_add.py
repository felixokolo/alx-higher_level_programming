#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv
    lent = len(args) - 1
    pos = 0
    sums = 0
    while pos < lent:
        sums += int(args[pos+1])
        pos += 1
    print("{}".format(sums))
