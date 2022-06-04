#!/usr/bin/python3

def max_integer(my_list=[]):
    lent = len(my_list)
    if lent == 0:
        return None
    maxi = my_list[0]
    for x in my_list:
        if x > maxi:
            maxi = x
    return maxi
