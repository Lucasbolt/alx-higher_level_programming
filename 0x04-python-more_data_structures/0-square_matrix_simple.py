#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for a in matrix:
        nw = []
        for b in a:
            nw.append(b*b)
        new_matrix.append(nw)
    return new_matrix
