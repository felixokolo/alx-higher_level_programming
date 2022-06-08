#!/usr/bin/python3
def weight_average(my_list=[]):
    w_tot, sums = 0, 0
    for s, w in my_list:
        sums += s * w
        w_tot += w
    if w_tot > 0:
        sums /= w_tot
    return sums
