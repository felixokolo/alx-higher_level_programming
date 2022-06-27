#!/usr/bin/python3

"""Function that divides all elements of a matrix"""

def matrix_divided(matrix, div):
    """divides all elements of a matrix

    >>> matrix = [[1, 2, 3], [4, 5, 6]]

    >>> matrix_divided(matrix, 5)
    [[0.2, 0.4, 0.6], [0.8, 1.0, 1.2]]
    >>> matrix_divided(matrix, 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    >>> print(matrix)
    [[1, 2, 3], [4, 5, 6]]
    >>> matrix_divided(matrix, 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero
    """
    result = []
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if i == 0:
            lent = len(matrix[i])
        else:
            if lent != len(matrix[i]):
                raise TypeError("Each row of the matrix must have the same size")
            lent = len(matrix[i])
        for j in range(lent):
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return list(map(lambda x: list(map(lambda y: round(y/div, 2), x)), matrix))


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/2-matrix_divided.txt")