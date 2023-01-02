#!/usr/bin/python3
"""
This module contains a function that takes in a matrix (list of lists) of integers/floats
and returns a new matrix containing the results of each element of the initial matrix (divided
by div) as new element of the returned matrix.
"""

def matrix_divided(matrix, div):
    """
    The matrix dividing function.
    Takes in a list of lists (with integers or floats as elements) returns a new `matrix`
    with each element divide by `div`.

    Args:
        matrix (list of lists): elements must be either integer or float
        div (integer or float): div can't be equal to zero.
    
    Raises:
        TypeError: if matrix is not list or list of list. If matrix contains elements other than integers or floats.
        ZeroDivisionError: if div is zero.
    
    Returns:
        A new matrix with each element being a result of division of former elements and div.
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for a in matrix:
        if not isinstance(a, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for b in a:
            if not (isinstance(b, int) or isinstance(b, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    length = len(matrix[0])
    for a in matrix:
        if len(a) != length:
            raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    Nmatrix = []
    for a in matrix:
        na = []
        for b in a:
            na.append(round(b/div, 2))
        Nmatrix.append(na)
    return Nmatrix
