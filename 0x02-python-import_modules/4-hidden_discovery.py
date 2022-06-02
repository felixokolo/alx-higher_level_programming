#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import hidden_4

    defined = dir(hidden_4)
    for defi in defined:
        if defi[0] != '_':
            print(defi)
