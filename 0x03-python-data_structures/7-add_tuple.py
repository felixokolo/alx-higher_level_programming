#!/usr/bin/python3

if __name__ == "__main__":
    def add_tuple(tuple_a=(), tuple_b=()):
        if len(a) == 0 and len(b) == 0:
            return (0, 0)
        if len(a) == 0:
            a = (0, 0)
        if len(a) == 1:
            a = a + (0,)
        if len(b) == 0:
            b = (0, 0)
        if len(b) == 1:
            b = b + (0,)
        if len(a) > 1 and len(b) > 1:
            return (a[0]+b[0], a[1]+b[1])
