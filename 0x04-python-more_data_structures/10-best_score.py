#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    if len(a_dictionary) == 0:
        return None
    best_k, best_v = list(a_dictionary.items())[0]
    for k, v in a_dictionary.items():
        if v > best_v:
            best = v
            best_k = k
    return best_k
