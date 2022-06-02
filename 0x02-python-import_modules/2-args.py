#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv
    lent = len(args) - 1
    pos = 0
    if lent == 0:
        print("{} arguments.".format(lent))
    elif lent > 0:
        if lent == 1:
            print("{} argument:".format(lent))
        if lent > 1:
            print("{} arguments:".format(lent))
        while pos < lent:
            print("{}: {}".format(pos+1, args[pos+1]))
            pos += 1
