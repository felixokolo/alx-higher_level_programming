#!/usr/bin/python3

if __name__ == "__main__":
    def multiple_returns(sentence):
        lent = len(sentence)
        if lent == 0:
            first = None
        first = sentence[0]
        return (lent, first)
