#!/usr/bin/python3
def remove_char_at(str, n):
    strg = ""
    i = 0
    for c in str:
        if i != n:
            strg = strg + c
        i = i + 1
    return strg
