#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = []
    for a in matrix:
        square.append(list(map(lambda a: a ** 2, a)))
    return (square)
