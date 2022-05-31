#!/usr/bin/python3
def pow(a, b):
    ans = 1
    if b == 0:
        return 1
    if b == 1:
        return a
    if b > 1:
        for i in range(b - 1):
            ans = ans * a
        return ans
    if b == -1:
        return 1 / a
    if b < -1:
        for i in range(-b - 1):
            ans = ans * a
        return 1 / ans
    return 0
