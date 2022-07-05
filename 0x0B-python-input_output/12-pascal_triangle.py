#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """that returns a list of lists of integers
    representing the Pascal’s triangle of n
    Args:
        n (int): size of pascals triangle
    Returns: list of list
    """

    if n < 1:
        return []
    ret = [[1]]
    for i in range(1, n):
        prev = 0
        cur = ret[i-1]
        pres = []
        for j in cur:
            pres.append(j+prev)
            prev = j
        pres.append(1)
        ret.append(pres)
    return ret
