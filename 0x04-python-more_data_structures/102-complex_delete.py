#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None:
        return
    dels = []
    for k, v in a_dictionary.items():
        if v == value:
            dels.append(k)
    for k in dels:
        del a_dictionary[k]
    return a_dictionary
