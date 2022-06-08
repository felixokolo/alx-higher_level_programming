#!/usr/bin/python3
def roman_to_int(roman_string):
    rom = {'I': 1, 'V': 5,
           'X': 10, 'L': 50,
           'C': 100, 'D': 500,
           'M': 1000}

    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    lent = len(roman_string)
    sums = 0
    for idx, ch in zip(range(lent), roman_string.upper()):
        if idx < lent - 1:
            if rom[roman_string.upper()[idx + 1]] <= rom[ch]:
                sums += rom[ch]
            else:
                sums -= rom[ch]
        else:
            sums += rom[ch]
    return sums
