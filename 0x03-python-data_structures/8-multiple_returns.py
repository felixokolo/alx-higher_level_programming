#!/usr/bin/python3

def multiple_returns(sentence):
    lent = len(sentence)
    if lent == 0:
        first = None
    first = sentence[0]
    return (lent, first)