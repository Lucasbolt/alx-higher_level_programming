#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        for b in a:
            if b == a[-1]:
                print('{:d}'.format(b), end='')
            else:
                print('{:d}'.format(b), end=' ')
        print('')
