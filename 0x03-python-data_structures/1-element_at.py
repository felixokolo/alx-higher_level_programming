#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0:
        return None
    lent = len(my_list)
    if idx >= lent:
        return None
    return my_list[idx]
