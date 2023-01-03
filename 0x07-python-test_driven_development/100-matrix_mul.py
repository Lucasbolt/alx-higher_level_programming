#!/usr/bin/python3
"""
Defines a function that calculates the product of two matrices.
"""

def check(matrix, name):
    """
    Runs different tests on `matrix` to make sure it's in compliance with the requirements.
    """
    if not isinstance(matrix, list):
        raise TypeError('{} must be a list'.format(name))

    if len(matrix) == 0:
        raise ValueError("{} can't be empty".format(name))

    #size = len(matrix[0])

    for i in matrix:
        if not isinstance(i, list):
            raise TypeError("{} must be a list of lists".format(name))
    size = len(matrix[0])
    for i in matrix:
        if len(i) == 0:
            raise ValueError("{} can't be empty".format(name))

        for a in i:
            if not (isinstance(a, int) or isinstance(a, float)):
                raise TypeError("{} should contain only integers or floats".format(name))
        if len(i) != size:
            raise TypeError("each row of {} must be of the same size".format(name))


def matrix_mul(m_a, m_b):
    """
    Compute and returns the product of two matrix.
    """
    check(m_a, 'm_a'); check(m_b, 'm_b')
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    L_index = 0
    M_index = 0
    index = 0
    while M_index < len(m_a):
        ent = []
        L_index = 0
        while L_index < len(m_b[0]):
            a = 0
            while index < len(m_a[0]):
                a += m_a[M_index][index] * m_b[index][L_index]
                index += 1
            ent.append(a)
            L_index += 1
            index = 0
        result.append(ent)
        M_index += 1
    return result
